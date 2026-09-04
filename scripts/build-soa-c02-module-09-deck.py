"""
Builds certifications/soa-c02/lectures/09-implementing-and-managing-security-and-compliance-policies.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-09-deck.py

Paired with instructor-private/09-implementing-and-managing-security-and-compliance-policies-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02", "lectures",
                    "09-implementing-and-managing-security-and-compliance-policies.pptx")

d = Deck(9, "Implementing and Managing Security and Compliance Policies",
          "Domain 3 kept things consistent and automated. Domain 4 asks whether all of it is actually secure and compliant.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 9 · Lecture", ["Implementing and Managing", "Security and Compliance Policies"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 9", "Question of the Day", "Before we start",
    [("A developer's IAM policy explicitly allows deleting any S3 bucket in the account", "Does that mean they actually can, no matter what else is in place?"),
     ("Recap: Domain 3 closed with consistent provisioning and hands-off automation", "Domain 4 asks whether all of it is secure and compliant"),
     ("Tonight's task", "Domain 4, Task 4.1 — the first module of Domain 4: security and compliance policies")])

# 3 — Objectives
d.numbered_list_slide("Module 9", "Objectives", "Five things by the end of tonight", [
    ("Distinguish an IAM policy from a Service Control Policy", "and explain what each one actually controls"),
    ("Explain how AWS Config continuously evaluates configuration", "against defined rules, on an ongoing basis"),
    ("Describe how Config rules can trigger automatic remediation", "closing the loop from detection to fix"),
    ("Explain what Security Hub aggregates, and what it doesn't replace", "a dashboard, not a detector"),
    ("Design a security and compliance strategy for a multi-account requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Secure Once Isn't the Same as Secure Continuously",
    "Domain 4 opens with the guardrails that define what's allowed, and continuous checks that reality still matches them", "Module 9")

# 5 — Section intro: IAM vs SCP
d.content_slide("IAM Policies vs. Service Control Policies",
    "Both look like JSON Allow/Deny documents — they control very different things", "Module 9", dark=True)

# 6 — Exam trap: IAM vs SCP
d.quad_box_slide("COMMON EXAM TRAP", "IAM Policies vs. SCPs", "Granting permission vs. capping it",
    [("IAM policy", "attached to a user, group, or role — actually grants permissions."),
     ("Service Control Policy", "applied at the account or OU level, through Organizations."),
     ("Grants permissions", "only an IAM policy can do this."),
     ("Restricts, never grants", "an SCP sets a maximum boundary — it can only take away, not give.")],
    note="One line: IAM policies grant, SCPs only ever restrict — a principal needs both.")

# 7 — Applied
d.table_slide("Module 9", "IAM vs. SCP, Applied", "Reading which control a scenario is describing",
    ["Requirement", "Right control"],
    [["“No account in this OU can ever disable CloudTrail”", "An SCP applied at the OU level"],
     ["“Grant this specific user permission to read this bucket”", "An IAM policy attached to that user"]],
    col_widths=[7.4, 5.2],
    note="Organization-wide, unconditional restriction is SCP language; granting a specific principal permission is IAM policy language.")

# 8 — Section intro: AWS Config
d.content_slide("AWS Config: Continuous Compliance Evaluation",
    "Compliant at launch doesn't mean compliant next week", "Module 9")

# 9 — Exam trap: Config
d.quad_box_slide("COMMON EXAM TRAP", "Continuous, Not One-Time", "And it can fix what it finds",
    [("Config rule", "AWS-managed or custom, backed by Lambda — defines what compliant looks like."),
     ("Continuous evaluation", "resources are checked on an ongoing basis, not just at creation."),
     ("Automatic remediation", "a non-compliant resource can trigger an SSM Automation runbook."),
     ("Not a one-time check", "and not the same as CloudFormation drift detection, which only compares against a template.")],
    note="One line: Config checks compliance continuously, and can close the loop with automatic remediation.")

# 10 — Applied
d.table_slide("Module 9", "Config, Applied", "Matching the need to the right mechanism",
    ["Need", "Right mechanism"],
    [["Verify every account stays compliant with a standard, ongoing", "AWS Config rules, evaluated continuously"],
     ["Fix a non-compliant resource automatically, no person involved", "A Config rule paired with SSM Automation remediation"]],
    col_widths=[7.4, 5.2],
    note="Ongoing verification is Config; automatic fixing is Config plus SSM Automation.")

# 11 — Section intro: Security Hub
d.content_slide("Security Hub: One View, Many Sources",
    "Checking GuardDuty, Config, and Inspector separately across 40 accounts doesn't scale", "Module 9", dark=True)

# 12 — Exam trap: Security Hub
d.quad_box_slide("COMMON EXAM TRAP", "Aggregator, Not a Detector", "Security Hub doesn't replace what feeds it",
    [("Security Hub", "aggregates findings from GuardDuty, Config, Inspector, and more."),
     ("Aggregates and scores", "one standardized view, scored against standards like CIS or PCI DSS."),
     ("Doesn't generate detection", "it has no threat detection or config evaluation of its own."),
     ("Needs the underlying services", "running, and enabled, for there to be anything to aggregate.")],
    note="One line: Security Hub aggregates and scores what other services find — it doesn't find anything on its own.")

# 13 — Applied
d.table_slide("Module 9", "Security Hub, Applied", "What Security Hub does and doesn't do",
    ["Statement", "Reality"],
    [["“One dashboard for GuardDuty, Config, and Inspector findings across accounts”", "Correct — that's exactly what Security Hub aggregates"],
     ["“Enabling Security Hub alone replaces the need for GuardDuty and Config”", "Incorrect — with nothing feeding it, there's nothing to aggregate"]],
    col_widths=[8.0, 4.6],
    note="Security Hub is the dashboard — the detection still has to come from somewhere.")

# 14 — Putting it together
d.numbered_list_slide("Module 9", "Putting It Together: Security and Compliance at Meridian", "Every piece from tonight, in one design", [
    ("SCPs at the Organizations level enforcing hard boundaries", "no disabling CloudTrail, no non-approved Regions, regardless of any account's IAM policies"),
    ("IAM policies granting least-privilege permissions within whatever the SCPs allow", "the actual grants, scoped to what each team needs"),
    ("Config rules continuously evaluating every account, with automatic remediation for well-understood fixes", "detection and correction, closing the loop"),
    ("Security Hub aggregating GuardDuty, Config, and Inspector findings across every account", "one dashboard, scored against the CIS Benchmark"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 9", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“An SCP can grant a permission an IAM policy doesn't”", "SCPs only ever restrict — they can never grant permissions on their own."),
    ("“Config only checks resources once, at creation”", "It evaluates continuously, on an ongoing basis."),
    ("“Security Hub generates its own threat findings”", "It aggregates and scores what GuardDuty, Config, and Inspector report."),
], dark=True)

# 16 — Recap
d.content_slide("Recap",
    "IAM policies vs. SCPs, AWS Config's continuous evaluation and remediation, Security Hub as an aggregator", "Module 9", dark=True)

# 17 — Closing
d.closing_slide("Implementing and Managing", "Security and Compliance Policies", "Next up: Module 10 — data and infrastructure protection strategies")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
