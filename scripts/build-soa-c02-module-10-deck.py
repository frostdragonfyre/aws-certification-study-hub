"""
Builds certifications/soa-c02/lectures/10-implementing-data-and-infrastructure-protection-strategies.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-10-deck.py

Paired with instructor-private/10-implementing-data-and-infrastructure-protection-strategies-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02", "lectures",
                    "10-implementing-data-and-infrastructure-protection-strategies.pptx")

d = Deck(10, "Implementing Data and Infrastructure Protection Strategies",
          "Module 9 set the guardrails and checked them continuously. Tonight protects the data and network traffic directly.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 10 · Lecture", ["Implementing Data and", "Infrastructure Protection"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 10", "Question of the Day", "Before we start",
    [("A principal has full IAM permission for a KMS action, but is still denied access to the key", "How is that possible?"),
     ("Recap: Module 9 covered guardrails and continuous compliance checking", "tonight gets concrete — protecting data and network traffic directly"),
     ("Tonight's task", "Domain 4, Task 4.2 — the final module of Domain 4: data and infrastructure protection")])

# 3 — Objectives
d.numbered_list_slide("Module 10", "Objectives", "Five things by the end of tonight", [
    ("Distinguish an AWS managed key from a customer managed key in KMS", "and what control each one gives you"),
    ("Explain how a KMS key policy and an IAM policy work together", "both have to allow the action"),
    ("Distinguish Security Groups from Network ACLs", "and know when each fits"),
    ("Distinguish Secrets Manager from Parameter Store", "and when rotation justifies the extra cost"),
    ("Design a data and network protection strategy for a stated requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Protecting the Data and the Traffic, Not Just the Access",
    "Module 9 set who's allowed to do what. Tonight protects the data itself and the network it moves across.", "Module 10")

# 5 — Section intro: KMS
d.content_slide("KMS: AWS Managed Keys vs. Customer Managed Keys",
    "Not every encryption key gives you the same control", "Module 10", dark=True)

# 6 — Exam trap: KMS
d.quad_box_slide("COMMON EXAM TRAP", "Two Kinds of Keys, Two Levels of Control", "And both a key policy and an IAM policy have to agree",
    [("AWS managed key", "created and controlled by AWS — no custom rotation, no cross-account sharing."),
     ("Customer managed key", "you control the key policy, rotation, cross-account sharing, and deletion."),
     ("Key policy", "a resource-based policy on the key itself — it must allow the principal too."),
     ("Both must allow", "the key policy and the IAM policy both have to permit the action.")],
    note="One line: customer managed keys give you control AWS managed keys don't — and access always needs both policies to agree.")

# 7 — Section intro: Security Groups vs NACLs
d.content_slide("Security Groups vs. Network ACLs",
    "Both control VPC traffic — at different layers, with very different rules", "Module 10")

# 8 — Exam trap: SG vs NACL
d.quad_box_slide("COMMON EXAM TRAP", "Security Groups vs. NACLs", "Stateful and Allow-only, vs. stateless with Deny",
    [("Security Group", "instance-level, stateful — a response is automatically allowed back out."),
     ("Network ACL", "subnet-level, stateless — inbound and outbound each need their own rule."),
     ("Allow rules only", "a Security Group has no way to explicitly Deny traffic."),
     ("Allow and Deny rules", "a NACL supports both, evaluated in numbered order.")],
    note="One line: Security Groups can only allow — a NACL is what explicitly blocks something.")

# 9 — Applied
d.table_slide("Module 10", "Security Groups vs. NACLs, Applied", "Matching the requirement to the right control",
    ["Requirement", "Right control"],
    [["Explicitly block a specific known-bad IP, allow everything else", "A NACL — Security Groups have no Deny rules"],
     ["Standard instance-level allow-listing, simplest configuration", "A Security Group — stateful, no outbound rule needed for responses"]],
    col_widths=[7.6, 5.0],
    note="A requirement to explicitly block something is always the NACL tell.")

# 10 — Section intro: Secrets Manager vs Parameter Store
d.content_slide("Secrets Manager vs. Systems Manager Parameter Store",
    "Both store encrypted values — they diverge on one capability: rotation", "Module 10", dark=True)

# 11 — Exam trap: Secrets Manager vs Parameter Store
d.quad_box_slide("COMMON EXAM TRAP", "Rotation Is the Deciding Factor", "Don't pay for rotation you don't need",
    [("Secrets Manager", "built-in automatic rotation for RDS, Redshift, DocumentDB, or custom via Lambda."),
     ("Parameter Store SecureString", "encrypted storage, lower cost, no built-in rotation."),
     ("Automatic rotation", "needed on a schedule — Secrets Manager."),
     ("No built-in rotation", "a static value, cost matters — Parameter Store SecureString.")],
    note="One line: rotation need decides it — Secrets Manager rotates, Parameter Store is cheaper when nothing needs to.")

# 12 — Applied
d.table_slide("Module 10", "Secrets Manager vs. Parameter Store, Applied", "Matching the value to the right store",
    ["Requirement", "Right store"],
    [["A database credential rotating automatically every 30 days", "Secrets Manager — built-in rotation support"],
     ["A static configuration value, cost-sensitive, no rotation needed", "Parameter Store SecureString — lower cost"]],
    col_widths=[7.6, 5.0],
    note="Needing rotation points to Secrets Manager; not needing it points to the cheaper option.")

# 13 — Putting it together
d.numbered_list_slide("Module 10", "Putting It Together: Protecting Meridian's Data and Network", "Every piece from tonight, in one design", [
    ("Customer managed KMS keys for Meridian Loyalty's and Ridgeline's databases", "control over rotation, cross-account sharing, and scheduled deletion"),
    ("Security Groups as the default, with NACLs layered to block known-bad IPs", "instance-level allow-listing, plus explicit subnet-level Deny where needed"),
    ("Secrets Manager for RDS credentials with automatic rotation, Parameter Store for the rest", "no hardcoded passwords, without paying for rotation nothing needs"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 10", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“An AWS managed key can be shared across accounts”", "Only customer managed keys support cross-account sharing and custom rotation."),
    ("“Security Groups can block a specific bad IP”", "They only support Allow rules — a NACL is what can explicitly Deny."),
    ("“Secrets Manager and Parameter Store are interchangeable”", "Secrets Manager adds built-in rotation; Parameter Store doesn't."),
], dark=True)

# 15 — Domain 4, Complete
d.table_slide("Module 10", "Domain 4, Complete", "Two modules, one secure and compliant foundation",
    ["Module", "Task"],
    [["Module 9", "Task 4.1 — security and compliance policies"],
     ["Module 10", "Task 4.2 — data and infrastructure protection strategies"]],
    col_widths=[3.6, 9.0],
    note="Guardrails and continuous checks, plus direct protection of data and traffic — Domain 4's two tasks, closed.")

# 16 — Recap
d.content_slide("Recap",
    "AWS managed vs. customer managed KMS keys, Security Groups vs. NACLs, Secrets Manager vs. Parameter Store", "Module 10", dark=True)

# 17 — Closing
d.closing_slide("Implementing Data and", "Infrastructure Protection", "Domain 4 complete — next up: Domain 5, networking and content delivery")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
