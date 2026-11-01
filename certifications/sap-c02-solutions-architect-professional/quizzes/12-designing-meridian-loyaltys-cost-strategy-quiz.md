[Course index](../README.md) · [Read the paired lesson](../modules/12-designing-meridian-loyaltys-cost-strategy.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 12 Knowledge Check**

Designing Meridian Loyalty's Cost Strategy · 20 questions · Practice — not graded

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

> Purchase options should be matched to a workload's actual predictability and tolerance for interruption, not applied uniformly across every workload.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which purchase option fits Meridian Loyalty's overnight tier-recalculation batch job, which can restart if interrupted?
>
> **A.** On-Demand
> **B.** A three-year EC2 Instance Savings Plan
> **C.** Spot Instances
> **D.** Dedicated Hosts

**3. [Fill in the Blank] Easy**

> ____________ ____________ costs the most per hour but requires no commitment, fitting a brand-new workload before its usage pattern is understood.

**4. [Multiple Choice] Easy**

> Which Savings Plan type applies automatically across any instance family, Region, OS, and even Fargate and Lambda usage?

> **A.** EC2 Instance Savings Plan
> **B.** Compute Savings Plan
> **C.** Reserved Instances
> **D.** Spot Savings Plan (not a real AWS offering)

**5. [True / False] Easy**

> Module 6's Cost and Usage Report and Cost Explorer require a brand-new reporting pipeline to be built for each new workload.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does a Savings Plan fit Meridian Loyalty's web and application tier specifically?

> **A.** Because the tier can tolerate sudden termination
> **B.** Because it runs continuously with a steady, predictable baseline, matching the usage commitment a Savings Plan requires
> **C.** Because Savings Plans are always the cheapest option regardless of workload
> **D.** Because the web tier is brand-new with no usage history

**7. [Fill in the Blank] Moderate**

> ____________ ____________, defined as an org-wide standard in Module 6, get applied to every Meridian Loyalty resource so its costs are broken out clearly.

**8. [Multiple Choice] Moderate**

> Why does Meridian Loyalty's future favor Compute Savings Plans over EC2 Instance Savings Plans?

> **A.** Compute Savings Plans always provide a deeper discount
> **B.** The flexibility to change instance family or move to Fargate/Lambda without losing the discount is worth more than the last few points of savings an EC2 Instance Savings Plan would lock in, given onboarding new brands and evolving workloads
> **C.** EC2 Instance Savings Plans cannot be used with Auto Scaling groups
> **D.** Compute Savings Plans are required for any workload using DynamoDB

**9. [True / False] Moderate**

> AWS Budgets, set for Meridian Loyalty using Module 6's existing tooling, alerts Sofía's team if actual spend diverges from what was planned.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does an EC2 Instance Savings Plan commit to, in exchange for the deepest possible discount?

> **A.** A dollar amount per hour, flexible across any instance family
> **B.** A specific instance family within a specific Region, with no flexibility if needs change
> **C.** Nothing — it requires no commitment at all
> **D.** Fargate and Lambda usage exclusively

**11. [Fill in the Blank] Moderate**

> ____________ Instances offer the deepest discount of all, in exchange for being reclaimed with little notice when AWS needs the capacity back.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A new solution has a guest-facing web tier that cannot tolerate sudden termination mid-request. Which purchase option is the wrong fit for this specific tier?

> **A.** A Savings Plan, since the tier's baseline is steady
> **B.** Spot Instances, since the tier cannot tolerate the interruption Spot capacity reclamation would cause
> **C.** On-Demand, before usage patterns are understood
> **D.** All purchase options are equally wrong for this tier

**13. [Scenario / Judgment] Hard**

> A reviewer proposes an EC2 Instance Savings Plan for Meridian Loyalty's web tier, arguing it maximizes discount. What's the risk, given Meridian Loyalty is onboarding new brands and may shift instance types?

> **A.** There is no risk — EC2 Instance Savings Plans are always the better choice
> **B.** The commitment is locked to a specific instance family and Region; if the workload's instance needs shift as new brands onboard, that commitment doesn't flex, unlike a Compute Savings Plan
> **C.** EC2 Instance Savings Plans cannot be purchased for workloads with fewer than three brands
> **D.** EC2 Instance Savings Plans expire automatically after 90 days regardless of term length

**14. [Scenario / Judgment] Hard**

> Sofía wants Meridian Loyalty's spend to show up clearly in the organization's existing cost dashboard, without building a new one. What accomplishes this?

> **A.** A brand-new, separate Cost Explorer instance just for Meridian Loyalty
> **B.** Applying Module 6's cost allocation tags to Meridian Loyalty's resources, so the existing organization-wide CUR and Cost Explorer pick up its spend automatically
> **C.** Manually calculating Meridian Loyalty's costs from invoices each month
> **D.** Disabling cost tracking for new workloads until they mature

**15. [Scenario / Judgment] Hard**

> A student argues that Spot Instances should be avoided entirely because "the instance can just disappear." What's the flaw in this reasoning as a blanket rule?

> **A.** There is no flaw — Spot should always be avoided
> **B.** Spot's interruption risk only matters for workloads that can't tolerate it; a workload like Meridian Loyalty's overnight batch job, which can simply restart, benefits from Spot's deep discount without meaningful downside
> **C.** Spot Instances never actually get interrupted in practice
> **D.** Spot Instances can only be used for storage, never compute

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Module 6 already covered cost optimization, so this module is redundant." Correct this using this module's content and Module 6's.

> **A.** They're right — the two modules cover identical content
> **B.** Module 6 built organization-wide cost visibility tooling — Cost Explorer, CUR, budgets, tagging standards — that apply automatically to every account; this module is the per-workload purchasing decision that tooling supports, made for Meridian Loyalty specifically, plugging into Module 6's tooling rather than duplicating it
> **C.** Module 6 only applies to Café Sol and Haven & Co., never to new solutions
> **D.** This module replaces Module 6's content entirely

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since Spot Instances are the cheapest option, every Meridian Loyalty workload should run on Spot to minimize cost." Evaluate this using this module's content.

> **A.** Agree — Spot should always be used regardless of workload characteristics
> **B.** Disagree — Spot's deep discount comes with interruption risk that fits only workloads tolerant of it, like the batch job; the guest-facing web tier cannot tolerate sudden termination, so applying Spot there would trade cost savings for a real reliability failure, not a good trade
> **C.** Disagree, but only because Spot Instances cannot be used with any AWS service besides EC2
> **D.** Agree, since Spot Instances never actually get reclaimed in practice

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Domain 2's six tasks are described as combining into "one coherent new solution" rather than six independent decisions.

> **A.** They're actually unrelated topics that happen to be grouped together by coincidence
> **B.** Each task addressed a different concern for the same solution — how it deploys, survives a disaster, stays secure, scales under load, stays fast, and costs the right amount — and together they describe one complete, real Meridian Loyalty, not six separate systems
> **C.** Only the deployment task (Module 7) actually matters; the rest are optional additions
> **D.** The six tasks must be implemented in a specific order and cannot be revisited once complete

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping cost allocation tags for Meridian Loyalty, arguing "the total org bill is all that matters." Argue against this using this module's content.

> **A.** Agree — tagging is unnecessary busywork if the org bill is tracked
> **B.** Disagree — without tags, Meridian Loyalty's spend blends into the org's total rather than being broken out clearly, making it impossible to see whether its specific purchase-option choices (Savings Plans, Spot) are actually working as intended or to catch a divergence with Budgets
> **C.** Disagree, but only because AWS requires tags for billing to function at all
> **D.** Agree, since Cost Explorer cannot use tags under any circumstances

**20. [Scenario / Judgment] Very Hard**

> A student says: "Cost optimization is just about picking the cheapest option for everything." Evaluate this using this module's content.

> **A.** Agree — the cheapest available option is always the correct choice
> **B.** Disagree — this module's entire approach is matching the purchase option to the workload's actual behavior: commitment for predictable baselines, interruption tolerance for Spot, flexibility for Compute Savings Plans given an evolving future. The cheapest option in isolation (like Spot everywhere) can actively harm a workload that can't tolerate its trade-offs
> **C.** Disagree, but only because AWS sets a fixed price that cannot be optimized
> **D.** Agree, since this module recommends Spot Instances for every workload

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
