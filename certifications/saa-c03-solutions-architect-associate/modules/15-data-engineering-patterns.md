<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](14-building-serverless-architectures-and-microservices.md) · [Next module](16-planning-for-disaster.md) · [Quiz](../quizzes/15-data-engineering-patterns-quiz.md) · [Slides](../lectures/15-data-engineering-patterns.pptx)
<!-- /hub-navigation -->

# Module 15: Data Engineering Patterns

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

Every order, every menu view, every loyalty-points transaction the café's systems now generate is a small piece of data — and right now, most of it disappears the moment it's used. Frank wants to know which menu items actually sell best by time of day. Martha wants to spot slow weeks before they happen, not after. None of that is possible from a system built only to process one order at a time; it requires capturing, storing, and analyzing data at a completely different scale than a single transaction.

This module is about **data engineering patterns**: how to capture continuous streams of data as they happen, store large volumes of raw and processed data cost-effectively, and query it for real answers — without building any of that on top of the café's operational, transaction-processing database.

## Learning objectives

By the end of this module, you should be able to:

- Explain what Amazon Kinesis does and how it captures streaming data in real time
- Describe what AWS Glue does and how it prepares data for analysis
- Explain what a data lake is and how Amazon S3 serves as one
- Describe how Amazon Athena queries data directly in a data lake
- Explain why analytics workloads are kept separate from operational databases

---

## Amazon Kinesis: Capturing Data as It Happens

The café's point-of-sale terminals, its website, and its mobile app all generate a continuous stream of small events — an order placed, a menu item viewed, a loyalty scan — arriving constantly, not in one predictable batch. **Amazon Kinesis** is built to capture and process exactly this kind of continuous, real-time data stream, at a scale a single database table was never designed to absorb.

Producers write records onto a Kinesis **data stream** continuously, and one or more consumers read from it — independently, and without slowing the producers down. This is a familiar shape from Module 13: producers and consumers decoupled from each other, except here the "message" is a continuous flow of small events rather than individual, discrete tasks like an order confirmation.

> ⚠️ **Exam trap:** Kinesis is for *streaming* data arriving continuously and needing near-real-time processing — clickstream data, IoT sensor readings, application logs. It is not the right answer for data that already exists in bulk and needs to be moved or transformed once, which is squarely AWS Glue's job instead.

## AWS Glue: Preparing Data for Analysis

Raw data — whether captured from Kinesis or sitting in existing files — usually isn't in a shape that's ready to query. Fields are inconsistent, formats don't match, and there's no catalog of what data even exists or where. **AWS Glue** is a managed **ETL (Extract, Transform, Load)** service: it extracts data from a source, transforms it into a clean, consistent, query-ready format, and loads the result somewhere it can be analyzed.

Glue also maintains a **Data Catalog** — a persistent metadata store describing the tables, schemas, and locations of data across your data lake, so that other services (Athena among them) know what data exists and how it's structured, without you having to define it separately in each place you query it.

### Kinesis vs. Glue: know the difference

| | Amazon Kinesis | AWS Glue |
|---|---|---|
| Handles | Continuous, real-time streaming data | Batch extract, transform, and load (ETL) |
| Timing | As events happen | Scheduled or triggered jobs |
| Typical use | Clickstream, IoT, application logs | Cleaning and cataloging data for analysis |

## Amazon S3 as a Data Lake

A **data lake** is a centralized repository that holds large volumes of data in its raw, native format — structured, semi-structured, and unstructured alike — without requiring it to be transformed into a fixed schema before it's stored. **Amazon S3** is commonly used as the storage layer for a data lake: durable, effectively unlimited in scale, and inexpensive enough to hold years of raw order history, log files, and clickstream data without needing to decide in advance exactly how every byte of it will eventually be queried.

This is a deliberate contrast with a traditional database, which expects data to already fit a predefined schema before it's written. A data lake keeps the raw data as-is, and applies structure only when it's actually read — sometimes called **schema-on-read**, versus a database's **schema-on-write**.

## Amazon Athena: Querying the Data Lake Directly

Once raw and processed data is sitting in S3, **Amazon Athena** lets you run standard SQL queries directly against it — with no database to provision, no data to load anywhere else first, and no servers to manage. Athena reads the data in place in S3 (often using the table definitions Glue's Data Catalog already maintains) and charges based on the amount of data scanned per query.

For Frank's "which menu items sell best by time of day" question, this means: no separate analytics database has to be stood up and kept in sync — Athena queries the order history sitting in the data lake directly, using ordinary SQL Frank's team already knows.

### Putting the pipeline together

| Step | Service |
|---|---|
| Capture continuous events as they happen | Kinesis |
| Clean, transform, and catalog the raw data | Glue |
| Store raw and processed data at scale, cheaply | S3 (as a data lake) |
| Query it with SQL, without provisioning a database | Athena |

## Why Analytics Stays Off the Operational Database

It would be simpler, on the surface, to just run Frank's analytics queries directly against the same RDS database the ordering system uses. This is a mistake the exam expects you to catch: **analytics workloads and operational (transactional) workloads have very different access patterns**, and running both on the same database means they compete for the same resources.

The café's ordering system needs RDS to stay fast and responsive for small, frequent read/write transactions — placing an order, updating inventory. A large analytics query scanning months of order history is the opposite shape of workload: infrequent, but scanning huge amounts of data at once. Running that query against the live operational database risks slowing down, or even briefly locking, the very system customers are actively placing orders through. Separating analytics into its own pipeline — Kinesis, Glue, S3, and Athena — means Frank's queries never compete with a customer trying to check out.

## Putting It Together: The Café's Analytics Pipeline

Order events, menu views, and loyalty scans stream continuously into Kinesis. AWS Glue jobs clean and catalog that raw data on a schedule, landing it in S3, which serves as the café's data lake — holding years of history cheaply, in its raw and processed forms alike. Frank and Martha's questions get answered by Athena, querying that data lake directly with SQL, with no separate analytics database to provision and no risk to the operational RDS database the ordering system depends on every minute of the day.

## What to skip

You don't need to write Kinesis Data Streams consumer code, hand-author Glue ETL scripts, or memorize Athena's exact per-query pricing formula — that's implementation depth beyond the associate exam. What matters is recognizing the shape of a data engineering problem, matching each piece — capture, transform, store, query — to the right service, and knowing why that pipeline stays separate from the operational database.

## Key takeaways

- Kinesis captures continuous, real-time streaming data; Glue is batch ETL that cleans, transforms, and catalogs data — different timing, different job.
- A data lake (commonly built on S3) stores data in its raw, native format at scale, applying structure on read rather than requiring a fixed schema on write like a traditional database.
- Athena queries data directly in S3 with standard SQL, with no database to provision and no data movement required first.
- Analytics workloads and operational (transactional) workloads have different access patterns and should run on separate infrastructure, so large analytical queries never compete with, or slow down, live transaction processing.
- The four-step shape — capture, transform, store, query — maps directly to Kinesis, Glue, S3, and Athena, in that order.

## Further reading

- [Amazon Kinesis Data Streams Developer Guide](https://docs.aws.amazon.com/streams/latest/dev/introduction.html) — producers, consumers, and shard concepts.
- [AWS Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) — the Data Catalog and ETL jobs in depth.
- [Amazon Athena User Guide](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) — querying S3 data with SQL.

---

**Next:** [Module 16 — Planning for Disaster](16-planning-for-disaster.md)
