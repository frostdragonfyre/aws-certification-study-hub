"""
Builds certifications/mla-c01-machine-learning-engineer-associate/lectures/01-ingest-and-store-data.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-mla-c01-module-01-deck.py

Paired with instructor-private/01-ingest-and-store-data-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "mla-c01-machine-learning-engineer-associate", "lectures",
                    "01-ingest-and-store-data.pptx")

d = Deck(1, "Ingest and Store Data",
          "Every ML system starts here: getting data from wherever it lives into somewhere a training job can actually use it.",
          cert_code="MLA-C01")

# 1 — Title
d.title_slide("Module 1 · Lecture", ["Ingest and Store", "Data"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 1", "Question of the Day", "Before we start",
    [("A fraud-detection model needs to evaluate Café Sol's transactions within seconds of each purchase", "Would a nightly batch job ever be the right way to capture that data?"),
     ("Welcome to MLA-C01 — AWS Certified Machine Learning Engineer, Associate", "the third and final certification track in this course"),
     ("Tonight's task", "Domain 1, Task 1.1 — the first module of the entire course")])

# 3 — Objectives
d.numbered_list_slide("Module 1", "Objectives", "Five things by the end of tonight", [
    ("Choose between S3, EFS, and FSx for a stated ML data-access pattern", "matching storage to how the data is actually accessed"),
    ("Distinguish batch ingestion from streaming ingestion", "and know which AWS services fit each"),
    ("Choose an appropriate data format for a stated access pattern", "Parquet, JSON, CSV, ORC, Avro, RecordIO"),
    ("Ingest data into SageMaker Data Wrangler and SageMaker Feature Store", "the on-ramp into the rest of the ML lifecycle"),
    ("Design a data ingestion and storage strategy for a stated requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Every ML System Starts With Data Somewhere It Shouldn't Stay",
    "Ingestion and storage decisions made here shape everything downstream — feature engineering, training, deployment.", "Module 1")

# 5 — Section intro: S3 vs EFS vs FSx
d.content_slide("S3 vs. EFS vs. FSx",
    "All three store ML data — they differ in how that data can be accessed", "Module 1", dark=True)

# 6 — Exam trap: S3 vs EFS vs FSx
d.quad_box_slide("COMMON EXAM TRAP", "Matching Storage to Access Pattern", "Object storage isn't a shared file system",
    [("Amazon S3", "durable object storage — the default for bulk data, accessed by one job at a time."),
     ("EFS / FSx", "shared, POSIX-style file systems — many instances read the same files concurrently."),
     ("Bulk data, single-job access", "S3 is the right starting point."),
     ("Simultaneous, shared access needed", "EFS or FSx, not S3 alone.")],
    note="One line: concurrent, shared file-level access across many instances calls for EFS or FSx — S3 is an object store, not a shared file system.")

# 7 — Applied
d.table_slide("Module 1", "S3 vs. EFS vs. FSx, Applied", "Matching the access pattern to the right storage",
    ["Access pattern", "Right storage"],
    [["A large image dataset read simultaneously by many GPU training instances", "FSx for Lustre, backed by S3, for high-throughput shared access"],
     ["Historical order records, accessed by one or two training jobs at a time", "Amazon S3 — bulk, durable, no concurrent-access requirement"]],
    col_widths=[7.6, 5.0],
    note="Simultaneous shared access points to EFS or FSx; single-job bulk access points to S3.")

# 8 — Section intro: Batch vs streaming ingestion
d.content_slide("Batch vs. Streaming Ingestion",
    "Data arrives in one of two shapes — already sitting in bulk, or continuously arriving", "Module 1")

# 9 — Exam trap: Batch vs streaming ingestion
d.quad_box_slide("COMMON EXAM TRAP", "Already There vs. Arriving Now", "The ingestion mechanism has to match which one you're facing",
    [("Batch ingestion", "moves data that already exists — periodic exports, bulk historical datasets."),
     ("Streaming ingestion", "Kinesis, Flink, or Kafka capture continuously generated data close to real time."),
     ("Data already exists, no freshness need", "batch ingestion into S3."),
     ("Continuous data, near-real-time need", "streaming ingestion.")],
    note="One line: bulk and already-there is batch — continuous and time-sensitive is streaming.")

# 10 — Applied
d.table_slide("Module 1", "Batch vs. Streaming, Applied", "Matching the data source to the right ingestion",
    ["Data source", "Right ingestion"],
    [["Café Sol's point-of-sale transactions, needed near real time for fraud detection", "Kinesis Data Streams — continuous, near-real-time capture"],
     ["Ridgeline's historical order exports, no freshness requirement", "Batch ingestion into S3"]],
    col_widths=[7.6, 5.0],
    note="Time-sensitive and continuous points to streaming; already-there and bulk points to batch.")

# 11 — Section intro: Choosing a data format
d.content_slide("Choosing a Data Format",
    "The format shapes both storage cost and how efficiently a job can read the data", "Module 1", dark=True)

# 12 — Exam trap: Data format
d.quad_box_slide("COMMON EXAM TRAP", "Row-Based vs. Columnar", "How the data gets read decides which format fits",
    [("Row-based (CSV, JSON)", "simple, readable — but reads every field in every row, even unneeded ones."),
     ("Columnar (Parquet, ORC)", "reads only the columns a query actually needs, and compresses far better."),
     ("A query needs a few columns, at scale", "a columnar format — Parquet or ORC."),
     ("SageMaker built-in algorithm training I/O", "RecordIO, purpose-built for that job.")],
    note="One line: column-subset access at scale wants Parquet or ORC — SageMaker built-in training I/O wants RecordIO.")

# 13 — Applied
d.table_slide("Module 1", "Data Format, Applied", "Matching the read pattern to the right format",
    ["Read pattern", "Right format"],
    [["Analytics jobs each querying 4 of 60 columns, repeatedly, at scale", "Parquet — columnar, reads only the needed columns"],
     ["Streaming records into a SageMaker built-in algorithm's training job", "RecordIO — purpose-built for that I/O path"]],
    col_widths=[7.6, 5.0],
    note="Column-subset analytical access points to Parquet or ORC; SageMaker built-in training I/O points to RecordIO.")

# 14 — Putting it together
d.numbered_list_slide("Module 1", "Putting It Together: Diego's Ingestion Strategy for Meridian", "Every piece from tonight, in one strategy", [
    ("S3 as the default landing zone for bulk transaction and order history exports", "durable, accessed by a small number of training jobs at a time"),
    ("FSx for Lustre, backed by S3, for the distributed image-training job needing high-throughput concurrent access", "many GPU instances, one shared dataset"),
    ("Kinesis Data Streams capturing Café Sol's transactions continuously for near-real-time fraud detection", "a continuous source, not a periodic export"),
    ("Parquet as the standard format for anything trained or queried at scale, merged with AWS Glue", "column-subset reads stay fast, and engineered features land in SageMaker Feature Store for reuse"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 1", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“S3 works fine no matter how many instances need concurrent access”", "S3 lacks a live, shared file view — EFS or FSx fits that pattern instead."),
    ("“Batch is always simpler, so always use it”", "A continuous, time-sensitive source defeats the purpose of a batch job's inherent delay."),
    ("“RecordIO is just a general-purpose format”", "It's built specifically for SageMaker built-in algorithm training I/O, not BI or analytics."),
], dark=True)

# 16 — Recap
d.content_slide("Recap",
    "S3 vs. EFS vs. FSx, batch vs. streaming ingestion, row-based vs. columnar data formats", "Module 1", dark=True)

# 17 — Closing
d.closing_slide("Ingest and Store", "Data", "Domain 1 underway")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
