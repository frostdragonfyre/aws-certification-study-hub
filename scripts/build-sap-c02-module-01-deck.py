"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/01-welcome-to-solutions-architect-professional.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-01-deck.py

Paired with instructor-private/01-welcome-to-solutions-architect-professional-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "01-welcome-to-solutions-architect-professional.pptx")

d = Deck(1, "Welcome to Solutions Architect Professional",
          "One workload, one account, one team is Associate. This course starts where that stops being true.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 1 · Lecture", ["Welcome to Solutions", "Architect Professional"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 1", "Question of the Day", "Before we start",
    [("SAA-C03 ended with one café, one AWS account, one Region", "What changes about the design problem the moment there's more than one account and more than one business?"),
     ("Recap: sixteen modules building Café Sol's architecture", "VPC, RDS Multi-AZ, CloudFormation, decoupling, caching, serverless, a data lake, disaster recovery"),
     ("Tonight's shift", "From designing one workload well to designing a strategy that spans several")])

# 3 — Objectives
d.numbered_list_slide("Module 1", "Objectives", "Five things by the end of tonight", [
    ("Explain what distinguishes Professional from Associate", "beyond raw difficulty"),
    ("Describe the SAP-C02 exam's four domains", "and roughly what share of the exam each represents"),
    ("Explain what a multi-account AWS environment is", "and why organizations adopt one"),
    ("Describe this course's new case study", "and the organizational complexity it introduces"),
    ("Map a scenario to the correct exam domain", "the actual exam skill from here forward"),
])

# 4 — Problem framing
d.content_slide("From Associate to Professional: What Actually Changes",
    "Same underlying services — a different scope of problem to reason about", "Module 1")

# 5 — Three (four) shifts
d.four_up_slide("Module 1", "What Actually Shifts", "None of it means the services are different",
    [(1, "Organizational scope", "Multiple AWS accounts, teams, and compliance requirements — not one workload in one account."),
     (2, "Existing systems", "Most scenarios improve or migrate something already in production, not a blank slate."),
     (3, "Real trade-offs", "Multiple valid designs, judged against one specific stated priority."),
     (4, "Same services underneath", "RDS is still RDS — what changes is the scope you're asked to reason about.")])

# 6 — Four domains table
d.table_slide("Module 1", "The SAP-C02 Exam: Four Domains", "Weighted differently — and this course maps to them directly",
    ["Domain", "Weight", "What it's asking"],
    [["1. Organizational Complexity", "26%", "Networking, security, accounts, cost — across an org"],
     ["2. New Solutions", "29%", "Designing new systems — the largest single domain"],
     ["3. Continuous Improvement", "25%", "Making something already in production better"],
     ["4. Migration & Modernization", "20%", "Moving legacy workloads into AWS, then modernizing"]],
    col_widths=[4.6, 1.8, 5.6],
    note="This course: Modules 2–6 → Domain 1, Modules 7–12 → Domain 2, Modules 13–14 → Domain 3, Modules 15–16 → Domain 4.")

# 7 — Exam trap
d.quad_box_slide("COMMON EXAM TRAP", "It's Not About Knowing More Services", "The exam tests scope of reasoning, not a longer service list",
    [("Associate assumption", "“Professional just means harder questions about more services.” Mostly wrong."),
     ("What's actually tested", "Applying services you likely know to multi-account, already-in-production situations."),
     ("The real skill", "Picking the option that fits the stated priority, not the abstractly “best” one."),
     ("Read for", "Which stated priority — cost, timeline, compliance, operations — a question is actually optimizing for.")],
    note="One line: know the services already. This exam tests what you do with them across accounts and constraints.")

# 8 — Multi-account environment
d.content_slide("What a Multi-Account AWS Environment Is",
    "The account boundary becomes a design decision in its own right", "Module 1", dark=True)

# 9 — Why organizations split
d.four_up_slide("Module 1", "Why Organizations Split Across Accounts", "Four reasons that show up constantly at the professional level",
    [(1, "Isolation", "An incident, cost spike, or bad deploy in one account doesn't threaten another."),
     (2, "Billing clarity", "Costs per team, brand, or environment stay visible instead of blended together."),
     (3, "Blast radius", "Broad access granted in one account doesn't automatically extend into another."),
     (4, "Compliance boundaries", "A regulated workload gets its own scoped account, without constraining everything else.")])

# 10 — AWS Organizations preview
d.content_slide("AWS Organizations",
    "Ties multiple accounts together: consolidated billing, account creation, policy-based guardrails — full depth in Module 5", "Module 1")

# 11 — Case study intro
d.content_slide("Putting It Together: Meridian Hospitality Group",
    "The café from SAA-C03 was acquired six months ago and became a founding brand", "Module 1", dark=True)

# 12 — Three brands table
d.table_slide("Module 1", "Meridian's Three Brands", "Three brands, three very different starting points",
    ["Brand", "AWS status", "Starting point"],
    [["Café Sol", "Single account, well-architected", "The SAA-C03 café — Frank & Martha, now formally branded"],
     ["Haven & Co. Hotels", "Separate account, own systems", "Boutique hotel chain, acquired alongside Café Sol"],
     ["Ridgeline Diner Co.", "No cloud footprint at all", "40-year-old diner chain, acquired last quarter, fully on-premises"]],
    col_widths=[3.4, 4.0, 6.6])

# 13 — Sofía's mandate
d.numbered_list_slide("Module 1", "Sofía's New Mandate", "Promoted to Lead Solutions Architect for all of Meridian", [
    ("No longer one workload", "Now responsible for architecture decisions across everything Meridian owns"),
    ("Reports to Priya Anand, VP of Engineering", "“You built one great system. Now build the strategy that lets us run several.”"),
    ("Nikhil moves to platform engineering", "Supporting all of Meridian's brands, not just Café Sol"),
], note="This mandate is the throughline for the rest of this course — one architect, three brands, one coherent strategy.")

# 14 — Domain-to-module mapping / putting it together
d.numbered_list_slide("Module 1", "Putting It Together: How This Course Maps", "Each domain gets its own block of modules", [
    ("Domain 1 (Modules 2–6)", "Organizational complexity across all three of Meridian's accounts"),
    ("Domain 2 (Modules 7–12)", "New solutions Meridian needs going forward"),
    ("Domain 3 (Modules 13–14)", "Improving what Café Sol and Haven & Co. already have running"),
    ("Domain 4 (Modules 15–16)", "Getting Ridgeline out of the back room and into AWS"),
], note="By Module 16, every task statement in the exam guide will have had a dedicated module.")

# 15 — Common mix-ups
d.resource_list_slide("Module 1", "Common Mix-Ups", "Worth getting right before Module 2", [
    ("“Professional just means more services to memorize”", "It's organizational scope, existing systems, and real trade-offs — not service count."),
    ("“Café Sol always had that name”", "It didn't — it was just “the café” until the acquisition gave it a formal brand."),
    ("“One AWS account is simpler, so it's better”", "Simpler until an incident, cost spike, or compliance need in one brand threatens the others."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Module 2 opens Domain 1 with Task 1.1: architecting network connectivity across Meridian's three accounts", "Module 1")

# 17 — Closing
d.closing_slide("Welcome to Solutions", "Architect Professional", "Next up: architecting network connectivity across Meridian's accounts")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
