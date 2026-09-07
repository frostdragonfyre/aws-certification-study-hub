# Module 6: Implementing Backup and Restore Strategies

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Modules 4 and 5 kept Meridian's infrastructure running through demand spikes and component failures. But some failures — a bad deployment, a corrupted table, a mistaken deletion — aren't things Multi-AZ or Auto Scaling can undo, because the failure gets replicated everywhere just as fast as the good data was. This module is Domain 2's third and final task: making sure Priya can actually get data back, on a timeline the business can live with, closing out Domain 2.

## Learning objectives

By the end of this module, you should be able to:

- Define RTO and RPO, and explain what each one actually measures
- Describe how AWS Backup centralizes and automates backup policy across services
- Distinguish an RDS automated backup from a manual snapshot, and know what happens to each on deletion
- Explain why cross-Region backup copies matter for disaster recovery
- Design a backup and restore strategy that meets a stated RTO/RPO requirement

---

## RTO and RPO: Measuring Two Different Things

Before choosing any backup mechanism, Priya has to answer a business question, not a technical one: how much data can Meridian afford to lose, and how long can a system afford to be down? These have names.

**Recovery Point Objective (RPO)** measures how much data loss is acceptable, expressed as time — an RPO of 1 hour means the business accepts losing up to an hour's worth of data if a failure happens right before the next backup. **Recovery Time Objective (RTO)** measures how much downtime is acceptable — an RTO of 4 hours means the system must be back up and serving traffic within 4 hours of a failure, regardless of how much data was lost.

These aren't the same axis, and a stated requirement usually implies a specific backup frequency and restore mechanism: a tight RPO (say, 5 minutes) demands frequent, automated backups or continuous replication; a tight RTO demands a fast restore path — a pre-provisioned standby, not a from-scratch restore from a cold snapshot that takes hours to rehydrate.

> ⚠️ **Exam trap:** a scenario stating "the business can tolerate losing at most 15 minutes of data" is describing an **RPO** requirement — it's about data loss, not downtime. A scenario stating "the system must be back online within 30 minutes" is describing an **RTO** requirement — it's about downtime, not data loss. Confusing which requirement is which leads to designing the wrong mechanism: tuning backup frequency to fix an RTO problem, or provisioning standby capacity to fix an RPO problem, solves the wrong half of the requirement.

## AWS Backup: One Policy, Many Services

Individually configuring backups for EBS volumes, RDS databases, DynamoDB tables, and EFS file systems — each with its own console, its own schedule, its own retention rules — is exactly the kind of fragmented, easy-to-miss-one-resource setup that leads to gaps. **AWS Backup** centralizes this: a single service where Priya defines a **backup plan** — schedule, retention, lifecycle rules to transition backups to cold storage — and assigns resources to it by tag or by resource ID, across nearly all of Meridian's backup-eligible services at once.

AWS Backup also supports **cross-Region** and **cross-account** backup copies as part of the same plan, meaning disaster-recovery-grade backup coverage doesn't require a separate, manually maintained process layered on top.

> ⚠️ **Exam trap:** a scenario describing inconsistent backup coverage — some resources backed up reliably, others missed entirely, because each team configures its own service's backups independently — is pointing at AWS Backup's centralized policy model as the fix, not asking for tighter per-service configuration. The problem is fragmentation itself, and centralizing under one plan is the architectural answer.

## RDS Automated Backups vs. Manual Snapshots

Amazon RDS offers two backup mechanisms that are easy to blur together, but behave very differently at the moment that matters most: deletion.

**Automated backups** happen daily during a defined backup window, plus continuous transaction log capture that enables **point-in-time recovery** to any second within the retention period (up to 35 days). The catch: automated backups are tied to the database instance's lifecycle — by default, they're **deleted when the instance itself is deleted**, unless final snapshot creation is explicitly requested at deletion time.

**Manual snapshots** are user-initiated, retained indefinitely regardless of what happens to the source instance, and persist even after the instance is deleted, with no retention limit tied to a policy.

> ⚠️ **Exam trap:** a scenario asking for point-in-time recovery to a specific second is describing automated backups' transaction log capability, not a manual snapshot (which is a single point-in-time copy, not continuous). But a scenario emphasizing that a backup must survive the deletion of the database instance itself is pointing at a manual snapshot, or an automated backup deletion request with "retain automated backups" explicitly configured — the default automated backup behavior alone will not survive instance deletion.

## Putting It Together: Meridian's Backup and Restore Strategy

Priya's strategy, closing out Domain 2:

- **AWS Backup** centralizing backup plans for Meridian Loyalty's EBS volumes, DynamoDB tables, and Café Sol's EFS file systems — one schedule and retention policy, assigned by tag, instead of per-service configuration nobody's tracking end to end.
- **RDS automated backups** with point-in-time recovery enabled for Ridgeline's operational database, tuned to the stated RPO, plus **manual snapshots** taken before any risky schema change, since those need to survive independently of the instance's own lifecycle.
- **Cross-Region backup copies** through AWS Backup, so a Region-wide event doesn't take out both the primary data and every backup of it at once.
- Every plan mapped explicitly back to a stated RTO and RPO, not chosen by default settings — the specific numbers decide the specific mechanism.

## What to skip

You don't need to memorize AWS Backup's exact per-service supported feature matrix or RDS's precise backup window mechanics — that's implementation depth beyond this exam. What matters is defining RTO vs. RPO correctly, knowing AWS Backup's role as a centralizing mechanism, understanding what happens to RDS backups at instance deletion, and matching a backup strategy to a stated recovery requirement.

## Key takeaways

- RPO measures acceptable data loss; RTO measures acceptable downtime — they drive different design decisions and are easy to swap by accident.
- AWS Backup centralizes backup plans — schedule, retention, cross-Region/cross-account copies — across services, fixing the fragmentation of configuring each service's backups independently.
- RDS automated backups are deleted with the instance by default (unless a final snapshot is requested); manual snapshots persist independently and indefinitely.
- Cross-Region backup copies protect against losing both primary data and its backups in the same Region-wide event.
- This closes Domain 2: Module 4 matched capacity to demand, Module 5 survived component failure, and Module 6 made sure data itself can actually be recovered on a timeline the business can live with.

## Further reading

- [Recovery Time Objective and Recovery Point Objective](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html) — defining RTO and RPO for a disaster recovery strategy.
- [What Is AWS Backup?](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) — centralized backup plans across AWS services.
- [Backing Up and Restoring an Amazon RDS DB Instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithAutomatedBackups.html) — automated backups, point-in-time recovery, and manual snapshots.
- [Creating a Backup Plan Using AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/creating-a-backup-plan.html) — schedules, lifecycle rules, and cross-Region copy.
