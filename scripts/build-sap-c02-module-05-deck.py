"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/05-designing-a-multi-account-aws-environment.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-05-deck.py

Paired with instructor-private/05-designing-a-multi-account-aws-environment-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "05-designing-a-multi-account-aws-environment.pptx")

d = Deck(5, "Designing a Multi-Account AWS Environment",
          "Every module so far assumed a sensible account structure already existed. Tonight we actually design it.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 5 · Lecture", ["Designing a Multi-Account", "AWS Environment"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 5", "Question of the Day", "Before we start",
    [("Modules 2 through 4 assumed Café Sol's and Haven & Co.'s accounts, and Security/Production OUs, already existed", "Where did that structure actually come from — and how does it stay consistent as Meridian grows?"),
     ("Recap: connectivity, security controls, and reliability tooling", "All built on top of an account structure we haven't designed yet"),
     ("Tonight's task", "Domain 1, Task 1.4 — designing the multi-account environment itself, closing out Domain 1")])

# 3 — Objectives
d.numbered_list_slide("Module 5", "Objectives", "Five things by the end of tonight", [
    ("Describe a landing zone's foundational accounts", "management, Log Archive, and Audit — and what each is for"),
    ("Explain what Account Factory automates", "pre-configured provisioning, not manual setup after the fact"),
    ("Explain what tag policies enforce", "and why consistent tagging matters at scale"),
    ("Describe how an organization trail centralizes logging", "across every account, including ones created later"),
    ("Explain how consolidated billing works", "one bill, preserved per-account visibility"),
])

# 4 — Problem framing
d.content_slide("The Structure Everything Else Was Built On",
    "Modules 2 through 4 assumed it existed. Tonight, we design it deliberately", "Module 5")

# 5 — Landing zone accounts
d.table_slide("Module 5", "The Landing Zone's Foundational Accounts", "In place before any brand's workload account is created",
    ["Account", "Purpose"],
    [["Management (payer)", "Creates and manages member accounts; consolidates billing; kept nearly empty of workloads"],
     ["Log Archive", "Receives and stores logs from every other account, in one restricted location"],
     ["Audit", "Security tooling with read access across the org — review without standing per-account access"]],
    col_widths=[3.4, 9.2],
    note="These live in Meridian's Security OU — separate from the Production OU holding actual brand workloads.")

# 6 — Exam trap: log/audit separation
d.quad_box_slide("COMMON EXAM TRAP", "Logs and Review Don't Belong Inside Workload Accounts", "The fix is account separation, not tighter per-account IAM",
    [("The scenario signal", "“workload accounts shouldn't hold long-term audit logs” or “review shouldn't need standing access everywhere.”"),
     ("Not the fix", "more granular IAM policy inside each individual workload account."),
     ("The actual fix", "a dedicated Log Archive account, and a dedicated Audit account with org-wide read access."),
     ("Why", "centralizing logs and review is a structural decision, not a per-account permissions tweak.")],
    note="One line: log storage and security review live in their own dedicated accounts — not inside every workload account.")

# 7 — Account Factory
d.content_slide("AWS Control Tower Account Factory",
    "A new account, pre-configured with the landing zone's baseline — from the moment it's created", "Module 5", dark=True)

# 8 — Account Factory mechanics
d.numbered_list_slide("Module 5", "What Account Factory Actually Sets Up", "Before the account is ever handed to a team", [
    ("Correct OU placement", "so the right SCPs and guardrails apply immediately, not after a manual step"),
    ("Standard networking", "consistent with every other account in that OU"),
    ("Logging wired to the Log Archive account", "from day one — nothing to remember to configure later"),
], note="For Ridgeline's eventual account: inherits Meridian's baseline automatically, the same way an OU-level SCP does.")

# 9 — Tag policies
d.content_slide("Tag Policies: Enforcing Consistent Resource Tagging",
    "“Environment=prod” and “env: production” look identical to a human — not to Cost Explorer", "Module 5")

# 10 — Why tagging matters
d.four_up_slide("Module 5", "What Consistent Tagging Actually Enables", "Two things break without it",
    [(1, "Cost allocation", "Break down spend by brand, environment, or team — only if tags actually agree."),
     (2, "Log attribution", "Tell which brand's resource generated a given log entry, even with logs centralized."),
     (3, "Automated cleanup", "Scripts that act on tag values need those values to be consistent, not guessed at."),
     (4, "Org-wide enforcement", "Tag policies apply at the OU level, the same pattern as SCPs and backup policies.")])

# 11 — Organization trail
d.content_slide("Organization Trail: One CloudTrail, Every Account",
    "Created once, from the management account — captures every account automatically, including ones created later", "Module 5", dark=True)

# 12 — Organization trail properties
d.split_card_slide("Module 5", "What Makes an Organization Trail Different", "Compared to a single-account CloudTrail trail",
    "A single-account trail",
    [("Has to be enabled per account", "easy to forget in a newly created account"),
     ("Only member accounts control it", "a compromised account could tamper with its own logs")],
    "An organization trail",
    "Created once, applies everywhere",
    ["Automatically captures new accounts, including Ridgeline's future one", "Only the management account can disable or modify it"])

# 13 — Consolidated billing
d.content_slide("Consolidated Billing: One Bill, Per-Brand Visibility",
    "Usage aggregated for pricing benefits — cost still broken down per account, and per tag", "Module 5")

# 14 — Putting it together
d.numbered_list_slide("Module 5", "Putting It Together: Meridian's Multi-Account Design", "Every piece from Domain 1, in one structure", [
    ("A landing zone: management, Log Archive, and Audit accounts", "all inside the Security OU, separate from Production and Sandbox"),
    ("Account Factory provisioning every new brand's account", "pre-configured with the right OU, SCPs, guardrails, and logging"),
    ("Tag policies requiring Brand and CostCenter tags org-wide", "making per-brand cost and ownership tracking possible at all"),
    ("An organization trail and consolidated billing", "one centralized log record, one invoice, per-brand visibility"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 5", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Account Factory means the job is done”", "It sets the baseline at creation — ongoing governance still continues after that."),
    ("“Consolidated billing exposes every account's detail to every other account”", "It preserves per-account visibility — it doesn't remove access controls."),
    ("“Tagging is just cosmetic”", "Without it, cost allocation and log attribution both stop working reliably at scale."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Module 6 closes Domain 1 with Task 1.5: cost optimization and visibility strategies across Meridian's organization", "Module 5")

# 17 — Closing
d.closing_slide("Designing a Multi-Account", "AWS Environment", "Next up: cost optimization and visibility across Meridian's organization")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
