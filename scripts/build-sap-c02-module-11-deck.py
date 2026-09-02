"""
Builds certifications/sap-c02/lectures/11-designing-performance-efficiency-for-meridian-loyalty.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-11-deck.py

Paired with instructor-private/11-designing-performance-efficiency-for-meridian-loyalty-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02", "lectures",
                    "11-designing-performance-efficiency-for-meridian-loyalty.pptx")

d = Deck(11, "Designing Performance Efficiency for Meridian Loyalty",
          "Module 10 made sure it doesn't fall over. Tonight makes sure it's actually fast.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 11 · Lecture", ["Designing Performance Efficiency", "for Meridian Loyalty"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 11", "Question of the Day", "Before we start",
    [("A guest opens the app from a hotel in another city", "What makes that request fast — and what makes the operations team's reporting query NOT slow it down?"),
     ("Recap: Module 10 made sure Meridian Loyalty scales under load", "Elasticity, scheduled and target tracking scaling, SQS decoupling, DynamoDB capacity modes"),
     ("Tonight's task", "Domain 2, Task 2.5 — matching the right resource to the right job, not just adding more of everything")])

# 3 — Objectives
d.numbered_list_slide("Module 11", "Objectives", "Five things by the end of tonight", [
    ("Match an EC2 instance family to a workload's resource profile", "instead of defaulting to general purpose"),
    ("Explain Graviton's cost/performance trade-off", "for compatible workloads"),
    ("Choose between CloudFront and Global Accelerator", "for a given performance requirement"),
    ("Explain how Aurora Read Replicas offload reporting queries", "from the transactional path"),
    ("Design a complete performance efficiency strategy", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("From Scaling Under Load to Being Fast for Every Guest",
    "Module 10 made sure nothing breaks. Tonight makes sure every request is actually quick", "Module 11")

# 5 — Compute intro
d.content_slide("Choosing the Right Compute for Meridian Loyalty",
    "Which instance family Auto Scaling actually launches is its own decision", "Module 11", dark=True)

# 6 — Exam trap: instance family fit
d.quad_box_slide("COMMON EXAM TRAP", "Match the Family to the Bottleneck", "Bigger and more expensive isn't automatically better",
    [("General purpose", "balances compute, memory, and networking — Meridian Loyalty's typical web/app tier."),
     ("Compute optimized", "favors CPU — the overnight tier-recalculation batch job."),
     ("Memory optimized", "favors RAM — large in-memory analytics, not a current Meridian Loyalty need."),
     ("Graviton", "better price-performance for compatible workloads, across several families.")],
    note="One line: read the actual bottleneck — CPU-bound, memory-bound, or balanced — before picking a family.")

# 7 — Instance family table
d.table_slide("Module 11", "Where Each Family Actually Fits", "Applied to Meridian Loyalty's real workloads",
    ["Workload", "Right family"],
    [["Everyday web and application tier", "General purpose"],
     ["Overnight tier-recalculation batch job", "Compute optimized"],
     ["A future large in-memory analytics job", "Memory optimized"],
     ["Any compatible workload, for lower cost per unit of performance", "Graviton (across families)"]],
    col_widths=[7.6, 5.0],
    note="Memory-optimized for the ordinary web tier wastes money on RAM the workload doesn't need.")

# 8 — CloudFront/GA intro
d.content_slide("Getting Guests Close to Their Data",
    "Guests open the app from wherever they happen to be — two services get traffic closer, differently", "Module 11")

# 9 — Exam trap: CloudFront vs Global Accelerator
d.quad_box_slide("COMMON EXAM TRAP", "Cacheable Content vs. Live Traffic", "They solve different problems, not the same one twice",
    [("“Content can be cached”", "points to CloudFront — static assets, cacheable API responses."),
     ("“Must reach the origin every time”", "points to Global Accelerator — live, uncacheable traffic."),
     ("Global Accelerator supports TCP/UDP generally", "not just HTTP/HTTPS, with static anycast IPs."),
     ("Not competing options", "a well-designed architecture often uses both, for different traffic.")],
    note="One line: cacheable content is CloudFront. Traffic that must hit the live app every time is Global Accelerator.")

# 10 — CloudFront vs GA split card
d.split_card_slide("Module 11", "CloudFront vs. Global Accelerator, Applied", "Different parts of Meridian Loyalty's traffic, different service",
    "Amazon CloudFront",
    [("Static assets, cacheable balance-check responses", "cached at edge locations close to guests"),
     ("Reduces latency and origin load", "for anything that can be cached at all")],
    "AWS Global Accelerator",
    "Live point-redemption API calls",
    ["Must reach the origin every time", "Static anycast IPs, automatic failover across Regions"])

# 11 — Aurora Read Replicas intro
d.content_slide("Offloading Reporting from the Transactional Path",
    "A different problem from Module 10's ElastiCache — isolating a workload, not caching hot reads", "Module 11", dark=True)

# 12 — Read replicas applied
d.numbered_list_slide("Module 11", "Aurora Read Replicas, Applied to Meridian Loyalty", "Isolating analytical load from transactional load", [
    ("The operations team runs reporting queries", "points earned by brand, redemption trends — scanning large amounts of data"),
    ("Run directly against the primary, they'd compete with guests", "for the same database capacity, mid-transaction"),
    ("Read Replicas are additional, current read-only copies", "kept in sync through Aurora's native replication"),
    ("The transactional path keeps its full capacity", "undisturbed by a long-running analytical query"),
], note="Different tool from ElastiCache: this isolates a kind of workload, not a repeated hot read.")

# 13 — Putting it together
d.numbered_list_slide("Module 11", "Putting It Together: Meridian Loyalty's Performance Strategy", "Every piece from tonight, in one design", [
    ("Instance families matched to actual workload", "general purpose for web/app, compute optimized for batch, Graviton where compatible"),
    ("CloudFront caching static assets and cacheable responses", "at the edge, close to guests wherever they are"),
    ("Global Accelerator routing live, uncacheable API traffic", "to the closest healthy endpoint over AWS's backbone"),
    ("Aurora Read Replicas absorbing reporting queries", "keeping analytical load off the transactional primary entirely"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 11", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Bigger instances are always better”", "Match the family to the actual bottleneck — CPU, memory, or balanced."),
    ("“CloudFront and Global Accelerator do the same job”", "One caches content; the other routes live, uncacheable traffic."),
    ("“Read Replicas and ElastiCache solve the same problem”", "One isolates a workload type; the other caches repeated hot reads."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 12 closes out Domain 2 with Task 2.6: cost optimization for Meridian Loyalty as a new solution", "Module 11")

# 16 — Recap
d.content_slide("Recap",
    "Instance families matched to bottlenecks, CloudFront for cacheable content, Global Accelerator for live traffic, Read Replicas isolating reporting", "Module 11", dark=True)

# 17 — Closing
d.closing_slide("Designing Performance Efficiency", "for Meridian Loyalty", "Next up: cost optimization, closing out Domain 2")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
