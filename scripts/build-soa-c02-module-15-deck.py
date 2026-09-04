"""
Builds certifications/soa-c02/lectures/15-implementing-compute-and-storage-performance-optimization.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-15-deck.py

Paired with instructor-private/15-implementing-compute-and-storage-performance-optimization-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02", "lectures",
                    "15-implementing-compute-and-storage-performance-optimization.pptx")

d = Deck(15, "Implementing Compute and Storage Performance Optimization",
          "Module 14 found savings. Tonight closes the loop — making sure compute and storage actually perform the way each workload needs.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 15 · Lecture", ["Compute and Storage", "Performance Optimization"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 15", "Question of the Day", "Before we start",
    [("A database is under load from the same handful of queries, run over and over, returning nearly the same results", "Is a bigger database always the right fix?"),
     ("Recap: Module 14 found savings and caught spend surprises", "tonight closes the loop — performance, not just cost"),
     ("Tonight's task", "Domain 6, Task 6.2 — the final module of Domain 6, and of the entire course")])

# 3 — Objectives
d.numbered_list_slide("Module 15", "Objectives", "Five things by the end of tonight", [
    ("Distinguish Instance Store from EBS", "and know when ephemeral local storage actually fits"),
    ("Choose the right EBS volume type for a stated performance requirement", "gp3 vs. io2"),
    ("Match an S3 storage class and lifecycle policy to a stated access pattern", "Standard, Standard-IA, Glacier"),
    ("Recognize when adding a cache is the right fix for a slow, read-heavy workload", "not always a bigger database"),
    ("Design a compute and storage performance strategy for a stated requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Costing Less Isn't the Same as Performing Right",
    "Module 14 found savings. Tonight makes sure compute and storage perform the way each workload needs.", "Module 15")

# 5 — Section intro: Instance Store vs EBS
d.content_slide("Instance Store vs. EBS",
    "Both provide block storage for an instance — they differ in what happens to the data", "Module 15", dark=True)

# 6 — Exam trap: Instance Store vs EBS
d.quad_box_slide("COMMON EXAM TRAP", "Ephemeral Speed vs. Persistent Storage", "The fastest option isn't always the right one",
    [("Instance Store", "physically attached, extremely fast — but ephemeral, lost on stop or terminate."),
     ("EBS", "network-attached, persistent — survives stop, terminate, and can be reattached."),
     ("Temporary, reproducible data", "highest performance matters more than persistence — Instance Store."),
     ("Data that must survive the instance", "an application volume, a database — EBS.")],
    note="One line: data that can be lost fits Instance Store — data that must survive fits EBS.")

# 7 — Applied
d.table_slide("Module 15", "Instance Store vs. EBS, Applied", "Matching the data to the right storage",
    ["Data", "Right storage"],
    [["Batch-processing scratch space, regenerated every run", "Instance Store — reproducible, doesn't need to persist"],
     ["A database's primary data volume", "EBS — must survive the instance's lifecycle"]],
    col_widths=[7.6, 5.0],
    note="Reproducible and disposable points to Instance Store; must-survive points to EBS.")

# 8 — Section intro: S3 storage classes
d.content_slide("S3 Storage Classes and Lifecycle Policies",
    "Not all data needs to be equally accessible, equally quickly, at the same price", "Module 15")

# 9 — Exam trap: S3 storage classes
d.quad_box_slide("COMMON EXAM TRAP", "Access Frequency Sets the Class", "And a lifecycle policy automates the move as data ages",
    [("S3 Standard", "frequently accessed — millisecond retrieval, highest per-GB cost."),
     ("S3 Glacier", "archival — lowest cost, retrieval takes minutes to hours."),
     ("Infrequent but immediate access", "Standard-IA — lower cost, still millisecond retrieval."),
     ("Rarely accessed, delay acceptable", "Glacier, moved there automatically by a lifecycle policy.")],
    note="One line: frequency of access sets the class — a lifecycle policy handles the transition as that frequency drops.")

# 10 — Applied
d.table_slide("Module 15", "S3 Storage Classes, Applied", "Matching the access pattern to the right class",
    ["Access pattern", "Right storage class"],
    [["Accessed constantly, needs the fastest retrieval", "S3 Standard"],
     ["Rarely accessed, a retrieval delay of minutes to hours is fine", "S3 Glacier, reached via a lifecycle policy"]],
    col_widths=[7.6, 5.0],
    note="Constant access stays in Standard; archival access moves to Glacier automatically.")

# 11 — Section intro: Caching vs resizing
d.content_slide("When a Cache Is the Right Fix",
    "“The database is slow” doesn't always mean the database needs to change", "Module 15", dark=True)

# 12 — Exam trap: Caching vs resizing
d.quad_box_slide("COMMON EXAM TRAP", "The Database Isn't Always the Problem", "Repeated reads point to a caching gap, not a sizing gap",
    [("Repeated, read-heavy queries", "the database re-fetches the same answers over and over."),
     ("Add ElastiCache", "absorbs the repeated load from memory, without touching the database."),
     ("CPU and memory look fine", "but response times are still slow — a caching gap, not a sizing problem."),
     ("Resizing alone", "doesn't fix redundant, repeated work — it just delays the same problem.")],
    note="One line: repeated, read-heavy queries point to adding a cache, not resizing or replacing the database.")

# 13 — Putting it together
d.numbered_list_slide("Module 15", "Putting It Together: Optimizing Meridian's Performance", "Every piece from tonight, in one strategy", [
    ("EBS gp3 as the default, with Provisioned IOPS (io2) reserved for Meridian Loyalty's demanding database tier", "the right baseline for most workloads, provisioned IOPS only where genuinely needed"),
    ("Instance Store for Café Sol's transient batch-processing scratch space", "regenerated every run, never needs to survive an instance replacement"),
    ("S3 lifecycle policies automatically moving Ridgeline's order records to Standard-IA, then Glacier", "no one manually tracking and moving aging data"),
    ("ElastiCache in front of Meridian Loyalty's rewards-lookup database", "absorbing repeated, read-heavy queries without touching the database itself"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 15", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Instance Store and EBS are basically the same”", "Instance Store is ephemeral; EBS persists past the instance's lifecycle."),
    ("“Glacier is always the cheapest, so always use it”", "Only for data that can tolerate a minutes-to-hours retrieval delay."),
    ("“Slow database response always means resize it”", "Repeated read-heavy queries often mean the fix is a cache, not a bigger database."),
], dark=True)

# 15 — SOA-C02 track complete
d.table_slide("Module 15", "SOA-C02 Track, Complete", "Six domains, one course, fifteen modules",
    ["Domain", "What it covered"],
    [["Domain 1 (Modules 1–3)", "Watching the systems — metrics, alarms, remediation, and logging"],
     ["Domain 2 (Modules 4–6)", "Keeping them running — scalability, high availability, backup and restore"],
     ["Domain 3 (Modules 7–8)", "Building it the same way every time — provisioning and automating the routine work"],
     ["Domain 4 (Modules 9–10)", "Securing what's running — policies, continuous compliance, data and network protection"],
     ["Domain 5 (Modules 11–13)", "Connecting it — networking, DNS and content delivery, troubleshooting"],
     ["Domain 6 (Modules 14–15)", "Making it efficient — cost optimization, compute and storage performance"]],
    col_widths=[3.8, 8.8],
    note="Six genuinely different operational disciplines — not one skill repeated six times.")

# 16 — Recap
d.content_slide("Recap",
    "Instance Store vs. EBS, S3 storage classes and lifecycle policies, caching vs. resizing the database", "Module 15", dark=True)

# 17 — Closing
d.closing_slide("Compute and Storage", "Performance Optimization", "SOA-C02 track complete")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
