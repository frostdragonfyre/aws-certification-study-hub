"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/16-planning-for-disaster.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-16-deck.py

Paired with instructor-private/16-planning-for-disaster-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "16-planning-for-disaster.pptx")

d = Deck(16, "Planning for Disaster",
          "Multi-AZ protects against a data center failing. It does nothing if the whole Region does.")

# 1 — Title
d.title_slide("Module 16 · Lecture", ["Planning for", "Disaster"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 16", "Question of the Day", "Before we start",
    [("Everything built this course assumes the café's AWS Region is available",
      "What actually happens if that entire Region goes down — not a server, not an AZ, the whole Region?"),
     ("Recap: sixteen modules of building the café's architecture", "VPC, RDS Multi-AZ, CloudFormation, decoupling, caching, serverless, a data lake"),
     ("Tonight's shift", "From “we never planned for it” to a deliberate, chosen recovery strategy")])

# 3 — Objectives
d.numbered_list_slide("Module 16", "Objectives", "Five things by the end of tonight", [
    ("Define RTO and RPO", "and explain what each one actually measures"),
    ("Describe the four AWS disaster recovery strategies", "and how they trade cost against recovery speed"),
    ("Explain how Route 53 supports failover", "between Regions"),
    ("Describe how backups fit into a DR strategy", "and what AWS Backup centralizes"),
    ("Match a DR strategy to a stated RTO/RPO requirement", "the actual exam skill tonight"),
])

# 4 — The café's untested assumption
d.content_slide("The Café's Untested Assumption",
    "Multi-AZ protects against an Availability Zone failing. It does nothing if the whole Region does.", "Module 16")

# 5 — RTO and RPO
d.content_slide("RTO and RPO: The Two Numbers That Define “Disaster”",
    "Two specific questions to answer before choosing any strategy at all", "Module 16", dark=True)

# 6 — Exam trap: RTO vs RPO
d.quad_box_slide("COMMON EXAM TRAP", "RTO and RPO Are Frequently Swapped", "Two different questions — read carefully which one a scenario describes",
    [("RTO — Recovery Time Objective", "How long can systems be down? “Offline for at most 2 hours” is RTO."),
     ("RPO — Recovery Point Objective", "How much data can we lose? “Afford to lose at most 15 minutes” is RPO."),
     ("RTO = downtime", "About getting back up — not about data."),
     ("RPO = data loss", "About how recent your last good backup or replica needs to be.")],
    note="Study cue: “how long until we're back up” is RTO. “How much can we lose” is RPO. Don't swap them.")

# 7 — The four DR strategies
d.table_slide("Module 16", "The Four AWS Disaster Recovery Strategies", "Cost trades off directly against recovery speed",
    ["Strategy", "Secondary Region", "RTO / RPO"],
    [["Backup and Restore", "Nothing running — restore from backups", "Hours"],
     ["Pilot Light", "Core kept in sync, rest scaled down", "Tens of minutes"],
     ["Warm Standby", "Scaled-down, fully functional copy running", "Minutes"],
     ["Multi-Site Active/Active", "Full environment, actively serving traffic", "Near-zero"]],
    col_widths=[4.2, 5.0, 2.8],
    note="Cheapest and slowest at the top. Most expensive and fastest at the bottom.")

# 8 — Backup and Restore & Pilot Light
d.split_card_slide("Module 16", "Backup and Restore vs. Pilot Light", "The two lower-cost, slower-recovery strategies",
    "Backup and Restore",
    [("Nothing runs day-to-day", "backups stored, ready to restore if disaster strikes"),
     ("Cheapest option", "but also the longest recovery — provisioning from scratch")],
    "Pilot Light",
    "A small core stays “lit”",
    ["A database kept continuously in sync via replication", "The rest of the environment scales up around it when declared"])

# 9 — Warm Standby & Multi-Site Active/Active
d.split_card_slide("Module 16", "Warm Standby vs. Multi-Site Active/Active", "The two higher-cost, faster-recovery strategies",
    "Warm Standby",
    [("A scaled-down copy runs continuously", "fully functional, handling traffic at reduced capacity"),
     ("Scales up during failover", "recovery in minutes, not tens of minutes")],
    "Multi-Site Active/Active",
    "Both Regions, full capacity, always on",
    ["Not primary and standby — two equal, active sites", "Traffic simply shifts on failure, no scale-up needed at all"])

# 10 — Exam trap: matching speed to strategy
d.quad_box_slide("COMMON EXAM TRAP", "A Tight RTO Rules Out the Slow Strategies", "Read the required recovery speed before picking a strategy",
    [("RTO of minutes or less?", "Backup and Restore and Pilot Light physically cannot meet it."),
     ("That leaves", "Warm Standby or Multi-Site Active/Active, depending on how close to zero."),
     ("Cost mentioned as secondary?", "That's the signal to pick the faster of the two, not the cheaper."),
     ("The wording matters", "regardless of how the rest of the scenario is phrased.")],
    note="Study cue: match the required speed first — cost only breaks the tie between the strategies that can actually meet it.")

# 11 — Route 53
d.content_slide("Amazon Route 53: Routing Traffic Away from a Failed Region",
    "Health checks and failover routing — traffic redirects automatically, no manual DNS change mid-outage", "Module 16", dark=True)

# 12 — AWS Backup
d.content_slide("AWS Backup: The Foundation Under Every Strategy",
    "Every one of the four strategies still depends on backups being current and actually restorable", "Module 16")

# 13 — Matching a DR strategy to a stated requirement
d.table_slide("Module 16", "Matching a DR Strategy to a Stated Requirement", "The actual exam skill — read the requirement, pick the strategy",
    ["Stated requirement", "Best-fit strategy"],
    [["“We can be down for most of a day; minimize cost”", "Backup and Restore"],
     ["“We need to be back up within about 30 minutes”", "Pilot Light"],
     ["“Back up within a few minutes, cost is secondary”", "Warm Standby"],
     ["“We cannot tolerate any real downtime at all”", "Multi-Site Active/Active"]],
    col_widths=[7.6, 4.8])

# 14 — Putting it together
d.numbered_list_slide("Module 16", "Putting It Together: The Café's Disaster Recovery Plan", "A multi-hour outage would be costly — not catastrophic. That points to Pilot Light.", [
    ("RDS replicates continuously to a secondary Region", "the core that stays “lit,” always current"),
    ("Application infrastructure is ready to scale up, not running day-to-day", "keeping standing cost down between disasters"),
    ("Route 53 health checks redirect traffic the moment the primary Region fails", "and Module 11's CloudFormation template stands the rest back up"),
], note="This is the same V6 multi-Region requirement from Module 11 — the template that redeploys the architecture is what stands up Pilot Light when it's needed.")

# 15 — Common mix-ups
d.resource_list_slide("Module 16", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“RTO and RPO both measure downtime”", "RTO measures downtime; RPO measures data loss, as a window of time."),
    ("“Pilot Light is basically Warm Standby”", "Pilot Light's app tier isn't running — it needs tens of minutes to scale up, not minutes."),
    ("“The fastest strategy is always the right one”", "The right strategy matches the stated RTO/RPO — not the fastest option by default."),
], dark=True)

# 16 — Course wrap-up
d.content_slide("Course Wrap-Up",
    "All 16 modules are complete — hands-on practice continues in AWS Academy's guided and challenge labs", "Module 16")

# 17 — Closing
d.closing_slide("Planning for", "Disaster", "SAA-C03 course complete — on to the guided labs and exam prep")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
