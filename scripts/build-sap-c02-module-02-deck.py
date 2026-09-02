"""
Builds certifications/sap-c02/lectures/02-architecting-network-connectivity-strategies.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-02-deck.py

Paired with instructor-private/02-architecting-network-connectivity-strategies-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02", "lectures",
                    "02-architecting-network-connectivity-strategies.pptx")

d = Deck(2, "Architecting Network Connectivity Strategies",
          "Three AWS islands, one on-premises data center, and no shared way to reach any of them.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 2 · Lecture", ["Architecting Network", "Connectivity Strategies"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 2", "Question of the Day", "Before we start",
    [("Café Sol, Haven & Co., and Ridgeline can't currently reach each other", "What actually has to be designed before that changes — for three accounts, and for one on-premises data center?"),
     ("Recap: Module 1 introduced Meridian Hospitality Group", "Three brands, three starting points, one Lead Solutions Architect"),
     ("Tonight's task", "Domain 1, Task 1.1 — architecting network connectivity strategies")])

# 3 — Objectives
d.numbered_list_slide("Module 2", "Objectives", "Five things by the end of tonight", [
    ("Compare VPC peering and Transit Gateway", "and explain why hub-and-spoke scales better than a full mesh"),
    ("Compare Direct Connect and Site-to-Site VPN", "for hybrid connectivity to an on-premises data center"),
    ("Explain what AWS PrivateLink does", "and how it differs from full network-level connectivity"),
    ("Describe how Route 53 Resolver works across boundaries", "between VPCs and between AWS and on-premises"),
    ("Recommend a connectivity strategy for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Three Disconnected Islands",
    "No shared way for Café Sol, Haven & Co., and Ridgeline to reach each other, or central IT to reach any of them", "Module 2")

# 5 — Peering vs Transit Gateway
d.content_slide("Connecting Multiple VPCs: Peering vs. Transit Gateway",
    "A full mesh grows quadratically — a hub-and-spoke model doesn't", "Module 2", dark=True)

# 6 — Exam trap: peering vs TGW
d.quad_box_slide("COMMON EXAM TRAP", "Peering Doesn't Scale — And Isn't Transitive", "Read the VPC count and growth signal before choosing",
    [("VPC peering", "Direct, one-to-one, non-transitive. A↔B and B↔C does not give A↔C."),
     ("A full mesh", "grows quadratically — 10 VPCs need 45 peering connections."),
     ("Transit Gateway", "Hub-and-spoke — each VPC attaches once; the hub routes centrally."),
     ("The signal", "A handful of VPCs, no growth plans → peering. Many VPCs, or stated growth → Transit Gateway.")],
    note="One line: small and fixed stays peering-friendly. Many, or growing, points to Transit Gateway.")

# 7 — Direct Connect vs VPN
d.table_slide("Module 2", "Direct Connect vs. Site-to-Site VPN", "Two standard ways to reach an on-premises network",
    ["", "Site-to-Site VPN", "Direct Connect"],
    [["Path", "Public internet, IPsec tunnel", "Dedicated private physical circuit"],
     ["Setup time", "Hours", "Weeks — real circuits provisioned"],
     ["Performance", "Variable — subject to internet", "Consistent latency, high throughput"],
     ["Cost", "Lower", "Higher"]],
    col_widths=[2.4, 5.0, 5.4],
    note="A common pattern: Direct Connect primary, Site-to-Site VPN as automatic failover.")

# 8 — Exam trap: VPN vs DX
d.quad_box_slide("COMMON EXAM TRAP", "Don't Default to Direct Connect", "Read the stated timeline and throughput requirement",
    [("“Working by next week”", "points to VPN — Direct Connect's provisioning timeline usually can't meet it."),
     ("“Consistent, high-throughput, ongoing transfer”", "points to Direct Connect."),
     ("Not “more enterprise” = better", "Direct Connect isn't automatically the right answer just because it sounds more serious."),
     ("Both together", "is a valid, common answer — Direct Connect primary, VPN as failover.")],
    note="One line: match the stated timeline and throughput — don't reach for Direct Connect by reflex.")

# 9 — PrivateLink
d.content_slide("AWS PrivateLink: Private Access Without Full Connectivity",
    "Expose one specific service — not the whole VPC — with no peering or route table changes", "Module 2")

# 10 — Route 53 Resolver
d.content_slide("Route 53 Resolver: DNS Across VPCs and On-Premises",
    "Routing gets packets there. Resolver is what lets you use a hostname to find it", "Module 2", dark=True)

# 11 — Resolver endpoints
d.split_card_slide("Module 2", "Inbound vs. Outbound Resolver Endpoints", "Two directions, two different jobs",
    "Outbound endpoint",
    [("Forwards queries out", "from inside a VPC to DNS servers elsewhere, like an on-premises DNS server"),
     ("Used over an existing hybrid connection", "typically the Direct Connect or VPN link already in place")],
    "Inbound endpoint",
    "Accepts queries from outside the VPC",
    ["Lets on-premises resolve AWS-hosted names", "Combined with Resolver rules to forward specific domains correctly"])

# 12 — Meridian's strategy table
d.table_slide("Module 2", "Meridian's Network Connectivity Strategy", "Every piece from tonight, matched to what it's good at",
    ["Piece", "Meridian's use"],
    [["Transit Gateway", "Hub, with Café Sol and Haven & Co. VPCs attached as spokes"],
     ["Shared services VPC + PrivateLink", "Central logging, directory, auth — exposed as one service, not full access"],
     ["Site-to-Site VPN → Direct Connect later", "VPN now for Ridgeline HQ; Direct Connect once workloads go live"],
     ["Route 53 Resolver", "Hostnames resolve correctly in both directions during and after migration"]],
    col_widths=[4.6, 8.0])

# 13 — Putting it together
d.numbered_list_slide("Module 2", "Putting It Together: Why This Combination", "Not one service — four, each solving a different piece", [
    ("Transit Gateway, not a peering mesh", "because Meridian expects to add more brands over time"),
    ("PrivateLink for shared services, not a shared route table", "because each brand only needs specific services, not broad reach"),
    ("VPN now, Direct Connect planned later for Ridgeline", "matching the actual timeline and throughput needs as they change"),
], note="Route 53 Resolver ties all of it together — routing alone was never the whole problem.")

# 14 — Common mix-ups
d.resource_list_slide("Module 2", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“VPC peering is transitive”", "It isn't — A↔B and B↔C never gives you A↔C without a hub."),
    ("“Direct Connect is always better than VPN”", "It performs better, but costs more and takes weeks to provision — VPN often fits better, or the two combine."),
    ("“PrivateLink is the same as full network access”", "It exposes one specific service only — not broader reach into the provider's VPC."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 3 continues Domain 1 with Task 1.2: prescribing security controls across Meridian's accounts", "Module 2")

# 16 — Matching requirement to connectivity choice
d.table_slide("Module 2", "Matching a Requirement to the Right Connectivity Choice", "The actual exam skill — read the requirement, pick the tool",
    ["Stated requirement", "Best-fit choice"],
    [["“A handful of VPCs, no growth planned”", "VPC Peering"],
     ["“Growing number of accounts, centralized control needed”", "AWS Transit Gateway"],
     ["“Working within days, cost-sensitive”", "AWS Site-to-Site VPN"],
     ["“Consistent, high-throughput, ongoing transfer”", "AWS Direct Connect"],
     ["“One shared service, no broader network access allowed”", "AWS PrivateLink"]],
    col_widths=[8.6, 4.0])

# 17 — Closing
d.closing_slide("Architecting Network", "Connectivity Strategies", "Next up: prescribing security controls across Meridian's accounts")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
