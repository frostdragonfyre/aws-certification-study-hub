**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 15 Knowledge Check**

Data Engineering Patterns · 20 questions · Practice — not graded

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

> Amazon Kinesis is built to capture continuous, real-time streaming data.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service is a managed ETL (Extract, Transform, Load) service?
>
> **A.** Kinesis
> **B.** Glue
> **C.** Athena
> **D.** S3

**3. [Fill in the Blank] Easy**

> A centralized repository that holds large volumes of raw, native-format data without requiring a fixed schema before storage is called a data ____________.

**4. [Multiple Choice] Easy**

> Which service lets you run standard SQL queries directly against data sitting in S3, without provisioning a database?
>
> **A.** RDS
> **B.** Athena
> **C.** Glue
> **D.** Kinesis

**5. [True / False] Easy**

> A data lake requires data to be transformed into a fixed schema before it can be stored.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What does AWS Glue maintain that lets other services know what data exists and how it's structured?
>
> **A.** A VPC
> **B.** A Data Catalog
> **C.** A CloudFormation stack
> **D.** A visibility timeout

**7. [Fill in the Blank] Moderate**

> Applying structure to data only when it's read, rather than requiring a fixed schema before it's written, is called schema-on-____________.

**8. [Multiple Choice] Moderate**

> What primarily determines the cost of an Amazon Athena query?
>
> **A.** The number of tables in the Data Catalog
> **B.** The amount of data scanned per query
> **C.** The number of Glue jobs that have run
> **D.** EC2 instance hours

**9. [True / False] Moderate**

> Kinesis and Glue solve the same problem and can be used interchangeably.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What is the primary difference in timing between Kinesis and Glue?
>
> **A.** Kinesis runs scheduled batch jobs; Glue processes data in real time
> **B.** Kinesis handles continuous, real-time streaming data; Glue runs scheduled or triggered batch ETL jobs
> **C.** Both only run on a fixed nightly schedule
> **D.** There is no meaningful timing difference between them

**11. [Fill in the Blank] Moderate**

> Amazon ____________ is commonly used as the storage layer underneath a data lake, due to its durability, scale, and low cost.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> The café's POS terminals, website, and mobile app generate a continuous stream of small events — orders, menu views, loyalty scans. What's the best fit for capturing them as they happen?
>
> **A.** Amazon RDS
> **B.** Amazon Kinesis
> **C.** Amazon Athena
> **D.** AWS CloudFormation

**13. [Scenario / Judgment] Hard**

> Raw captured order data has inconsistent fields and needs cleaning and cataloging before it can be usefully analyzed. What's the best fit?
>
> **A.** AWS Glue
> **B.** Kinesis alone
> **C.** DAX
> **D.** Amazon Route 53

**14. [Scenario / Judgment] Hard**

> Frank wants to run ad-hoc SQL queries against years of order history sitting in S3, without standing up a separate database. What's the best fit?
>
> **A.** Amazon RDS
> **B.** Amazon Athena
> **C.** Amazon ElastiCache
> **D.** AWS Step Functions

**15. [Scenario / Judgment] Hard**

> A team considers running Frank's monthly analytics queries directly against the live RDS ordering database, to "keep things simple." What's the risk?
>
> **A.** There is no risk to this approach
> **B.** The analytics query's access pattern — scanning huge amounts of data at once — competes with the operational database's need to stay fast for frequent, small transactions, risking slowdowns for customers actively checking out
> **C.** RDS cannot execute SELECT queries at all
> **D.** Analytics queries always run faster directly on RDS than anywhere else

**16. [Scenario / Judgment] Hard**

> A design stores raw clickstream data directly in RDS instead of S3, on the reasoning that "S3 doesn't support structured data." What's the flaw in this reasoning?
>
> **A.** The reasoning is correct
> **B.** S3 can hold structured, semi-structured, and unstructured data alike as a data lake, and is far more cost-effective and scalable for large raw volumes than a transactional database designed around a fixed schema-on-write model
> **C.** S3 cannot store any file over 1 MB
> **D.** RDS is always cheaper than S3 for this use case

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Athena is basically a database, just like RDS." Correct this using this module's content.
>
> **A.** They're right — the two are interchangeable
> **B.** Athena queries data directly in S3, in place, with no database to provision and no data to load anywhere first; RDS is a managed relational database that provisions and holds its own data — both accept SQL, but they solve different problems
> **C.** RDS and Athena are interchangeable for the café's live order-processing (OLTP) workload
> **D.** Athena stores its own separate copy of the data, independent of S3

**18. [Scenario / Judgment] Very Hard**

> Connect this module to Module 13. Decoupling separated producers and consumers using queues. How does Kinesis's producer/consumer relationship compare?
>
> **A.** It's identical, with no meaningful difference
> **B.** Same core idea — producers write continuously without waiting on consumers, and one or more independent consumers read separately — but Kinesis's "message" is a continuous flow of small stream events rather than discrete queued tasks like an order confirmation
> **C.** Kinesis has no concept of producers or consumers
> **D.** Kinesis fully replaced SQS as a service

**19. [Scenario / Judgment] Very Hard**

> A design pipes raw Kinesis stream data directly into Athena queries, skipping Glue entirely, and the team is confused why their queries return inconsistent, poorly structured results. What's missing?
>
> **A.** Nothing is missing — this is expected behavior
> **B.** Glue's transform-and-catalog step — raw streamed data typically needs cleaning, consistent formatting, and cataloging before it's genuinely useful to query, which is exactly the job Glue does between capture and query
> **C.** Athena requires RDS as a mandatory intermediate step
> **D.** Kinesis output is always already fully query-ready with no further processing needed

**20. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since S3 is cheap and durable, all analytics workloads should just query it directly with Athena — there's no need for a separate operational database at all." Argue against this using this module's content.
>
> **A.** Agree fully — Athena and S3 can replace every operational database
> **B.** Athena and S3 fit large-scale analytical queries over historical data well, but the café's live ordering system still needs RDS's fast, frequent, consistent small transactional reads and writes — the two solve different access patterns, and replacing the operational database with Athena would not serve the checkout flow's needs
> **C.** RDS becomes obsolete the moment S3 exists
> **D.** Athena supports the same transactional guarantees as RDS

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
