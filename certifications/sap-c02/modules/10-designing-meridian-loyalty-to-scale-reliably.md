# Module 10: Designing Meridian Loyalty to Scale Reliably

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 8 made sure Meridian Loyalty survives a disaster. This module makes sure it survives success — a coordinated marketing push across Café Sol, Haven & Co., and eventually Ridgeline that sends guest traffic far above any normal day, without a single guest noticing anything but a fast app. This is Task 2.4: designing the actual scaling behavior a new solution needs, not just the failover behavior Module 8 already covered.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish scalability from elasticity, and explain why a new solution needs both
- Choose between target tracking and scheduled Auto Scaling policies for a given traffic pattern
- Explain how Amazon SQS decouples a write-heavy event path from a traffic spike
- Choose between DynamoDB on-demand and provisioned capacity (with Auto Scaling) for a given workload's traffic predictability
- Design a complete scaling strategy for a stated new-solution scenario

---

## Scalability vs. Elasticity

These two terms get used almost interchangeably in casual conversation, and the exam expects you to keep them separate.

- **Scalability** is a system's ability to handle growth at all — by adding resources, the system can serve more load than it could before. A system can be scalable without ever shrinking back down.
- **Elasticity** is the ability to scale automatically, in both directions, in response to actual demand — growing when a promotional push hits, and just as importantly, shrinking back down afterward so Meridian isn't paying for peak capacity at 3 a.m. on a random Tuesday.

Meridian Loyalty needs both: an architecture that's fundamentally capable of handling ten times its normal traffic (scalability), built on services that adjust to real demand automatically rather than requiring someone to manually resize things before and after every campaign (elasticity).

> ⚠️ **Exam trap:** a system that can be scaled up by an engineer manually resizing an instance is scalable, but it isn't elastic — elasticity specifically requires the scaling to happen automatically, in response to demand, in both directions. The exam will describe a scenario and expect you to identify which property it's actually asking about.

## Auto Scaling: Target Tracking vs. Scheduled Scaling

Meridian Loyalty's compute tier needs to grow and shrink with demand — but "demand" shows up in two different shapes, and Auto Scaling has a policy type built for each.

- **Target tracking scaling** watches a metric (like average CPU utilization or request count per target) and automatically adds or removes instances to keep that metric near a target value. This handles organic, unpredictable fluctuation — a slightly busier evening, an unplanned bump in guests checking their balances.
- **Scheduled scaling** adjusts capacity at specific, known times, ahead of demand you can already predict. When Café Sol, Haven & Co., and Ridgeline coordinate a joint "double points weekend" promotion, Sofía already knows exactly when traffic will spike — scheduled scaling adds capacity proactively, minutes before the campaign goes live, rather than reactively scrambling to catch up after target tracking notices load already climbing.

Meridian Loyalty's actual design uses **both**: scheduled scaling handles the known, calendar-driven campaign spikes, and target tracking handles everything else in between.

> ⚠️ **Exam trap:** "we know exactly when the spike happens" points to scheduled scaling. "Demand fluctuates unpredictably and we need the system to react on its own" points to target tracking. A scenario describing a planned, calendar-driven event and a student reaching only for target tracking is missing the actual opportunity to scale ahead of demand instead of reacting to it.

## Decoupling with Amazon SQS

A "double points weekend" doesn't just mean more people checking balances — it means a burst of actual point-earning events arriving all at once, all needing to be written to Meridian Loyalty's database. Writing every single one synchronously, the moment it happens, means the database — and the guest-facing request — is exposed directly to the size of the spike.

**Amazon SQS** sits between the event source and the writer: point-earning events land in a queue the instant they happen, and a fleet of consumers — itself scaled by Auto Scaling — drains that queue and writes to the database at a sustainable rate. The guest-facing action (the purchase, the check-in) completes immediately either way; the actual database write happens a moment later, decoupled from the traffic spike entirely.

This is the same pattern from SAA-C03: decoupling doesn't eliminate the spike, it absorbs it — the queue smooths a burst into a rate the downstream system can actually sustain.

