"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/10-designing-meridian-loyalty-to-scale-reliably.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-10-deck.py

Paired with instructor-private/10-designing-meridian-loyalty-to-scale-reliably-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "10-designing-meridian-loyalty-to-scale-reliably.pptx")

d = Deck(10, "Designing Meridian Loyalty to Scale Reliably",
          "Module 8 made sure it survives a disaster. Tonight, it survives success.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 10 · Lecture", ["Designing Meridian Loyalty", "to Scale Reliably"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 10", "Question of the Day", "Before we start",
    [("Three brands are about to run a coordinated “double points weekend”", "How does Meridian Loyalty handle traffic far above any normal day, without a guest noticing?"),
     ("Recap: Module 8 made sure Meridian Loyalty survives a disaster", "RTO/RPO, Warm Standby, Aurora Global Database, Resilience Hub"),
     ("Tonight's task", "Domain 2, Task 2.4 — the scaling behavior a new solution needs, not the failover behavior")])

# 3 — Objectives
d.numbered_list_slide("Module 10", "Objectives", "Five things by the end of tonight", [
    ("Distinguish scalability from elasticity", "and explain why a new solution needs both"),
    ("Choose between target tracking and scheduled scaling", "for a given traffic pattern"),
    ("Explain how Amazon SQS decouples a write-heavy path", "from a traffic spike"),
    ("Choose DynamoDB's capacity mode", "based on how predictable a workload's traffic actually is"),
    ("Design a complete scaling strategy for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("From Surviving a Disaster to Surviving Success",
    "Module 8 covered failover. Tonight covers what happens when everything works — and everyone shows up at once", "Module 10")

# 5 — Scalability vs elasticity intro
d.content_slide("Scalability vs. Elasticity", "Used almost interchangeably in conversation — the exam keeps them separate", "Module 10", dark=True)

# 6 — Exam trap: scalability vs elasticity
d.quad_box_slide("COMMON EXAM TRAP", "Can It Grow, or Does It Grow Itself?", "Two different properties, easy to blur together",
    [("Scalability", "the ability to handle growth at all, by adding resources — doesn't require ever shrinking back."),
     ("Elasticity", "scaling automatically, in both directions, in response to real demand."),
     ("Manual resizing by an engineer", "makes a system scalable, but not elastic — no automatic behavior."),
     ("Meridian Loyalty needs both", "capable of 10x load, and services that adjust to demand on their own.")],
    note="One line: scalable means it CAN grow. Elastic means it grows and shrinks itself, automatically.")

# 7 — Target tracking vs scheduled scaling table
d.table_slide("Module 10", "Target Tracking vs. Scheduled Scaling", "Two policy types, for two different traffic shapes",
    ["Traffic pattern", "Right policy"],
    [["Organic, unpredictable fluctuation", "Target tracking — reacts to a metric like CPU or request count"],
     ["Known, calendar-driven campaign spike", "Scheduled scaling — adds capacity proactively, ahead of time"],
     ["Both at once (Meridian Loyalty's actual case)", "Both together — scheduled for known events, target tracking for the rest"]],
    col_widths=[6.6, 6.0],
    note="Scheduled scaling: minutes before the campaign goes live, not scrambling after load already climbed.")

# 8 — SQS decoupling
d.content_slide("Decoupling with Amazon SQS", "A burst of point-earning events shouldn't hit the database directly", "Module 10")

# 9 — Exam trap: SQS decoupling
d.quad_box_slide("COMMON EXAM TRAP", "Absorbing a Spike vs. Eliminating It", "Decoupling changes how a spike is experienced downstream, not whether it happened",
    [("Writing synchronously, direct to the database", "exposes the DB and the guest-facing request to the spike's full size."),
     ("SQS queues the event the instant it happens", "the guest-facing action completes immediately either way."),
     ("A scaled consumer fleet drains the queue", "writing to the database at a sustainable rate."),
     ("The spike still happened", "SQS absorbed it into a rate the downstream system can actually sustain.")],
    note="One line: SQS doesn't eliminate the spike — it smooths how the database experiences it.")

# 10 — DynamoDB capacity modes
d.split_card_slide("Module 10", "DynamoDB: On-Demand vs. Provisioned with Auto Scaling", "Which one fits Meridian Loyalty's event table, and when",
    "On-Demand Capacity",
    [("No capacity planning at all", "scales instantly to whatever load arrives, at higher per-request cost"),
     ("The safer choice at launch", "no traffic history yet, campaign timing still new")],
    "Provisioned + Auto Scaling",
    "Lower cost once traffic is predictable",
    ["Reacts to a target utilization metric", "An instantaneous extreme spike can still outrun it"])

# 11 — ElastiCache
d.content_slide("Reducing Load with Amazon ElastiCache", "Most reads during a campaign weekend are the same guests, checking the same balance", "Module 10", dark=True)

# 12 — Four facets
d.four_up_slide("Module 10", "Four Facets of One Scaling Strategy", "Different layers, the same underlying goal", [
    (1, "Elasticity", "Compute grows and shrinks automatically with real demand."),
    (2, "Scheduling", "Known campaign spikes get capacity ahead of time, not after."),
    (3, "Decoupling", "SQS absorbs a write burst into a sustainable rate."),
    (4, "Capacity Mode", "DynamoDB's mode matches how predictable traffic actually is."),
])

# 13 — Putting it together
d.numbered_list_slide("Module 10", "Putting It Together: Meridian Loyalty's Scaling Strategy", "Every piece from tonight, in one design", [
    ("Elasticity, not just scalability, as the actual goal", "capacity that grows and shrinks automatically with real demand"),
    ("Scheduled scaling for known spikes, target tracking for the rest", "proactive ahead of campaigns, reactive for organic fluctuation"),
    ("SQS decoupling the point-earning write path", "absorbing a burst rather than exposing the database directly to it"),
    ("DynamoDB on-demand at launch, provisioned later", "once traffic patterns are well understood"),
    ("ElastiCache in front of Aurora", "serving repeated guest-balance reads without proportionally loading the database"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 10", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Scalable and elastic mean the same thing”", "Scalable means it CAN grow; elastic means it grows and shrinks itself, automatically."),
    ("“SQS eliminates the traffic spike”", "It absorbs the spike into a sustainable rate — the spike still happened."),
    ("“On-demand DynamoDB is always the right choice”", "It's the safer choice for new or unpredictable workloads — provisioned costs less once traffic is understood."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 11 continues Domain 2 with Task 2.5: designing performance efficiency for Meridian Loyalty", "Module 10")

# 16 — Recap
d.content_slide("Recap",
    "Elasticity beyond scalability, scheduled and target tracking scaling together, SQS absorbing spikes, capacity mode matched to predictability", "Module 10", dark=True)

# 17 — Closing
d.closing_slide("Designing Meridian Loyalty", "to Scale Reliably", "Next up: performance efficiency for Meridian Loyalty")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
