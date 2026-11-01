[Course index](../README.md) · [Read the paired lesson](../modules/06-adding-a-database-layer.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 6 Review Quiz**

Adding a Database Layer · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|
| | |

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

> A relational database organizes data into structured tables with defined schemas and enforced relationships between them.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service is a managed relational database supporting engines such as MySQL, PostgreSQL, and MariaDB?
>
> **A.** Amazon DynamoDB
> **B.** Amazon RDS
> **C.** Amazon Redshift
> **D.** Amazon Neptune

**3. [Fill in the Blank] Easy**

> Amazon ____________ is AWS's fully managed non-relational database, built for fast performance at very large scale.

**4. [Multiple Choice] Easy**

> What does an RDS Multi-AZ deployment provide?
>
> **A.** Additional read capacity across many Regions
> **B.** A synchronous standby replica in a second Availability Zone with automatic failover
> **C.** Automatic conversion from relational to non-relational storage
> **D.** Unlimited free storage

**5. [True / False] Easy**

> In a DynamoDB table, every item must have exactly the same set of attributes as every other item.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which AWS database service is purpose-built for graph data, such as relationships in a social network or recommendation engine?
>
> **A.** Amazon Redshift
> **B.** Amazon ElastiCache
> **C.** Amazon Neptune
> **D.** Amazon DocumentDB

**7. [Fill in the Blank] Moderate**

> RDS ____________ replicas offload read traffic to additional copies of a database without consuming the primary instance's write capacity.

**8. [Multiple Choice] Moderate**

> What is Amazon Aurora, in relation to Amazon RDS?
>
> **A.** A completely separate service that competes with RDS
> **B.** A premium engine option you select inside RDS, built for higher performance and availability
> **C.** The free tier version of RDS
> **D.** A migration tool for moving databases into RDS

**9. [True / False] Moderate**

> Amazon Redshift is purpose-built for data warehousing and large-scale analytical queries rather than everyday transactional workloads.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which AWS service is designed specifically to move data from an on-premises database into an AWS-hosted one, often with minimal downtime?
>
> **A.** AWS Database Migration Service
> **B.** Amazon ElastiCache
> **C.** AWS CloudFormation
> **D.** Amazon Athena

**11. [Fill in the Blank] Moderate**

> Amazon ____________ provides in-memory caching, used to deliver extremely low-latency reads in front of a primary database.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> An application looks up single user profiles by user ID millions of times per hour, with no joins and no complex queries, and different profiles store different optional fields. Which database fits best?
>
> **A.** Amazon RDS with a MySQL engine
> **B.** Amazon DynamoDB
> **C.** Amazon Redshift
> **D.** Amazon Neptune

**13. [Scenario / Judgment] Hard**

> A relational database is healthy on writes but readers are experiencing slow query times during peak hours. Which feature directly addresses this?
>
> **A.** Multi-AZ deployment
> **B.** Read replicas
> **C.** Automated backups
> **D.** Converting the database to DynamoDB

**14. [Scenario / Judgment] Hard**

> A finance team needs to run large analytical queries across seven years of historical transaction data to produce trend reports. Which service is built for this?
>
> **A.** Amazon RDS
> **B.** Amazon DynamoDB
> **C.** Amazon Redshift
> **D.** Amazon ElastiCache

**15. [Scenario / Judgment] Hard**

> A company faces both a risk of database downtime during an AZ failure and a read-traffic bottleneck at peak hours. What should they implement?
>
> **A.** Multi-AZ only, since it also improves read performance
> **B.** Read replicas only, since replicas provide automatic failover
> **C.** Both Multi-AZ and read replicas, because failover protection and read scaling are separate problems
> **D.** Neither — a larger instance size solves both automatically

**16. [Scenario / Judgment] Hard**

> Why is choosing a database service described in this module as the same skill as choosing an S3 storage class in Module 4?
>
> **A.** Both decisions are made in the same AWS console screen
> **B.** Both require matching the shape of the data and its access pattern to the right tool rather than defaulting to the most familiar option
> **C.** Both services charge identical prices
> **D.** Both are decided automatically by AWS with no input from the architect

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "DynamoDB scales better than RDS, so it's the better choice for any application expecting growth." What's the correct correction?
>
> **A.** They're right — scale is the deciding factor for every database choice
> **B.** Scalability doesn't override structure. If the data genuinely requires complex joins and enforced referential integrity, a relational service is the right choice regardless of how well a NoSQL alternative scales
> **C.** RDS actually scales better than DynamoDB in all cases
> **D.** DynamoDB and RDS are interchangeable, so either works

**18. [Scenario / Judgment] Very Hard**

> A subscription service needs a highly available relational database. Its dataset grows continuously, and read traffic is heavy and unpredictable enough that it will need substantially more read replicas than a standard RDS engine supports. Which option fits best?
>
> **A.** Amazon DynamoDB, because it handles unpredictable traffic
> **B.** Amazon Redshift, because it handles large datasets
> **C.** Amazon Aurora, because it supports more read replicas and scales its storage automatically while remaining relational
> **D.** Amazon Neptune, because it handles relationships between records

**19. [Scenario / Judgment] Very Hard**

> Why is it a mistake to describe Amazon Redshift as "RDS for bigger data"?
>
> **A.** Redshift is actually smaller in capacity than RDS
> **B.** They target different workload types — Redshift is built for OLAP analytical queries across historical data, while RDS handles OLTP transactional operations, and they behave differently as a result
> **C.** Redshift is a non-relational database and RDS is relational
> **D.** Redshift can only be used with DynamoDB as a front end

**20. [Scenario / Judgment] Very Hard**

> The café's order and inventory data must stay properly related (orders link to customers and products), survive an outage, absorb spiky morning read traffic, and grow continuously without manual storage management. Which choice best satisfies all four requirements, and why?
>
> **A.** Amazon DynamoDB, because it scales automatically and handles spiky traffic well
> **B.** Amazon Aurora, because the enforced relationships rule out a NoSQL option, while the availability, aggressive read scaling, and auto-growing storage requirements point past a standard RDS engine
> **C.** Amazon Redshift, because it manages large and growing datasets
> **D.** Amazon ElastiCache, because caching solves spiky read traffic

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
