# Module 7: Storage

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 3 — Cloud Technology and Services
**Estimated study time:** 45 minutes

## Why this matters

Every piece of compute covered last module eventually has to read or write data somewhere, and "somewhere" is not one-size-fits-all on AWS. Storage splits into three fundamentally different types — object, block, and file — and most of Domain 3's storage questions are really testing whether you know which type a given scenario needs, not whether you've memorized a service's feature list.

This module builds that vocabulary, then layers on Amazon S3's storage classes (since S3 alone shows up constantly, in enough different flavors to be its own mini-topic), and finishes with the services that move data into and protect data already in AWS: Storage Gateway, the Snow family, and backup/lifecycle tools.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish object, block, and file storage, and name the AWS service for each
- Describe Amazon S3 and its core storage classes, and match a scenario to the right class
- Describe Amazon EBS and explain when it's the right choice over S3
- Describe Amazon EFS and how it differs from EBS
- Describe AWS Storage Gateway and the AWS Snow Family at a high level
- Explain the role of S3 lifecycle policies and AWS Backup
- Avoid the most common storage traps on the exam

---

## Three Types of Storage

Before any specific service, the exam expects you to sort a scenario into one of three storage types:

| Type | What it is | AWS service |
|---|---|---|
| **Object storage** | Stores whole files ("objects") with metadata, accessed over the web — no traditional file system, no direct OS attachment | Amazon S3 |
| **Block storage** | Raw, low-level storage volumes attached to a single compute instance, like a virtual hard drive | Amazon EBS |
| **File storage** | A shared file system, accessible by multiple instances at once over a network, organized in folders | Amazon EFS |

> ⚠️ **Exam trap:** "needs to be accessed by many EC2 instances at the same time, organized like a shared drive" is file storage (EFS) — not block storage (EBS), which attaches to exactly one instance at a time. "Store and retrieve any amount of unstructured data over the web" is object storage (S3), not a file system at all.

## Amazon S3: Object Storage

**Amazon S3 (Simple Storage Service)** stores data as objects inside **buckets**, with virtually unlimited capacity and 99.999999999% (11 nines) durability. There's no server to manage — you interact with S3 entirely through its API or the console, and it's the default answer whenever a scenario mentions backups, static website hosting, data lakes, or serving media files at scale.

## S3 Storage Classes

Not all data in S3 needs to be retrieved at the same speed or the same frequency, so S3 offers multiple **storage classes**, each trading retrieval speed and cost differently:

| Storage class | Best for | Retrieval |
|---|---|---|
| S3 Standard | Frequently accessed data | Milliseconds |
| S3 Standard-IA (Infrequent Access) | Data accessed less often, but needed quickly when it is | Milliseconds, lower storage cost, retrieval fee applies |
| S3 One Zone-IA | Infrequent access, data that can be recreated if lost | Milliseconds, single AZ (lower cost, less redundancy) |
| S3 Glacier Instant Retrieval | Archive data needing millisecond access | Milliseconds |
| S3 Glacier Flexible Retrieval | Archive data, retrieval isn't urgent | Minutes to hours |
| S3 Glacier Deep Archive | Long-term archive, rarely if ever accessed | Hours (cheapest storage class) |

> ⚠️ **Exam trap:** the classes form a clean spectrum from "frequent, fast, expensive" to "rare, slow, cheap." A scenario describing compliance archives kept "just in case," accessed maybe once a year, is Glacier Deep Archive — not Standard-IA, which is for data still accessed somewhat regularly.

## S3 Lifecycle Policies

An **S3 lifecycle policy** automatically transitions objects between storage classes — or deletes them — based on rules you define, without any manual intervention. A common pattern: keep logs in S3 Standard for 30 days, move them to Standard-IA for 90 days, then to Glacier Deep Archive after a year, and delete them after seven years for compliance.

This automates exactly the kind of cost-optimization decision the storage-class table above describes — matching data to the right class as its access pattern changes over time, without anyone remembering to move it manually.

## Amazon EBS: Block Storage

