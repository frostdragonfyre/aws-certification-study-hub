"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/07-creating-a-networking-environment.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-07-deck.py

Paired with instructor-private/07-creating-a-networking-environment-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "07-creating-a-networking-environment.pptx")

d = Deck(7, "Creating a Networking Environment",
          "Get the network wrong and nothing built on top of it is actually secure.")

# 1 — Title
d.title_slide("Module 7 · Lecture", ["Creating a", "Networking Environment"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 7", "Question of the Day", "Before we start",
    [("“The database is on a private subnet” — what actually makes it private?",
      "Module 6 asserted this. Tonight we explain it for real."),
     ("Recap: Module 6 added the database layer", "RDS, separated from the web tier — but not yet deliberately placed on a network"),
     ("Tonight's shift", "From “which service” to “where does it live, and what can reach it”")])

# 3 — Objectives
d.numbered_list_slide("Module 7", "Objectives", "Five things by the end of tonight", [
    ("Explain what a VPC is", "and why every AWS resource with a network presence lives inside one"),
    ("Describe what makes a subnet public or private", "hint: it's not a setting on the subnet"),
    ("Explain the internet gateway and NAT gateway", "two very different jobs, often confused"),
    ("Size a VPC with CIDR notation", "at the level the exam actually expects"),
    ("Diagnose networking symptoms", "from a described problem, not just a diagram"),
])

# 4 — Big picture: four pieces
d.four_up_slide("Module 7", "The Big Picture: Four Pieces", "Everything tonight sits under one of these", [
    ("1", "VPC", "The isolated network you define — sized by CIDR block"),
    ("2", "Subnet", "A slice of the VPC, tied to exactly one Availability Zone"),
    ("3", "Route table", "Decides where a subnet's traffic is allowed to go"),
    ("4", "Gateway", "Internet gateway (public, two-way) or NAT gateway (private, outbound only)"),
])

# 5 — The café's networking problem
d.content_slide("The Café's Networking Problem",
    "Olivia's question: “where, exactly, does any of this actually live?”", "Module 7")

# 6 — VPC: the foundation
d.content_slide("Amazon VPC: The Foundation",
    "Your own logically isolated slice of AWS — default VPC for experiments, custom VPC for everything real", "Module 7")

# 7 — CIDR sizing
d.table_slide("Module 7", "Sizing a VPC: CIDR Blocks", "Smaller suffix = bigger range — the #1 CIDR mix-up",
    ["CIDR suffix", "Addresses available", "Typical use"],
    [["/16", "65,536", "A whole VPC — room to grow"],
     ["/24", "256", "A single subnet — a comfortable default"],
     ["/28", "16", "A small subnet — e.g. a NAT gateway"]],
    col_widths=[2.6, 3.2, 6.4],
    note="Exam trap: a VPC's CIDR block can't simply be shrunk once subnets are carved out of it — size generously up front.")

# 8 — Subnets: one AZ each
d.content_slide("Subnets: One Availability Zone Each",
    "A subnet never spans AZs — which is exactly why HA starts at the subnet layer", "Module 7", dark=True)

# 9 — What makes a subnet public
d.split_card_slide("Module 7", "What Makes a Subnet “Public”?", "Not a setting on the subnet — a route in its route table",
    "Public subnet",
    [("Route table has a route to an internet gateway", "0.0.0.0/0 → internet gateway"),
     ("Typical residents", "load balancers, bastion hosts, NAT gateways")],
    "Private subnet",
    "No route to an internet gateway",
    ["Database tier lives here", "May still route outbound-only through NAT"])

# 10 — Route tables
d.numbered_list_slide("Module 7", "Route Tables: Where Traffic Actually Goes", "Every VPC starts with one", [
    ("Main route table, auto-associated with every subnet", "unless a subnet is explicitly associated with a custom one"),
    ("Default route: stay inside the VPC", "traffic to the VPC's own CIDR block never leaves it — this is how tiers talk to each other"),
    ("Add a route to an internet gateway", "0.0.0.0/0 → IGW — this one route is what makes a subnet public"),
    ("No such route = private", "by definition, not by label"),
], note="Study cue: “public” and “private” are properties of a route table, not a subnet.")

# 11 — Internet gateway
d.content_slide("Internet Gateway: The Front Door",
    "Attaches to the VPC itself, not any one subnet — free, redundant, no capacity planning", "Module 7")

# 12 — NAT gateway
d.numbered_list_slide("Module 7", "NAT Gateway: Outbound Only, On Purpose", "Three facts the exam expects cold", [
    ("Deployed into a public subnet", "even though it serves a private one — it needs its own route to the IGW"),
    ("Scoped to one Availability Zone", "for HA, deploy one NAT gateway per AZ, not one for the whole VPC"),
    ("Billed hourly plus per-GB data processing", "a real, ongoing cost — unlike the internet gateway"),
])

# 13 — Exam trap: NAT GW vs IGW (quad box)
d.quad_box_slide("COMMON EXAM TRAP", "NAT Gateway vs. Internet Gateway", "The exam loves this pair",
    [("NAT Gateway", "Lives in a public subnet, gives PRIVATE subnets outbound-only internet access."),
     ("Internet Gateway", "Attached to the VPC itself, gives PUBLIC subnets two-way internet access."),
     ("One NAT per AZ", "For high availability, don't let one NAT gateway be a single point of failure."),
     ("NAT Instance (legacy)", "Self-managed EC2 alternative — no built-in redundancy. Recognize it, don't design with it.")],
    note="Study cue: NAT gateway is for subnets that need OUT but not IN.")

# 14 — Gateway comparison table
d.table_slide("Module 7", "Gateway Comparison, Side by Side", "Same job category, opposite design",
    ["", "Internet Gateway", "NAT Gateway"],
    [["Attaches to", "The VPC", "A specific public subnet"],
     ["Direction", "Inbound + outbound", "Outbound only"],
     ["Serves", "Public subnets", "Private subnets"],
     ["AZ scope", "VPC-wide", "Single AZ (one per AZ for HA)"],
     ["Cost", "No hourly charge", "Hourly + per-GB processing"]],
    col_widths=[2.6, 4.6, 5.0])

# 15 — Putting it together: the café's V4 network
d.numbered_list_slide("Module 7", "Putting It Together: The Café's V4 Network", "One VPC, two AZs, by design", [
    ("One VPC, sized generously (a /16)", "room to grow without ever needing to resize"),
    ("Two Availability Zones", "resilience starts here — no single AZ is a single point of failure"),
    ("Public + private subnet in each AZ", "web tier public, database tier private — by route table, not by promise"),
    ("One NAT gateway per AZ", "the database patches itself without ever being reachable from the internet"),
], note="This is the literal technical requirement behind Module 1's V4 milestone.")

# 16 — Common mix-ups
d.resource_list_slide("Module 7", "Common Mix-Ups", "Worth getting right before Module 8", [
    ("“The route table must be wrong”", "If a route to the IGW genuinely exists and traffic still can't get in, suspect security groups/NACLs (Module 9) first."),
    ("“A subnet is permanently public or private”", "It's not a label — add a route to an IGW and the same subnet becomes public."),
    ("“NAT gateways are redundant across AZs automatically”", "They are not — one NAT gateway serves one AZ only."),
], dark=True)

# 17 — Assignment
d.content_slide("Before Next Class",
    "Skim the Module 7 guided lab overview — you'll build this exact VPC yourself in the Learner Lab", "Module 7")

# 18 — Closing
d.closing_slide("Creating a", "Networking Environment", "Next up: connecting multiple networks together")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
