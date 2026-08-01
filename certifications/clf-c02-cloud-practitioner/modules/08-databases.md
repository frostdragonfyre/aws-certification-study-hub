# Module 8: Databases

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 3 — Cloud Technology and Services
**Estimated study time:** 45 minutes

## Why this matters

Every application built across the last few modules eventually needs somewhere to store data that isn't a file — customer records, orders, sensor readings, click streams. This module is about matching that data's shape to the right AWS database service, and it starts with the same managed-versus-unmanaged distinction that ran through Module 6's compute spectrum, applied now to databases specifically.

AWS names four database services constantly on this exam — Amazon RDS, Amazon DynamoDB, Amazon Redshift, and Amazon Aurora — and the questions almost always come down to one underlying split: is this data relational (structured, tables and rows, needs SQL) or non-relational (flexible, needs to scale massively, needs NoSQL)? Get that split right, and picking the specific service becomes recognition instead of memorization.

## Learning objectives

By the end of this module, you should be able to:

- Explain the difference between unmanaged and managed database solutions
- Explain Amazon RDS and identify its core functionality
- Explain Amazon DynamoDB and identify its core functionality
- Explain Amazon Redshift and when it fits
- Explain Amazon Aurora and how it relates to RDS
- Distinguish SQL (relational) from NoSQL (non-relational) databases
- Avoid the most common database traps on the exam

---

## Unmanaged vs. Managed Services, Applied to Databases

Module 6 introduced this distinction for compute; here it's the foundation for everything in this module.

- **Unmanaged**: scaling, fault tolerance, and availability are managed by you. Launch a web server on an EC2 instance, and it won't scale to handle increased load or replace an unhealthy instance unless you set that up yourself.
- **Managed**: scaling, fault tolerance, and availability are typically built into the service. Host a static website in Amazon S3, and features like scaling and fault tolerance are handled automatically and internally — you configure S3, but you don't manage its underlying infrastructure.

Running a relational database yourself, self-managed on an EC2 instance, means you personally handle patching, backups, failover, and scaling — real operational work that has nothing to do with the application logic you actually want to build. **Amazon RDS** exists specifically to take that operational burden off your plate.

> ⚠️ **Exam trap:** "managed" doesn't mean "zero configuration" — it means AWS handles more of the undifferentiated operational work (patching, backups, failover) so you can focus on the parts that are actually specific to your application.

## Amazon RDS: Managed Relational Databases