**Amazon EBS (Elastic Block Store)** provides persistent block-level storage volumes that attach to a single EC2 instance, behaving like a virtual hard drive. EBS volumes persist independently of the instance's lifecycle — you can stop an instance and its EBS volume (and data) stays intact, ready to reattach.

EBS is the answer whenever a scenario describes a database's data files, an application's boot volume, or any workload needing low-latency, consistent, block-level access from a single instance.

> ⚠️ **Exam trap:** EBS attaches to one instance at a time (in the standard case) — it is not a shared storage answer. If a scenario needs simultaneous access from multiple instances, that's EFS, not EBS.

## Amazon EFS: File Storage

**Amazon EFS (Elastic File System)** provides a scalable, shared file system that multiple EC2 instances can mount and access at the same time, growing and shrinking automatically as files are added or removed — no capacity to provision in advance.

The exam cue is "shared" and "simultaneous": a fleet of web servers that all need to read and write the same set of files is an EFS scenario.

## Moving Data In: AWS Storage Gateway

**AWS Storage Gateway** is a hybrid storage service that connects an on-premises environment to AWS storage, letting on-premises applications use S3, EBS, or other AWS storage as if it were local. It's the answer whenever a scenario describes an organization wanting cloud storage benefits (durability, scale) while keeping some on-premises presence, often for a gradual cloud migration.

## Moving Data In (at Massive Scale): The AWS Snow Family

For extremely large datasets where transferring data over the internet would take too long, the **AWS Snow Family** provides physical devices — ranging from a rugged, portable Snowcone up to a shipping-container-scale Snowmobile — that AWS ships to a customer, gets filled with data on-premises, and ships back to be uploaded directly into AWS.

> ⚠️ **Exam trap:** the Snow Family's cue is always a combination of *very large data volume* and *limited or unreliable network bandwidth* — "we have 50 petabytes and a slow internet connection" is a Snow Family scenario. If bandwidth is fine, a standard online transfer is simpler and faster.

## Protecting Data: AWS Backup

**AWS Backup** is a centralized service for automating and managing backups across many AWS services — EBS, RDS, DynamoDB, EFS, and more — from one place, instead of configuring backup policies separately for each service. It's the answer whenever a scenario emphasizes a single, consistent backup policy applied across multiple AWS resource types.

---

## What to skip

You don't need to calculate exact S3 storage-class pricing, configure real lifecycle policy JSON, or know every Snow Family device's exact capacity — that level of detail belongs to the Solutions Architect Associate exam. For Cloud Practitioner, focus on sorting a scenario into object/block/file storage, and matching an access pattern to the right S3 storage class.

## Key takeaways

- Object storage (S3), block storage (EBS), and file storage (EFS) solve three different problems — sort the scenario by access pattern before picking a service.
- S3 storage classes form a spectrum from frequent/fast/expensive (Standard) to rare/slow/cheap (Glacier Deep Archive); lifecycle policies automate moving data along that spectrum over time.
- EBS attaches to a single instance; EFS is shared across multiple instances simultaneously — that distinction is the most common EBS-vs-EFS exam trap.
- Storage Gateway connects on-premises applications to AWS storage; the Snow Family physically ships massive datasets into AWS when bandwidth alone won't cut it.
- AWS Backup centralizes and automates backup policy across many AWS services from a single place.

## Further reading

- [Amazon S3](https://aws.amazon.com/s3/) — storage classes, durability, and use cases.
- [Amazon EBS](https://aws.amazon.com/ebs/) and [Amazon EFS](https://aws.amazon.com/efs/) — for comparing block and file storage directly.
- [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) and [AWS Snow Family](https://aws.amazon.com/snow/) — hybrid and offline data transfer options.
- [AWS Backup](https://aws.amazon.com/backup/) — centralized backup management across AWS services.

*Service capabilities mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 6 — Compute](06-compute.md) · **Next:** [Module 8 — Databases](08-databases.md) · **Quiz:** [Module 7 Quiz](../quizzes/07-storage-quiz.md) · **Activity:** [Module 7 Activity](../labs/07-storage-activity.md)
