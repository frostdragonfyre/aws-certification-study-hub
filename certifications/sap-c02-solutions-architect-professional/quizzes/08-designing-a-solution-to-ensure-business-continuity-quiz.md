[Course index](../README.md) · [Read the paired lesson](../modules/08-designing-a-solution-to-ensure-business-continuity.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 8 Knowledge Check**

Designing a Solution to Ensure Business Continuity · 20 questions · Practice — not graded

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

> Meridian Loyalty's RTO and RPO targets were derived from a described business impact, not chosen reflexively.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which DR strategy was chosen for Meridian Loyalty, given its RTO of 15 minutes and RPO of 1 minute?
>
> **A.** Backup and Restore
> **B.** Pilot Light
> **C.** Warm Standby
> **D.** Multi-Site Active/Active

**3. [Fill in the Blank] Easy**

> Amazon Aurora ____________ ____________ replicates a relational Aurora database across Regions with typical replication lag under one second.

**4. [Multiple Choice] Easy**

> Which service provides multi-Region, multi-active replication, where every Region can accept both reads and writes?
>
> **A.** Amazon Aurora Global Database
> **B.** Amazon DynamoDB Global Tables
> **C.** AWS Backup
> **D.** Route 53 Resolver

**5. [True / False] Easy**

> Backup and Restore's typical multi-hour RTO would meet Meridian Loyalty's stated 15-minute RTO requirement.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why wasn't Multi-Site Active/Active chosen for Meridian Loyalty, even though it would meet the stated RTO/RPO?
>
> **A.** It technically cannot meet a 15-minute RTO
> **B.** It would run full production capacity in two Regions continuously, more than the stated targets actually require, at meaningfully higher cost than Warm Standby
> **C.** It is not a real AWS-supported DR strategy
> **D.** It requires DynamoDB and cannot be used with Aurora

**7. [Fill in the Blank] Moderate**

> AWS ____________ ____________ assesses Meridian Loyalty's actual architecture against its resilience policy, confirming the design meets its stated RTO/RPO targets.

**8. [Multiple Choice] Moderate**

> During an actual failover, roughly how quickly can an Aurora Global Database secondary Region's read replica be promoted to a full read/write primary?
>
> **A.** About one minute
> **B.** About 24 hours
> **C.** Instantaneously, with zero delay
> **D.** Promotion is not supported by Aurora Global Database

**9. [True / False] Moderate**

> Route 53 Application Recovery Controller, introduced in Module 4, can be applied directly to Meridian Loyalty's specific failover mechanism.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What kind of data model does Amazon Aurora Global Database fit, as used for Meridian Loyalty's reward-balance data?
>
> **A.** Relational, structured data
> **B.** Unstructured object storage
> **C.** Multi-active NoSQL writes across every Region simultaneously
> **D.** Data that requires no replication at all

**11. [Fill in the Blank] Moderate**

> Meridian Loyalty's stated targets are RTO: ____________ minutes, RPO: ____________ minute.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A new solution's described business impact is: "if this goes down, the business loses revenue every second, and any lost data is unacceptable." What does this description suggest about the appropriate RTO/RPO, using this module's reasoning?
>
> **A.** A long RTO and RPO, similar to an internal reporting system
> **B.** A near-zero RTO and RPO, likely pointing toward Multi-Site Active/Active rather than Warm Standby
> **C.** RTO and RPO are irrelevant to this description
> **D.** Backup and Restore, since it's the cheapest option regardless of the description

**13. [Scenario / Judgment] Hard**

> A new solution's data needs multiple Regions to each accept both reads and writes simultaneously, not just one designated primary Region with read replicas elsewhere. Which service fits?
>
> **A.** Amazon Aurora Global Database
> **B.** Amazon DynamoDB Global Tables
> **C.** AWS Backup
> **D.** Neither — this requirement cannot be met by any AWS service

**14. [Scenario / Judgment] Hard**

> Sofía wants to confirm that Meridian Loyalty's chosen architecture actually meets its 15-minute RTO and 1-minute RPO targets, rather than assuming it does because the design sounds reasonable. What should she use?
>
> **A.** AWS Resilience Hub, assessing the real architecture against a defined resilience policy
> **B.** A budget action
> **C.** A tag policy
> **D.** VPC peering

**15. [Scenario / Judgment] Hard**

> Meridian's operations team wants an explicit, auditable way to trigger Meridian Loyalty's failover to its Warm Standby environment, with safeguards against making an incident worse. What provides this?
>
> **A.** AWS Cost Anomaly Detection
> **B.** Route 53 Application Recovery Controller, with its routing controls and safety rules
> **C.** AWS Config alone
> **D.** A cross-account IAM role

**16. [Scenario / Judgment] Hard**

> A reviewer proposes choosing Pilot Light for Meridian Loyalty instead of Warm Standby, arguing it's cheaper. What's the risk in this choice, given the stated 15-minute RTO?
>
> **A.** There is no risk — Pilot Light is strictly better in every case
> **B.** Pilot Light's tens-of-minutes RTO is borderline and risky against a hard 15-minute requirement, since its application tier isn't running day-to-day and must be scaled up during failover
> **C.** Pilot Light cannot be used with Aurora Global Database under any circumstances
> **D.** Pilot Light always exceeds Warm Standby's cost, making the comparison irrelevant

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Module 4 already covered disaster recovery, so this module is redundant." Correct this using this module's content and Module 4's.
>
> **A.** They're right — the two modules cover identical content
> **B.** Module 4 covered organization-wide tooling that makes resilience consistent and measurable across every workload, explicitly stopping short of choosing a DR strategy for any one workload; this module is that per-workload decision, made for Meridian Loyalty specifically, and it plugs directly into Module 4's tooling rather than duplicating it
> **C.** Module 4 only applies to Café Sol and Haven & Co., never to new solutions
> **D.** This module replaces Module 4's content entirely

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since DynamoDB Global Tables supports writes in every Region, it's strictly more capable than Aurora Global Database and should always be preferred." Evaluate this using this module's content.
>
> **A.** Agree — DynamoDB Global Tables should always be chosen regardless of data model
> **B.** Disagree — the two serve different data models and replication needs; Aurora Global Database fits relational, structured data with one designated primary Region and fast promotion, while DynamoDB Global Tables' multi-active model fits a different NoSQL access pattern. "More capable" isn't the deciding factor — fit to the actual data model is
> **C.** Disagree, but only because DynamoDB Global Tables doesn't actually support multi-Region writes
> **D.** Agree, since Aurora Global Database cannot replicate across Regions at all

**19. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Sofía negotiated Meridian Loyalty's RTO and RPO with the business based on actual impact, rather than simply requesting the tightest possible targets by default.
>
> **A.** Tighter targets are always free, so there was no reason to negotiate
> **B.** A near-zero RTO/RPO generally requires more standing infrastructure running continuously, which costs more; matching the target to the real business impact (guests can't earn or redeem points, but it isn't a by-the-second revenue emergency) avoids paying for a fully active-active deployment the actual impact doesn't justify
> **C.** RTO and RPO are set automatically by AWS and cannot be negotiated
> **D.** The tightest possible targets were requested, contrary to what the module describes

**20. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping Resilience Hub validation entirely, arguing that choosing Warm Standby and Aurora Global Database is self-evidently sufficient to meet the stated targets. Argue against this using this module's content.
>
> **A.** Agree — the chosen strategy and technology are always sufficient on paper, no verification needed
> **B.** Disagree — choosing a strategy and technology doesn't confirm the actual implementation meets the targets; Resilience Hub assesses the real architecture against the resilience policy, rather than assuming the design works because it sounds right, which is exactly the gap this module and Module 4 both describe
> **C.** Disagree, but only because Resilience Hub is required by AWS for every deployment
> **D.** Agree, since Route 53 ARC alone makes Resilience Hub redundant

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
