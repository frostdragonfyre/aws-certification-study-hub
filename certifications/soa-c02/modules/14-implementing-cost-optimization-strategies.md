# Module 14: Implementing Cost Optimization Strategies

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Domain 5 made sure Meridian's systems connect, deliver content, and can be troubleshot. Domain 6 asks a different question: are they costing what they should? This module is Domain 6's first task, opening the domain with the tools that find savings and catch surprises before they show up on an invoice.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish when Savings Plans or Reserved Instances fit versus when Spot Instances fit
- Distinguish Compute Optimizer from Cost Explorer, and know what each one is for
- Distinguish AWS Budgets from Cost Anomaly Detection
- Explain why rightsizing recommendations need real utilization data behind them
- Design a cost optimization strategy for a stated workload and spend pattern

---

## Savings Plans and Reserved Instances vs. Spot Instances

All three are discount mechanisms compared to On-Demand pricing, but they trade off differently between commitment and reliability.

**Savings Plans and Reserved Instances (RIs)** both require a **commitment** — typically a 1- or 3-year term — in exchange for a significant discount, and both fit workloads with **steady, predictable, baseline usage** that Priya knows will keep running regardless of what happens. Savings Plans are more flexible about which instance family or Region the commitment applies to; RIs are more rigid but can be even cheaper for a workload that truly never changes shape.

**Spot Instances** offer the deepest discount of the three, in exchange for the opposite tradeoff: AWS can **reclaim the capacity with short notice** when it's needed elsewhere. Spot only fits workloads that are **fault-tolerant and flexible about interruption** — batch processing, CI/CD build fleets, stateless web tiers behind a load balancer that can lose an instance without losing the request.

> ⚠️ **Exam trap:** a scenario describing **steady, predictable, always-on** usage that must **not** be interrupted is describing a fit for **Savings Plans or Reserved Instances**. A scenario describing **flexible, fault-tolerant, interruption-tolerant** work, where the deepest possible discount matters more than guaranteed availability, is describing a fit for **Spot Instances** — using Spot for a workload that can't tolerate interruption is the trap.

## Compute Optimizer vs. Cost Explorer

Both tools help with cost, but they answer very different questions.

**Compute Optimizer** analyzes actual **utilization metrics** (CPU, memory where available, network, and more) over time and uses machine learning to recommend **specific rightsizing changes** — a smaller instance type, a different instance family, or an EBS volume type change — for resources that are over-provisioned or under-provisioned relative to what they actually use. It answers: "is this specific resource the right size for its real usage?"

**Cost Explorer** visualizes **spend and usage trends** — by service, account, tag, or time period — and can forecast future spend based on historical patterns. It answers: "where is money going, and where is it trending?" Cost Explorer shows you the spend; it doesn't analyze a resource's utilization metrics the way Compute Optimizer does.

> ⚠️ **Exam trap:** a scenario asking for a **specific rightsizing recommendation** for an over-provisioned EC2 instance, based on its **actual utilization**, is describing **Compute Optimizer**. A scenario asking to **visualize or forecast spend trends** across services, accounts, or tags is describing **Cost Explorer** — reaching for Cost Explorer to get an instance-level rightsizing recommendation is the trap.

## AWS Budgets vs. Cost Anomaly Detection

Both alert on cost, but they're triggered by different things.

**AWS Budgets** alerts based on a **threshold you define** — a dollar amount or a percentage of a planned budget — and can notify when actual or forecasted spend crosses that line. It requires knowing in advance what "too much" looks like. **Cost Anomaly Detection** uses **machine learning** to learn a normal spend pattern and alert on **unusual deviations from it**, without needing a predefined threshold — it can catch an unexpected spend spike that's well under any budget limit you'd have thought to set, simply because it doesn't match the established pattern.

> ⚠️ **Exam trap:** a scenario needing an alert when spend crosses a **known, predefined dollar or percentage threshold** is describing **AWS Budgets**. A scenario needing to catch an **unexpected or unusual** spend pattern that might not cross any specific threshold at all is describing **Cost Anomaly Detection**.

## Putting It Together: Optimizing Meridian's Costs

Priya's cost strategy, opening Domain 6:

- **Savings Plans** covering Meridian Loyalty's steady baseline compute, with **Spot Instances** for Café Sol's fault-tolerant nightly batch reporting jobs.
- **Compute Optimizer** reviewed monthly across all three systems, rightsizing over-provisioned instances based on actual utilization rather than guesswork.
- **Cost Explorer** for the monthly spend review with leadership, broken down by service and tag to show where budget is actually going.
- **AWS Budgets** set on each team's monthly allocation, paired with **Cost Anomaly Detection** account-wide to catch a spend spike that wouldn't have crossed any budget threshold but still doesn't match the normal pattern.

## What to skip

You don't need to memorize Savings Plans' exact discount percentages by term length or Compute Optimizer's specific ML model — that's implementation depth beyond this exam. What matters is knowing the commitment-versus-interruption tradeoff across Savings Plans, RIs, and Spot; when Compute Optimizer's utilization-based rightsizing fits versus Cost Explorer's spend visualization; and threshold-based Budgets versus pattern-based Cost Anomaly Detection.

## Key takeaways

- Savings Plans and Reserved Instances fit steady, predictable, uninterruptible usage; Spot Instances fit flexible, fault-tolerant, interruption-tolerant workloads, in exchange for the deepest discount.
- Compute Optimizer recommends specific rightsizing changes based on actual utilization; Cost Explorer visualizes and forecasts spend trends — they answer different questions.
- AWS Budgets alerts against a threshold you define; Cost Anomaly Detection uses machine learning to catch unusual spend patterns you didn't predefine a threshold for.
- Domain 6 continues: Module 14 finds savings and catches spend surprises, and Module 15 closes the domain and the course with compute and storage performance optimization.

## Further reading

- [Savings Plans](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html) and [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-reserved-instances.html) — commitment-based discounts.
- [AWS Compute Optimizer](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) — utilization-based rightsizing recommendations.
- [AWS Budgets](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) — threshold-based cost and usage alerts.
- [AWS Cost Anomaly Detection](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) — machine-learning-based spend anomaly alerts.
