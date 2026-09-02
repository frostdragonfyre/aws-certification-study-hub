"""
Builds certifications/sap-c02/lectures/08-designing-a-solution-to-ensure-business-continuity.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-08-deck.py

Paired with instructor-private/08-designing-a-solution-to-ensure-business-continuity-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02", "lectures",
                    "08-designing-a-solution-to-ensure-business-continuity.pptx")

d = Deck(8, "Designing a Solution to Ensure Business Continuity",
          "Module 4 built the tooling. Tonight it gets used for the first time, for real.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 8 · Lecture", ["Designing a Solution to", "Ensure Business Continuity"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 8", "Question of the Day", "Before we start",
    [("Meridian Loyalty tracks real guest reward balances across three brands", "What RTO and RPO does a guest rewards platform actually need — and how do you decide, instead of guessing?"),
     ("Recap: Module 4 built org-wide reliability tooling", "But explicitly stopped short of picking a DR strategy for any one workload"),
     ("Tonight's task", "Domain 2, Task 2.2 — Module 4's tooling, applied to Meridian Loyalty for real")])

# 3 — Objectives
d.numbered_list_slide("Module 8", "Objectives", "Five things by the end of tonight", [
    ("Translate a business requirement into RTO/RPO targets", "for a new solution, from a described business impact"),
    ("Select a DR strategy that fits those targets", "using SAA-C03's four strategies as an actual design decision"),
    ("Compare Aurora Global Database and DynamoDB Global Tables", "for cross-Region data replication"),
    ("Apply Module 4's Resilience Hub and Route 53 ARC", "to this one specific new workload"),
    ("Design a complete continuity solution for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("From Org-Wide Tooling to One Real Decision",
    "Module 4 stopped short of picking a strategy for any one workload. Tonight, that decision gets made", "Module 8")

# 5 — Setting RTO/RPO
d.content_slide("Setting RTO and RPO for a New Solution",
    "Not “as fast as possible” — negotiated from the actual described business impact", "Module 8", dark=True)

# 6 — Exam trap: deriving RTO/RPO
d.quad_box_slide("COMMON EXAM TRAP", "Derive the Target — Don't Recall a Definition", "The exam expects you to read the impact, not just know what RTO/RPO mean",
    [("Guests can't earn or redeem points", "inconvenient and reputationally costly — not a by-the-second emergency."),
     ("A short data gap is recoverable", "manually reconcilable from receipts and support tickets if it comes to that."),
     ("That's a moderate-urgency signal", "not a trading platform's near-zero target, not an internal tool's multi-hour tolerance."),
     ("The result", "RTO: 15 minutes, RPO: 1 minute — tight, but not reflexively maximal.")],
    note="One line: read the described impact first. The RTO/RPO number follows from it — it isn't guessed.")

# 7 — Choosing the strategy
d.table_slide("Module 8", "Matching the Target to a DR Strategy", "SAA-C03's four strategies, applied as an actual decision",
    ["Strategy", "Fits 15 min / 1 min?"],
    [["Backup and Restore", "No — multi-hour RTO doesn't meet the requirement"],
     ["Pilot Light", "Borderline — tens-of-minutes RTO is risky against a hard 15-minute target"],
     ["Warm Standby", "Yes — comfortably meets both, at meaningfully less cost than active/active"],
     ["Multi-Site Active/Active", "Yes, but more capacity than the target actually requires"]],
    col_widths=[3.6, 9.0],
    note="Warm Standby: the cheapest strategy that still comfortably meets both numbers.")

# 8 — Aurora Global Database vs DynamoDB Global Tables
d.split_card_slide("Module 8", "Aurora Global Database vs. DynamoDB Global Tables", "Which one implements Warm Standby's continuous replication",
    "Aurora Global Database",
    [("Relational data, one primary Region", "sub-second replication lag to read replicas elsewhere"),
     ("Fast promotion during failover", "secondary Region promoted to read/write in about a minute")],
    "DynamoDB Global Tables",
    "Multi-Region, multi-active replication",
    ["Every Region accepts both reads and writes", "A different replication model — not just “the DynamoDB version”"])

# 9 — Exam trap: Aurora vs DynamoDB
d.quad_box_slide("COMMON EXAM TRAP", "One Primary Region vs. Multi-Active Writes", "Read for which replication model the scenario actually describes",
    [("“Relational data, one primary, fast promotion”", "points to Aurora Global Database."),
     ("“Every Region must accept writes at once”", "points to DynamoDB Global Tables."),
     ("Not interchangeable", "these are different replication models, not equivalent options for the same problem."),
     ("Meridian Loyalty's core data", "lives in Aurora — so Aurora Global Database is the actual fit here.")],
    note="One line: one primary with fast promotion is Aurora. Multi-Region simultaneous writes is DynamoDB Global Tables.")

# 10 — Applying Module 4's tooling
d.content_slide("Applying Module 4's Org-Wide Tooling to This One Workload",
    "Choosing a strategy and a database doesn't complete the picture on its own", "Module 8")

# 11 — Resilience Hub + Route 53 ARC applied
d.numbered_list_slide("Module 8", "Module 4's Tooling, Now Applied for Real", "Not new tooling — the same tooling, pointed at Meridian Loyalty", [
    ("Resilience Hub gets Meridian Loyalty registered", "with a resilience policy set to RTO: 15 min, RPO: 1 min — then it assesses the real architecture"),
    ("Confirms the design actually meets its targets", "not assumed to work because Warm Standby “sounds right” on paper"),
    ("Route 53 ARC provides the failover mechanism", "readiness checks, a routing control, and safety rules — all from Module 4"),
], note="This is the payoff of Module 4's investment: no brand-new tooling built just for Meridian Loyalty.")

# 12 — Putting it together
d.numbered_list_slide("Module 8", "Putting It Together: Meridian Loyalty's Continuity Solution", "Every piece from tonight, in one design", [
    ("RTO: 15 minutes, RPO: 1 minute", "derived from the actual business impact — not an arbitrary target"),
    ("Warm Standby as the DR strategy", "the cheapest of the four that still comfortably meets both numbers"),
    ("Aurora Global Database for replication", "sub-second lag, roughly one-minute promotion during failover"),
    ("Resilience Hub validates it; Route 53 ARC executes failover", "both inherited directly from Module 4's organizational tooling"),
])

# 13 — Domain 1 to Domain 2 callback
d.table_slide("Module 8", "Two Halves of One Reliability Picture", "Module 4 and this module aren't redundant — they're complementary",
    ["", "What it covers"],
    [["Module 4 (Domain 1)", "Org-wide tooling: backup policy enforcement, Resilience Hub, Route 53 ARC — for every workload"],
     ["Module 8 (Domain 2)", "The per-workload decision: RTO/RPO, DR strategy, replication technology — for Meridian Loyalty specifically"]],
    col_widths=[3.2, 9.4])

# 14 — Common mix-ups
d.resource_list_slide("Module 8", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Module 4 already covered this — it's redundant”", "Module 4 built the tooling; this module is the per-workload decision it supports."),
    ("“Aurora Global Database and DynamoDB Global Tables are interchangeable”", "Different replication models — one primary Region vs. multi-active writes."),
    ("“The design works because it sounds reasonable”", "Resilience Hub actually verifies it meets the stated RTO/RPO — nothing is assumed."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 9 continues Domain 2 with Task 2.3: determining security controls for Meridian Loyalty specifically", "Module 8")

# 16 — Recap
d.content_slide("Recap",
    "RTO/RPO derived from real impact, Warm Standby chosen deliberately, Aurora Global Database implementing it, Module 4's tooling verifying it", "Module 8", dark=True)

# 17 — Closing
d.closing_slide("Designing a Solution to", "Ensure Business Continuity", "Next up: determining security controls for Meridian Loyalty")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
