# Module 4: Designing Reliable and Resilient Architectures

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

SAA-C03 covered disaster recovery for one workload: pick a strategy, replicate to a secondary Region, done. That's still true and still necessary — but it's a per-workload decision, made by one team, for one system. Task 1.3 asks a different question: as the organization's architect, how do you make resilience consistent, measurable, and centrally governed across every workload Meridian owns, without personally reviewing every backup policy and failover plan by hand?

This module is about the organizational tooling that makes reliability a managed, org-wide practice rather than something each brand's team reinvents independently — and gets right or wrong on their own.

## Learning objectives

By the end of this module, you should be able to:

- Explain how AWS Backup uses organization-wide backup policies to enforce consistent backup practices across every account
- Describe what AWS Resilience Hub assesses, and how it scores an application against defined resilience targets
- Explain what Amazon Route 53 Application Recovery Controller adds beyond basic Route 53 health checks and failover routing
- Distinguish the org-level view of reliability (Domain 1) from the per-workload DR strategy decision (a design skill practiced further in Domain 2)
- Recommend organization-level reliability tooling for a stated multi-account scenario

---

## AWS Backup: Organization-Wide Backup Policies

SAA-C03 introduced AWS Backup as a way to centralize backup configuration within one account. At the organization level, AWS Backup goes further: through integration with **AWS Organizations**, a **backup policy** can be defined once and attached to an OU — automatically applying to every account inside it, the same way an SCP does.

This solves a real problem for Meridian. Without an org-wide backup policy, nothing stops an engineer on Haven & Co.'s team from quietly turning off backups on a production database, or configuring a backup schedule that doesn't meet Meridian's actual retention requirements — and nobody at the organization level would necessarily notice until it's too late. An organization-wide backup policy, attached at the Production OU level, defines backup frequency, retention period, and cross-Region copy requirements once, and every account in that OU — Café Sol's today, Ridgeline's once it's migrated in — inherits it automatically, without depending on each team to configure it correctly on their own.

> ⚠️ **Exam trap:** a scenario describing inconsistent backup practices across multiple accounts, or a backup configuration a team "forgot" to set correctly, is usually pointing at organization-wide AWS Backup policies attached at the OU level — not at fixing each account's backup configuration individually, which doesn't scale and doesn't prevent the next account from making the same mistake.

## AWS Resilience Hub: Measuring Resilience Against a Target

Defining a backup policy is necessary but not sufficient — it says data is being backed up, not that a given application can actually *recover* within the time and data-loss targets the business actually needs. **AWS Resilience Hub** closes that gap: you define an application (its component AWS resources) and set explicit **resilience policies** — RTO and RPO targets, the same concepts from SAA-C03's disaster recovery module, but now formalized and tracked centrally — and Resilience Hub assesses the actual architecture against those targets.

The assessment identifies specific gaps: a database without cross-Region replication when the resilience policy requires a Region-level recovery capability, or a compute tier that isn't distributed across enough Availability Zones to meet a stated AZ-failure tolerance. Resilience Hub doesn't just report a pass/fail — it produces a resilience score and concrete, actionable recommendations for closing each gap.

This matters at the organization level specifically because it lets Sofía track resilience posture across all of Meridian's applications from one place, rather than trusting each brand's team to self-report whether their system actually meets its stated recovery targets.

## Amazon Route 53 Application Recovery Controller: Coordinated, Safe Failover

SAA-C03 covered Route 53 health checks and failover routing for a single application. At organizational scale, coordinating failover safely across multiple applications and accounts introduces a new risk: an automated failover mechanism that fires incorrectly — due to a false-positive health check, for instance — can cause more damage than the outage it was meant to protect against, especially if multiple systems fail over inconsistently or simultaneously in ways that weren't planned for.

**Amazon Route 53 Application Recovery Controller (Route 53 ARC)** adds three capabilities on top of basic Route 53 failover for exactly this reason:

