"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/09-securing-user-application-and-data-access.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-09-deck.py

Paired with instructor-private/09-securing-user-application-and-data-access-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "09-securing-user-application-and-data-access.pptx")

d = Deck(9, "Securing User, Application, and Data Access",
          "IAM manages AWS. Tonight is everything IAM was never meant to do.")

# 1 — Title
d.title_slide("Module 9 · Lecture", ["Securing User, Application,", "and Data Access"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 9", "Question of the Day", "Before we start",
    [("Should a café customer placing an order get an IAM user?",
      "Module 3 never had to answer this — tonight explains exactly why not."),
     ("Recap: Module 3 built the IAM foundation", "users, groups, roles, policies, least privilege"),
     ("Tonight's shift", "From “managing AWS” to “authenticating customers, protecting credentials, protecting data”")])

# 3 — Objectives
d.numbered_list_slide("Module 9", "Objectives", "Five things by the end of tonight", [
    ("Explain why customers need Cognito, not IAM", "different identity, different tool, on purpose"),
    ("Distinguish Cognito user pools from identity pools", "authentication vs. temporary AWS access"),
    ("Explain what Secrets Manager solves", "hardcoded credentials are a real, common mistake"),
    ("Compare Secrets Manager to Parameter Store", "rotation and cost are the deciding factors"),
    ("Explain KMS and envelope encryption", "at the level the exam actually expects"),
])

# 4 — The café's access problem, expanded
d.content_slide("The Café's Access Problem, Expanded",
    "V2 added online ordering — and a whole category of access problem Module 3 never touched", "Module 9")

# 5 — Cognito
d.content_slide("Amazon Cognito: Authentication for App Users",
    "IAM manages access TO AWS. Cognito authenticates the people USING what you built on AWS.", "Module 9")

# 6 — User pools vs identity pools
d.table_slide("Module 9", "User Pools vs. Identity Pools", "Two related, distinct jobs — often used together",
    ["", "User pools", "Identity pools"],
    [["Job", "Authentication (who is this person)", "Authorization (temporary AWS access)"],
     ["Output", "Sign-in tokens", "Temporary AWS credentials"],
     ["Typical use", "Customer sign-up and login", "Letting a user talk directly to an AWS service"]],
    col_widths=[2.6, 5.0, 5.0])

# 7 — Exam trap: IAM vs Cognito
d.quad_box_slide("COMMON EXAM TRAP", "IAM vs. Cognito", "Same word (“identity”), two very different jobs",
    [("IAM", "Manages access to AWS itself — for admins, and services that need to act on AWS resources."),
     ("Cognito User Pool", "Authenticates an application's actual end users — customers, not AWS accounts."),
     ("Cognito Identity Pool", "Grants a logged-in (or guest) user temporary AWS credentials — scoped, never standing access."),
     ("The trap", "“Create an IAM user for each customer” is always the wrong answer for public-facing apps.")],
    note="Study cue: if the scenario says “customers create accounts and log in,” think Cognito, not IAM.")

# 8 — Secrets Manager
d.content_slide("AWS Secrets Manager: Credentials That Aren't Hardcoded",
    "Stored centrally, encrypted, retrieved at runtime — with built-in automatic rotation", "Module 9", dark=True)

# 9 — Secrets Manager vs Parameter Store
d.table_slide("Module 9", "Secrets Manager vs. Parameter Store", "Both store secrets — one rotates them for you",
    ["", "Secrets Manager", "Parameter Store"],
    [["Built-in automatic rotation", "Yes", "No (custom automation required)"],
     ["Cost", "Per secret, per month", "Free tier available"],
     ["Best for", "DB credentials, API keys needing rotation", "General config values, no-rotation secrets"]],
    col_widths=[3.4, 4.6, 4.6])

# 10 — KMS
d.content_slide("AWS KMS: Protecting the Data Itself",
    "Everything so far controls WHO can ask. KMS protects what they'd find if they bypassed all of it.", "Module 9")

# 11 — Envelope encryption
d.numbered_list_slide("Module 9", "Envelope Encryption, Step by Step", "Why KMS stays fast even at scale", [
    ("KMS generates a unique data key", "a fresh key created for this specific piece of data"),
    ("The data key encrypts your data, locally", "fast — it never has to leave where the data lives"),
    ("KMS encrypts the data key itself", "using your KMS key, then stores it alongside the encrypted data"),
    ("Decryption reverses the process", "KMS decrypts the data key first, then the data key decrypts your data"),
])

# 12 — Exam trap: at rest vs in transit
d.split_card_slide("Module 9", "At Rest vs. In Transit", "Two different protections — a complete design needs both",
    "Encryption at rest",
    [("What it protects", "data while stored — S3, EBS, RDS"),
     ("How", "AWS KMS, via envelope encryption")],
    "Encryption in transit",
    "Data while it's moving",
    ["Across a network, client to server", "Handled by TLS/HTTPS, not KMS"])

# 13 — Putting it together
d.numbered_list_slide("Module 9", "Putting It Together: The Café's V2 Access Model", "Four problems, four deliberate tools", [
    ("Customers authenticate via a Cognito user pool", "and never touch IAM at all"),
    ("The web tier retrieves RDS credentials from Secrets Manager", "at runtime, rotating automatically — never hardcoded"),
    ("RDS and stored customer data are encrypted via KMS", "a storage-layer compromise alone doesn't hand over readable data"),
], note="Administering AWS, authenticating customers, protecting credentials, protecting data — four different problems, on purpose.")

# 14 — Common mix-ups
d.resource_list_slide("Module 9", "Common Mix-Ups", "Worth getting right before Module 10", [
    ("“Just create an IAM user for each customer”", "Wrong tool — IAM manages AWS access, Cognito authenticates app users."),
    ("“A customer managed key is more secure”", "Same encryption strength — the difference is who controls the key's policy."),
    ("“Encrypted at rest means fully protected”", "Encryption in transit (TLS) is a separate, still-necessary protection."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Skim the Module 9 guided lab overview — you'll set up a Cognito user pool yourself in the Learner Lab", "Module 9")

# 16 — Closing
d.closing_slide("User, Application,", "and Data Access", "Next up: monitoring, elasticity, and high availability")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
