# Module 6: Adding a Database Layer

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 55 minutes

## Why this matters

The café's compute layer from Module 5 can now run the online-ordering application — but an application without a database has nowhere to actually keep an order once it's placed. Orders, inventory, customer records: all of it needs somewhere durable to live, queryable fast enough to keep up with real traffic. This module is where that layer gets built.

It's also where a decision from Module 4 comes back with more weight behind it: just like choosing a storage class, choosing a database service is about matching the *shape* of the data and the *shape* of the access pattern to the right tool — not defaulting to whichever database happens to be the most familiar name.

## Learning objectives

By the end of this module, you should be able to:

- Compare database types and services offered by AWS
- Explain when to use Amazon Relational Database Service (Amazon RDS)
- Describe the advanced features of Amazon RDS
- Explain when to use Amazon DynamoDB
- Identify AWS purpose-built database services
- Describe how to migrate data into AWS databases
- Apply AWS Well-Architected Framework principles when designing a database layer

---

## Comparing Database Types

Before any specific service, the first decision is structural: what *shape* does this data actually have, and how will it actually get queried?

| Database type | Data shape | Query pattern |
|---|---|---|
| Relational | Structured tables, defined schemas, enforced relationships | Complex queries and joins across related tables, using SQL |
| Non-relational (NoSQL) | Flexible, often schema-less — key-value, document, or other shapes | Fast, simple lookups at massive scale, often by a known key |
| Purpose-built | Shaped for one specific problem (graph relationships, time series, in-memory caching, etc.) | Whatever access pattern that specific problem actually needs |

This structural question comes before any specific service name. A workload needing enforced relationships and complex joins across orders, customers, and inventory points toward relational. A workload needing to look up a single item by key at very high speed and scale, with a structure that varies item to item, points toward non-relational. A workload solving a genuinely specialized problem — like traversing relationships in a social graph — points toward a purpose-built service built for exactly that shape.

## Amazon RDS: Managed Relational Databases

**Amazon RDS** is a managed relational database service, supporting several familiar engines (like MySQL, PostgreSQL, and MariaDB) without requiring you to install, patch, or manage the underlying database software yourself. RDS is the right starting point whenever a workload's data genuinely fits the relational shape: structured, related, and queried with SQL.

RDS's advanced features are where it earns its place as more than "a database on a server AWS manages for you":

- **Multi-AZ deployments** maintain a synchronous standby replica in a second Availability Zone, with automatic failover if the primary fails — the same high-availability pattern from earlier in this course, applied specifically to the database layer.
- **Read replicas** offload read traffic to additional copies of the database, scaling read-heavy workloads without touching the primary instance's write capacity. RDS supports a meaningful number of read replicas, though the exact limit varies by engine.
- **Automated backups and snapshots** protect against data loss without requiring a manually scheduled backup process.

> ⚠️ **Trap to know:** Multi-AZ (failover protection) and read replicas (read scaling) solve two different problems and are frequently needed together, not as alternatives to each other. A scenario describing both a failover risk *and* a read-traffic bottleneck needs both fixes applied — one alone only solves half the situation.

## Amazon Aurora: RDS's Premium Engine

**Amazon Aurora** is a MySQL- and PostgreSQL-compatible engine option available inside RDS — not a separate product line, but a premium choice you select within the same managed relational service. Aurora is built for higher performance and availability than the standard open-source engines running on RDS, with storage that automatically scales with the data in a cluster's volume, rather than requiring manually provisioned capacity.

Aurora also supports a notably higher number of read replicas than RDS's standard engines — a detail that matters directly for any scenario describing high, unpredictable read traffic on top of an already-large and still-growing relational dataset. When a scenario needs a highly available relational database that also needs to scale reads aggressively and grow its storage automatically, Aurora is very often the specific answer being tested for, distinct from choosing RDS with a standard engine.

## Amazon DynamoDB: Managed NoSQL at Scale

**Amazon DynamoDB** is AWS's fully managed, non-relational database, built for fast, consistent performance at any scale, with no fixed schema required — items in the same table can have different sets of attributes side by side. DynamoDB is the right fit when a workload needs to look up items quickly by a known key, at a scale where a relational database's structure and joins would become a bottleneck rather than a benefit.

The trade-off is real, not just a matter of taste: DynamoDB doesn't give you the same complex, ad hoc querying and enforced relationships a relational database provides. A scenario needing complex joins and strict referential integrity belongs on RDS or Aurora regardless of how scalable a NoSQL alternative claims to be — scalability alone doesn't override a genuine structural need.

