"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/06-cost-optimization-and-visibility-strategies.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-06-deck.py

Paired with instructor-private/06-cost-optimization-and-visibility-strategies-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "06-cost-optimization-and-visibility-strategies.pptx")

d = Deck(6, "Cost Optimization and Visibility Strategies",
          "One consolidated bill and a Brand tag are ingredients, not answers.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 6 · Lecture", ["Cost Optimization and", "Visibility Strategies"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 6", "Question of the Day", "Before we start",
    [("Meridian has one consolidated bill and a Brand tag on every resource", "Does that tell Sofía whether this month's spend is normal, or something finance needs to know about right now?"),
     ("Recap: Module 5 built the raw ingredients", "Consolidated billing and consistent tagging — necessary, but not yet actionable on their own"),
     ("Tonight's task", "Domain 1, Task 1.5 — cost optimization and visibility, closing out Domain 1")])

# 3 — Objectives
d.numbered_list_slide("Module 6", "Objectives", "Five things by the end of tonight", [
    ("Explain what Cost Explorer is used for", "and how it differs from a Cost and Usage Report"),
    ("Describe what a Cost and Usage Report provides", "that Cost Explorer's interface doesn't"),
    ("Explain how AWS Budgets supports proactive control", "thresholds, alerts, and budget actions"),
    ("Explain how Cost Anomaly Detection differs from a budget", "pattern-based vs. threshold-based"),
    ("Recommend the right tool for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Raw Ingredients Aren't an Answer",
    "A consolidated bill and a Brand tag don't tell you whether this month's spend is normal", "Module 6")

# 5 — Cost Explorer
d.content_slide("AWS Cost Explorer: Visualizing and Analyzing Spend",
    "Interactive exploration and near-term forecasting — filterable by account, service, Region, or tag", "Module 6", dark=True)

# 6 — CUR
d.content_slide("AWS Cost and Usage Report: The Complete, Granular Export",
    "When Cost Explorer's built-in views aren't enough — the raw data underneath, for custom reporting", "Module 6")

# 7 — Exam trap: Cost Explorer vs CUR
d.quad_box_slide("COMMON EXAM TRAP", "Interactive Exploration vs. Raw Export", "Read for which one a scenario is actually asking for",
    [("“Explore and visualize trends interactively”", "points to Cost Explorer."),
     ("“Custom dashboards outside AWS”", "or the most granular line-item data — both point to CUR."),
     ("They're complementary", "Cost Explorer for exploring through AWS's interface; CUR is the data underneath."),
     ("Not competing tools", "an organization commonly uses both, for different jobs.")],
    note="One line: Cost Explorer explores. CUR exports. Read for which job the scenario describes.")

# 8 — Budgets
d.content_slide("AWS Budgets: Proactive, Threshold-Based Control",
    "Notified before the bill arrives — not after, the way Cost Explorer's forecast alone would leave you", "Module 6", dark=True)

# 9 — Budget actions
d.numbered_list_slide("Module 6", "Budget Actions: Beyond Just a Notification", "A budget can trigger a response, not just an alert", [
    ("A threshold is breached", "cost or usage crosses the defined budget, scoped to an account, OU, tag, or the org"),
    ("A budget action fires automatically", "e.g. applying an SCP restricting further resource creation"),
    ("No manual intervention required", "the moment the threshold is crossed, the response already happened"),
], note="For Meridian: a Sandbox account that blows through its budget gets restricted automatically.")

# 10 — Cost Anomaly Detection
d.content_slide("AWS Cost Anomaly Detection: Catching Unusual Spend Patterns",
    "A fixed threshold catches a known line being crossed — not a spike that's still comfortably under budget", "Module 6")

# 11 — Exam trap: Budgets vs Anomaly Detection
d.quad_box_slide("COMMON EXAM TRAP", "A Fixed Number vs. A Learned Pattern", "The two are complementary, not redundant",
    [("“Alert if spend crosses this dollar amount”", "AWS Budgets — a fixed, defined threshold."),
     ("“Alert if spend looks unusual vs. normal patterns”", "AWS Cost Anomaly Detection — even under any set threshold."),
     ("A scenario can ask for both", "a known limit, and pattern-based detection of anything that looks off."),
     ("Anomaly detection catches it earlier", "before an issue accumulates into an amount a threshold would eventually catch.")],
    note="One line: Budgets watches a number. Anomaly Detection watches a pattern. Use both.")

# 12 — Table: four tools compared
d.table_slide("Module 6", "Four Tools, Four Different Jobs", "Matching the tool to what's actually being asked",
    ["Tool", "Best for"],
    [["Cost Explorer", "Interactive exploration and near-term forecasting"],
     ["Cost and Usage Report", "Granular, custom reporting and external BI tooling"],
     ["AWS Budgets", "Proactive alerts (and automated action) on a known threshold"],
     ["Cost Anomaly Detection", "Catching unusual patterns, independent of any fixed threshold"]],
    col_widths=[4.2, 8.4])

# 13 — Putting it together
d.numbered_list_slide("Module 6", "Putting It Together: Meridian's Cost Strategy", "Every piece from tonight, in one design — closing out Domain 1", [
    ("Cost Explorer, filtered by the Brand tag", "available to finance and each brand's engineering leads"),
    ("CUR delivered to a central, restricted S3 bucket", "feeding Meridian's own BI tooling for per-brand chargeback"),
    ("A Budget per brand's OU, with budget actions on Sandbox", "scoped by tag, alerting the right team directly"),
    ("Cost Anomaly Detection running org-wide", "catching what a threshold would only catch later, if at all"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 6", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Cost Explorer and CUR do the same thing”", "One's for interactive exploration; the other's the raw export for custom reporting."),
    ("“Consolidated billing and tagging already solved cost visibility”", "They made data available and attributable — these tools make it actionable."),
    ("“Anomaly Detection makes Budgets unnecessary”", "Budgets enforces a known limit; Anomaly Detection catches what no threshold defines."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "That's all of Domain 1. Module 7 opens Domain 2 with Task 2.1: designing a deployment strategy for a new solution", "Module 6")

# 16 — Domain 1 recap
d.table_slide("Module 6", "Domain 1, Complete", "Five tasks, five modules, one coherent organizational foundation",
    ["Module", "Task"],
    [["2", "Architecting network connectivity strategies"],
     ["3", "Prescribing security controls at the organization level"],
     ["4", "Designing reliable and resilient architectures"],
     ["5", "Designing a multi-account AWS environment"],
     ["6", "Cost optimization and visibility strategies"]],
    col_widths=[2.2, 10.4])

# 17 — Closing
d.closing_slide("Cost Optimization and", "Visibility Strategies", "Domain 1 complete. Next up: designing a deployment strategy for a new solution")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
