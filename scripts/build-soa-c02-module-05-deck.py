"""
Builds certifications/soa-c02/lectures/05-implementing-high-availability-and-resilient-environments.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-05-deck.py

Paired with instructor-private/05-implementing-high-availability-and-resilient-environments-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02", "lectures",
                    "05-implementing-high-availability-and-resilient-environments.pptx")

d = Deck(5, "Implementing High Availability and Resilient Environments",
          "Module 4 made sure capacity keeps up with demand. This module asks what happens when a piece of it fails.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 5 · Lecture", ["Implementing High Availability", "and Resilient Environments"])

# 2 — QOTD + recap + framing
d.numbered_list_slide("Module 5", "Question of the Day", "Before we start",
    [("A single EC2 instance behind Meridian Loyalty's checkout service just failed", "Does a customer notice, or does something else already have this covered?"),
     ("Recap: Module 4 matched scaling mechanisms to demand shape", "This module asks a different question — surviving failure, not just load"),
     ("Tonight's task", "Domain 2, Task 2.2 — Multi-AZ, Route 53 failover, and ELB cross-zone load balancing")])

# 3 — Objectives
d.numbered_list_slide("Module 5", "Objectives", "Five things by the end of tonight", [
    ("Explain what Multi-AZ deployments actually protect against", "and what they don't"),
    ("Distinguish an RDS Multi-AZ standby from an Aurora Replica", "same goal, two different mechanisms"),
    ("Describe Route 53 health checks and DNS failover", "redirecting traffic away from an unhealthy endpoint"),
    ("Explain what cross-zone load balancing changes", "traffic distribution across AZs, not within one"),
    ("Design a resilient architecture for a stated availability requirement", "the actual exam skill tonight"),
])

# 4 — Section intro: Multi-AZ
d.content_slide("Multi-AZ: Surviving the Loss of a Data Center",
    "Redundant resources across at least two Availability Zones — so one AZ's failure doesn't take down the app", "Module 5", dark=True)

# 5 — Exam trap 1
d.quad_box_slide("COMMON EXAM TRAP", "What Multi-AZ Actually Covers", "A data center failure, not a Region failure",
    [("RDS Multi-AZ standby", "synchronous, passive — serves no reads, exists purely for failover."),
     ("Aurora Replica", "serves reads continuously, promoted automatically on failure."),
     ("Protects against", "the loss of one data center — power, networking, hardware."),
     ("Does NOT protect against", "a Region-wide event — that needs cross-Region replication.")],
    note="One line: Multi-AZ survives losing a data center, not losing a Region.")

# 6 — Applied
d.table_slide("Module 5", "Multi-AZ, Applied", "Matching the requirement to the right mechanism",
    ["Requirement", "Right mechanism"],
    [["Automatic failover, standby idle until needed", "RDS Multi-AZ standby replica"],
     ["Failover target already serving useful read traffic", "Aurora Replica, promoted on failure"]],
    col_widths=[6.6, 6.0],
    note="A requirement for the standby to already be useful points to Aurora, not a plain RDS standby.")

# 7 — Section intro: Route 53
d.content_slide("Route 53 Health Checks and DNS Failover",
    "Routing traffic away from an endpoint that's failed entirely — not just one component of it", "Module 5")

# 8 — Exam trap 2
d.quad_box_slide("COMMON EXAM TRAP", "DNS Failover Is Not Instant", "It changes what a query resolves to — not an existing connection",
    [("Health check", "monitors an endpoint, marks it healthy or unhealthy."),
     ("Failover routing policy", "returns the secondary's address once the primary fails its check."),
     ("Governed by TTL", "clients keep a cached record until it expires."),
     ("Not connection-level failover", "in-progress connections aren't redirected instantly by DNS alone.")],
    note="One line: DNS failover changes future lookups — cached clients keep going to the old address until TTL expires.")

# 9 — Applied
d.table_slide("Module 5", "Route 53 Failover, Applied", "What the scenario is actually asking for",
    ["Scenario detail", "What it's pointing at"],
    [["Redirect all NEW traffic once primary Region fails its health check", "Route 53 health check + failover routing policy"],
     ["Near-instant failover for connections already in progress", "A layer below DNS — ELB or database endpoint failover, not Route 53 alone"]],
    col_widths=[7.0, 5.6],
    note="TTL is the detail that gives this one away — DNS failover is never instant for cached clients.")

# 10 — Section intro: cross-zone LB
d.content_slide("ELB Cross-Zone Load Balancing",
    "Changes what “distribute across AZs” means at the individual instance level", "Module 5", dark=True)

# 11 — Exam trap 3
d.quad_box_slide("COMMON EXAM TRAP", "ALB vs. NLB Defaults", "One default is on, the other is off — and it can't always change",
    [("Application Load Balancer", "cross-zone enabled by default, can't be turned off."),
     ("Network Load Balancer", "cross-zone disabled by default, must be enabled explicitly."),
     ("Without it", "each node still splits its share evenly per AZ, regardless of instance count."),
     ("Uneven AZ instance counts + NLB", "a strong signal to check whether cross-zone is enabled.")],
    note="One line: ALB defaults to on and locked; NLB defaults to off and must be turned on.")

# 12 — Applied
d.table_slide("Module 5", "Cross-Zone Load Balancing, Applied", "Reading an uneven-traffic scenario correctly",
    ["Observation", "Likely fix"],
    [["NLB, AZ A has 2 instances, AZ B has 8, A's instances are overloaded", "Enable cross-zone load balancing (NLB defaults to off)"],
     ["ALB with the same uneven instance counts", "Already enabled by default — look elsewhere for the cause"]],
    col_widths=[7.6, 5.0],
    note="The load balancer type changes the diagnosis — always check ALB vs. NLB first.")

# 13 — Putting it together
d.numbered_list_slide("Module 5", "Putting It Together: A Resilient Meridian Loyalty", "Every piece from tonight, in one design", [
    ("Aurora Multi-AZ (replicas across AZs) for automatic database failover", "already serving reads beforehand, not sitting idle"),
    ("Cross-zone load balancing on the ALB in front of checkout", "even traffic across AZs even if instance counts drift"),
    ("Route 53 health checks and failover routing watching the whole stack", "ready to redirect to a standby Region if something bigger breaks"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 5", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Multi-AZ protects against a Region going down”", "It protects against losing one data center — Region failure needs cross-Region replication."),
    ("“Route 53 failover is instant for every connection”", "It's DNS-level, governed by TTL — not connection-level failover."),
    ("“Cross-zone load balancing is the same on every load balancer”", "ALB defaults to on and locked; NLB defaults to off."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 6 covers Task 2.3 — recovering data after something goes wrong despite all of this, and closes Domain 2", "Module 5")

# 16 — Recap
d.content_slide("Recap",
    "Multi-AZ vs. Region failure, RDS standby vs. Aurora Replica, Route 53 DNS failover and TTL, ALB vs. NLB cross-zone defaults", "Module 5", dark=True)

# 17 — Closing
d.closing_slide("Implementing High Availability", "and Resilient Environments", "Next up: Module 6 — backup and restore strategies")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
