"""
Builds certifications/saa-c03/lectures/08-connecting-networks.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-08-deck.py

Paired with instructor-private/08-connecting-networks-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03", "lectures",
                    "08-connecting-networks.pptx")

d = Deck(8, "Connecting Networks",
          "One VPC was Module 7. Tonight is what happens when there's more than one network.")

# 1 — Title
d.title_slide("Module 8 · Lecture", ["Connecting", "Networks"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 8", "Question of the Day", "Before we start",
    [("The café now has two AWS VPCs. How do resources in one reach the other?",
      "Nothing in Module 7 answers this — that module was about ONE VPC."),
     ("Recap: Module 7 built one VPC", "public/private subnets, route tables, internet gateway, NAT gateway"),
     ("Tonight's shift", "From “inside one network” to “connecting multiple networks together”")])

# 3 — Objectives
d.numbered_list_slide("Module 8", "Objectives", "Five things by the end of tonight", [
    ("Explain VPC peering and its core limitation", "not transitive — this trips up almost everyone once"),
    ("Know when Transit Gateway beats a peering mesh", "it's about the math, not just the feature list"),
    ("Distinguish Site-to-Site VPN from Direct Connect", "cost, setup time, and encryption all differ"),
    ("Explain what AWS PrivateLink actually solves", "narrower than peering, and deliberately so"),
    ("Match a described scenario to the right service", "exactly how the exam will ask it"),
])

# 4 — The café's new problem
d.content_slide("The Café's New Problem",
    "A commissary kitchen VPC, and a back-office network that was never moving to AWS", "Module 8")

# 5 — VPC Peering
d.content_slide("VPC Peering: Connecting Two VPCs Directly",
    "Private IPs, never the public internet — the simplest way to connect exactly two VPCs", "Module 8")

# 6 — Peering's limit: not transitive
d.split_card_slide("Module 8", "Peering's Limit: Not Transitive", "The single most tested fact about VPC peering",
    "What works",
    [("VPC A peered directly with VPC B", "A and B can reach each other"),
     ("VPC B peered directly with VPC C", "B and C can reach each other")],
    "What doesn't work",
    "A reaching C through B",
    ["A and C have NO path to each other", "Each pairing needs its OWN direct peering connection"])

# 7 — Peering vs Transit Gateway
d.table_slide("Module 8", "Peering vs. Transit Gateway", "The math is why one replaces the other at scale",
    ["", "VPC Peering", "Transit Gateway"],
    [["Topology", "Direct, one-to-one", "Hub-and-spoke"],
     ["Transitive routing", "No", "Yes"],
     ["Best for", "A small, stable # of VPCs", "Many VPCs, or VPCs + on-prem"],
     ["Connections for n networks", "Up to n(n-1)/2", "n"]],
    col_widths=[3.2, 4.5, 4.5],
    note="4 VPCs fully peered = 6 connections. 10 VPCs = 45. That growth curve is the whole argument for Transit Gateway.")

# 8 — Site-to-Site VPN
d.content_slide("Getting Back to On-Premises: Site-to-Site VPN",
    "An encrypted connection to on-premises, running over the public internet", "Module 8", dark=True)

# 9 — Direct Connect
d.content_slide("When VPN Isn't Enough: AWS Direct Connect",
    "A dedicated physical connection — bypasses the public internet entirely", "Module 8")

# 10 — Exam trap: VPN vs Direct Connect
d.quad_box_slide("COMMON EXAM TRAP", "Site-to-Site VPN vs. Direct Connect", "The exam loves this pair too",
    [("Site-to-Site VPN", "Fast setup, built-in encryption, rides the public internet — variable performance."),
     ("Direct Connect", "Weeks to provision, dedicated physical path, consistent performance — NOT encrypted by default."),
     ("Cost", "VPN: low, pay-as-you-go. Direct Connect: higher, ongoing."),
     ("Need both worlds?", "Run a VPN over a Direct Connect connection for dedicated AND encrypted.")],
    note="Study cue: Direct Connect is private, not automatically encrypted — pair it with VPN if encryption is required.")

# 11 — AWS PrivateLink
d.content_slide("A Different Problem: AWS PrivateLink",
    "Not a network-to-network connection — private access to ONE specific service", "Module 8")

# 12 — Matching the scenario to the service
d.table_slide("Module 8", "Matching the Scenario to the Service", "How the exam actually asks these questions",
    ["Scenario", "Right service"],
    [["Two VPCs, likely to stay just two", "VPC Peering"],
     ["Many VPCs (or VPCs + on-prem), central connectivity", "Transit Gateway"],
     ["On-prem, fast + cheap, encryption required", "Site-to-Site VPN"],
     ["On-prem, consistent dedicated performance", "Direct Connect"],
     ["Reach ONE service privately, not a whole network", "AWS PrivateLink"]],
    col_widths=[7.5, 4.7])

# 13 — Putting it together
d.numbered_list_slide("Module 8", "Putting It Together: The Café's Two Connections", "Two different problems, two different tools", [
    ("VPC Peering", "connects the original location's VPC to the new commissary kitchen's VPC — both are AWS networks"),
    ("Site-to-Site VPN", "connects the original location's on-premises point-of-sale network into AWS — that back office was never moving to the cloud"),
], note="Neither tool substitutes for the other — they connect fundamentally different kinds of endpoints.")

# 14 — Common mix-ups
d.resource_list_slide("Module 8", "Common Mix-Ups", "Worth getting right before Module 9", [
    ("“Peering can chain through a shared VPC”", "It can't — peering is not transitive, full stop."),
    ("“Direct Connect is automatically encrypted”", "It's a private physical path, not an encrypted tunnel — pair it with VPN if needed."),
    ("“PrivateLink and peering solve the same problem”", "PrivateLink reaches one service; peering connects two whole networks."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Skim the Module 8 guided lab overview — you'll peer two VPCs yourself in the Learner Lab", "Module 8")

# 16 — Closing
d.closing_slide("Connecting", "Networks", "Next up: securing user, application, and data access")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
