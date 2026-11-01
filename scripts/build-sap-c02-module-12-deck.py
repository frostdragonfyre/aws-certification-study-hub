"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/12-designing-meridian-loyaltys-cost-strategy.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-12-deck.py

Paired with instructor-private/12-designing-meridian-loyaltys-cost-strategy-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "12-designing-meridian-loyaltys-cost-strategy.pptx")

d = Deck(12, "Designing Meridian Loyalty's Cost Strategy",
          "Module 6 closed out Domain 1 with cost tooling. Tonight closes out Domain 2 the same way.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 12 · Lecture", ["Designing Meridian Loyalty's", "Cost Strategy"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 12", "Question of the Day", "Before we start",
    [("Meridian Loyalty now has a steady web tier and an interruptible batch job", "Should both be purchased the same way? Why or why not?"),
     ("Recap: Module 6 closed Domain 1 with org-wide cost tooling", "Cost Explorer, CUR, budgets, tagging standards — but no per-workload purchasing decision"),
     ("Tonight's task", "Domain 2, Task 2.6 — the last piece, and the module that closes out Domain 2")])

# 3 — Objectives
d.numbered_list_slide("Module 12", "Objectives", "Five things by the end of tonight", [
    ("Match a purchase option to a workload's predictability", "and its actual tolerance for interruption"),
    ("Distinguish Compute Savings Plans from EC2 Instance Savings Plans", "and choose correctly between them"),
    ("Explain how Module 6's cost tooling applies automatically", "to a new workload"),
    ("Design a complete cost strategy for a stated scenario", "the actual exam skill tonight"),
    ("Summarize how all six Domain 2 tasks combine", "into one coherent new solution"),
])

# 4 — Problem framing
d.content_slide("Closing Domain 2 the Way Module 6 Closed Domain 1",
    "Module 6 built the tooling. Tonight, the per-workload cost decision gets made", "Module 12")

# 5 — Purchase options intro
d.content_slide("Matching Purchase Options to Workload Predictability",
    "Meridian Loyalty's workloads have different relationships to time and interruption", "Module 12", dark=True)

# 6 — Exam trap: purchase option fit
d.quad_box_slide("COMMON EXAM TRAP", "Match the Option to the Workload's Behavior", "Not “commitment sounds responsible” or “deepest discount wins”",
    [("On-Demand", "no commitment — the right fit before a workload's usage pattern is understood."),
     ("Savings Plans / Reserved Instances", "a usage commitment for a lower rate — fits a steady, predictable baseline."),
     ("Spot Instances", "the deepest discount, in exchange for tolerating reclamation with little notice."),
     ("The batch job vs. the web tier", "one can restart if interrupted; the other can't tolerate that at all.")],
    note="One line: match the option to actual interruption tolerance and predictability, not a reflex toward commitment or discount.")

# 7 — Purchase option table
d.table_slide("Module 12", "Purchase Options, Applied to Meridian Loyalty", "Two workloads, two different right answers",
    ["Workload", "Right purchase option"],
    [["Web and application tier — steady, continuous baseline", "Savings Plan"],
     ["Overnight tier-recalculation batch job — restarts fine if interrupted", "Spot Instances"],
     ["A brand-new workload with no usage history yet", "On-Demand, until the pattern is understood"]],
    col_widths=[7.6, 5.0],
    note="Spot for the batch job: deepest discount, for a workload that was never latency-sensitive anyway.")

# 8 — Compute vs EC2 Instance SP intro
d.content_slide("Compute Savings Plans vs. EC2 Instance Savings Plans",
    "Once Savings Plans are the right tool, there's still a choice to make", "Module 12")

# 9 — Exam trap: flexibility vs discount depth
d.quad_box_slide("COMMON EXAM TRAP", "Flexibility vs. Maximum Discount", "Two Savings Plan types, trading off in opposite directions",
    [("Compute Savings Plans", "any instance family, Region, OS, tenancy — even Fargate and Lambda."),
     ("EC2 Instance Savings Plans", "one specific instance family and Region — the deepest possible discount."),
     ("Meridian Loyalty is onboarding new brands", "and may shift instance families as the platform matures."),
     ("That future favors flexibility", "a Compute Savings Plan, over locking in the last few points of discount.")],
    note="One line: stable and specific favors EC2 Instance Savings Plans. Evolving and uncertain favors Compute Savings Plans.")

# 10 — Compute SP vs EC2 Instance SP split card
d.split_card_slide("Module 12", "Compute SP vs. EC2 Instance SP, Applied", "Which one fits Meridian Loyalty's actual future",
    "Compute Savings Plans",
    [("Dollar-amount commitment per hour", "applies across instance family, Region, OS, tenancy, Fargate, Lambda"),
     ("The right fit for Meridian Loyalty", "flexibility as brands onboard and workloads evolve")],
    "EC2 Instance Savings Plans",
    "Deepest possible discount",
    ["Locked to one instance family and Region", "No flexibility if instance needs shift"])

# 11 — Applying Module 6's tooling intro
d.content_slide("Applying Module 6's Tooling to This One Workload",
    "The same inherit-don't-rebuild pattern from Modules 8 and 9", "Module 12", dark=True)

# 12 — Module 6's tooling applied
d.numbered_list_slide("Module 12", "Module 6's Tooling, Now Applied for Real", "Not new tooling — the same tooling, covering Meridian Loyalty", [
    ("Cost allocation tags, an org-wide standard from Module 6", "applied to every Meridian Loyalty resource"),
    ("The CUR and Cost Explorer already aggregate every account", "picking up Meridian Loyalty's spend automatically once tagged"),
    ("AWS Budgets, set for Meridian Loyalty specifically", "alerts the team if actual spend diverges from the sized plan"),
], note="This is the same payoff Modules 8 and 9 found with Module 4's and Module 3's tooling.")

# 13 — Putting it together
d.numbered_list_slide("Module 12", "Putting It Together: Meridian Loyalty's Cost Strategy", "Every piece from tonight, in one design", [
    ("Savings Plan for the steady web tier, Spot for the batch job", "purchase option matched to actual workload behavior"),
    ("Compute Savings Plans specifically", "favoring flexibility as brands and instance needs evolve"),
    ("Module 6's tags, CUR, Cost Explorer, and Budgets", "already covering Meridian Loyalty, inherited not rebuilt"),
])

# 14 — Two halves callback
d.table_slide("Module 12", "Two Halves of One Cost Picture", "Module 6 and this module aren't redundant — they're complementary",
    ["", "What it covers"],
    [["Module 6 (Domain 1)", "Org-wide cost tooling: Cost Explorer, CUR, budgets, tagging standards — for every account"],
     ["Module 12 (Domain 2)", "The per-workload decision: purchase options, Savings Plan type — for Meridian Loyalty specifically"]],
    col_widths=[3.2, 9.4])

# 15 — Domain 2, Complete
d.table_slide("Module 12", "Domain 2, Complete", "One new solution, six tasks, built from nothing across six weeks",
    ["Module", "Task"],
    [["Module 7", "Deployment strategy"],
     ["Module 8", "Business continuity"],
     ["Module 9", "Security controls"],
     ["Module 10", "Scaling reliably"],
     ["Module 11", "Performance efficiency"],
     ["Module 12", "Cost strategy"]],
    col_widths=[3.2, 9.4])

# 16 — Common mix-ups
d.resource_list_slide("Module 12", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Savings Plans everywhere sounds responsible”", "Match the option to actual predictability and interruption tolerance instead."),
    ("“Spot is cheapest, so use it everywhere”", "The web tier can't tolerate sudden termination — Spot fits the batch job, not it."),
    ("“Module 6 already covered this — it's redundant”", "Module 6 built the tooling; this module is the per-workload decision it supports."),
], dark=True)

# 17 — Closing
d.closing_slide("Designing Meridian Loyalty's", "Cost Strategy", "Domain 2 complete. Next up: Domain 3 begins")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
