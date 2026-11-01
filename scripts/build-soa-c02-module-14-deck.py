"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/14-implementing-cost-optimization-strategies.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-14-deck.py

Paired with instructor-private/14-implementing-cost-optimization-strategies-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "14-implementing-cost-optimization-strategies.pptx")

d = Deck(14, "Implementing Cost Optimization Strategies",
          "Domain 5 made sure everything connects and can be troubleshot. Domain 6 asks whether it's costing what it should.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 14 · Lecture", ["Implementing Cost", "Optimization Strategies"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 14", "Question of the Day", "Before we start",
    [("An account's spend spikes unexpectedly, but never crosses any budget threshold anyone set", "How would you catch that?"),
     ("Recap: Domain 5 made sure everything connects, delivers content, and can be troubleshot", "Domain 6 asks whether it's costing what it should"),
     ("Tonight's task", "Domain 6, Task 6.1 — the first module of Domain 6: cost optimization strategies")])

# 3 — Objectives
d.numbered_list_slide("Module 14", "Objectives", "Five things by the end of tonight", [
    ("Distinguish when Savings Plans or Reserved Instances fit versus Spot Instances", "the commitment-vs-interruption tradeoff"),
    ("Distinguish Compute Optimizer from Cost Explorer", "and know what each one is for"),
    ("Distinguish AWS Budgets from Cost Anomaly Detection", "threshold-based vs. pattern-based alerting"),
    ("Explain why rightsizing recommendations need real utilization data behind them", "not guesswork"),
    ("Design a cost optimization strategy for a stated workload and spend pattern", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Connected and Troubleshootable — But Is It Costing What It Should?",
    "Domain 5 handled connectivity. Domain 6 finds savings and catches spend surprises.", "Module 14")

# 5 — Section intro: Savings Plans/RI vs Spot
d.content_slide("Savings Plans and Reserved Instances vs. Spot Instances",
    "All three beat On-Demand pricing — they trade off commitment against reliability", "Module 14", dark=True)

# 6 — Exam trap: Savings Plans/RI vs Spot
d.quad_box_slide("COMMON EXAM TRAP", "Commitment vs. Interruption", "The deepest discount comes with the biggest tradeoff",
    [("Savings Plans / Reserved Instances", "commitment-based — steady, predictable, always-on usage."),
     ("Spot Instances", "deepest discount — AWS can reclaim capacity with short notice."),
     ("Steady, must-not-interrupt usage", "Savings Plans or Reserved Instances."),
     ("Flexible, fault-tolerant usage", "Spot Instances, for the deepest discount.")],
    note="One line: usage that can't be interrupted needs Savings Plans or RIs — usage that can tolerate it can go Spot for the deepest discount.")

# 7 — Applied
d.table_slide("Module 14", "Savings Plans/RIs vs. Spot, Applied", "Matching the workload to the right discount",
    ["Workload", "Right discount mechanism"],
    [["Steady baseline compute expected to run regardless of demand", "Savings Plans or Reserved Instances"],
     ["Fault-tolerant nightly batch job that can restart if interrupted", "Spot Instances — deepest discount"]],
    col_widths=[7.6, 5.0],
    note="Must-not-interrupt points to Savings Plans/RIs; can-restart-if-interrupted points to Spot.")

# 8 — Section intro: Compute Optimizer vs Cost Explorer
d.content_slide("Compute Optimizer vs. Cost Explorer",
    "Both help with cost — but they answer very different questions", "Module 14")

# 9 — Exam trap: Compute Optimizer vs Cost Explorer
d.quad_box_slide("COMMON EXAM TRAP", "Utilization vs. Spend Trends", "Is this resource right-sized, or where is spend headed",
    [("Compute Optimizer", "actual utilization metrics — specific rightsizing recommendations."),
     ("Cost Explorer", "spend and usage trends — visualized and forecasted."),
     ("Is this resource the right size?", "Compute Optimizer, based on real utilization."),
     ("Where is spend trending?", "Cost Explorer, across services, accounts, and tags.")],
    note="One line: a specific rightsizing call needs Compute Optimizer — a spend trend needs Cost Explorer.")

# 10 — Applied
d.table_slide("Module 14", "Compute Optimizer vs. Cost Explorer, Applied", "Matching the question to the right tool",
    ["Question", "Right tool"],
    [["Is this specific EC2 instance over-provisioned for its real usage?", "Compute Optimizer — utilization-based"],
     ["Where has spend trended over the last six months, by service?", "Cost Explorer — spend visualization"]],
    col_widths=[7.6, 5.0],
    note="A resource-level sizing question is Compute Optimizer; a spend-trend question is Cost Explorer.")

# 11 — Section intro: Budgets vs Cost Anomaly Detection
d.content_slide("AWS Budgets vs. Cost Anomaly Detection",
    "Both alert on cost — but they're triggered by different things", "Module 14", dark=True)

# 12 — Exam trap: Budgets vs Cost Anomaly Detection
d.quad_box_slide("COMMON EXAM TRAP", "Known Threshold vs. Unusual Pattern", "One needs a number set in advance, the other doesn't",
    [("AWS Budgets", "alerts on a threshold you define — a dollar amount or percentage."),
     ("Cost Anomaly Detection", "machine learning — alerts on unusual deviation from the normal pattern."),
     ("A known threshold to alert on", "AWS Budgets."),
     ("An unexpected pattern, no threshold set", "Cost Anomaly Detection.")],
    note="One line: a threshold you can name in advance is Budgets — a pattern break with no such threshold is Cost Anomaly Detection.")

# 13 — Applied
d.table_slide("Module 14", "Budgets vs. Cost Anomaly Detection, Applied", "Matching the alert need to the right tool",
    ["Requirement", "Right tool"],
    [["Alert when monthly spend crosses $10,000", "AWS Budgets — a predefined threshold"],
     ["Catch an unusual spend spike that stays under every threshold anyone set", "Cost Anomaly Detection — pattern-based"]],
    col_widths=[7.6, 5.0],
    note="A specific dollar or percentage line is Budgets; an unpredicted pattern break is Cost Anomaly Detection.")

# 14 — Putting it together
d.numbered_list_slide("Module 14", "Putting It Together: Optimizing Meridian's Costs", "Every piece from tonight, in one strategy", [
    ("Savings Plans for Meridian Loyalty's steady baseline, Spot Instances for Café Sol's nightly batch jobs", "matching the discount mechanism to each workload's tolerance for interruption"),
    ("Compute Optimizer reviewed monthly across all three systems", "rightsizing based on actual utilization, not guesswork"),
    ("Cost Explorer for the monthly spend review with leadership, broken down by service and tag", "showing where budget is actually going"),
    ("AWS Budgets on each team's allocation, paired with account-wide Cost Anomaly Detection", "catching both known-threshold overages and unpredicted spend patterns"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 14", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Spot Instances are always the best choice since they're cheapest”", "Only for workloads that can tolerate AWS reclaiming the capacity."),
    ("“Cost Explorer can tell you which instance to downsize”", "That's Compute Optimizer's job — it analyzes actual utilization."),
    ("“Cost Anomaly Detection needs a threshold, just like Budgets”", "It specifically doesn't — it learns a normal pattern instead."),
], dark=True)

# 16 — Recap
d.content_slide("Recap",
    "Savings Plans/RIs vs. Spot, Compute Optimizer vs. Cost Explorer, Budgets vs. Cost Anomaly Detection", "Module 14", dark=True)

# 17 — Closing
d.closing_slide("Implementing Cost", "Optimization Strategies", "Domain 6 underway — next up: compute and storage performance, closing the course")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
