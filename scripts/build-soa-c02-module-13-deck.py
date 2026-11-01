"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/13-troubleshooting-network-connectivity-issues.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-13-deck.py

Paired with instructor-private/13-troubleshooting-network-connectivity-issues-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "13-troubleshooting-network-connectivity-issues.pptx")

d = Deck(13, "Troubleshooting Network Connectivity Issues",
          "Modules 11 and 12 built the network. Tonight is what to do when something doesn't connect the way it should.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 13 · Lecture", ["Troubleshooting Network", "Connectivity Issues"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 13", "Question of the Day", "Before we start",
    [("Reachability Analyzer and Flow Logs both show a fully allowed path, but an app still can't connect", "What's actually going on?"),
     ("Recap: Module 11 connected the network, Module 12 routed and delivered content over it", "tonight is what to do when something doesn't connect the way it should"),
     ("Tonight's task", "Domain 5, Task 5.3 — the final module of Domain 5: troubleshooting network connectivity")])

# 3 — Objectives
d.numbered_list_slide("Module 13", "Objectives", "Five things by the end of tonight", [
    ("Distinguish VPC Reachability Analyzer from VPC Flow Logs", "and know when each fits"),
    ("Use route tables, NACLs, and Security Groups, in that order, to localize a problem", "widest blast radius first"),
    ("Recognize a per-instance versus a per-subnet symptom pattern", "the tell for which layer is at fault"),
    ("Recognize when a connectivity complaint isn't a networking problem at all", "OS firewalls and DNS resolution"),
    ("Design a troubleshooting approach for a stated connectivity failure", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Something Doesn't Connect — Now What?",
    "Modules 11 and 12 built the network. Tonight is finding out why it broke.", "Module 13")

# 5 — Section intro: Reachability Analyzer vs Flow Logs
d.content_slide("VPC Reachability Analyzer vs. VPC Flow Logs",
    "One tests a path before traffic exists, the other records what already happened", "Module 13", dark=True)

# 6 — Exam trap: Reachability Analyzer vs Flow Logs
d.quad_box_slide("COMMON EXAM TRAP", "Before Traffic Exists vs. After It Happened", "Proactive path testing, or a retrospective traffic record",
    [("Reachability Analyzer", "point-in-time path analysis — no real traffic needed, tests before deploying."),
     ("VPC Flow Logs", "records actual traffic metadata — accepted or rejected, after it already happened."),
     ("Test a path before traffic exists", "no real traffic needed — Reachability Analyzer."),
     ("Investigate traffic that already flowed", "accepted or rejected, over time — Flow Logs.")],
    note="One line: no real traffic yet, that's Reachability Analyzer — traffic that already happened, that's Flow Logs.")

# 7 — Applied
d.table_slide("Module 13", "Reachability Analyzer vs. Flow Logs, Applied", "Matching the need to the right tool",
    ["Requirement", "Right tool"],
    [["Verify a new cross-account connection works before go-live", "Reachability Analyzer — no real traffic needed"],
     ["Investigate what traffic hit an ENI last week, accepted or rejected", "VPC Flow Logs — a retrospective record"]],
    col_widths=[7.6, 5.0],
    note="Before deployment points to Reachability Analyzer; after the fact points to Flow Logs.")

# 8 — Section intro: Route table / NACL / SG
d.content_slide("Localizing the Problem: Blast Radius",
    "Route tables and NACLs affect a whole subnet — Security Groups affect one instance", "Module 13")

# 9 — Exam trap: Route Table / NACL / SG
d.quad_box_slide("COMMON EXAM TRAP", "Blast Radius Tells You Where to Look", "Whole subnet, or just one instance",
    [("Route table", "subnet-wide — nothing in the subnet can reach the destination at all."),
     ("Security Group", "per-instance — one instance fails while its subnet-mate works fine."),
     ("Whole subnet affected equally", "check the route table, then the NACL, first."),
     ("One instance affected, neighbors fine", "check that instance's Security Group.")],
    note="One line: a whole-subnet symptom starts at the route table — a single-instance symptom starts at its Security Group.")

# 10 — Applied
d.table_slide("Module 13", "Localizing the Problem, Applied", "Matching the symptom to the right layer",
    ["Symptom", "Where to look"],
    [["Every instance in a subnet loses reachability to a destination at once", "Route table first — widest blast radius"],
     ["One instance can't be reached, an identical neighbor in the same subnet works fine", "That instance's Security Group — narrowest blast radius"]],
    col_widths=[7.6, 5.0],
    note="Whole-subnet symptoms start wide; single-instance symptoms start narrow.")

# 11 — Section intro: Not really networking
d.content_slide("When It Isn't Really a Networking Problem",
    "A clean AWS-level path doesn't rule out everything else", "Module 13", dark=True)

# 12 — Exam trap: Not really networking
d.quad_box_slide("COMMON EXAM TRAP", "When AWS Says the Path Is Fine", "Look above the network layer next",
    [("Clean AWS-level path", "Reachability Analyzer and Flow Logs both show nothing wrong."),
     ("OS-level firewall", "Windows Firewall or iptables can still block it locally."),
     ("Can't resolve a hostname at all", "a DNS resolution issue — not routing or firewalling."),
     ("Still can't connect", "with everything AWS-level clean — look above the network layer.")],
    note="One line: if AWS-level tools show a clean path and it still fails, the cause is probably outside AWS's network layer.")

# 13 — Putting it together
d.numbered_list_slide("Module 13", "Putting It Together: Troubleshooting Meridian's Connectivity", "Every piece from tonight, in one approach", [
    ("Reachability Analyzer run against every new cross-VPC or hybrid connection before it goes live", "catching a missing route or an overly restrictive Security Group early"),
    ("Flow Logs enabled on every production VPC", "a historical record for investigating a specific incident after the fact"),
    ("A standard troubleshooting order — route table, then NACL, then Security Group", "narrowing from subnet-wide to instance-specific, in that sequence"),
    ("A standing reminder: a clean AWS-level path still leaves the OS firewall and DNS resolution to check", "before assuming AWS is at fault"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 13", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Reachability Analyzer and Flow Logs are interchangeable”", "One needs no real traffic and tests ahead of time; the other records what already happened."),
    ("“A single misbehaving instance means the NACL is wrong”", "A NACL problem hits the whole subnet — a lone instance points to its Security Group."),
    ("“A clean AWS-level path means the network is fine”", "It rules out AWS's network layer — not an OS firewall or DNS resolution."),
], dark=True)

# 15 — Domain 5, Complete
d.table_slide("Module 13", "Domain 5, Complete", "Three modules, one connected and troubleshootable network",
    ["Module", "Task"],
    [["Module 11", "Task 5.1 — networking features and connectivity"],
     ["Module 12", "Task 5.2 — domains, DNS, and content delivery"],
     ["Module 13", "Task 5.3 — troubleshooting network connectivity issues"]],
    col_widths=[3.6, 9.0],
    note="Connected, routed, and now troubleshootable — Domain 5's three tasks, closed.")

# 16 — Recap
d.content_slide("Recap",
    "Reachability Analyzer vs. Flow Logs, route table/NACL/Security Group blast radius, non-networking causes", "Module 13", dark=True)

# 17 — Closing
d.closing_slide("Troubleshooting Network", "Connectivity Issues", "Domain 5 complete — next up: Domain 6, cost and performance optimization")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
