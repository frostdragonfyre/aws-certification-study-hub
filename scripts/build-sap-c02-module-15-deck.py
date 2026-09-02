"""
Builds certifications/sap-c02/lectures/15-migrating-ridgeline-diner-co-to-aws.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-15-deck.py

Paired with instructor-private/15-migrating-ridgeline-diner-co-to-aws-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02", "lectures",
                    "15-migrating-ridgeline-diner-co-to-aws.pptx")

d = Deck(15, "Migrating Ridgeline Diner Co. to AWS",
          "Domain 3 improved what's already in AWS. Ridgeline has never touched the cloud at all.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 15 · Lecture", ["Migrating Ridgeline Diner Co.", "to AWS"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 15", "Question of the Day", "Before we start",
    [("Ridgeline runs a POS system, an inventory database, and a reporting server", "on physical servers. Should all three move to AWS the same way?"),
     ("Recap: Domain 3 improved systems already running in AWS", "Well-Architected reviews, Resilience Hub, FIS, Compute Optimizer, cost audits"),
     ("Tonight's task", "Domain 4, Tasks 4.1 and 4.2 — the first real migration in this course")])

# 3 — Objectives
d.numbered_list_slide("Module 15", "Objectives", "Four things by the end of tonight", [
    ("Apply the migration strategies to a portfolio of on-premises systems", "the “R” strategies, chosen per system"),
    ("Explain what AWS Application Migration Service does for a rehost", "continuous replication ahead of cutover"),
    ("Distinguish a homogeneous database migration from a heterogeneous one", "same engine vs. different engine"),
    ("Design a complete migration strategy for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("The First System That's Never Touched the Cloud",
    "Ridgeline's systems run on physical servers in the back office — nothing here started cloud-native", "Module 15")

# 5 — Migration strategies intro
d.content_slide("Matching Each System to a Migration Strategy",
    "Not every system deserves the same treatment — the exam expects a specific vocabulary", "Module 15", dark=True)

# 6 — Exam trap: choosing the right R
d.quad_box_slide("COMMON EXAM TRAP", "Match the Strategy to the System", "Not one strategy for everything — urgency, debt, and benefit all matter",
    [("Retire", "the unused scheduling tool — nobody has opened it in over a year."),
     ("Rehost", "the point-of-sale system — critical, understood, no time to redesign now."),
     ("Replatform", "the inventory database — real benefit from RDS, no full redesign needed."),
     ("Refactor", "the reporting server — aging custom software, worth a real redesign.")],
    note="One line: match urgency, technical debt, and modernization benefit to the right strategy, per system.")

# 7 — Ridgeline's systems table
d.table_slide("Module 15", "Ridgeline's Portfolio, Mapped", "Four systems, four different right answers",
    ["System", "Strategy"],
    [["Internal scheduling tool — unused for over a year", "Retire"],
     ["Point-of-sale system — critical, time-sensitive", "Rehost"],
     ["Inventory database — benefits from managed service", "Replatform onto Amazon RDS"],
     ["Reporting server — aging custom software, lower urgency", "Refactor"]],
    col_widths=[7.6, 5.0],
    note="Four systems, four strategies — chosen deliberately, not applied uniformly.")

# 8 — MGN intro
d.content_slide("Rehosting at Scale with AWS Application Migration Service",
    "Choosing rehost still leaves the actual move to do — by hand, that's slow and risky", "Module 15")

# 9 — MGN applied
d.numbered_list_slide("Module 15", "AWS Application Migration Service, Applied", "Automating the point-of-sale system's move", [
    ("MGN continuously replicates the server's disk state", "to a staging area in AWS, well before cutover ever happens"),
    ("At cutover, it launches a ready-to-run EC2 copy", "already current, not built from scratch that day"),
    ("The actual downtime window is short", "because the replication has been running continuously in the background"),
    ("Speed and low risk, exactly what the POS system needs", "no redesign, no lengthy offline rebuild"),
])

# 10 — Database migration intro
d.content_slide("Migrating Ridgeline's Database",
    "Replatforming to RDS still requires the data itself to actually move", "Module 15", dark=True)

# 11 — Exam trap: homogeneous vs heterogeneous
d.quad_box_slide("COMMON EXAM TRAP", "Same Engine vs. Different Engine", "One fact decides which tools the migration actually needs",
    [("Homogeneous migration", "same database engine, source to target — DMS alone is sufficient."),
     ("Heterogeneous migration", "different engines — SCT must convert the schema before DMS moves data."),
     ("SCT isn't optional for heterogeneous", "DMS itself doesn't translate schemas or code between engines."),
     ("Ridgeline's inventory DB", "SQL Server to RDS for SQL Server — homogeneous, DMS alone.")],
    note="One line: same engine is DMS alone. Different engine needs SCT first, then DMS.")

# 12 — Homogeneous vs heterogeneous table
d.table_slide("Module 15", "Which Tools a Migration Actually Needs", "Applied to two different database scenarios",
    ["Migration", "Tools required"],
    [["Ridgeline's SQL Server to RDS for SQL Server", "DMS alone — homogeneous, same engine"],
     ["A hypothetical Oracle to Aurora migration", "SCT converts the schema first, then DMS moves the data"]],
    col_widths=[7.6, 5.0],
    note="The engine, not the hosting model, decides homogeneous vs. heterogeneous.")

# 13 — Putting it together
d.numbered_list_slide("Module 15", "Putting It Together: Ridgeline's Migration Plan", "Every piece from tonight, in one design", [
    ("Retire the unused tool, rehost the POS system via MGN", "fast, low-risk, minimal downtime at cutover"),
    ("Replatform the inventory database onto Amazon RDS", "a homogeneous migration — DMS alone, no SCT needed"),
    ("Refactor the reporting server once urgent moves are done", "the system with real modernization value to capture"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 15", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Rehost everything for safety”", "Ignores real modernization opportunity — match strategy per system instead."),
    ("“SCT is optional for a heterogeneous migration”", "It's required — DMS alone doesn't translate schemas between engines."),
    ("“Moving to a managed service always means heterogeneous”", "Homogeneous vs. heterogeneous is about the engine, not the hosting model."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 16 closes out Domain 4 and the SAP-C02 track: modernizing what's been migrated", "Module 15")

# 16 — Recap
d.content_slide("Recap",
    "Strategy matched per system, MGN automating rehost cutover, homogeneous vs. heterogeneous deciding DMS alone or DMS plus SCT", "Module 15", dark=True)

# 17 — Closing
d.closing_slide("Migrating Ridgeline Diner Co.", "to AWS", "Next up: modernization, closing out Domain 4")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
