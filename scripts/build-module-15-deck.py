"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/15-data-engineering-patterns.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-15-deck.py

Paired with instructor-private/15-data-engineering-patterns-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "15-data-engineering-patterns.pptx")

d = Deck(15, "Data Engineering Patterns",
          "Most of the café's data disappears the moment it's used. That's the actual problem.")

# 1 — Title
d.title_slide("Module 15 · Lecture", ["Data Engineering", "Patterns"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 15", "Question of the Day", "Before we start",
    [("Frank wants to know which menu items sell best by time of day",
      "Can today's system actually answer that, or does the data just disappear after each order?"),
     ("Recap: Module 14 made small, event-driven jobs run without servers", "Lambda, API Gateway, Step Functions — serverless compute"),
     ("Tonight's shift", "From processing one transaction at a time to capturing and analyzing all of them")])

# 3 — Objectives
d.numbered_list_slide("Module 15", "Objectives", "Five things by the end of tonight", [
    ("Explain what Amazon Kinesis does", "and how it captures streaming data in real time"),
    ("Describe what AWS Glue does", "and how it prepares data for analysis"),
    ("Explain what a data lake is", "and how Amazon S3 serves as one"),
    ("Describe how Amazon Athena queries data", "directly in a data lake, with standard SQL"),
    ("Explain why analytics stays separate", "from the café's operational, transaction-processing database"),
])

# 4 — The café's data problem
d.content_slide("The Café's Data Problem",
    "Every order, view, and loyalty scan is data — and right now, most of it disappears after it's used", "Module 15")

# 5 — Kinesis
d.content_slide("Amazon Kinesis: Capturing Data as It Happens",
    "POS terminals, the website, the app — a continuous stream of small events, constantly", "Module 15", dark=True)

# 6 — Exam trap: streaming vs one-time bulk data
d.quad_box_slide("COMMON EXAM TRAP", "Kinesis Is Not for One-Time Bulk Data", "“Streaming” and “moving a big batch once” are different jobs",
    [("Kinesis fits", "Continuous events needing near-real-time processing — clicks, IoT readings, logs."),
     ("Producers and consumers", "Decoupled, same shape as Module 13 — but the “message” is a continuous flow."),
     ("Data that already exists in bulk?", "Moving or transforming it once is not a streaming problem."),
     ("That's Glue's job instead", "A scheduled, one-time or periodic batch transform, not a live stream.")],
    note="Study cue: continuous and real-time points to Kinesis. Bulk and one-time points to Glue.")

# 7 — Glue
d.content_slide("AWS Glue: Preparing Data for Analysis",
    "Extract, transform, load — and a Data Catalog so other services know what data exists", "Module 15")

# 8 — Kinesis vs Glue table
d.table_slide("Module 15", "Kinesis vs. Glue", "Know the difference, not just the names",
    ["", "Amazon Kinesis", "AWS Glue"],
    [["Handles", "Continuous, real-time streaming data", "Batch extract, transform, and load (ETL)"],
     ["Timing", "As events happen", "Scheduled or triggered jobs"],
     ["Typical use", "Clickstream, IoT, application logs", "Cleaning and cataloging data for analysis"]],
    col_widths=[3.0, 4.7, 4.7])

# 9 — S3 as a data lake
d.content_slide("Amazon S3 as a Data Lake",
    "Raw, native-format data at scale — structured, semi-structured, and unstructured alike", "Module 15", dark=True)

# 10 — schema-on-read vs schema-on-write
d.split_card_slide("Module 15", "Schema-on-Read vs. Schema-on-Write", "When structure actually gets applied",
    "Traditional Database",
    [("Schema-on-write", "data must already fit a predefined schema before it's written"),
     ("Structure decided upfront", "before you know every way the data will eventually be used")],
    "Data Lake (S3)",
    "Schema-on-read",
    ["Raw data is kept as-is, in its native format", "Structure is applied only when it's actually queried"])

# 11 — Athena
d.content_slide("Amazon Athena: Querying the Data Lake Directly",
    "Standard SQL, straight against S3 — no database to provision, no data to move first", "Module 15")

# 12 — Putting the pipeline together
d.four_up_slide("Module 15", "The Data Pipeline, Step by Step", "Capture, transform, store, query", [
    ("1", "Capture", "Continuous events as they happen — Kinesis"),
    ("2", "Transform", "Clean, transform, and catalog the raw data — Glue"),
    ("3", "Store", "Raw and processed data at scale, cheaply — S3, as a data lake"),
    ("4", "Query", "Standard SQL, no database to provision — Athena"),
])

# 13 — Exam trap: why analytics stays off the operational database
d.quad_box_slide("COMMON EXAM TRAP", "Why Analytics Stays Off the Operational Database", "Different access patterns, competing for the same resources",
    [("RDS needs to stay fast", "for small, frequent transactions — placing an order, updating inventory."),
     ("A big analytics query", "is the opposite shape — infrequent, but scanning huge amounts of data at once."),
     ("Running both together", "risks slowing down, or briefly locking, the system customers are actively using."),
     ("The fix: separate the pipeline", "Kinesis, Glue, S3, and Athena — analytics never competes with checkout.")],
    note="Study cue: “can we just query the analytics off the production database?” is almost always the wrong answer.")

# 14 — Putting it together
d.numbered_list_slide("Module 15", "Putting It Together: The Café's Analytics Pipeline", "Frank and Martha's questions, answered without touching checkout", [
    ("Order events, menu views, and loyalty scans stream into Kinesis", "continuously, as they happen"),
    ("Glue jobs clean and catalog that raw data on a schedule", "landing it in S3 — the café's data lake"),
    ("Athena queries the data lake directly with SQL", "no separate analytics database, no risk to the live RDS ordering system"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 15", "Common Mix-Ups", "Worth getting right before Module 16", [
    ("“Kinesis and Glue do the same thing”", "Kinesis is real-time streaming capture; Glue is scheduled batch ETL."),
    ("“A data lake needs a fixed schema like a database”", "A data lake applies structure on read — raw data is kept as-is."),
    ("“Just run analytics on the production database”", "Different access patterns compete for the same resources — keep them separate."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Think about what happens to all of this — orders, the data lake, everything — if the café's Region goes down", "Module 15")

# 17 — Closing
d.closing_slide("Data Engineering", "Patterns", "Next up: planning for disaster")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
