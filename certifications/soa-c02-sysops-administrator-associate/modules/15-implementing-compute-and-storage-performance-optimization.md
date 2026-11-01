<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](14-implementing-cost-optimization-strategies.md) · [Quiz](../quizzes/15-implementing-compute-and-storage-performance-optimization-quiz.md) · [Slides](../lectures/15-implementing-compute-and-storage-performance-optimization.pptx)
<!-- /hub-navigation -->

# Module 15: Implementing Compute and Storage Performance Optimization

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Module 14 found savings and caught spend surprises. This module closes the loop on the other half of optimization: making sure compute and storage are actually performing the way each workload needs, not just costing less. This is Domain 6's second task, closing out both Domain 6 and the entire SOA-C02 course.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish Instance Store from EBS, and know when ephemeral local storage actually fits
- Choose the right EBS volume type for a stated performance requirement
- Match an S3 storage class and lifecycle policy to a stated access pattern
- Recognize when adding a cache is the right fix for a slow, read-heavy workload
- Design a compute and storage performance strategy for a stated requirement

---

## Instance Store vs. EBS

Both provide block-level storage for an EC2 instance, but they differ in the one thing that matters most: what happens to the data.

**Instance Store** is physically attached NVMe SSD storage on the same host as the instance — it delivers extremely high IOPS and very low latency, because there's no network hop involved. But it's **ephemeral**: the data is lost the moment the instance stops, terminates, or the underlying hardware fails. It fits temporary data, caches, buffers, or data that's already replicated elsewhere and can be rebuilt.

**EBS (Elastic Block Store)** is network-attached, persistent block storage that survives an instance stop and can be detached and reattached to a different instance. It's the default choice for anything that needs to survive past the life of the instance — an application's data volume, a database's storage, anything that can't simply be regenerated.

Within EBS, the volume type matters too: **General Purpose SSD (gp3)** is the cost-effective default, with a solid baseline of IOPS and throughput independent of volume size. **Provisioned IOPS SSD (io2)** is built for workloads needing consistently high, predictable IOPS at low latency — typically demanding database workloads where gp3's baseline isn't enough.

> ⚠️ **Exam trap:** a scenario describing data that's **temporary, reproducible, or already replicated elsewhere**, where the absolute highest performance matters more than persistence, is describing a fit for **Instance Store**. A scenario where data **must survive** an instance stop, terminate, or replacement is describing a fit for **EBS** — using Instance Store for data that can't be lost is the trap.

## S3 Storage Classes and Lifecycle Policies

Not all data needs to be equally accessible, equally quickly, at the same price. S3 storage classes trade retrieval speed and availability for cost, and **lifecycle policies** automate moving an object between classes as it ages.

**S3 Standard** fits **frequently accessed** data, at the highest per-GB cost of the commonly used classes, with millisecond access. **S3 Standard-IA (Infrequent Access)** costs less per GB but still offers millisecond retrieval — it fits data accessed **infrequently but still needed immediately** when it is accessed, like older records that are rarely, but occasionally, pulled up on demand. The **S3 Glacier** family costs the least per GB by far, but trades away instant access — retrieval can take anywhere from minutes to hours depending on the specific Glacier tier, fitting **long-term archival** data that's essentially never accessed except for compliance or rare recovery needs.

A lifecycle policy automates the transition — for example, moving objects to Standard-IA after 30 days of no access, then to Glacier after 90 days — so Priya doesn't have to manually track and move aging data herself.

> ⚠️ **Exam trap:** a scenario describing data accessed **frequently** is a fit for **S3 Standard**. Data accessed **infrequently but needing immediate retrieval when it is accessed** points to **Standard-IA**. Data that's essentially **archival**, where a retrieval delay of minutes to hours is acceptable, points to **Glacier** — and a scenario describing data that predictably ages out of frequent access over time is a signal to automate the whole thing with a **lifecycle policy**, not manual intervention.

## When a Cache Is the Right Fix

"The database is slow" doesn't always mean the database itself needs to change. A common pattern: the same handful of queries get run over and over, returning largely the same results each time, and the database spends real capacity re-computing or re-fetching something it just answered moments ago.

**Amazon ElastiCache** (for Redis or Memcached) sits in front of the database and serves those repeated, read-heavy queries from memory instead of hitting the database every time — dramatically reducing both latency and load on the database, often without touching the database's own sizing at all. It's not a replacement for the database; it's a layer that absorbs the specific access pattern the database was struggling with.

> ⚠️ **Exam trap:** a scenario describing a database under load from **repeated, read-heavy queries returning largely the same data** is pointing at **adding a cache (ElastiCache)** in front of the database, not resizing the database instance or migrating to a different database engine — reaching for a bigger or different database when the actual problem is a caching gap is the trap.

## Putting It Together: Optimizing Meridian's Performance

Priya's compute and storage performance strategy, closing out Domain 6 and the course:

- **EBS gp3** as the default for application data volumes, with **Provisioned IOPS (io2)** reserved for Meridian Loyalty's demanding database tier.
- **Instance Store** for Café Sol's transient batch-processing scratch space, where the data is regenerated every run and never needs to survive an instance replacement.
- **S3 lifecycle policies** automatically moving Ridgeline's order records from Standard to Standard-IA after 30 days, and to Glacier after a year, without anyone manually managing the transition.
- **ElastiCache** in front of Meridian Loyalty's rewards-lookup database, absorbing the repeated, read-heavy queries that were driving unnecessary database load.

## What to skip

You don't need to memorize every EBS volume type's exact IOPS-per-GB ratio or every Glacier tier's precise retrieval time window — that's implementation depth beyond this exam. What matters is knowing Instance Store's ephemeral tradeoff against EBS's persistence, matching an access pattern to the right S3 storage class and automating the transition with a lifecycle policy, and recognizing when a caching layer — not a bigger database — is the actual fix.

## Key takeaways

- Instance Store is fast but ephemeral, fitting temporary or reproducible data; EBS is persistent and the default for anything that must survive the instance's lifecycle, with gp3 as the cost-effective baseline and io2 for demanding, consistent IOPS needs.
- S3 Standard fits frequent access, Standard-IA fits infrequent-but-immediate access, and Glacier fits archival data tolerant of a retrieval delay — lifecycle policies automate the transition as data ages.
- Repeated, read-heavy database queries are often a caching gap, not a database sizing problem — ElastiCache absorbs that load without touching the database itself.
- This closes Domain 6, and the entire SOA-C02 course: fifteen modules building from monitoring and remediation through reliability, deployment automation, security, networking, and now cost and performance — a complete picture of operating what Sofía's team designed.

## Further reading

- [Amazon EC2 Instance Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) — ephemeral, host-attached storage.
- [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) — gp3, io2, and the rest of the EBS family.
- [Amazon S3 Storage Classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html) — Standard, Standard-IA, and the Glacier family.
- [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) — caching read-heavy database workloads.
