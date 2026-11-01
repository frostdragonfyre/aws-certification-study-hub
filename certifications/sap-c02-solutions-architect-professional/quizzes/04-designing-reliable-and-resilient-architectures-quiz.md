[Course index](../README.md) · [Read the paired lesson](../modules/04-designing-reliable-and-resilient-architectures.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 4 Knowledge Check**

Designing Reliable and Resilient Architectures · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|

*Instructions: Answer every question. Questions get harder as you go — the last several are exam-style judgment questions where more than one answer looks reasonable. For those, pick the BEST answer and be ready to defend it out loud.*

| **Question types** | **What to do** |
|---|---|
| Multiple Choice | Circle one letter. |
| True / False | Circle TRUE or FALSE. |
| Fill in the Blank | Write your answer on the line. |
| Scenario / Judgment | Circle the BEST answer. Note WHY the others fail. |

---

## Easy Questions

**1. [True / False] Easy**

> An AWS Backup organization-wide policy can be attached to an OU, automatically applying to every account inside it.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service assesses an application's architecture against defined RTO/RPO targets and produces a resilience score?
>
> **A.** AWS Backup
> **B.** AWS Resilience Hub
> **C.** Amazon Route 53
> **D.** AWS Organizations

**3. [Fill in the Blank] Easy**

> Amazon Route 53 ____________ ____________ ____________ adds readiness checks, routing controls, and safety rules on top of basic Route 53 failover.

**4. [Multiple Choice] Easy**

> What does a Route 53 ARC readiness check verify?
>
> **A.** That a standby Region or resource is actually capable of taking over, not just present
> **B.** That an IAM policy has been correctly attached
> **C.** That an SCP has been attached to the correct OU
> **D.** That a backup policy has been configured

**5. [True / False] Easy**

> AWS Resilience Hub only checks whether backups exist, without assessing whether an application can actually meet its stated RTO/RPO.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> An engineer on Haven & Co.'s team quietly misconfigures their backup schedule, and nobody at the organization level notices until data is lost. What organization-level control would have prevented this?
>
> **A.** A Route 53 health check
> **B.** An AWS Backup organization-wide policy attached at the OU level
> **C.** A VPC peering connection
> **D.** An IAM Identity Center permission set

**7. [Fill in the Blank] Moderate**

> A Route 53 ARC ____________ rule prevents a failover action from making things worse — for example, blocking a change that would take the last healthy Region out of service.

**8. [Multiple Choice] Moderate**

> What does a Route 53 ARC routing control provide?
>
> **A.** An automatic, un-auditable failover mechanism with no operator involvement
> **B.** A simple on/off switch giving operators or automation a deliberate, auditable mechanism for controlling where traffic flows
> **C.** A replacement for AWS Backup
> **D.** A way to attach SCPs to organizational units

**9. [True / False] Moderate**

> Choosing which specific DR strategy (like Pilot Light or Warm Standby) fits one new workload's stated RTO/RPO is this module's core Domain 1 skill.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What specifically does AWS Resilience Hub identify beyond "backups exist"?
>
> **A.** Whether an IAM user's password has expired
> **B.** Specific architectural gaps, like a database missing cross-Region replication required by a stated resilience policy
> **C.** Whether an SCP is attached to the correct OU
> **D.** Whether a VPC peering connection is transitive

**11. [Fill in the Blank] Moderate**

> An AWS Backup policy attached at the OU level defines backup frequency, retention period, and ____________ ____________ requirements once, inherited automatically by every account in that OU.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Meridian's leadership wants to know, across all three brands, whether each brand's critical systems can actually recover within their stated RTO/RPO — not just whether backups are configured. Which tool answers this?
>
> **A.** AWS Backup alone
> **B.** AWS Resilience Hub, assessing each application against its resilience policy
> **C.** A VPC peering connection
> **D.** An SCP attached to the Production OU

**13. [Scenario / Judgment] Hard**

> Meridian's operations team wants an explicit, auditable way to trigger failover themselves, rather than relying solely on automatic health-check-driven behavior. What fits?
>
> **A.** A Route 53 ARC routing control
> **B.** An AWS Backup policy
> **C.** A cross-account IAM role
> **D.** A Transit Gateway attachment

**14. [Scenario / Judgment] Hard**

> A false-positive health check nearly triggers a failover that would have taken the last remaining healthy Region out of service. What Route 53 ARC feature exists specifically to prevent this?
>
> **A.** A readiness check
> **B.** A routing control
> **C.** A safety rule
> **D.** An SCP

**15. [Scenario / Judgment] Hard**

> Ridgeline's account joins Meridian's Production OU after migration. Without any additional configuration, what backup requirements will it automatically inherit?
>
> **A.** None — backup policies must be manually configured per account regardless of OU membership
> **B.** The organization-wide AWS Backup policy already attached to the Production OU
> **C.** Only the backup policy Ridgeline's own team configures independently
> **D.** Backup policies cannot apply to accounts added after a policy is attached

**16. [Scenario / Judgment] Hard**

> A question describes choosing between Pilot Light and Warm Standby for a specific new order-processing system, based on its stated RTO. Which part of this course does that question belong to?
>
> **A.** This module's Domain 1 content
> **B.** A Domain 2 skill, covered later in this course when Meridian designs new solutions
> **C.** AWS Backup organization-wide policy configuration
> **D.** Route 53 ARC safety rule configuration

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Since AWS Backup is already configured for Café Sol's account, Meridian's reliability strategy is complete." Correct this using this module's content.
>
> **A.** They're right — backup configuration alone is sufficient for organization-level reliability
> **B.** Backups being configured for one account doesn't guarantee consistency across other accounts, doesn't confirm any application can actually recover within its stated RTO/RPO, and doesn't provide a safe, coordinated failover mechanism — an organization-wide policy, Resilience Hub assessment, and Route 53 ARC are all still needed
> **C.** AWS Backup is unrelated to reliability
> **D.** Resilience Hub and Route 53 ARC are redundant with AWS Backup and unnecessary

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Automatic health-check-driven failover is always safer than giving operators a manual routing control, since it removes human delay." Evaluate this using this module's content.
>
> **A.** Agree without qualification — automation should always be preferred over any manual mechanism
> **B.** Disagree — a false-positive health check can trigger an incorrect failover automatically, which is exactly why Route 53 ARC pairs automated behavior with routing controls (an explicit, auditable trigger) and safety rules (preventing an action from making things worse), rather than relying on automatic behavior alone
> **C.** Disagree, but only because automated failover is technically impossible with Route 53
> **D.** Agree, since safety rules only apply to manual routing controls, never to automated failover

**19. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Sofía needs both an organization-wide AWS Backup policy and AWS Resilience Hub — why doesn't one make the other redundant?
>
> **A.** They are redundant, and either alone is sufficient
> **B.** An organization-wide backup policy guarantees that backups happen consistently across accounts, but says nothing about whether an application's actual architecture can recover within its stated RTO/RPO; Resilience Hub assesses that recovery capability directly, against explicit targets — they answer different questions
> **C.** AWS Backup only works within a single account and cannot be used at the organization level at all
> **D.** Resilience Hub replaces the need for backups entirely

**20. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping org-wide tooling entirely and just trusting each brand's team to independently configure their own backups, DR strategy, and failover mechanism correctly. Argue against this using this module's content.
>
> **A.** Agree — each team knows their own workload best, so central tooling adds no value
> **B.** Disagree — without organization-wide enforcement, nothing prevents inconsistent or missing backup configuration, unverified recovery capability, or an uncoordinated failover mechanism from going unnoticed until an actual incident, which is exactly the gap AWS Backup policies, Resilience Hub, and Route 53 ARC are designed to close
> **C.** Disagree, but only because AWS technically prohibits per-team configuration
> **D.** Agree, since Domain 1 tooling is optional and has no bearing on actual outcomes

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
