"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/07-provisioning-and-maintaining-cloud-resources.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-07-deck.py

Paired with instructor-private/07-provisioning-and-maintaining-cloud-resources-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "07-provisioning-and-maintaining-cloud-resources.pptx")

d = Deck(7, "Provisioning and Maintaining Cloud Resources",
          "Domain 2 kept the infrastructure alive. Domain 3 asks how it gets created and kept consistent in the first place.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 7 · Lecture", ["Provisioning and Maintaining", "Cloud Resources"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 7", "Question of the Day", "Before we start",
    [("Meridian now has 40 AWS accounts, each needing the same baseline VPC and IAM roles", "Does someone click through the console 40 times?"),
     ("Recap: Domain 2 closed with capacity, survival, and recovery", "Domain 3 asks how resources get created and kept consistent to begin with"),
     ("Tonight's task", "Domain 3, Task 3.1 — the first module of Domain 3: provisioning and maintaining cloud resources")])

# 3 — Objectives
d.numbered_list_slide("Module 7", "Objectives", "Five things by the end of tonight", [
    ("Explain what a CloudFormation stack is and how a template drives it", "and what a change set previews before an update runs"),
    ("Describe how StackSets deploy across multiple accounts and Regions", "one template, many places, from one administrator account"),
    ("Explain what drift detection finds, and what it does not fix", "a diagnostic step, not a remediation"),
    ("Describe how Service Catalog lets non-admins provision safely", "self-service without broad IAM permissions"),
    ("Design a provisioning strategy for a multi-account, self-service requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Infrastructure That's Consistent, Not Just Working",
    "Domain 3 opens with the most basic provisioning question: does everyone get the same thing, the same way, every time?", "Module 7")

# 5 — Section intro: CloudFormation
d.content_slide("CloudFormation: Infrastructure as Code",
    "A template defines it, a stack deploys it, a change set previews it", "Module 7", dark=True)

# 6 — CloudFormation and change sets applied
d.numbered_list_slide("Module 7", "CloudFormation and Change Sets, Applied", "Turning a risky update into a safe one", [
    ("A template declares every resource an application needs", "EC2, RDS, IAM roles, a VPC — created, updated, or deleted together as a stack"),
    ("A change set previews an update before anything happens", "flags additions, modifications, and replacements"),
    ("A replacement can mean tearing down and recreating a resource", "for something like a database, that can mean data loss"),
    ("Reviewing the change set is how Priya catches that beforehand", "not after the update has already run"),
])

# 7 — Section intro: StackSets
d.content_slide("StackSets: The Same Template, Many Accounts and Regions",
    "One administrator account, dozens of stack instances", "Module 7")

# 8 — Exam trap: StackSets
d.quad_box_slide("COMMON EXAM TRAP", "StackSets vs. Individual Stacks", "Scope is the whole difference",
    [("A single stack", "one account, one Region — nothing more."),
     ("A StackSet", "deploys the same template as stack instances across many accounts and Regions."),
     ("One administrator account", "manages every stack instance from a single place."),
     ("Updating the StackSet's template", "propagates the change to every instance at once.")],
    note="One line: a stack is one account and one Region — a StackSet scales a template across many of both.")

# 9 — Applied
d.table_slide("Module 7", "StackSets, Applied", "Matching the deployment need to the right mechanism",
    ["Need", "Right mechanism"],
    [["A baseline VPC and IAM roles identical across 40 accounts", "A CloudFormation StackSet, deployed once, updated centrally"],
     ["A single application's resources in one account", "A standard CloudFormation stack"]],
    col_widths=[7.2, 5.4],
    note="Scope tells you which one — one account and Region is a stack, many is a StackSet.")

# 10 — Section intro: Drift detection
d.content_slide("Drift Detection: Finding What Changed Outside CloudFormation",
    "Someone changes a resource by hand — now what does CloudFormation actually know?", "Module 7", dark=True)

# 11 — Exam trap: Drift detection
d.quad_box_slide("COMMON EXAM TRAP", "Drift Detection Is Read-Only", "Finding the mismatch isn't the same as fixing it",
    [("Drift", "a resource no longer matches what its template says."),
     ("Drift detection", "compares actual configuration to the template and reports differences."),
     ("Read-only", "it identifies drift — it does not undo it."),
     ("Fixing it", "means manually reverting the change, or an update that brings it back in line.")],
    note="One line: drift detection tells you what changed — it doesn't change anything back.")

# 12 — Applied
d.table_slide("Module 7", "Drift Detection, Applied", "What to do once drift is found",
    ["Observation", "Right response"],
    [["A resource has drifted from its template", "Investigate, then revert the manual change or update the stack"],
     ["Assuming CloudFormation “automatically” fixes drift", "Incorrect — drift detection only reports; it never remediates alone"]],
    col_widths=[7.2, 5.4],
    note="Drift detection is the diagnostic step, not the fix.")

# 13 — Section intro: Service Catalog
d.content_slide("Service Catalog: Self-Service Without Losing Control",
    "Not everyone who provisions something should need to be a CloudFormation expert", "Module 7")

# 14 — Exam trap: Service Catalog
d.quad_box_slide("COMMON EXAM TRAP", "Self-Service Without Broad Permissions", "The fix isn't wider IAM access",
    [("Products", "pre-approved CloudFormation templates, vetted and locked to safe configuration."),
     ("Portfolios", "products grouped and assigned to specific users or teams."),
     ("Self-service, restricted", "users launch only the products they're permitted to."),
     ("Not broader IAM permissions", "the underlying resource permissions stay with Service Catalog, not the user.")],
    note="One line: the fix for self-service provisioning is Service Catalog, not wider IAM access.")

# 15 — Putting it together
d.numbered_list_slide("Module 7", "Putting It Together: Provisioning at Meridian", "Every piece from tonight, in one design", [
    ("CloudFormation templates as the source of truth, change sets reviewed before risky updates", "catching a resource replacement before it happens"),
    ("StackSets deploying Meridian's baseline identically across every account and Region", "one template, one place to update it"),
    ("Drift detection run on a schedule against critical stacks", "catching an out-of-band change instead of letting it persist silently"),
    ("Service Catalog portfolios giving developers self-service access to pre-approved products", "without broad provisioning permissions"),
])

# 16 — Common mix-ups
d.resource_list_slide("Module 7", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“A single stack can span accounts”", "It's scoped to one account and one Region — StackSets scale across many."),
    ("“Drift detection fixes drift”", "It only reports the mismatch — remediation is a separate step."),
    ("“Self-service means broad IAM permissions”", "Service Catalog restricts self-service to pre-approved products instead."),
], dark=True)

# 17 — Closing
d.closing_slide("Provisioning and", "Maintaining Cloud Resources", "Next up: Module 8 — automating manual and repeatable processes")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