## DynamoDB Capacity: On-Demand vs. Provisioned with Auto Scaling

Meridian Loyalty's real-time point-earning event stream lives in DynamoDB (the multi-active piece from Module 8's replication discussion), and that table's capacity mode is its own scaling decision, separate from the compute tier.

- **On-demand capacity mode** automatically accommodates traffic as it arrives, with no capacity planning at all — DynamoDB scales instantly to whatever load shows up, at a higher per-request cost. This fits workloads with unpredictable or spiky traffic, or brand-new workloads without enough traffic history to plan around.
- **Provisioned capacity with Auto Scaling** sets a baseline and scaling policy in advance, at meaningfully lower cost per request once traffic is predictable — but it still reacts to a target utilization metric, so a truly instantaneous, extreme spike can outrun it before Auto Scaling catches up.

At launch, with no traffic history yet and campaign timing still new, **on-demand** is the safer starting point for Meridian Loyalty's event table. Once traffic patterns are well understood — steady day-to-day baseline, known campaign timing — **provisioned capacity with Auto Scaling** becomes the more cost-effective choice, since scheduled scaling can pre-provision for known events the same way it does for the compute tier.

> ⚠️ **Exam trap:** "brand-new workload, no traffic history, spiky and unpredictable" points to on-demand. "Well-understood, steady traffic with occasional known spikes" points to provisioned with Auto Scaling, for meaningfully lower cost. Defaulting to on-demand forever, past the point where traffic is actually predictable, leaves cost savings on the table.

## Reducing Load with Amazon ElastiCache

Most of Meridian Loyalty's read traffic is the same handful of guests checking the same balance repeatedly during a campaign weekend — exactly the access pattern a cache is built for. **Amazon ElastiCache** sits in front of Aurora, serving hot guest-balance reads from memory instead of hitting the database for every single check, which keeps Aurora's load proportional to actual writes and cache misses rather than every guest's every glance at the app.

## Putting It Together: Meridian Loyalty's Scaling Strategy

Sofía's complete scaling design for Meridian Loyalty:

- **Elasticity, not just scalability**, as the actual design goal — capacity that grows and shrinks automatically with real demand.
- **Scheduled scaling for known campaign spikes, target tracking for everything else** — proactive ahead of planned events, reactive for organic fluctuation.
- **Amazon SQS decoupling the point-earning write path**, absorbing a burst into a sustainable rate rather than exposing the database directly to it.
- **DynamoDB on-demand at launch**, moving to provisioned with Auto Scaling once traffic patterns are well understood.
- **ElastiCache in front of Aurora**, serving the repeated guest-balance reads a campaign weekend generates without proportionally loading the database.

## What to skip

You don't need to memorize Auto Scaling's exact cooldown timers or ElastiCache's full eviction policy catalog — that's implementation depth beyond this exam. What matters is telling scalability apart from elasticity, matching target tracking versus scheduled scaling to the actual traffic pattern described, understanding what SQS decoupling actually buys you, and choosing DynamoDB's capacity mode based on how predictable the workload's traffic really is.

## Key takeaways

- Scalability is the ability to handle growth; elasticity is scaling automatically, in both directions, in response to real demand — a new solution generally needs both.
- Scheduled scaling fits known, calendar-driven demand; target tracking fits organic, unpredictable fluctuation — Meridian Loyalty's design uses both together.
- SQS decouples a write-heavy event path from a traffic spike, absorbing a burst into a rate the downstream system can sustain, without eliminating the underlying spike.
- DynamoDB on-demand fits new or unpredictable workloads; provisioned capacity with Auto Scaling fits well-understood, predictable traffic, at meaningfully lower cost once that predictability exists.
- ElastiCache reduces database load by serving repeated hot reads from memory — proportionally valuable exactly when the same data (like a guest's balance) gets checked over and over during a spike.

## Further reading

- [AWS Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html) — target tracking and scheduled scaling policies.
- [Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) — decoupling architectures.
- [Amazon DynamoDB Read/Write Capacity Modes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html) — on-demand vs. provisioned.
- [Amazon ElastiCache User Guide](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) — caching strategies for read-heavy workloads.
