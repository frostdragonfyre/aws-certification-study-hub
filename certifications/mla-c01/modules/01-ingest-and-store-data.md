# Module 1: Ingest and Store Data

**Course:** AWS Academy Machine Learning Engineering — building toward MLA-C01, AWS Certified Machine Learning Engineer – Associate
**Estimated study time:** 45 minutes

## Why this matters

Every ML system starts the same way: data has to get from wherever it lives into somewhere a training job can actually use it, in a format that doesn't waste time or money getting there. This is the first module of the MLA-C01 course, and it opens Domain 1 — Data Preparation for Machine Learning, the single largest domain on the exam at 28% of scored content. Nothing downstream — feature engineering, training, deployment — matters if the data underneath it was ingested or stored the wrong way.

## Learning objectives

By the end of this module, you should be able to:

- Choose between Amazon S3, Amazon EFS, and Amazon FSx for a stated ML data-access pattern
- Distinguish batch ingestion from streaming ingestion, and know which AWS services fit each
- Choose an appropriate data format (Parquet, JSON, CSV, ORC, Avro, RecordIO) for a stated access pattern
- Ingest data into SageMaker Data Wrangler and SageMaker Feature Store
- Design a data ingestion and storage strategy for a stated ML requirement

---

## S3 vs. EFS vs. FSx: Matching Storage to Access Pattern

All three store data AWS can train models against, but they answer different questions about how that data gets accessed.

**Amazon S3** is durable, virtually unlimited object storage — the default for a data lake, for bulk training datasets, and for anything accessed by a single job or a small number of jobs at a time. It's the right starting point for most ML data unless something specific rules it out.

**Amazon EFS** is a shared, POSIX-compliant file system that multiple instances can mount and read from **concurrently**, with each instance seeing a consistent, live view of the same files. It fits distributed training jobs where many instances need simultaneous, low-latency access to the same file set — something S3's object interface isn't built for.

**Amazon FSx** (for Lustre, or for NetApp ONTAP) is a high-performance file system built for the most demanding shared-access workloads — Lustre in particular is built for high-throughput, low-latency parallel access, often backed directly by an S3 bucket so a training job can read S3 data through a POSIX file interface at much higher throughput than S3 alone.

> ⚠️ **Exam trap:** a scenario describing **many training instances needing simultaneous, concurrent, POSIX-style access to the same files** is describing a fit for **EFS or FSx**, not S3 — S3 is an object store, not a shared file system, and doesn't give concurrent instances a live, consistent file-level view. A scenario describing bulk, durable storage accessed by one job at a time is a fit for **S3**.

## Batch vs. Streaming Ingestion

Data arrives in one of two shapes: already sitting somewhere in bulk, or continuously arriving in real time — and the ingestion mechanism has to match which one you're actually facing.

**Batch ingestion** moves data that already exists — periodic exports, bulk historical datasets, files landing in S3 on a schedule. It's the simpler, cheaper default when the data isn't time-sensitive and doesn't need to be reflected in a model or feature store within seconds of being generated.

**Streaming ingestion** handles data that's continuously generated and needs to be captured close to real time — **Amazon Kinesis** (Data Streams and Data Firehose), **Apache Flink** (via Amazon Managed Service for Apache Flink), and **Apache Kafka** are the AWS-native and AWS-supported ways to capture that continuous flow, buffer it, and land it somewhere durable.

> ⚠️ **Exam trap:** a scenario describing data that **already exists in bulk**, with no urgency about freshness, is a fit for **batch ingestion** into S3. A scenario describing data that's **continuously generated and needs near-real-time capture** — clickstream events, sensor readings, transaction feeds — is a fit for **streaming ingestion** with Kinesis, Flink, or Kafka — reaching for a batch job to handle a continuous stream is the trap.

## Choosing a Data Format

The format data is stored in shapes both storage cost and how efficiently a training job can read it.

