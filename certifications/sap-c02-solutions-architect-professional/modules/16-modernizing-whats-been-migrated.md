# Module 16: Modernizing What's Been Migrated

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 15 moved Ridgeline Diner Co.'s systems to AWS — retiring the unused tool, rehosting the point-of-sale system via AWS Application Migration Service, replatforming the inventory database onto Amazon RDS, and flagging the reporting server for a future redesign. None of that modernized anything; it moved Ridgeline's systems largely unchanged. This module is Domain 4, Tasks 4.3 and 4.4 — the last module of the SAP-C02 track: deciding what to modernize now that Ridgeline is stable in AWS, and how.

## Learning objectives

By the end of this module, you should be able to:

- Explain why migrating and modernizing in the same step multiplies risk, and why a stable migration should come first
- Describe containerizing a rehosted workload with Amazon ECS on AWS Fargate
- Explain how a scheduled batch process can be refactored into an event-driven, serverless design
- Match a workload's actual access pattern to the right database modernization option — caching, a purpose-built database, or staying relational
- Design a complete modernization roadmap for a set of previously migrated systems

---

## Migrate Then Modernize

The point-of-sale system has been running steadily on EC2 since Module 15's rehost — the same architecture it had on-premises, just moved. That was deliberate: modernizing a system in the same step as migrating it means an outage or a bug could come from either the move or the redesign, and there's no clean way to tell which. Combining them multiplies risk without buying anything in return.

The pattern the exam expects is often described as **crawl, walk, run**: migrate first, largely unchanged, to prove the system runs correctly in AWS (crawl). Let it stabilize and gather real operating data, the way Café Sol's six months of history informed Module 14's recommendations (walk). Only then modernize deliberately, using that real data to decide what's actually worth changing (run). Trying to migrate and modernize in a single "big bang" cutover skips the stabilization step entirely, and it's a pattern the exam consistently treats as the wrong answer.

> ⚠️ **Exam trap:** a scenario that combines "migrate to AWS" and "redesign for the cloud" into one cutover is describing unnecessary combined risk, not efficiency. The safer, exam-preferred answer nearly always separates the two: migrate first, modernize once the system has proven stable.

## Containerizing a Rehosted Workload

With the point-of-sale system stable on EC2, it's a candidate for its first real modernization step: containerizing it. The application code doesn't need a rewrite — it gets packaged into a container image and run on **Amazon ECS with AWS Fargate**, which removes the underlying EC2 instances from the team's responsibility entirely. Fargate handles the compute; the team stops patching and scaling servers for this workload.

This isn't the same as adopting microservices — the POS system stays a single application, just repackaged and no longer tied to specific EC2 instances. But it is a meaningfully shorter step toward microservices later than a monolith running directly on EC2 would be, if Ridgeline ever decides that redesign is worth it.

## Modernizing the Reporting Server

Module 15 flagged the reporting server — aging custom software running a nightly batch job — as the system worth a real redesign. Its current design runs a scheduled job on a physical server every night, generating reports regardless of whether new data actually arrived that day.

Deciding *how* to modernize a workload depends on matching the change to what's actually a bottleneck, not applying the same fix everywhere:

- **A workload that's already relational, with query patterns that haven't changed, usually stays relational.** Forcing a rewrite onto a different database model when the access pattern hasn't changed adds complexity without a real benefit.
- **A read-heavy workload with repeated queries often just needs a cache in front of the existing database** — Amazon ElastiCache — rather than a new database engine entirely.
- **A workload with a genuinely different access pattern** — high-volume key-value lookups at a scale a relational engine struggles with, for example — is a legitimate case for a **purpose-built database** like Amazon DynamoDB.
- The reporting server's actual problem isn't its database — it's that the job runs on a fixed schedule instead of in response to new data. Refactoring it to be **event-driven** — new data landing in Amazon S3 triggering an AWS Lambda function that generates the report — removes the dependency on a server being up at 2 a.m. and the wasted runs when nothing changed.

> ⚠️ **Exam trap:** "the database is slow" and "every legacy database should become DynamoDB" are not the same conclusion. The exam expects you to match the fix to the actual access pattern — add a cache for repeated reads, move to a purpose-built database only for a genuine pattern mismatch, and recognize when the real problem isn't the database at all, the way it isn't for Ridgeline's reporting server.

## Putting It Together: Ridgeline's Modernization Roadmap

Sofía's modernization plan, now that Ridgeline is stable in AWS:

- **Migrate first, modernize second** — the point-of-sale system was rehosted unchanged in Module 15, and only now, stable on EC2, does it get modernized.
- **Containerize the point-of-sale system** onto **Amazon ECS on AWS Fargate** — no rewrite, no more EC2 instances to manage for this workload.
- **Refactor the reporting server's nightly batch job into an event-driven design** — new data in Amazon S3 triggers an AWS Lambda function, replacing the fixed schedule.
- **Leave the inventory database on Amazon RDS** — its access pattern hasn't changed since the Module 15 replatform, so there's no real benefit to forcing it onto a different database model.

## What to skip

You don't need to memorize Fargate's underlying compute allocation model or the full list of DynamoDB access patterns that justify a purpose-built database — that's implementation depth beyond this exam. What matters is the sequencing (migrate, stabilize, then modernize), what containerizing with ECS on Fargate actually changes, and matching a modernization option to a genuine access-pattern problem rather than applying one everywhere.

## Key takeaways

- Migrating and modernizing in the same step multiplies risk; the exam-preferred pattern is crawl (migrate), walk (stabilize), run (modernize deliberately).
- Containerizing a rehosted workload with Amazon ECS on AWS Fargate removes server management without requiring a rewrite or a move to microservices.
- Refactoring a scheduled batch process into an event-driven design (S3 event triggering Lambda) removes the dependency on a fixed schedule and a server being available.
- A database modernization decision should match the actual access pattern: stay relational if the pattern hasn't changed, add a cache for repeated reads, and reach for a purpose-built database only for a genuine pattern mismatch.
- This closes Domain 4, and the SAP-C02 track: Domain 1 covered organizational complexity, Domain 2 designed Meridian Loyalty new, Domain 3 improved Café Sol as an existing AWS workload, and Domain 4 migrated and modernized Ridgeline Diner Co., a system that had never touched the cloud at all.

## Further reading

- [Amazon ECS on AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/AWS_Fargate.html) — running containers without managing servers.
- [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) — caching in front of an existing database.
- [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) — a purpose-built database for key-value and document access patterns.
- [Amazon EventBridge and event-driven architecture](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) — triggering workloads from events instead of fixed schedules.