## AWS Purpose-Built Database Services

Beyond general-purpose relational and NoSQL options, AWS offers databases purpose-built for specific data shapes and problems:

| Service | Purpose-built for |
|---|---|
| Amazon Redshift | Data warehousing and large-scale analytical (OLAP) queries across historical data |
| Amazon Neptune | Graph data — relationships between entities, like social networks or recommendation engines |
| Amazon ElastiCache | In-memory caching, for extremely low-latency reads in front of a primary database |
| Amazon DocumentDB | Document-oriented workloads, compatible with MongoDB |

> ⚠️ **Trap to know:** A scenario that sounds like it needs "a relational database" but explicitly rules out read replica support, or explicitly describes analytical queries across years of historical data rather than everyday transactions, is often pointing at Redshift, not RDS or Aurora — Redshift is built for OLAP, not OLTP, and it's easy to miss that distinction under time pressure.

## Migrating Data Into AWS Databases

Getting existing data into an AWS database is its own design decision, not an afterthought. AWS provides dedicated migration tooling — most notably the **AWS Database Migration Service (DMS)** — specifically to move data from an on-premises database (or a different cloud database) into an AWS-hosted one, in many cases with minimal downtime by continuously replicating changes during the migration window rather than requiring a single, disruptive cutover. Recognizing that migration is a distinct, planned step — with its own tooling — rather than something to figure out ad hoc after the destination database is already chosen, is itself part of designing the database layer deliberately.

## Applying the Well-Architected Framework to the Database Layer

A handful of best practices, specific to the database layer, recur constantly:

- **Performance Efficiency** — make selection choices based on the data's actual characteristics and access patterns, not habit. This is the structural question from the top of this module, applied as an ongoing discipline rather than a one-time decision.
- **Security** — implement secure key management and protect data at rest. A database is often where an architecture's most sensitive data actually lives, which makes it a natural focal point for encryption and access control.
- **Cost Optimization** — select resource type, size, and number based on real data, not a guess made on day one — the same "stop guessing" principle from Module 2, applied to database capacity specifically.

Notice the pattern from Module 5 repeating here: the Well-Architected Framework isn't a separate checklist to apply after the database layer is designed — the database-specific best practices above *are* the Framework, applied to this exact layer.

---

## What to skip

You don't need to memorize the exact maximum number of read replicas each engine supports, or specific current pricing for RDS instance sizes — these numbers change, and the exam tests the *decision logic* (relational vs. non-relational, OLTP vs. OLAP, RDS vs. Aurora vs. a purpose-built service) rather than current specifications. The guided lab and hands-on practice will build real familiarity with actually deploying a database.

## Key takeaways

- Start with data shape and access pattern, not a specific service name — relational, non-relational, and purpose-built each solve a different structural problem.
- Amazon RDS is managed relational database infrastructure; Multi-AZ solves failover risk, read replicas solve read-traffic scaling, and they're frequently needed together, not as alternatives.
- Amazon Aurora is a premium RDS engine option, not a separate product — built for higher performance, higher availability, more read replicas, and storage that scales automatically.
- Amazon DynamoDB is managed NoSQL for fast, flexible, massive-scale key-based lookups — but it trades away the complex joins and enforced relationships a relational database provides.
- Purpose-built services (Redshift for analytics, Neptune for graphs, ElastiCache for caching, DocumentDB for documents) exist because some problems have a shape that general-purpose relational or NoSQL databases don't fit well.
- Migration is its own deliberate design decision, with dedicated tooling like AWS Database Migration Service, not an afterthought once a destination database is chosen.

## Further reading

- [Amazon RDS documentation](https://docs.aws.amazon.com/rds/) — the official source for current engines, features, and Multi-AZ/read replica behavior.
- [Amazon DynamoDB documentation](https://docs.aws.amazon.com/amazondynamodb/) — the official source for DynamoDB's data model and scaling behavior.
- [AWS Database Migration Service](https://docs.aws.amazon.com/dms/) — the authoritative source for how AWS approaches minimal-downtime database migration.

*Service capabilities, read replica limits, and specifications mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 5 — Adding a Compute Layer Using Amazon EC2](05-adding-a-compute-layer-using-amazon-ec2.md) · **Next:** [Module 7 — Creating a Networking Environment](07-creating-a-networking-environment.md) · **Quiz:** [Module 6 Quiz](../quizzes/06-adding-a-database-layer-quiz.md) · **Activity:** [Module 6 Activity](../labs/06-adding-a-database-layer-activity.md)