**Amazon RDS (Relational Database Service)** is a managed service for relational databases, supporting several familiar database engines (MySQL, PostgreSQL, MariaDB, Oracle, and SQL Server, alongside AWS's own Aurora engine covered below). RDS directly addresses the challenges of a self-managed relational database:

| Challenge (self-managed) | How RDS addresses it |
|---|---|
| You patch the OS and database engine yourself | RDS automates patching |
| You configure and monitor your own backups | RDS provides automated backups and snapshots |
| A single instance is a single point of failure | **Multi-AZ deployments** maintain a synchronous standby in another AZ, with automatic failover |
| Read-heavy workloads bottleneck on one instance | **Read replicas** offload read traffic to additional copies |

Relational databases organize data into **tables** with defined **schemas** — rows and columns, with relationships enforced between tables — and are queried using **SQL (Structured Query Language)**. This structure is exactly what makes relational databases a strong fit for data with clear relationships and a need for consistency, like financial transactions or order records.

> ⚠️ **Exam trap:** RDS is still relational — it doesn't change *what kind* of database you're using, only how much of the operational burden AWS absorbs. A scenario asking for a fully managed *relational* database, with an existing schema and SQL queries, is RDS (or Aurora); it's not DynamoDB, no matter how "managed" sounds appealing in the scenario.

## Amazon DynamoDB: Managed NoSQL

**Amazon DynamoDB** is a fully managed **NoSQL** database — key-value and document data, without the fixed schema a relational database requires. DynamoDB is built for consistent, single-digit-millisecond performance at virtually any scale, and like S3, there's no server for you to size or manage.

NoSQL databases trade the rigid structure and complex relationship queries of SQL for flexibility and horizontal scale. A DynamoDB table can store items with different sets of attributes side by side, and it's the default answer whenever a scenario emphasizes massive scale, unpredictable or evolving data shape, and fast key-based lookups — a shopping cart, a session store, a mobile app's user profiles.

> ⚠️ **Exam trap:** "needs complex queries joining data across multiple tables" points to a relational database (RDS/Aurora). "Needs to scale massively with simple, fast key-based lookups" points to DynamoDB. Confusing these two is one of the most common Domain 3 mistakes.

## Amazon Redshift: Data Warehousing

**Amazon Redshift** is a fully managed **data warehouse** service, built for analytical queries across very large volumes of historical data — not for the fast, transactional, one-record-at-a-time workloads RDS and DynamoDB handle. Redshift uses columnar storage and is optimized for complex queries that aggregate and analyze massive datasets, like a company's entire sales history across every Region and year.

The distinction worth holding onto: RDS and DynamoDB are built for **OLTP** (online transaction processing — lots of small, fast read/write operations, like a checkout page). Redshift is built for **OLAP** (online analytical processing — fewer, much larger, more complex queries, like "what were total sales by category, by quarter, for the last five years").

> ⚠️ **Exam trap:** a scenario mentioning "business intelligence," "analytics," or "reporting across historical data" is pointing at Redshift — not RDS, even though both are technically SQL-queryable. The workload shape (many small transactions vs. few large analytical queries) is the deciding factor, not just "it uses SQL."

## Amazon Aurora: AWS's Own Relational Engine

**Amazon Aurora** is a relational database engine built by AWS, compatible with MySQL and PostgreSQL, and available as an engine option within RDS. AWS positions Aurora as offering higher performance and availability than the standard open-source engines running on RDS, while remaining a managed relational database with the same core RDS features — automated backups, Multi-AZ, read replicas.

The exam cue for Aurora: a scenario wanting MySQL or PostgreSQL compatibility, but with better performance and availability than a standard RDS deployment of that same engine, is describing Aurora.

## Putting the Four Together

A useful way to hold all four database services: sort by structure first, then by workload shape.

1. **Relational, transactional, standard engines** — Amazon RDS (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server).
2. **Relational, transactional, AWS's own high-performance engine** — Amazon Aurora (MySQL/PostgreSQL-compatible, running on RDS).
3. **Non-relational, transactional, massive scale** — Amazon DynamoDB (key-value/document, NoSQL).
4. **Relational structure, analytical workload** — Amazon Redshift (data warehousing, OLAP, historical/aggregate queries).

Every exam scenario in this module is really asking: is this relational or not, and is this a small-fast-transaction workload or a large-analytical-query workload?

---

## What to skip

You don't need to write actual SQL queries, configure real RDS parameter groups, or memorize Aurora's exact performance multipliers over standard MySQL — that hands-on depth belongs to the Solutions Architect Associate exam. For Cloud Practitioner, focus on sorting a scenario by structure (relational vs. NoSQL) and workload shape (transactional vs. analytical).

## Key takeaways

- Managed vs. unmanaged, from Module 6, applies directly to databases: RDS exists to remove the operational burden (patching, backups, failover, scaling) of running a relational database yourself.
- RDS is managed relational — supports MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, and Aurora — with Multi-AZ for failover and read replicas for scaling reads.
- DynamoDB is managed NoSQL — key-value/document data, no fixed schema, built for massive scale and single-digit-millisecond performance.
- Redshift is a data warehouse — built for OLAP, analytical queries across large historical datasets, not everyday transactional workloads.
- Aurora is AWS's own relational engine, MySQL/PostgreSQL-compatible, running on RDS with higher claimed performance and availability than the standard open-source engines.
- Sort every database scenario by structure (relational vs. NoSQL) first, then by workload shape (transactional vs. analytical).

## Further reading

- [Amazon RDS](https://aws.amazon.com/rds/) — supported engines, Multi-AZ, and read replica overview.
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/) — NoSQL concepts and use cases.
- [Amazon Redshift](https://aws.amazon.com/redshift/) — data warehousing overview.
- [Amazon Aurora](https://aws.amazon.com/rds/aurora/) — MySQL/PostgreSQL-compatible engine details.

*Service capabilities mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 7 — Storage](07-storage.md) · **Next:** [Module 9 — Cloud Architecture](09-cloud-architecture.md) · **Quiz:** [Module 8 Quiz](../quizzes/08-databases-quiz.md) · **Activity:** [Module 8 Activity](../labs/08-databases-activity.md)
