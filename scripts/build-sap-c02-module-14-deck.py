"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/14-improving-reliability-performance-and-cost.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-14-deck.py

Paired with instructor-private/14-improving-reliability-performance-and-cost-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "14-improving-reliability-performance-and-cost.pptx")

d = Deck(14, "Improving Reliability, Performance, and Cost",
          "Module 13 reviewed the process. Tonight covers the other three legs of continuous improvement.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 14 · Lecture", ["Improving Reliability,", "Performance, and Cost"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 14", "Question of the Day", "Before we start",
    [("Café Sol scores well in a Resilience Hub assessment", "Does that prove it survives a real failure, or just that it looks like it should on paper?"),
     ("Recap: Module 13 reviewed Café Sol's operations and security", "Well-Architected reviews, Trusted Advisor, runbooks, Access Analyzer"),
     ("Tonight's task", "Domain 3, Tasks 3.3–3.5 — reliability, performance, and cost, using six months of real data")])

# 3 — Objectives
d.numbered_list_slide("Module 14", "Objectives", "Four things by the end of tonight", [
    ("Distinguish Resilience Hub's assessment from FIS's real testing", "on paper vs. actually proven"),
    ("Explain why Compute Optimizer is more precise for an existing workload", "real usage history vs. none"),
    ("Distinguish Savings Plans coverage from utilization", "and what each one actually tells you"),
    ("Design a complete improvement plan for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Three Questions, One System, Six Months of Real Data",
    "Is it actually reliable, correctly sized, and worth what it costs — not assumed, but verified", "Module 14")

# 5 — Reliability intro
d.content_slide("Testing Reliability, Not Just Designing It",
    "Module 8 assessed a design before it ever ran. Café Sol has actually been running for six months", "Module 14", dark=True)

# 6 — Exam trap: Resilience Hub vs FIS
d.quad_box_slide("COMMON EXAM TRAP", "Assessing a Design vs. Actually Testing It", "A passing score and a proven system aren't the same thing",
    [("Resilience Hub assesses the design", "configuration, redundancy, backup — without anything breaking."),
     ("FIS actually injects real faults", "terminating an instance, throttling an API, in a controlled experiment."),
     ("A passing score isn't proof", "only an actual test proves assessed resilience holds up for real."),
     ("Sofía runs both against Café Sol", "Resilience Hub assesses it; FIS proves the failover really executes.")],
    note="One line: Resilience Hub assesses without breaking anything. FIS actually breaks something, safely, to prove it.")

# 7 — Resilience Hub + FIS applied
d.table_slide("Module 14", "Assessment and Proof, Applied to Café Sol", "Two tools, two different kinds of confidence",
    ["Question", "Right tool"],
    [["Does the design meet its resilience policy, on paper?", "AWS Resilience Hub"],
     ["Does the failover actually execute when something really breaks?", "AWS Fault Injection Service"],
     ["Confirming both, in a controlled game day", "Resilience Hub, then FIS"]],
    col_widths=[7.6, 5.0],
    note="This is chaos engineering, SAP-C02 style: verify resilience by testing it, not just scoring it.")

# 8 — Compute Optimizer intro
d.content_slide("Right-Sizing with Real Usage Data",
    "A new workload has no history. Café Sol, six months in, has exactly what a new workload lacks", "Module 14")

# 9 — Compute Optimizer applied
d.numbered_list_slide("Module 14", "Compute Optimizer, Applied to Café Sol's Fleet", "Evidence-based, not generic best-practice guesses", [
    ("Analyzes historical CloudWatch utilization", "CPU, memory, network — across EC2, ASGs, EBS, and Lambda"),
    ("An instance sized for a launch-day guess", "that turned out too large for actual demand"),
    ("Another instance running quietly hotter than it should", "under-provisioned, and risking a real performance problem"),
    ("Precise because it's built from six real months", "not a generic recommendation applied to any workload"),
], note="Meridian Loyalty at launch can't get this kind of recommendation — it has no usage history yet.")

# 10 — Cost audit intro
d.content_slide("Auditing What's Already Being Spent",
    "Module 12 was forward-looking. Six months of real spend now exists to check those choices against", "Module 14", dark=True)

# 11 — Exam trap: coverage vs utilization
d.quad_box_slide("COMMON EXAM TRAP", "Coverage vs. Utilization", "Two Savings Plans metrics, pointing to opposite fixes",
    [("Coverage: how much usage is discounted", "the percentage of eligible usage covered by a commitment."),
     ("Utilization: how much commitment is used", "the percentage of the purchased commitment actually consumed."),
     ("Low coverage points to more commitment", "real usage is happening at On-Demand rates that could be discounted."),
     ("Low utilization points to less, not more", "the existing commitment is already too large for actual usage.")],
    note="One line: low coverage means buy more. Low utilization means the opposite — don't buy more, it's already oversized.")

# 12 — Coverage/utilization applied
d.table_slide("Module 14", "Coverage and Utilization, Applied to Café Sol", "Different readings, different fixes",
    ["Finding", "What it means"],
    [["High coverage, low utilization", "Commitment may be oversized for actual usage — don't add more"],
     ["Low coverage, high utilization", "Real usage exceeds the commitment — buying more captures a discount"],
     ["High coverage, high utilization", "The commitment fits actual usage well — no change needed"]],
    col_widths=[5.6, 7.0],
    note="Reading which metric a scenario describes is the whole exam question here.")

# 13 — Putting it together
d.numbered_list_slide("Module 14", "Putting It Together: Café Sol's Improvement Plan", "Every piece from tonight, in one design", [
    ("Resilience Hub assessing the design, FIS testing it for real", "in a controlled game day — verified, not just assumed"),
    ("Compute Optimizer's evidence-based recommendations", "built from six real months of usage data"),
    ("Savings Plans coverage and utilization, reviewed separately", "pointing to different fixes depending on the actual gap"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 14", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“A passing Resilience Hub score proves resilience”", "It assesses the design on paper — FIS is what actually proves it."),
    ("“Compute Optimizer recommendations are just guesses”", "They're built from real historical utilization data, not generic advice."),
    ("“Low coverage and low utilization have the same fix”", "One means buy more commitment; the other means the opposite."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 15 begins Domain 4: migration and modernization — starting with Ridgeline Diner Co.", "Module 14")

# 16 — Recap
d.content_slide("Recap",
    "Resilience Hub assessing, FIS proving, Compute Optimizer using real history, coverage and utilization pointing to opposite fixes", "Module 14", dark=True)

# 17 — Closing
d.closing_slide("Improving Reliability,", "Performance, and Cost", "Next up: Domain 4 begins — migration and modernization")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