- **Readiness checks** continuously verify that a standby Region or resource is actually capable of taking over — not just present, but correctly configured, scaled, and ready — before you ever need it to.
- **Routing controls** are simple on/off switches that explicitly control where traffic flows, giving operators (or automation) a deliberate, auditable mechanism for triggering failover, rather than relying solely on automatic health-check-driven behavior.
- **Safety rules** prevent a failover action from making things worse — for example, blocking a routing control change that would take the last remaining healthy Region out of service.

For Meridian, Route 53 ARC is the piece that lets multiple brands' applications fail over in a coordinated, centrally governed way, with guardrails against the automation itself becoming a new source of outages.

## Domain 1's View of Reliability vs. a Per-Workload DR Decision

It's worth being explicit about the boundary this module sits on. Choosing *which* DR strategy — Backup and Restore, Pilot Light, Warm Standby, or Multi-Site Active/Active — fits one specific new workload's stated RTO/RPO is a Domain 2 skill, covered later in this course when Meridian designs new solutions. This module's Domain 1 skill is different: it's the organization-level tooling that makes resilience *consistent and measurable* across every workload, regardless of which specific DR strategy any one of them uses — backup policy enforcement, resilience scoring against targets, and coordinated, safe failover mechanisms that work the same way no matter which brand's application is failing over.

> ⚠️ **Exam trap:** a question asking "which DR strategy fits this new workload's RTO/RPO" is testing the Domain 2 skill from later in this course. A question asking "how do we make sure every account follows the same backup and resilience practices" or "how do we prevent an automated failover from making an outage worse" is testing this module's Domain 1 content. Read for which one is actually being asked.

## Putting It Together: Meridian's Organization-Level Reliability Strategy

Sofía's reliability strategy for Meridian, at the organization level:

- An **AWS Backup organization-wide policy** attached to the Production OU, defining backup frequency, retention, and cross-Region copy requirements once — inherited automatically by Café Sol today and Ridgeline once it's migrated in, with no per-account configuration required or trusted to memory.
- **AWS Resilience Hub** applications and resilience policies defined for each brand's critical systems, giving Sofía one place to see whether Café Sol's, Haven & Co.'s, and eventually Ridgeline's actual architectures meet their stated RTO/RPO targets — not just whether backups exist.
- **Route 53 Application Recovery Controller**, with readiness checks confirming each brand's standby capacity is genuinely ready, routing controls giving Meridian's operations team an explicit, auditable failover trigger, and safety rules preventing a bad automated decision from taking down more than the original incident did.

## What to skip

You don't need to memorize Resilience Hub's exact scoring formula or write Route 53 ARC routing control configuration by hand — that's implementation depth beyond this exam. What matters is recognizing what each service adds at the organization level, and telling this module's org-wide reliability tooling apart from the per-workload DR strategy decision covered later in Domain 2.

## Key takeaways

- AWS Backup organization-wide policies, attached via AWS Organizations at the OU level, enforce consistent backup frequency, retention, and cross-Region copy requirements across every account automatically — closing the gap left by per-account, per-team backup configuration.
- AWS Resilience Hub assesses an application's actual architecture against explicit RTO/RPO resilience policies, producing a resilience score and specific recommendations — going beyond "backups exist" to "this system can actually recover within its stated targets."
- Route 53 Application Recovery Controller adds readiness checks, routing controls, and safety rules on top of basic Route 53 failover, enabling coordinated, safe failover across multiple applications and accounts.
- This module's org-level reliability tooling (consistency and measurement across every workload) is a different skill from choosing a specific DR strategy for one new workload's stated requirement, which belongs to Domain 2.
- Meridian's strategy combines all three: org-wide backup policy enforcement, Resilience Hub scoring against targets, and Route 53 ARC for coordinated, governed failover.

## Further reading

- [AWS Backup: Organization-Wide Backup Policies](https://docs.aws.amazon.com/aws-backup/latest/devguide/manage-cross-account.html) — centralized backup policy management via AWS Organizations.
- [AWS Resilience Hub User Guide](https://docs.aws.amazon.com/resilience-hub/latest/userguide/introduction.html) — application resilience assessment and scoring against RTO/RPO policies.
- [Amazon Route 53 Application Recovery Controller Developer Guide](https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route53-recovery.html) — readiness checks, routing controls, and safety rules.
