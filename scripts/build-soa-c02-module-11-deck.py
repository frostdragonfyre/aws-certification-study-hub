"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/11-implementing-networking-features-and-connectivity.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-11-deck.py

Paired with instructor-private/11-implementing-networking-features-and-connectivity-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "11-implementing-networking-features-and-connectivity.pptx")

d = Deck(11, "Implementing Networking Features and Connectivity",
          "Domain 4 protected the data and the traffic inside a VPC. Domain 5 zooms out to how VPCs and networks connect.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 11 · Lecture", ["Implementing Networking", "Features and Connectivity"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 11", "Question of the Day", "Before we start",
    [("VPC A is peered with VPC B, and B is peered with VPC C", "Can a resource in A reach a resource in C?"),
     ("Recap: Domain 4 protected the data itself and the traffic inside a single VPC", "tonight zooms out to how VPCs and networks connect to each other"),
     ("Tonight's task", "Domain 5, Task 5.1 — the first module of Domain 5: networking features and connectivity")])

# 3 — Objectives
d.numbered_list_slide("Module 11", "Objectives", "Five things by the end of tonight", [
    ("Distinguish VPC peering from Transit Gateway", "and know when each fits"),
    ("Explain why VPC peering connections are non-transitive", "the detail that catches people"),
    ("Distinguish Site-to-Site VPN from Direct Connect", "and when each is the right hybrid connection"),
    ("Distinguish a Gateway endpoint from an Interface endpoint", "and which services each one supports"),
    ("Design a connectivity strategy for a stated multi-VPC or hybrid requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Connecting VPCs, and Connecting to Them",
    "Domain 4 secured what's inside a VPC. Tonight is how VPCs reach each other, and how on-premises reaches AWS.", "Module 11")

# 5 — Section intro: Peering vs Transit Gateway
d.content_slide("VPC Peering vs. Transit Gateway",
    "A direct one-to-one connection, or a hub that scales to many", "Module 11", dark=True)

# 6 — Exam trap: Peering vs Transit Gateway
d.quad_box_slide("COMMON EXAM TRAP", "One-to-One vs. Hub-and-Spoke", "And peering doesn't let traffic pass through a third VPC",
    [("VPC peering", "one-to-one, non-transitive — A peered to B, and B to C, doesn't mean A can reach C."),
     ("Transit Gateway", "a regional hub many VPCs attach to — transitive routing, built for scale."),
     ("A few VPCs", "peering's simplicity is enough — no growing mesh to manage."),
     ("Many VPCs, or growing", "four or more, or expected to grow — Transit Gateway avoids the mesh.")],
    note="One line: peering is simple but non-transitive and scales poorly — Transit Gateway is the hub for everything past a few VPCs.")

# 7 — Applied
d.table_slide("Module 11", "VPC Peering vs. Transit Gateway, Applied", "Matching the requirement to the right connection",
    ["Requirement", "Right connection"],
    [["Connect two VPCs, a simple one-off requirement", "VPC peering — simple, free, sufficient for two"],
     ["Ten VPCs today, more expected to be added over time", "Transit Gateway — the hub avoids the growing mesh"]],
    col_widths=[7.6, 5.0],
    note="A VPC count that's growing, or already several, is always the Transit Gateway tell.")

# 8 — Section intro: VPN vs Direct Connect
d.content_slide("Site-to-Site VPN vs. Direct Connect",
    "Both connect on-premises to AWS — over the internet, or off it entirely", "Module 11")

# 9 — Exam trap: VPN vs Direct Connect
d.quad_box_slide("COMMON EXAM TRAP", "Public Internet vs. Dedicated Line", "Fast and encrypted, or consistent and dedicated",
    [("Site-to-Site VPN", "encrypted IPsec tunnel over the public internet — minutes to hours to set up."),
     ("Direct Connect", "a dedicated private physical connection — consistent latency, higher bandwidth."),
     ("Quick and encrypted", "no special hardware, fast setup — Site-to-Site VPN."),
     ("Consistent and dedicated", "predictable performance, setup time isn't the constraint — Direct Connect.")],
    note="One line: need it fast and encrypted, that's VPN — need consistent dedicated performance, that's Direct Connect.")

# 10 — Applied
d.table_slide("Module 11", "VPN vs. Direct Connect, Applied", "Matching the requirement to the right link",
    ["Requirement", "Right link"],
    [["Connectivity needed quickly, encrypted, cost-sensitive", "Site-to-Site VPN — fast, encrypted, lower cost"],
     ["Data-intensive workload, consistent latency required, time to provision available", "Direct Connect — dedicated, predictable performance"]],
    col_widths=[7.6, 5.0],
    note="Needing it now points to VPN; needing consistent dedicated performance points to Direct Connect.")

# 11 — Section intro: Gateway vs Interface endpoints
d.content_slide("Gateway Endpoints vs. Interface Endpoints",
    "Both keep traffic off the public internet — for very different sets of services", "Module 11", dark=True)

# 12 — Exam trap: Gateway vs Interface
d.quad_box_slide("COMMON EXAM TRAP", "Two Kinds of VPC Endpoints", "One is a free route, the other is a priced ENI",
    [("Gateway endpoint", "S3 and DynamoDB only — a free route table entry, no ENI."),
     ("Interface endpoint", "most other services, via PrivateLink — an ENI, hourly plus per-GB cost."),
     ("S3 or DynamoDB, lowest cost", "no ENI needed — a Gateway endpoint."),
     ("Any other AWS service", "SNS, SQS, Systems Manager, and more — an Interface endpoint.")],
    note="One line: S3 and DynamoDB get the free Gateway endpoint — everything else needs an Interface endpoint.")

# 13 — Applied
d.table_slide("Module 11", "Gateway vs. Interface Endpoints, Applied", "Matching the service to the right endpoint",
    ["Requirement", "Right endpoint"],
    [["Private access to an S3 bucket, no added hourly cost", "Gateway endpoint — free route table entry, S3 supported"],
     ["Private access to Systems Manager from a private subnet", "Interface endpoint — PrivateLink, ENI-based"]],
    col_widths=[7.6, 5.0],
    note="S3 or DynamoDB points to Gateway; virtually everything else points to Interface.")

# 14 — Putting it together
d.numbered_list_slide("Module 11", "Putting It Together: Connecting Meridian's Environment", "Every piece from tonight, in one design", [
    ("Transit Gateway connecting Meridian Loyalty's, Café Sol's, and Ridgeline's VPCs", "instead of a growing mesh of individual peering connections"),
    ("Direct Connect as the primary link to Meridian's headquarters, with Site-to-Site VPN as automatic failover", "consistent performance, with a fallback that doesn't share the same physical line"),
    ("Gateway endpoints for S3, Interface endpoints for Systems Manager", "private access at the right cost for each service"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 11", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“If A is peered with B, and B with C, A can reach C”", "VPC peering is non-transitive — that traffic isn't routed at all."),
    ("“Direct Connect is always better than a VPN”", "Direct Connect takes weeks to provision — VPN is fast and often sufficient."),
    ("“Gateway endpoints work for any AWS service”", "Only S3 and DynamoDB — everything else needs an Interface endpoint."),
], dark=True)

# 16 — Recap
d.content_slide("Recap",
    "VPC peering vs. Transit Gateway, Site-to-Site VPN vs. Direct Connect, Gateway vs. Interface endpoints", "Module 11", dark=True)

# 17 — Closing
d.closing_slide("Implementing Networking", "Features and Connectivity", "Domain 5 underway — next up: domains, DNS, and content delivery")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
