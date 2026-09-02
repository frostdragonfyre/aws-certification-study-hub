# Module 16: Planning for Disaster

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

Everything built across this course — the VPC, the load balancer, Auto Scaling, RDS Multi-AZ, the CloudFormation templates, the caching layer, the decoupled order pipeline, the data lake — assumes the café's AWS Region is available. Multi-AZ protects against an Availability Zone failing. It does nothing if the entire Region the café is deployed in goes down. That's rare, but it isn't impossible, and "we never planned for it" is not a plan.

This module is about **disaster recovery (DR)**: deciding, deliberately and in advance, how much downtime and data loss the café can actually tolerate, and choosing a DR strategy that matches — rather than discovering the answer live, during an actual outage.

## Learning objectives

By the end of this module, you should be able to:

- Define RTO and RPO and explain what each one actually measures
- Describe the four standard AWS disaster recovery strategies and how they trade off cost against recovery speed
- Explain how Route 53 supports failover between Regions
- Describe how backups fit into a disaster recovery strategy, and what AWS Backup centralizes
- Match a DR strategy to a stated RTO/RPO requirement

---

## RTO and RPO: The Two Numbers That Define "Disaster"

Before choosing a DR strategy, you have to answer two specific questions, and the exam expects you to keep them straight:

- **Recovery Time Objective (RTO):** how long can the café's systems be down before the business impact is unacceptable? If Frank says "we can tolerate being offline for at most 2 hours," that's the RTO.
- **Recovery Point Objective (RPO):** how much data can the café afford to lose, measured as a window of time? If the answer is "we can afford to lose at most 15 minutes of order data," that's the RPO — it's about how *recent* your last good backup or replica needs to be, not how long recovery takes.

These two numbers, not a vague sense of "we want good disaster recovery," are what actually determine which strategy fits. A near-zero RTO and RPO is achievable — but it costs meaningfully more than a strategy that tolerates hours of downtime, and matching the spend to the actual business requirement is the whole design problem.