**Row-based formats** like **CSV** and **JSON** store each record as a complete row — simple, human-readable, and easy to generate, but inefficient to scan when a job only needs a handful of columns out of many, since it still has to read every field in every row.

**Columnar formats** like **Apache Parquet** and **Apache ORC** store data column by column instead — a query or training job that only needs a few columns reads only those columns, and columnar layouts typically compress far better than row-based ones, cutting both storage cost and I/O time on large datasets.

**RecordIO**, paired with **Protocol Buffers**, is optimized specifically for streaming data efficiently into **SageMaker's built-in algorithms** during training, minimizing the I/O overhead of reading many small files.

> ⚠️ **Exam trap:** a scenario describing **large-scale analytical access to a subset of columns** out of a wide dataset is a fit for a **columnar format (Parquet or ORC)** — reaching for CSV or JSON at that scale wastes both storage and read time. A scenario specifically about **efficient I/O into a SageMaker built-in algorithm's training job** points to **RecordIO**, not a general-purpose format chosen for human readability.

## Bringing Data Into SageMaker

Once data is ingested and stored, two SageMaker-native destinations matter for the rest of the ML lifecycle. **SageMaker Data Wrangler** is where raw, ingested data gets imported for exploration, visualization, cleaning, and transformation — the on-ramp into feature engineering, covered in the next module. **SageMaker Feature Store** is a purpose-built repository for storing engineered features so they can be reused consistently across training and inference, avoiding the classic problem of a feature computed one way for training and a slightly different way in production.

Merging data that arrives from multiple different sources — Meridian's transaction database, Café Sol's point-of-sale exports, Ridgeline's order history — typically happens through **AWS Glue** or **Apache Spark on Amazon EMR**, both built for combining and transforming data at scale before it lands in its final ingested form.

## Putting It Together: Diego's Ingestion Strategy for Meridian

Diego's data ingestion and storage design, opening Domain 1 and the MLA-C01 course:

- **S3** as the default landing zone for Meridian Loyalty's historical transaction exports and Ridgeline's order history — bulk, durable, accessed by a small number of training jobs at a time.
- **FSx for Lustre**, backed by an S3 bucket, for the distributed training job that needs many GPU instances reading the same large image dataset simultaneously at high throughput.
- **Kinesis Data Streams** capturing Café Sol's point-of-sale transactions continuously, for the fraud-detection model that needs near-real-time signal.
- **Parquet** as the standard format for anything that will be queried or trained against at scale, with **AWS Glue** merging Meridian's separate data sources into a single, consistent ingested dataset.

## What to skip

You don't need to memorize every FSx variant's exact throughput specification or every Kinesis shard-capacity number — that's implementation depth beyond this exam. What matters is knowing when a shared, concurrent file-access pattern rules out S3 in favor of EFS or FSx, when a continuous data source rules out simple batch ingestion, and matching a row-based versus columnar format to how the data will actually be read.

## Key takeaways

- S3 is the default for bulk, durable ML data; EFS and FSx fit workloads needing concurrent, POSIX-style shared access across many training instances.
- Batch ingestion fits data that already exists in bulk; streaming ingestion (Kinesis, Flink, Kafka) fits continuously generated data needing near-real-time capture.
- Columnar formats (Parquet, ORC) fit large-scale analytical access to a subset of columns; RecordIO fits efficient I/O into SageMaker's built-in algorithms.
- SageMaker Data Wrangler is the on-ramp for exploring and transforming ingested data; SageMaker Feature Store keeps engineered features consistent between training and inference.
- This opens Domain 1 — the largest domain on the exam — and the entire MLA-C01 course: everything from feature engineering through deployment and monitoring builds on data that was ingested and stored correctly first.

## Further reading

- [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) — durable object storage for ML datasets.
- [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) — shared, POSIX-compliant file storage.
- [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html) — high-throughput file storage for large-scale training.
- [Amazon SageMaker Feature Store](https://docs.aws.amazon.com/sagemaker/latest/dg/feature-store.html) — a consistent feature repository for training and inference.
