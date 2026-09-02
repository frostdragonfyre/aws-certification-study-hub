# Module 15: Migrating Ridgeline Diner Co. to AWS

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Domain 3 improved systems that were already in AWS. Ridgeline Diner Co. — the 40-year-old regional chain Meridian acquired last quarter — has never touched the cloud at all: a point-of-sale system, an inventory database, and a reporting server, all running on physical servers in the back office of Ridgeline's original location. This module is Domain 4, Tasks 4.1 and 4.2: deciding how each of Ridgeline's systems actually moves to AWS, and how its database gets there specifically — the first real migration in this course, not a design built cloud-native from the start.

## Learning objectives

By the end of this module, you should be able to:

- Apply the migration strategies (the "R" strategies) to a portfolio of existing on-premises systems
- Explain what AWS Application Migration Service (MGN) does for a rehost migration
- Distinguish a homogeneous database migration from a heterogeneous one
- Explain when AWS Database Migration Service alone is sufficient, and when the AWS Schema Conversion Tool is also required
- Design a complete migration strategy for a stated existing-workload scenario

---

## Matching Each System to a Migration Strategy

Not every one of Ridgeline's systems deserves the same treatment, and the exam expects a specific vocabulary for the options: **retire** (turn it off — nobody actually uses it), **retain** (leave it exactly where it is, for now), **rehost** ("lift and shift" — move it to AWS with minimal change, usually to EC2), **relocate** (move a whole VMware-based environment to AWS with no changes, a narrower case than rehost), **repurchase** (replace it with a SaaS or different licensed product), **replatform** (move it with some optimization, like switching a self-managed database to RDS, without a full redesign), and **refactor/re-architect** (redesign the application to be cloud-native, usually for the workload with the most to gain from it).

Ridgeline's actual portfolio maps out differently system by system: an old internal scheduling tool nobody has opened in over a year is a clear **retire**. The point-of-sale system is critical, well-understood, and there's no time pressure to redesign it before Ridgeline needs to be operating normally on AWS — that's a **rehost**, moved as-is to get off physical hardware fast. The inventory database benefits meaningfully from a managed service — automated backups, patching, Multi-AZ — without needing a full redesign of the application using it, so that's a **replatform** onto Amazon RDS. The reporting server, built on aging, hard-to-maintain custom software that the team has wanted to modernize for years, is the one system worth a real redesign — a candidate for **refactor**, once the more urgent moves are done.

> ⚠️ **Exam trap:** the exam expects you to match the strategy to the system's actual constraints — urgency, technical debt, and how much benefit a redesign would actually provide — not apply one strategy to everything. Rehosting everything ignores real modernization opportunity; refactoring everything ignores time pressure and risk. A real migration portfolio uses several strategies, chosen deliberately per system.

## Rehosting at Scale with AWS Application Migration Service

The point-of-sale system's rehost, chosen for speed and minimal risk, still needs to actually happen — and doing it by hand, server by server, is slow and error-prone.

**AWS Application Migration Service (MGN)** automates a rehost: it continuously replicates a running on-premises server (its exact disk state, not just its configuration) to a staging area in AWS, and when the team is ready to cut over, it launches a fully provisioned, ready-to-run copy of that server on EC2 — with minimal downtime, because the replication has already been happening continuously in the background rather than starting at cutover time.

For Ridgeline's point-of-sale system, this means the actual cutover window — the period where the system might be briefly unavailable — is short, because MGN has already been keeping an EC2-ready copy current the whole time leading up to it, not building one from scratch the day of the move.

## Migrating Ridgeline's Database

The inventory database's replatform onto RDS still requires the data itself to actually move — and how that happens depends on one specific fact: is the database engine changing, or staying the same?

- **Homogeneous migration** moves data between the same database engine — Ridgeline's on-premises SQL Server to Amazon RDS for SQL Server, for example. **AWS Database Migration Service (DMS)** alone is sufficient here: the schema is already compatible, so DMS just needs to move the data (and can do so with minimal downtime, using ongoing replication).
- **Heterogeneous migration** moves data between different database engines — Ridgeline's on-premises Oracle database to Amazon Aurora, for example. Schemas, data types, and stored procedures don't match up automatically between different engines, so the **AWS Schema Conversion Tool (SCT)** has to convert the source schema and code into a format the target engine understands, **before** DMS handles the actual data movement.

Ridgeline's inventory database happens to already run on SQL Server, and RDS for SQL Server is the target — a **homogeneous** migration, so DMS alone gets the job done, with no schema conversion step required.

> ⚠️ **Exam trap:** "same database engine, source to target" points to DMS alone. "Different database engine, source to target" points to SCT converting the schema first, then DMS moving the data — SCT is not an optional extra step for a heterogeneous migration, it's a required one, because DMS itself doesn't translate schemas or code between different engines.

## Putting It Together: Ridgeline's Migration Plan

Sofía's migration plan for Ridgeline Diner Co.'s systems:

- **Retire** the unused scheduling tool; **rehost** the point-of-sale system via **AWS Application Migration Service** for a fast, low-risk move; **replatform** the inventory database onto **Amazon RDS**; **refactor** the reporting server once the more urgent moves are complete.
- The inventory database's migration is **homogeneous** (SQL Server to SQL Server), so **DMS alone** handles the data movement — no Schema Conversion Tool step required.

## What to skip

You don't need to memorize every one of MGN's replication mechanics or DMS's full list of supported source/target engine pairs — that's implementation depth beyond this exam. What matters is matching a migration strategy to a system's actual constraints, knowing what MGN automates for a rehost, and correctly identifying whether a database migration is homogeneous or heterogeneous — and what that means for whether SCT is required.

## Key takeaways

- Migration strategies should be matched per system to its actual urgency, technical debt, and modernization potential — not applied uniformly across an entire portfolio.
- AWS Application Migration Service automates a rehost by continuously replicating a server's disk state to AWS ahead of cutover, minimizing the actual downtime window.
- A homogeneous database migration (same engine, source to target) needs only AWS DMS; a heterogeneous migration (different engines) requires the AWS Schema Conversion Tool to convert the schema and code before DMS moves the data.
- Not every system in a real migration portfolio gets the same strategy — Ridgeline's four systems use four different approaches, chosen deliberately.
- Domain 4 is the first time this course has migrated an existing, never-cloud system — a genuinely different starting point from both Domain 2 (new) and Domain 3 (existing, already in AWS).

## Further reading

- [AWS Cloud Migration Strategies (the "R"s)](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/) — retire, retain, rehost, relocate, repurchase, replatform, refactor.
- [AWS Application Migration Service User Guide](https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html) — automated rehost migrations.
- [AWS Database Migration Service User Guide](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) — homogeneous and heterogeneous data migration.
- [AWS Schema Conversion Tool User Guide](https://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/CHAP_Welcome.html) — schema and code conversion for heterogeneous migrations.
