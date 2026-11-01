"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/06-implementing-backup-and-restore-strategies.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-06-deck.py

Paired with instructor-private/06-implementing-backup-and-restore-strategies-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "06-implementing-backup-and-restore-strategies.pptx")

d = Deck(6, "Implementing Backup and Restore Strategies",
          "Modules 4 and 5 kept the infrastructure running. Tonight is about getting data back when the infrastructure can't save it.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 6 · Lecture", ["Implementing Backup", "and Restore Strategies"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 6", "Question of the Day", "Before we start",
    [("A bad deployment corrupts a table, and Multi-AZ replicates the corruption to the standby instantly", "Does high availability save Priya here?"),
     ("Recap: Module 4 matched capacity to demand, Module 5 survived component failure", "tonight covers failures neither of those can undo"),
     ("Tonight's task", "Domain 2, Task 2.3 — the final module of Domain 2: backup and restore")])

# 3 — Objectives
d.numbered_list_slide("Module 6", "Objectives", "Five things by the end of tonight", [
    ("Define RTO and RPO, and explain what each one measures", "downtime vs. data loss — not the same axis"),
    ("Describe how AWS Backup centralizes policy across services", "one plan instead of per-service configuration"),
    ("Distinguish an RDS automated backup from a manual snapshot", "and what happens to each on deletion"),
    ("Explain why cross-Region backup copies matter", "surviving more than just the primary data"),
    ("Design a backup and restore strategy for a stated RTO/RPO", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Some Failures Replicate Just as Fast as the Good Data",
    "Multi-AZ and Auto Scaling can't undo a bad deployment, a corrupted table, or a mistaken deletion", "Module 6")

# 5 — Section intro: RTO/RPO
d.content_slide("RTO and RPO: Measuring Two Different Things",
    "A business question first — how much data loss, and how much downtime, is acceptable", "Module 6", dark=True)

# 6 — Exam trap: RTO vs RPO
d.quad_box_slide("COMMON EXAM TRAP", "RTO vs. RPO", "Two axes, two different design decisions",
    [("RPO", "Recovery Point Objective — how much data loss is acceptable, in time."),
     ("RTO", "Recovery Time Objective — how much downtime is acceptable."),
     ("Tight RPO", "needs frequent backups or continuous replication."),
     ("Tight RTO", "needs a fast restore path — a standby, not a cold restore.")],
    note="One line: RPO is about data loss, RTO is about downtime — solving one doesn't solve the other.")

# 7 — Applied
d.table_slide("Module 6", "RTO vs. RPO, Applied", "Reading which requirement a statement is actually describing",
    ["Statement", "Requirement"],
    [["“Can tolerate losing at most 15 minutes of data”", "RPO — data loss, drives backup frequency"],
     ["“Must be back online within 30 minutes”", "RTO — downtime, drives restore speed and standby readiness"]],
    col_widths=[7.2, 5.4],
    note="Data loss language is RPO; downtime language is RTO — the wording is the tell.")

# 8 — Section intro: AWS Backup
d.content_slide("AWS Backup: One Policy, Many Services",
    "Configuring each service's backups separately is exactly how gaps happen", "Module 6")

# 9 — AWS Backup applied
d.numbered_list_slide("Module 6", "AWS Backup, Applied", "Fixing fragmented, per-service backup configuration", [
    ("A backup plan defines schedule, retention, and lifecycle rules once", "assigned to resources by tag or resource ID"),
    ("Covers EBS, RDS, DynamoDB, EFS, and more from one place", "instead of each service's own console and schedule"),
    ("Cross-Region and cross-account copies are part of the same plan", "disaster-recovery coverage without a separate manual process"),
    ("The fix for inconsistent coverage is centralizing the plan", "not tightening each team's individual configuration"),
])

# 10 — Section intro: RDS backups
d.content_slide("RDS Automated Backups vs. Manual Snapshots",
    "Easy to blur together — very different at the moment that matters: deletion", "Module 6", dark=True)

# 11 — Exam trap: automated vs manual
d.quad_box_slide("COMMON EXAM TRAP", "What Survives Instance Deletion", "Same database, two backup types, one very different outcome",
    [("Automated backups", "daily plus transaction logs — point-in-time recovery to any second."),
     ("Tied to the instance", "deleted by default when the instance is deleted."),
     ("Manual snapshots", "user-initiated, retained indefinitely, independent of the instance."),
     ("To survive deletion", "use a manual snapshot, or explicitly retain automated backups.")],
    note="One line: automated backups die with the instance by default — manual snapshots don't.")

# 12 — Applied
d.table_slide("Module 6", "RDS Backups, Applied", "Matching the requirement to the right backup type",
    ["Requirement", "Right mechanism"],
    [["Recover to any specific second within 35 days", "Automated backups — continuous transaction log capture"],
     ["Must still exist after the instance is deleted", "A manual snapshot, or explicit retention at deletion"]],
    col_widths=[7.2, 5.4],
    note="A requirement to outlive the instance is the tell for a manual snapshot.")

# 13 — Putting it together
d.numbered_list_slide("Module 6", "Putting It Together: Meridian's Backup and Restore Strategy", "Every piece from tonight, in one design", [
    ("AWS Backup centralizing EBS, DynamoDB, and EFS backups by tag", "one schedule and retention policy, not per-service configuration"),
    ("RDS automated backups tuned to the stated RPO, plus manual snapshots before risky changes", "point-in-time recovery, and a copy that survives independently"),
    ("Cross-Region backup copies through AWS Backup", "so a Region-wide event doesn't take out the data and its backups together"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 6", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“RTO and RPO both just mean how fast we recover”", "RPO is data loss, RTO is downtime — different axes, different fixes."),
    ("“Automated backups always survive deleting the instance”", "They're deleted by default unless retention is explicitly requested."),
    ("“One Region's backups are enough”", "A Region-wide event can take out the primary data and its backups together."),
], dark=True)

# 15 — Domain 2, Complete
d.table_slide("Module 6", "Domain 2, Complete", "Three modules, one resilient foundation",
    ["Module", "Task"],
    [["Module 4", "Task 2.1 — scalability and elasticity"],
     ["Module 5", "Task 2.2 — high availability and resilient environments"],
     ["Module 6", "Task 2.3 — backup and restore strategies"]],
    col_widths=[3.6, 9.0],
    note="Capacity, survival, and recovery — Domain 2's three tasks, closed.")

# 16 — Recap
d.content_slide("Recap",
    "RTO vs. RPO, AWS Backup's centralized plans, RDS automated backups vs. manual snapshots, cross-Region backup copies", "Module 6", dark=True)

# 17 — Closing
d.closing_slide("Implementing Backup", "and Restore Strategies", "Domain 2 complete — next up: Domain 3, deployment and automation")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
