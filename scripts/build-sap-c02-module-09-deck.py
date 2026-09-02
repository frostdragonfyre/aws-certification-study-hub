"""
Builds certifications/sap-c02/lectures/09-determining-security-controls-for-new-solutions.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-09-deck.py

Paired with instructor-private/09-determining-security-controls-for-new-solutions-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02", "lectures",
                    "09-determining-security-controls-for-new-solutions.pptx")

d = Deck(9, "Determining Security Controls for New Solutions",
          "Module 3 built the guardrails. Tonight they get applied to a real, public-facing workload.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 9 · Lecture", ["Determining Security Controls", "for New Solutions"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 9", "Question of the Day", "Before we start",
    [("Meridian Loyalty is about to get a public-facing guest portal", "What security controls does a guest rewards platform actually need — and how do you decide, instead of adding everything?"),
     ("Recap: Module 3 built org-wide security guardrails", "SCPs, org-wide GuardDuty, aggregated Security Hub — but didn't decide any one workload's specific controls"),
     ("Tonight's task", "Domain 2, Task 2.3 — Module 3's guardrails, applied to Meridian Loyalty for real")])

# 3 — Objectives
d.numbered_list_slide("Module 9", "Objectives", "Five things by the end of tonight", [
    ("Derive security requirements from what a solution actually handles", "for Meridian Loyalty's guest data specifically"),
    ("Choose between Secrets Manager and Parameter Store", "based on whether automatic rotation is the real requirement"),
    ("Select the right mix of WAF, Shield Standard, and Shield Advanced", "for a public-facing workload"),
    ("Explain how Module 3's guardrails apply automatically", "to a new workload's account, with no new setup"),
    ("Design a complete security control set for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("From Org-Wide Guardrails to One Real Decision",
    "Module 3 stopped short of picking controls for any one workload. Tonight, that decision gets made", "Module 9")

# 5 — Setting security requirements
d.content_slide("Setting Security Requirements for a New Solution",
    "Not “add every security service” — derived from what Meridian Loyalty actually handles", "Module 9", dark=True)

# 6 — Exam trap: deriving requirements
d.quad_box_slide("COMMON EXAM TRAP", "Derive Requirements — Don't Add Everything", "The exam expects you to read what the workload handles, not reach for every service",
    [("Guest names, emails, transaction history", "personal data across three brands — real, but not payment card data."),
     ("Card numbers stay in each brand's POS systems", "Meridian Loyalty never touches them at all."),
     ("That's encryption plus access control", "not PCI-DSS-scope controls it was never in scope for."),
     ("The result", "strong protection for what it actually handles — nothing bolted on for its own sake.")],
    note="One line: derive requirements from the actual data. Meridian Loyalty needs strong protection for personal data, not PCI-DSS scope it was never in.")

# 7 — Secrets Manager vs Parameter Store
d.table_slide("Module 9", "Secrets Manager vs. Parameter Store", "Which one actually needs automatic rotation",
    ["Need", "Right service"],
    [["Database password — must rotate automatically on a schedule", "AWS Secrets Manager"],
     ["Static config values — no rotation required", "Systems Manager Parameter Store (cheaper)"],
     ["Third-party API key needing custom rotation", "AWS Secrets Manager, with a custom rotation function"],
     ["Non-sensitive feature flags", "Systems Manager Parameter Store"]],
    col_widths=[7.6, 5.0],
    note="Secrets Manager: automatic rotation is the deciding factor, not just “it's a secret.”")

# 8 — Exam trap: Secrets Manager default
d.quad_box_slide("COMMON EXAM TRAP", "Rotation Need vs. Reflexive Default", "Secrets Manager isn't automatically the right answer for every stored value",
    [("“Needs automatic rotation”", "points to Secrets Manager."),
     ("“Just needs encrypted storage, no rotation”", "points to Parameter Store, at lower cost."),
     ("Both support KMS encryption", "the difference is rotation, not encryption capability."),
     ("Meridian Loyalty's database password", "rotates automatically — Secrets Manager is the actual fit.")],
    note="One line: rotation requirement decides it, not a reflex toward the more capable-sounding service.")

# 9 — Protecting the guest-facing endpoint
d.content_slide("Protecting Meridian Loyalty's Guest-Facing Endpoint",
    "A public portal is a fundamentally different exposure than anything Café Sol has had so far", "Module 9", dark=True)

# 10 — WAF/Shield split
d.split_card_slide("Module 9", "WAF vs. Shield Standard vs. Shield Advanced", "Three layers, three different jobs",
    "Shield Standard",
    [("Automatic, free, on every resource", "defends against common network and transport layer DDoS attacks"),
     ("Always active", "no setup required, no additional cost")],
    "AWS WAF",
    "Application-layer rule-based inspection",
    ["Blocks SQL injection, XSS, bad IP ranges", "Shield Advanced adds enhanced detection, cost protection, and 24/7 DRT access"])

# 11 — Putting it together
d.numbered_list_slide("Module 9", "Putting It Together: Meridian Loyalty's Security Controls", "Every piece from tonight, in one design", [
    ("KMS encryption at rest, TLS in transit", "for guest personal data, driven by an honest inventory of what's actually handled"),
    ("Secrets Manager for the database password; Parameter Store for static config", "matched to whether rotation is the real requirement"),
    ("Shield Standard (automatic) plus WAF", "protecting the public guest portal, with Shield Advanced held in reserve"),
    ("Module 3's SCPs, GuardDuty, and Security Hub", "already in effect the moment the account was provisioned"),
])

# 12 — Applying Module 3's tooling
d.numbered_list_slide("Module 9", "Module 3's Guardrails, Now Applied for Real", "Not new tooling — the same tooling, already covering Meridian Loyalty", [
    ("Service Control Policies already constrain the account", "before anyone on the team writes a single IAM policy"),
    ("GuardDuty starts monitoring automatically", "no separate enablement step for this workload"),
    ("Security Hub aggregates Meridian Loyalty's findings", "into the same organization-wide view Module 3 built"),
], note="This is the same payoff Module 8 found with Resilience Hub and Route 53 ARC — plug in, don't rebuild.")

# 13 — Domain 1 to Domain 2 callback
d.table_slide("Module 9", "Two Halves of One Security Picture", "Module 3 and this module aren't redundant — they're complementary",
    ["", "What it covers"],
    [["Module 3 (Domain 1)", "Org-wide guardrails: SCPs, org-wide GuardDuty, aggregated Security Hub — for every account"],
     ["Module 9 (Domain 2)", "The per-workload decision: data protection, credential management, endpoint defense — for Meridian Loyalty specifically"]],
    col_widths=[3.2, 9.4])

# 14 — Common mix-ups
d.resource_list_slide("Module 9", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Module 3 already covered this — it's redundant”", "Module 3 built the guardrails; this module is the per-workload decision it supports."),
    ("“Secrets Manager is always the right choice for anything sensitive”", "Rotation need is the deciding factor — Parameter Store fits static values just as validly."),
    ("“Shield Standard means no DDoS protection is needed elsewhere”", "It's a free baseline — WAF and, situationally, Shield Advanced still matter."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 10 continues Domain 2 with Task 2.4: designing reliability for Meridian Loyalty as it scales", "Module 9")

# 16 — Recap
d.content_slide("Recap",
    "Requirements derived from actual data, Secrets Manager vs. Parameter Store matched to rotation need, WAF and Shield layered correctly, Module 3's guardrails already in effect", "Module 9", dark=True)

# 17 — Closing
d.closing_slide("Determining Security Controls", "for New Solutions", "Next up: designing reliability for Meridian Loyalty as it scales")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
