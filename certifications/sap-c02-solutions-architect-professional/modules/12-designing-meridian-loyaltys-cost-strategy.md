<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](11-designing-performance-efficiency-for-meridian-loyalty.md) · [Next module](13-continuously-improving-an-existing-solution.md) · [Quiz](../quizzes/12-designing-meridian-loyaltys-cost-strategy-quiz.md) · [Slides](../lectures/12-designing-meridian-loyaltys-cost-strategy.pptx)
<!-- /hub-navigation -->

# Module 12: Designing Meridian Loyalty's Cost Strategy

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 6 closed out Domain 1 by building the organization-wide cost tooling — Cost Explorer, the Cost and Usage Report, budgets and alerts, all built once for every account. It didn't decide how any one workload should actually be purchased or sized. This module is Task 2.6, and it closes out Domain 2 the same way Module 6 closed out Domain 1: the per-workload cost decision Module 6's tooling was built to support, made for Meridian Loyalty specifically — the last piece of a solution that's now been deployed, made resilient, secured, scaled, and made fast.

## Learning objectives

By the end of this module, you should be able to:

- Match a compute purchase option to a workload's actual predictability and interruptibility
- Distinguish Compute Savings Plans from EC2 Instance Savings Plans and choose correctly between them
- Explain how Module 6's cost visibility tooling applies to a new workload automatically
- Design a complete cost strategy for a stated new-solution scenario
- Summarize how all six Domain 2 tasks combine into one deployed, resilient, secure, scalable, performant, and cost-optimized solution

---

## Matching Purchase Options to Workload Predictability

Meridian Loyalty now has several genuinely different compute workloads, from Module 11's instance family discussion — and each one has a different relationship to time and interruption, which is exactly what determines the right purchase option.

- **On-Demand** costs the most per hour but requires no commitment at all — the right fit for a brand-new workload before its actual usage pattern is understood.
- **Savings Plans** (or Reserved Instances) trade a usage commitment, over one or three years, for a meaningfully lower rate — the right fit once a workload's baseline usage is steady and predictable.
- **Spot Instances** offer the deepest discount of all, in exchange for the instance being reclaimed with little notice when AWS needs the capacity back — the right fit only for workloads that can tolerate interruption.

Applied to Meridian Loyalty: the web and application tier runs continuously with a steady, predictable baseline — a Savings Plan fits. The overnight tier-recalculation batch job from Module 11 can simply restart if interrupted and has flexible timing — **Spot Instances** fit perfectly, at the deepest discount available, for a workload that was never latency-sensitive to begin with.

> ⚠️ **Exam trap:** the exam expects you to match the purchase option to the workload's actual tolerance for interruption and its usage predictability — not reach for Savings Plans everywhere because a commitment "sounds responsible," and not reach for Spot everywhere because the discount is deepest. A batch job that can restart is a great Spot candidate; a guest-facing web tier that can't tolerate sudden termination is not.

## Compute Savings Plans vs. EC2 Instance Savings Plans

Once Savings Plans are the right tool, there's still a choice between two Savings Plan types, and the exam expects you to know what each one actually commits to.

- **Compute Savings Plans** apply automatically to usage across any instance family, size, Region, operating system, or tenancy — and even extend to Fargate and Lambda usage. The commitment is a dollar amount per hour, not tied to a specific instance type, in exchange for a somewhat smaller discount than the more specific option.
- **EC2 Instance Savings Plans** commit to a specific instance family within a specific Region, in exchange for the deepest possible discount — but that commitment doesn't flex if the workload's instance family needs change.

Meridian Loyalty's actual future — new brands being onboarded, workloads that may shift instance families as the platform matures — favors **Compute Savings Plans**: the flexibility to change instance family or even move workloads to Fargate or Lambda without losing the discount is worth more than the last few points of savings an EC2 Instance Savings Plan would lock in.

> ⚠️ **Exam trap:** "usage pattern is well understood and stable, in one specific instance family, maximize discount" points to an EC2 Instance Savings Plan. "Usage may shift across instance types, Regions, or even to serverless" points to a Compute Savings Plan, trading a small amount of discount for meaningfully more flexibility.

## Applying Module 6's Tooling to This One Workload

Meridian Loyalty doesn't need a new cost-visibility program built from scratch — the same pattern from Modules 8 and 9 applies here too.

- **Cost allocation tags**, defined as an org-wide standard in Module 6, get applied to every Meridian Loyalty resource, so its costs are broken out clearly rather than blending into the org's total spend.
- **The Cost and Usage Report and Cost Explorer**, already aggregating every account organization-wide, pick up Meridian Loyalty's spend automatically the moment its resources are tagged and running — no separate reporting pipeline built just for this workload.
- **AWS Budgets**, set for Meridian Loyalty specifically using Module 6's existing budgeting tooling, alerts Sofía's team if actual spend diverges from what the Savings Plan and Spot mix was sized to cost.

## Putting It Together: Meridian Loyalty's Cost Strategy

Sofía's complete cost design for Meridian Loyalty:

- **A Savings Plan for the steady, predictable web and application tier**, and **Spot Instances for the interruption-tolerant overnight batch job** — purchase option matched to actual workload behavior, not applied uniformly.
- **Compute Savings Plans specifically**, favoring flexibility as Meridian Loyalty's instance needs evolve across brands and possibly into serverless, over squeezing out the last increment of discount.
- **Module 6's cost allocation tags, CUR, Cost Explorer, and Budgets**, already covering Meridian Loyalty the moment its resources exist and are tagged correctly — inherited, not rebuilt.

## Domain 2, Complete

With this module, Domain 2 is done: Module 7 designed how Meridian Loyalty deploys; Module 8 made it survive a disaster; Module 9 secured it; Module 10 made it scale; Module 11 made it fast; and Module 12 made sure none of that costs more than it needs to. Six tasks, one coherent new solution, built from nothing across six weeks.

## What to skip

You don't need to memorize Savings Plans' exact discount percentages by term length or Spot's interruption-notice timing down to the second — that's implementation depth beyond this exam. What matters is matching purchase options to workload predictability and interruption tolerance, choosing correctly between Compute and EC2 Instance Savings Plans, and recognizing that Module 6's cost tooling applies to a new workload automatically.

## Key takeaways

- On-Demand fits new, not-yet-understood workloads; Savings Plans fit steady, predictable baselines; Spot fits workloads that can tolerate interruption, at the deepest discount.
- Compute Savings Plans trade a small amount of discount for flexibility across instance family, Region, and even serverless; EC2 Instance Savings Plans lock in the deepest discount for a specific, stable instance family.
- Module 6's cost allocation tags, CUR, Cost Explorer, and Budgets apply to a new workload automatically, the moment its resources exist and are tagged — the same inherit-don't-rebuild pattern from Modules 8 and 9.
- This module is the per-workload cost decision Module 6's org-wide tooling was built to support — closing Domain 2 the same way Module 6 closed Domain 1.
- Domain 2's six tasks — deployment, business continuity, security, reliability at scale, performance, and cost — combine into one coherent new solution, not six independent decisions made in isolation.

## Further reading

- [AWS Savings Plans User Guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) — Compute vs. EC2 Instance Savings Plans.
- [Amazon EC2 Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances.html) — interruption-tolerant workloads.
- [AWS Cost Explorer User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) — revisit from Module 6, now applied to a specific workload.
- [AWS Budgets User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) — revisit from Module 6, now applied to Meridian Loyalty specifically.
