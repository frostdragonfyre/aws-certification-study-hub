<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](07-designing-a-deployment-strategy.md) · [Next module](09-determining-security-controls-for-new-solutions.md) · [Quiz](../quizzes/08-designing-a-solution-to-ensure-business-continuity-quiz.md) · [Slides](../lectures/08-designing-a-solution-to-ensure-business-continuity.pptx)
<!-- /hub-navigation -->

# Module 8: Designing a Solution to Ensure Business Continuity

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 4 built the organizational tooling that makes resilience consistent and measurable across Meridian — but it explicitly stopped short of picking a DR strategy for any one workload, because that's a per-workload design decision, made new each time. Meridian Loyalty is that decision, made for real: what RTO and RPO does a guest rewards platform actually need, which DR strategy fits those numbers, and what specific AWS data-replication technology actually implements it. This module is Task 2.2 — where Domain 1's tooling from Module 4 gets applied to an actual new solution for the first time.

## Learning objectives

By the end of this module, you should be able to:

- Translate a business requirement into concrete RTO and RPO targets for a new solution
- Select a DR strategy (from SAA-C03's four strategies) that fits a new solution's stated RTO/RPO
- Compare Amazon Aurora Global Database and Amazon DynamoDB Global Tables for cross-Region data replication
- Explain how AWS Resilience Hub and Route 53 Application Recovery Controller, introduced in Module 4, apply to a specific new workload
- Design a complete business continuity solution for a stated new-solution scenario

---

## Setting RTO and RPO for a New Solution

Before any DR strategy can be chosen, Meridian Loyalty needs actual numbers — not "we want good resilience," but a specific RTO and RPO, negotiated with the business based on real impact.

Meridian Loyalty tracks guest reward balances across three brands. If it goes down, guests can't earn or redeem points — inconvenient, and reputationally costly if it happens often or for long, but not an emergency the way a payment-processing outage would be. Losing a small amount of very recent transaction data (a few minutes of point-earning activity, worst case) is undesirable but recoverable — Meridian can manually reconcile a short gap from receipts and support tickets if it ever comes to that.

Based on that actual business impact, Sofía sets Meridian Loyalty's targets at **RTO: 15 minutes, RPO: 1 minute** — tight enough that guests rarely notice an interruption, but not so tight that Meridian pays for a fully active-active deployment a rewards platform doesn't actually need.

> ⚠️ **Exam trap:** the exam expects you to derive RTO/RPO from a described business impact, not just recall a definition. "Guests can't earn or redeem points, but the business isn't literally losing money by the second" is a moderate-urgency signal — not the near-zero RTO of a trading platform, and not the multi-hour tolerance of an internal reporting system either. Read the actual described impact before picking a strategy.

## Choosing a DR Strategy for Meridian Loyalty

With RTO of 15 minutes and RPO of 1 minute in hand, SAA-C03's four DR strategies (Backup and Restore, Pilot Light, Warm Standby, Multi-Site Active/Active) give a direct answer. Backup and Restore's multi-hour RTO doesn't meet a 15-minute requirement. Pilot Light's tens-of-minutes RTO is borderline and risky against a hard 15-minute target. Multi-Site Active/Active would comfortably meet both numbers, but at the cost of running full production capacity in two Regions continuously — more than a 15-minute/1-minute target actually requires.

**Warm Standby** is the fit: a scaled-down, but fully functional, copy of Meridian Loyalty runs continuously in a secondary Region, able to handle traffic immediately at reduced capacity and scale up during failover — recovery in minutes, comfortably inside the 15-minute RTO, at meaningfully less cost than full active-active.

This is exactly the Domain 1/Domain 2 boundary from Module 4: Module 4 covered the org-wide tooling that makes resilience consistent and measurable across every workload; this module is the actual per-workload decision that tooling supports.

## Aurora Global Database vs. DynamoDB Global Tables

Warm Standby's "scaled-down copy running continuously" requires actual cross-Region data replication underneath it — and which service provides that depends on what kind of database Meridian Loyalty's data actually lives in.

- **Amazon Aurora Global Database** replicates a relational Aurora database across Regions with typical replication lag under one second, and supports fast Region-level failover — the secondary Region's read replica can be promoted to a fully read/write primary in about a minute during an actual failover. This fits Meridian Loyalty's relational guest-and-transaction data, where Aurora is already the natural choice for structured, relational reward-balance records.
- **Amazon DynamoDB Global Tables** provides multi-Region, multi-active replication for DynamoDB tables — every Region can accept both reads and writes, with changes propagating automatically to every other Region, rather than one Region being primary and others being read replicas. This fits a NoSQL access pattern, like Meridian Loyalty's real-time point-earning event stream, where multiple Regions actively serving writes (not just reads) may eventually be worth considering as usage grows.

Meridian Loyalty's core reward-balance data lives in Aurora, so **Aurora Global Database** is the piece that actually implements the Warm Standby strategy's continuous cross-Region replication — the secondary Region's database is always current, ready to be promoted the moment a failover is declared.

> ⚠️ **Exam trap:** "relational data, one designated primary Region, fast promotion during failover" points to Aurora Global Database. "Multiple Regions need to accept writes simultaneously, not just reads" points to DynamoDB Global Tables' multi-active replication — a fundamentally different replication model, not just "the DynamoDB version of the same thing."

## Applying Module 4's Org-Wide Tooling to This One Workload

Choosing Warm Standby and Aurora Global Database doesn't complete the picture on its own — Module 4's organizational tooling is what makes sure this specific design actually works as intended, and stays that way:

- **AWS Resilience Hub** gets Meridian Loyalty registered as an application, with a resilience policy set to its actual RTO: 15 minutes, RPO: 1 minute targets. Resilience Hub then assesses the real architecture — confirming Aurora Global Database's replication lag and promotion time genuinely meet those targets, rather than assuming the design works because it sounds right on paper.
- **Route 53 Application Recovery Controller**, also from Module 4, provides the actual failover mechanism: readiness checks confirming the Warm Standby environment in the secondary Region is genuinely scaled and ready, a routing control giving Meridian's operations team an explicit, auditable way to trigger failover, and safety rules preventing that failover from making things worse.

This is the payoff of Module 4's investment: Meridian Loyalty doesn't need brand-new organizational tooling built just for it — it plugs into what Domain 1 already established.

## Putting It Together: Meridian Loyalty's Business Continuity Solution

Sofía's complete continuity design for Meridian Loyalty:

- **RTO: 15 minutes, RPO: 1 minute**, derived from the actual business impact of guests being unable to earn or redeem points — not an arbitrary or reflexively aggressive target.
- **Warm Standby** as the DR strategy, chosen because it's the cheapest of the four strategies that still comfortably meets both numbers.
- **Aurora Global Database** providing the continuous cross-Region replication Warm Standby depends on, with sub-second replication lag and roughly one-minute promotion during an actual failover.
- **AWS Resilience Hub** confirming the design actually meets its stated targets, and **Route 53 ARC** providing the safe, coordinated failover mechanism — both inherited directly from Module 4's organizational tooling.

## What to skip

You don't need to memorize Aurora Global Database's exact replication lag numbers under every load condition or DynamoDB Global Tables' conflict-resolution algorithm in detail — that's implementation depth beyond this exam. What matters is deriving RTO/RPO from a described business impact, matching it to the right DR strategy, choosing between Aurora Global Database and DynamoDB Global Tables based on the actual data model and replication needs, and connecting the design back to Module 4's Resilience Hub and Route 53 ARC.

## Key takeaways

- RTO and RPO targets for a new solution come from the actual described business impact of downtime and data loss — not a reflexive "as fast as possible" default.
- Warm Standby fits Meridian Loyalty's 15-minute RTO / 1-minute RPO: fast enough to meet the targets, without the cost of full active-active capacity the targets don't actually require.
- Aurora Global Database replicates relational data across Regions with sub-second lag and fast promotion, fitting one designated primary Region; DynamoDB Global Tables provides multi-active replication where multiple Regions need to accept writes simultaneously — a different replication model, not an equivalent.
- AWS Resilience Hub and Route 53 Application Recovery Controller, both introduced in Module 4, apply directly to this specific workload — validating the design against its targets and providing the actual coordinated failover mechanism.
- This module is the per-workload decision Module 4's org-wide tooling was built to support — the two are complementary halves of the same overall reliability picture.

## Further reading

- [Amazon Aurora Global Database Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) — cross-Region replication and failover promotion.
- [Amazon DynamoDB Global Tables Documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html) — multi-Region, multi-active replication.
- [AWS Resilience Hub User Guide](https://docs.aws.amazon.com/resilience-hub/latest/userguide/introduction.html) — revisit from Module 4, now applied to a specific application.
- [Amazon Route 53 Application Recovery Controller Developer Guide](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) — revisit from Module 4, now applied to a specific workload's failover.
