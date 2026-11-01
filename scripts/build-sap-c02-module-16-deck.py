"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/16-modernizing-whats-been-migrated.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-16-deck.py

Paired with instructor-private/16-modernizing-whats-been-migrated-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "16-modernizing-whats-been-migrated.pptx")

d = Deck(16, "Modernizing What's Been Migrated",
          "Module 15 moved Ridgeline to AWS unchanged. Tonight, modernize it deliberately — and close out the track.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 16 · Lecture", ["Modernizing What's Been", "Migrated"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 16", "Question of the Day", "Before we start",
    [("Ridgeline's point-of-sale system has run steadily on EC2 since Module 15", "Should it be redesigned now, or does it need something first?"),
     ("Recap: Module 15 matched a migration strategy to each of Ridgeline's systems", "retire, rehost via MGN, replatform onto RDS, refactor flagged for later"),
     ("Tonight's task", "Domain 4, Tasks 4.3 and 4.4 — modernizing what's already migrated")])

# 3 — Objectives
d.numbered_list_slide("Module 16", "Objectives", "Five things by the end of tonight", [
    ("Explain why migrating and modernizing in one step multiplies risk", "and why a stable migration should come first"),
    ("Describe containerizing a rehosted workload with ECS on Fargate", "no rewrite, no more servers to patch"),
    ("Explain refactoring a batch process into an event-driven design", "triggered by data, not a fixed schedule"),
    ("Match a workload's access pattern to the right database option", "cache, purpose-built, or stay relational"),
    ("Design a complete modernization roadmap for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Stable in AWS Isn't the Same as Modernized",
    "Module 15 moved Ridgeline's systems — largely unchanged. That was deliberate.", "Module 16")

# 5 — Section intro
d.content_slide("Deciding What's Actually Worth Modernizing",
    "Not every migrated system needs the same fix — some need a redesign, some need nothing at all", "Module 16", dark=True)

# 6 — Exam trap: migrate then modernize
d.quad_box_slide("COMMON EXAM TRAP", "Migrate Then Modernize, Not Both at Once", "Combining the two multiplies risk instead of saving time",
    [("“Big bang” migration and redesign", "combines two kinds of risk into one cutover, no clean way to isolate a failure."),
     ("Crawl: migrate first", "get the system running in AWS unchanged, prove the move works."),
     ("Walk: stabilize, gather real data", "real usage informs what modernization is actually worth doing."),
     ("Run: modernize deliberately", "containerize, refactor, or adopt a purpose-built database once stable.")],
    note="One line: migrating and modernizing at the same time multiplies risk — stabilize in AWS first, modernize deliberately after.")

# 7 — Applied table
d.table_slide("Module 16", "Ridgeline's POS System, Two Separate Moves", "Migration and modernization, kept deliberately apart",
    ["Move", "What happened"],
    [["Migration (Module 15)", "Rehost via AWS Application Migration Service — same architecture, now on EC2"],
     ["Modernization (tonight)", "Containerize onto ECS on Fargate — only once the move itself proved stable"]],
    col_widths=[6.6, 6.0],
    note="Same system, two different changes, made at two different times.")

# 8 — Containerizing intro
d.content_slide("Containerizing a Rehosted Workload",
    "The point-of-sale system has run steadily on EC2 since Module 15 — stable enough now to modernize deliberately", "Module 16")

# 9 — Containerizing applied
d.numbered_list_slide("Module 16", "Containerizing the POS System, Applied", "No rewrite required", [
    ("Package the POS application into a container image", "same code, no fresh rewrite required"),
    ("Run it on Amazon ECS with AWS Fargate", "no EC2 instances to patch or scale manually"),
    ("Fargate handles the underlying compute", "the team stops managing servers for this workload entirely"),
    ("This sets up further modernization later", "a container is a shorter step to microservices than a monolith on EC2"),
])

# 10 — Reporting server intro
d.content_slide("Modernizing the Reporting Server",
    "Module 15 flagged the reporting server for refactor — its aging nightly batch job is tonight's target", "Module 16", dark=True)

# 11 — Exam trap: matching modernization to access pattern
d.quad_box_slide("COMMON EXAM TRAP", "Matching Modernization to the Access Pattern", "“The database is slow” has more than one right fix",
    [("Relational stays relational", "if the access pattern hasn't changed, don't force a different database model."),
     ("Add a cache, don't replace the database", "read-heavy, repeated queries call for ElastiCache, not a new engine."),
     ("Purpose-built for a genuine new pattern", "a real pattern mismatch, like high-volume key-value lookups, justifies DynamoDB."),
     ("The reporting server's real problem", "a fixed schedule, not its database — event-driven fixes that, not a new engine.")],
    note="One line: modernize the piece with a real bottleneck — don't rewrite what already fits its access pattern.")

# 12 — Applied table
d.table_slide("Module 16", "From Nightly Batch Job to Event-Driven Reports", "The reporting server, before and after",
    ["Before", "After"],
    [["Fixed nightly job on a physical server, every night", "AWS Lambda, triggered only when new data lands in Amazon S3"],
     ["Runs whether or not new data actually arrived", "Runs exactly when there's something to report on"]],
    col_widths=[6.6, 6.0],
    note="The fix is event-driven triggering, not a different database.")

# 13 — Putting it together
d.numbered_list_slide("Module 16", "Putting It Together: Ridgeline's Modernization Roadmap", "Every piece from tonight, in one design", [
    ("Migrate first, modernize second", "the POS system was rehosted unchanged in Module 15, modernized only now"),
    ("Containerize the POS system onto ECS on Fargate", "no rewrite, no more EC2 instances to manage"),
    ("Refactor the reporting server to be event-driven", "an S3 event triggers Lambda, replacing the fixed schedule"),
    ("Leave the inventory database on Amazon RDS", "its access pattern hasn't changed — no forced modernization"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 16", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Migrate and modernize in the same step”", "Combines two different risks into one cutover — stabilize first, modernize after."),
    ("“Every legacy workload needs a purpose-built database”", "Only a genuine access-pattern mismatch justifies the change."),
    ("“Containerizing means microservices”", "Containerizing repackages one application — splitting it up is a separate, later decision."),
], dark=True)

# 15 — SAP-C02 track complete
d.table_slide("Module 16", "SAP-C02 Track, Complete", "Four domains, one course, sixteen modules",
    ["Domain", "What it covered"],
    [["Domain 1 (Modules 1–6)", "Organizational complexity — multi-account strategy, governance, cross-team requirements"],
     ["Domain 2 (Modules 7–12)", "Designing Meridian Loyalty new — no existing constraints to work around"],
     ["Domain 3 (Modules 13–14)", "Improving Café Sol — a system already stable in AWS, using six months of real data"],
     ["Domain 4 (Modules 15–16)", "Migrating and modernizing Ridgeline — a system that had never touched the cloud"]],
    col_widths=[4.6, 8.0],
    note="Four genuinely different starting points, four different toolsets — not one skill repeated four times.")

# 16 — Recap
d.content_slide("Recap",
    "Migrate then modernize, containerizing with ECS on Fargate, event-driven refactoring, matching database modernization to the actual access pattern", "Module 16", dark=True)

# 17 — Closing
d.closing_slide("Modernizing What's Been", "Migrated", "SAP-C02 track complete")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