> ⚠️ **Exam trap:** RTO and RPO are frequently swapped in distractor answers. RTO is about *downtime* (how long until we're back up). RPO is about *data loss* (how much data, measured in time, are we willing to lose). Read the scenario for which one is actually being described before picking a strategy.

## The Four AWS Disaster Recovery Strategies

AWS describes DR strategies along a spectrum, trading cost for recovery speed. Each one assumes a **secondary Region**, standing by in case the primary Region fails.

| Strategy | What's running in the secondary Region | RTO / RPO | Relative cost |
|---|---|---|---|
| Backup and Restore | Nothing — backups are stored, ready to restore | Hours | Lowest |
| Pilot Light | Core infrastructure exists but is scaled down/off (e.g., a database kept in sync, but no application servers running) | Tens of minutes | Low–moderate |
| Warm Standby | A scaled-down but fully functional copy of the full environment is running | Minutes | Moderate–high |
| Multi-Site Active/Active | The full environment runs in both Regions simultaneously, actively serving traffic | Near-zero | Highest |

### Backup and Restore

The simplest and cheapest strategy: back up data and configuration regularly, and if the primary Region fails, restore everything in the secondary Region from those backups. Nothing runs in the secondary Region day-to-day. This has the longest RTO of the four — you're provisioning infrastructure and restoring data from scratch during an actual disaster — but it's also the cheapest, since you're not paying for standing infrastructure you hope you never need.

### Pilot Light

Named for a furnace's pilot light: a small, core piece stays "lit" in the secondary Region — commonly a database kept continuously in sync via replication — while the rest of the environment (application and web servers) exists as infrastructure ready to scale up, but isn't running. When a disaster is declared, you scale up the rest of the environment around that already-current core, which is meaningfully faster than restoring everything from a backup.

### Warm Standby

A scaled-down, but fully functional, version of the complete environment runs continuously in the secondary Region — able to handle traffic immediately at reduced capacity, and scaled up to full capacity as needed during failover. This costs more than Pilot Light because more infrastructure is actually running all the time, but it cuts recovery time down to minutes rather than tens of minutes.

### Multi-Site Active/Active

Both Regions run the full environment simultaneously, actively serving live production traffic — not one primary and one standby, but two (or more) equal, active sites. If one Region fails, traffic simply shifts to the other, which was already handling real traffic and needs no scale-up or recovery step at all. This is the fastest possible recovery — near-zero RTO and RPO — and also the most expensive, since you're running (and paying for) full production capacity in more than one place, all the time.

> ⚠️ **Exam trap:** a scenario that specifies a very tight RTO (minutes or less) with cost as a secondary concern almost always points to Warm Standby or Multi-Site Active/Active — Backup and Restore or Pilot Light physically cannot meet that recovery speed, regardless of how the rest of the scenario is worded.

## Amazon Route 53: Routing Traffic Away from a Failed Region

A DR strategy with a healthy secondary Region still needs a way to actually redirect customer traffic there when the primary Region fails. **Route 53**, AWS's DNS service, supports **health checks** and **failover routing**: it continuously monitors the primary Region's endpoint, and if that health check fails, Route 53 automatically starts directing traffic to the secondary Region's endpoint instead — no manual DNS change required in the middle of an actual outage.

This is the piece that turns "we have a secondary Region ready" into "customers actually reach it automatically when they need to."

## Backups: The Foundation Under Every DR Strategy

Every one of the four strategies still depends on backups being current, reliable, and actually restorable — Backup and Restore obviously, but Pilot Light and Warm Standby both still rely on replicated or backed-up data being accurate as their starting point during failover.

**AWS Backup** is a centralized, managed backup service: instead of configuring separate backup mechanisms for RDS, EBS, DynamoDB, and other services individually, AWS Backup lets you define backup policies once and apply them across multiple AWS services consistently, including cross-Region backup copies — directly supporting the secondary-Region requirement every DR strategy depends on.

## Matching a DR Strategy to a Stated RTO/RPO

| Stated requirement | Best-fit strategy |
|---|---|
| "We can be down for most of a day; minimize cost" | Backup and Restore |
| "We need to be back up within about 30 minutes" | Pilot Light |
| "We need to be back up within a few minutes, cost is secondary" | Warm Standby |
| "We cannot tolerate any real downtime at all" | Multi-Site Active/Active |

## Putting It Together: The Café's Disaster Recovery Plan

The café's order-processing system, by this point in the course, is genuinely important to the business — but a multi-hour outage, while costly, wouldn't be catastrophic the way it would be for, say, a hospital system. That points toward Pilot Light: RDS replicating continuously to a secondary Region, application infrastructure ready to scale up but not running day-to-day, and Route 53 health checks ready to redirect traffic the moment the primary Region's health check fails. AWS Backup handles the cross-Region backup policy underneath it. This is the same V6 multi-Region requirement from Module 11's CloudFormation template — the template that already knows how to deploy the café's architecture a second time is exactly what stands up the Pilot Light environment when it's needed.

## What to skip

You don't need to memorize exact RTO/RPO numbers for each strategy beyond their relative ordering, hand-configure Route 53 health check thresholds, or write AWS Backup policy JSON — that's implementation depth beyond the associate exam. What matters is the four-strategy spectrum, correctly reading which of RTO or RPO a scenario is describing, and matching the stated requirement to the right strategy.

## Key takeaways

- RTO measures acceptable downtime; RPO measures acceptable data loss, as a window of time — they are frequently swapped in exam distractors, so read carefully.
- The four DR strategies — Backup and Restore, Pilot Light, Warm Standby, and Multi-Site Active/Active — trade cost for recovery speed, in that order, from cheapest/slowest to most expensive/fastest.
- Route 53 health checks and failover routing automatically redirect traffic to a secondary Region when the primary Region's endpoint fails, with no manual DNS change needed mid-outage.
- Every DR strategy depends on reliable, current backups underneath it; AWS Backup centralizes and automates that across multiple AWS services, including cross-Region copies.
- The right strategy is determined by the stated RTO/RPO requirement, not by "more disaster recovery is always better" — matching spend to actual business tolerance is the design problem.

## Further reading

- [AWS Whitepaper: Disaster Recovery of Workloads on AWS](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-workloads-on-aws.html) — the four strategies in full depth.
- [Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) — health checks and failover routing.
- [AWS Backup Developer Guide](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) — centralized backup policies and cross-Region copies.

---

## Course complete

This is the final module in the SAA-C03 track — all 16 modules are now written. From here, hands-on practice continues in AWS Academy's own guided and challenge labs, working through the café case study's full V1–V7 architecture evolution, before sitting the AWS Certified Solutions Architect – Associate exam itself.
