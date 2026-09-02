"""
Builds certifications/sap-c02/lectures/03-prescribing-security-controls-at-the-organization-level.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-03-deck.py

Paired with instructor-private/03-prescribing-security-controls-at-the-organization-level-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02", "lectures",
                    "03-prescribing-security-controls-at-the-organization-level.pptx")

d = Deck(3, "Prescribing Security Controls at the Organization Level",
          "Connectivity without governance just means everyone can reach further than they should.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 3 · Lecture", ["Prescribing Security Controls", "at the Organization Level"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 3", "Question of the Day", "Before we start",
    [("Module 2 connected Café Sol, Haven & Co., and Ridgeline's future network", "Now that they can reach each other, what stops any engineer from reaching further than they should?"),
     ("Recap: Transit Gateway, PrivateLink, VPN/Direct Connect, Route 53 Resolver", "Connectivity — but no governance layered on top of it yet"),
     ("Tonight's task", "Domain 1, Task 1.2 — prescribing security controls across the organization")])

# 3 — Objectives
d.numbered_list_slide("Module 3", "Objectives", "Five things by the end of tonight", [
    ("Explain what an SCP does — and does not do", "and how it differs from an IAM policy"),
    ("Describe how organizational units apply policy to groups of accounts", "including accounts added later"),
    ("Explain what IAM Identity Center centralizes", "one identity, scoped access to many accounts"),
    ("Distinguish preventive and detective guardrails", "and how Control Tower applies both"),
    ("Explain the cross-account role pattern", "and why it replaces shared long-lived credentials"),
])

# 4 — Problem framing
d.content_slide("Governance, Not Just Connectivity",
    "Deciding what's allowed before any individual account's administrator can misconfigure it", "Module 3")

# 5 — SCPs intro
d.content_slide("Service Control Policies: Setting the Outer Boundary",
    "The maximum available permissions for accounts in an OU — set before any IAM policy is written", "Module 3", dark=True)

# 6 — Exam trap: SCPs don't grant
d.quad_box_slide("COMMON EXAM TRAP", "SCPs Never Grant Permissions", "They only set a ceiling — an IAM policy still has to grant the permission",
    [("The mistake", "“We attached an SCP allowing S3 access, so users can access S3 now.”"),
     ("What's actually true", "An SCP sets a maximum boundary — it never grants anything by itself."),
     ("Still required", "An IAM policy inside the account, actually granting the permission to a user or role."),
     ("What the SCP controls", "Whether that IAM grant is allowed to take effect at all.")],
    note="One line: SCPs restrict. They don't provision. Read for which one a scenario is actually missing.")

# 7 — OUs
d.content_slide("Organizational Units: Applying Policy to Groups of Accounts",
    "Attach once at the OU level — every account inside it, including ones added later, inherits it", "Module 3")

# 8 — Meridian's OU structure
d.table_slide("Module 3", "A Typical OU Structure", "Grouped by purpose and risk level",
    ["OU", "Holds", "Policy posture"],
    [["Security OU", "Centralized logging and security tooling accounts", "Strictest SCPs"],
     ["Production OU", "Each brand's live, customer-facing workloads", "Strict — layered on top of org-wide policy"],
     ["Sandbox OU", "Engineer experimentation", "Looser, but not absent"]],
    col_widths=[2.8, 6.2, 4.0])

# 9 — IAM Identity Center
d.content_slide("AWS IAM Identity Center: One Identity, Many Accounts",
    "Sign in once — get scoped access to specific accounts through permission sets", "Module 3", dark=True)

# 10 — Preventive vs detective
d.split_card_slide("Module 3", "Preventive vs. Detective Guardrails", "Two different jobs, both part of AWS Control Tower",
    "Preventive",
    [("Blocks the action outright", "implemented under the hood using SCPs"),
     ("Example", "no user, however permissive, can disable CloudTrail logging")],
    "Detective",
    "Flags violations after the fact",
    ["Implemented using AWS Config rules", "Example: identifies an S3 bucket that became public, without having blocked it"])

# 11 — Exam trap: preventive vs detective
d.quad_box_slide("COMMON EXAM TRAP", "Match the Guardrail Type to the Requirement", "“Must never happen” and “must be caught if it happens” are different asks",
    [("“Must be blocked from ever happening”", "Preventive guardrail — implemented via SCP."),
     ("“Must be detected and reported if it happens”", "Detective guardrail — implemented via AWS Config."),
     ("Asking for both", "is Control Tower's actual default behavior, not an either/or choice."),
     ("Not everything can be prevented", "some drift can only be caught after the fact — that's still valuable.")],
    note="One line: block what can be blocked. Detect what can't. Both belong in the same design.")

# 12 — Cross-account roles
d.content_slide("Cross-Account Roles: Access Without Shared Credentials",
    "Short-lived, scoped, individually logged — instead of one long-lived secret shared everywhere", "Module 3")

# 13 — Cross-account role mechanics
d.numbered_list_slide("Module 3", "How a Cross-Account Role Actually Works", "sts:AssumeRole, not a shared password", [
    ("The target account creates a role", "with a trust policy naming exactly which external principal may assume it"),
    ("The external principal calls sts:AssumeRole", "and receives short-lived temporary credentials, not a long-lived secret"),
    ("The role's own permissions define the session", "exactly and only what that assumed session can do — nothing more"),
], note="Every assumption is individually logged in CloudTrail. A leaked credential expires; it doesn't compromise every account forever.")

# 14 — Putting it together
d.numbered_list_slide("Module 3", "Putting It Together: Meridian's Org-Level Security Design", "Every piece from tonight, in one design", [
    ("Security, Production, and Sandbox OUs", "each with SCPs scoped to its actual risk level"),
    ("Control Tower: preventive guardrails for the worst mistakes, detective for the rest", "e.g. logging can never be disabled; a public bucket gets flagged"),
    ("IAM Identity Center as the single sign-on source", "permission sets scoped per account, per engineer"),
    ("Cross-account roles for every legitimate cross-boundary need", "no long-lived credentials shared anywhere in the design"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 3", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“An SCP is enough to grant access”", "It only sets a ceiling — an IAM policy still has to grant the actual permission."),
    ("“Preventive guardrails make detective guardrails unnecessary”", "Some drift can't be prevented up front — detective guardrails catch what prevention can't."),
    ("“Cross-account access needs a shared IAM user”", "It needs a role with a trust policy and sts:AssumeRole — never long-lived shared keys."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Module 4 continues Domain 1 with Task 1.3: designing reliable and resilient architectures across Meridian's accounts", "Module 3")

# 17 — Closing
d.closing_slide("Prescribing Security Controls", "at the Organization Level", "Next up: designing reliable and resilient architectures across Meridian's accounts")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
