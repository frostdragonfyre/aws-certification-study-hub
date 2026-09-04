**NET-3100BB2 · AWS MACHINE LEARNING ENGINEER ASSOCIATE · WAKE TECH**

**Module 1 Knowledge Check**

Ingest and Store Data · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|

*Instructions: Answer every question. Questions get harder as you go — the last several are exam-style judgment questions where more than one answer looks reasonable. For those, pick the BEST answer and be ready to defend it out loud.*

| **Question types** | **What to do** |
|---|---|
| Multiple Choice | Circle one letter. |
| True / False | Circle TRUE or FALSE. |
| Fill in the Blank | Write your answer on the line. |
| Scenario / Judgment | Circle the BEST answer. Note WHY the others fail. |

---

## Easy Questions

**1. [True / False] Easy**

> Amazon S3 gives multiple training instances a live, concurrent, POSIX-style view of the same files.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service is a shared, POSIX-compliant file system that multiple instances can mount and read from concurrently?

> **A.** Amazon S3
> **B.** Amazon EFS
> **C.** Amazon Redshift
> **D.** AWS Glue

**3. [Fill in the Blank] Easy**

> ____________ ingestion moves data that already exists in bulk, such as periodic exports or historical datasets.

**4. [Multiple Choice] Easy**

> Which storage format is optimized specifically for efficient I/O into SageMaker's built-in algorithms during training?

> **A.** CSV
> **B.** JSON
> **C.** RecordIO
> **D.** Plain text

**5. [True / False] Easy**

> Columnar formats like Parquet typically compress better than row-based formats like CSV.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does a columnar format like Parquet read faster than CSV when a query only needs a few columns out of many?

> **A.** Parquet stores each row as a single compressed block
> **B.** Parquet stores data column by column, so only the needed columns are read
> **C.** CSV is actually a type of columnar format
> **D.** Parquet cannot be compressed at all

**7. [Fill in the Blank] Moderate**

> Amazon ____________ (Data Streams or Data Firehose), Apache Flink, and Apache Kafka are the AWS-native and AWS-supported ways to capture continuously generated data close to real time.

**8. [Multiple Choice] Moderate**

> A training job needs many GPU instances to read the same large image dataset simultaneously at very high throughput, backed by data already in S3. What fits best?

> **A.** Amazon S3 alone, with each instance downloading its own copy
> **B.** Amazon FSx for Lustre, backed by the S3 bucket
> **C.** Amazon DynamoDB
> **D.** AWS Glue DataBrew

**9. [True / False] Moderate**

> SageMaker Feature Store exists to keep engineered features consistent between training and inference.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which AWS services are commonly used to merge data arriving from multiple different sources at scale?

> **A.** AWS Glue or Apache Spark on Amazon EMR
> **B.** Amazon CloudFront
> **C.** AWS Budgets
> **D.** Amazon Route 53

**11. [Fill in the Blank] Moderate**

> SageMaker ____________ is where raw, ingested data gets imported for exploration, visualization, cleaning, and transformation.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Café Sol's point-of-sale system generates a continuous stream of transactions that a fraud-detection model needs to evaluate in near real time. What ingestion approach fits best?

> **A.** A nightly batch job loading the previous day's transactions into S3
> **B.** Kinesis Data Streams capturing the transactions continuously as they occur
> **C.** A weekly manual export to CSV
> **D.** Storing transactions only in FSx for Lustre

**13. [Scenario / Judgment] Hard**

> Ridgeline's historical order data sits in bulk, is only accessed by one or two training jobs at a time, and has no freshness requirement. What storage and ingestion approach fits best?

> **A.** Amazon EFS with a continuous streaming pipeline
> **B.** Amazon S3 with a batch ingestion job
> **C.** Amazon FSx for Lustre with real-time replication
> **D.** Kinesis Data Streams with a one-second retention window

**14. [Scenario / Judgment] Hard**

> A dataset will be queried repeatedly by analytics jobs that each only need 4 of its 60 columns. What data format choice fits best?

> **A.** CSV, since it's the simplest to generate
> **B.** JSON, since it's human-readable
> **C.** Parquet, since a columnar format lets each query read only the needed columns
> **D.** RecordIO, since it's the most compact for any workload

**15. [Scenario / Judgment] Hard**

> A team wants to make sure the exact same engineered features are used both when training a model and when serving predictions in production. What should they use?

> **A.** SageMaker Data Wrangler alone, re-run separately in each environment
> **B.** SageMaker Feature Store, as a shared, consistent feature repository
> **C.** Two separate, independently maintained CSV files
> **D.** Amazon CloudFront

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Since S3 can store any file, it's always the right choice no matter how many training instances need to read the data at once." Correct this using this module's content.

> **A.** They're right — S3 is always the correct choice regardless of access pattern
> **B.** They're wrong: S3 is an object store without a live, concurrent, POSIX-style view across instances — many training instances needing simultaneous, low-latency shared access to the same files is a fit for EFS or FSx instead, not S3 alone
> **C.** EFS and FSx cannot be used for ML training data
> **D.** S3 provides the same concurrent file semantics as EFS

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes ingesting Café Sol's continuous transaction stream with a nightly batch job instead of Kinesis, arguing "batch is simpler and cheaper." Evaluate this using this module's content.

> **A.** Agree — batch ingestion is always simpler and should always be preferred
> **B.** Disagree — the fraud-detection use case needs near-real-time signal, and a nightly batch job would introduce up to a day of delay before fraudulent transactions are even seen, defeating the purpose; Kinesis's continuous capture is what the requirement actually calls for
> **C.** Disagree, but only because batch jobs cannot read from point-of-sale systems
> **D.** Agree, since Kinesis cannot handle transaction-level data

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why choosing RecordIO for a general-purpose analytics dataset queried by business intelligence tools would likely be the wrong call.

> **A.** RecordIO and Parquet are functionally identical for every use case
> **B.** RecordIO is optimized specifically for efficient I/O into SageMaker's built-in algorithms during training, not for general-purpose analytical querying — a columnar format like Parquet or ORC fits a BI workload's column-subset access pattern far better
> **C.** RecordIO cannot be read by any AWS service
> **D.** Business intelligence tools require row-based formats exclusively

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that all of Meridian's ML data should be stored in FSx for Lustre by default, "since it's the fastest option available." Argue against this using this module's content.

> **A.** Agree — FSx for Lustre has no downside compared to S3
> **B.** Disagree — FSx for Lustre is built for demanding, concurrent, high-throughput shared access, which most of Meridian's bulk, single-job-at-a-time datasets don't need; S3 remains the simpler, more cost-effective default, with FSx reserved for the specific workloads that actually require that level of shared throughput
> **C.** Disagree, but only because FSx for Lustre cannot be backed by S3
> **D.** Agree, since S3 cannot store training data at all

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as data eventually lands in AWS somewhere, the storage service, ingestion method, and format chosen don't really matter." Evaluate this claim using this module's content.

> **A.** Agree — all AWS storage, ingestion, and format choices perform identically
> **B.** Disagree — S3 versus EFS versus FSx trades off concurrent access very differently, batch versus streaming ingestion trades off freshness and complexity, and row-based versus columnar format trades off read efficiency and cost — each choice depends on the specific access pattern, not a one-size-fits-all default
> **C.** Disagree, but only because AWS has just one storage option
> **D.** Agree, since cost and performance are unrelated to storage, ingestion, or format choice

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
