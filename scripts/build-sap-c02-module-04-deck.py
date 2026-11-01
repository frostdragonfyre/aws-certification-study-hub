"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/04-designing-reliable-and-resilient-architectures.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-04-deck.py

Paired with instructor-private/04-designing-reliable-and-resilient-architectures-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "04-designing-reliable-and-resilient-architectures.pptx")

d = Deck(4, "Designing Reliable and Resilient Architectures",
          "One workload's DR plan doesn't make resilience consistent, measurable, or governed across an organization.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 4 · Lecture", ["Designing Reliable and", "Resilient Architectures"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 4", "Question of the Day", "Before we start",
    [("SAA-C03's DR module picked one strategy for one workload", "How do you make resilience consistent and measurable across every workload Meridian owns — without reviewing each one by hand?"),
     ("Recap: Modules 2 and 3 built connectivity and governance", "Now every account can reach what it needs to, under consistent security controls"),
     ("Tonight's task", "Domain 1, Task 1.3 — designing reliable and resilient architectures, at the organization level")])

# 3 — Objectives
d.numbered_list_slide("Module 4", "Objectives", "Five things by the end of tonight", [
    ("Explain AWS Backup's organization-wide policies", "enforcing consistent backup practices across every account"),
    ("Describe what AWS Resilience Hub assesses", "and how it scores an application against resilience targets"),
    ("Explain what Route 53 ARC adds beyond basic failover", "readiness checks, routing controls, safety rules"),
    ("Distinguish org-level reliability from a per-workload DR choice", "this module vs. a skill practiced later in Domain 2"),
    ("Recommend org-level reliability tooling for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("From One Workload's DR Plan to Organization-Wide Reliability",
    "Consistent, measurable, and centrally governed — not reinvented by every brand's team independently", "Module 4")

# 5 — AWS Backup org policies
d.content_slide("AWS Backup: Organization-Wide Backup Policies",
    "Defined once at the OU level — inherited automatically, not configured (or forgotten) per account", "Module 4", dark=True)

# 6 — Exam trap: backup consistency
d.quad_box_slide("COMMON EXAM TRAP", "Inconsistent Backups Point to Org-Wide Policy", "Not to fixing each account's configuration one at a time",
    [("The risk", "an engineer quietly disables or misconfigures backups, and nobody notices until it's too late."),
     ("The fix isn't per-account", "reviewing every account's settings by hand doesn't scale and won't catch the next mistake."),
     ("The fix is the OU level", "a backup policy attached to the OU defines frequency, retention, and cross-Region copy once."),
     ("Every account in that OU inherits it", "automatically, including accounts added later, like Ridgeline's.")],
    note="One line: inconsistent or forgotten backups point at an org-wide policy — not a per-account fix.")

# 7 — Resilience Hub
d.content_slide("AWS Resilience Hub: Measuring Resilience Against a Target",
    "Backups existing isn't the same as an application actually meeting its RTO/RPO", "Module 4")

# 8 — Resilience Hub mechanics
d.numbered_list_slide("Module 4", "How Resilience Hub Actually Works", "A resilience policy, an assessment, a score", [
    ("Define the application", "the component AWS resources that make it up"),
    ("Set a resilience policy", "explicit RTO/RPO targets — the same concepts from SAA-C03, now tracked centrally"),
    ("Resilience Hub assesses the real architecture against it", "identifying specific gaps — e.g. no cross-Region replication where the policy requires it"),
], note="Not a pass/fail — a resilience score and concrete, actionable recommendations for closing each gap.")

# 9 — Route 53 ARC
d.content_slide("Route 53 Application Recovery Controller: Coordinated, Safe Failover",
    "At scale, an automated failover that fires incorrectly can do more damage than the outage it was meant to prevent", "Module 4", dark=True)

# 10 — Route 53 ARC three features
d.table_slide("Module 4", "Three Things Route 53 ARC Adds", "Beyond basic health checks and failover routing",
    ["Feature", "What it does"],
    [["Readiness checks", "Continuously verify a standby is actually capable of taking over — not just present"],
     ["Routing controls", "A deliberate, auditable on/off switch — not automation alone"],
     ["Safety rules", "Block a failover action that would make things worse, e.g. removing the last healthy Region"]],
    col_widths=[3.6, 9.0])

# 11 — Exam trap: Domain 1 vs Domain 2
d.quad_box_slide("COMMON EXAM TRAP", "This Module vs. a Per-Workload DR Choice", "Two different skills, tested separately",
    [("“Which DR strategy fits this one new workload?”", "Pilot Light vs. Warm Standby vs. — that's Domain 2, covered later."),
     ("“How do we keep every account consistent?”", "Org-wide backup policy enforcement — that's this module, Domain 1."),
     ("“Does a system actually meet its RTO/RPO?”", "That's a Resilience Hub assessment — also this module."),
     ("“How do we fail over safely across accounts?”", "Route 53 ARC — this module.")],
    note="One line: picking one workload's DR strategy is Domain 2. Making resilience consistent org-wide is this module.")

# 12 — Putting it together
d.numbered_list_slide("Module 4", "Putting It Together: Meridian's Reliability Strategy", "Every piece from tonight, in one design", [
    ("AWS Backup org-wide policy on the Production OU", "frequency, retention, cross-Region copy — inherited automatically by every account"),
    ("Resilience Hub applications and policies per brand", "one place to see whether stated RTO/RPO targets are actually met"),
    ("Route 53 ARC across brands' failover", "readiness checks, routing controls, and safety rules preventing a bad automated decision"),
])

# 13 — Meridian's three brands, reliability view
d.table_slide("Module 4", "Reliability Tooling Applied Across Meridian", "The same three tools, per brand",
    ["Brand", "What org-wide tooling gives them"],
    [["Café Sol", "Backup policy inherited automatically; Resilience Hub confirms its existing DR plan meets targets"],
     ["Haven & Co.", "Same backup policy applied, closing any gaps its own team hadn't configured"],
     ["Ridgeline (post-migration)", "Inherits the same policy on day one — no separate setup required"]],
    col_widths=[3.6, 9.0])

# 14 — Common mix-ups
d.resource_list_slide("Module 4", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Backups being configured means reliability is handled”", "Backups existing isn't the same as meeting a stated RTO/RPO — that's what Resilience Hub checks."),
    ("“Automatic failover alone is always safest”", "A false positive can trigger it incorrectly — routing controls and safety rules exist for exactly this."),
    ("“This module is about picking a DR strategy”", "It isn't — that's Domain 2. This module is org-wide consistency and measurement."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 5 continues Domain 1 with Task 1.4: designing a multi-account AWS environment for Meridian", "Module 4")

# 16 — Recap
d.content_slide("Recap",
    "Org-wide backup policy, Resilience Hub scoring, and Route 53 ARC — reliability made consistent and measurable, not reinvented per brand", "Module 4", dark=True)

# 17 — Closing
d.closing_slide("Designing Reliable and", "Resilient Architectures", "Next up: designing a multi-account AWS environment for Meridian")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
