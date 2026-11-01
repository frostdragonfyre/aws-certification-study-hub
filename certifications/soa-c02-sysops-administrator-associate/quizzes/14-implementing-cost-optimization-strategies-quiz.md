[Course index](../README.md) · [Read the paired lesson](../modules/14-implementing-cost-optimization-strategies.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 14 Knowledge Check**

Implementing Cost Optimization Strategies · 20 questions · Practice — not graded

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

> Spot Instances are a good fit for workloads that cannot tolerate interruption.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which tool recommends specific rightsizing changes based on a resource's actual utilization metrics?

> **A.** Cost Explorer
> **B.** Compute Optimizer
> **C.** AWS Budgets
> **D.** Cost Anomaly Detection

**3. [Fill in the Blank] Easy**

> AWS ____________ alerts based on a dollar amount or percentage threshold that you define in advance.

**4. [Multiple Choice] Easy**

> Which tool uses machine learning to catch unusual spend patterns without a predefined threshold?

> **A.** AWS Budgets
> **B.** Cost Anomaly Detection
> **C.** Compute Optimizer
> **D.** Trusted Advisor

**5. [True / False] Easy**

> Savings Plans and Reserved Instances both require a commitment in exchange for a discount.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does a fault-tolerant, flexible batch processing job fit Spot Instances well?

> **A.** Spot Instances are never reclaimed by AWS
> **B.** The workload can tolerate AWS reclaiming the capacity with short notice, and gains the deepest discount of the three options in exchange
> **C.** Spot Instances require a 1- or 3-year commitment
> **D.** Spot Instances are only available for storage, not compute

**7. [Fill in the Blank] Moderate**

> Cost Explorer visualizes and forecasts ____________ trends by service, account, tag, or time period.

**8. [Multiple Choice] Moderate**

> A team wants to know where their AWS spend is trending over the last six months, broken down by service. What fits best?

> **A.** Compute Optimizer, since it analyzes utilization
> **B.** Cost Explorer, since it visualizes and forecasts spend trends
> **C.** Cost Anomaly Detection, since it uses machine learning
> **D.** Savings Plans, since they reduce spend directly

**9. [True / False] Moderate**

> Cost Anomaly Detection requires a predefined dollar threshold to trigger an alert.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> An EC2 instance has been consistently underutilized for months. What tool identifies a specific smaller instance type to switch to?

> **A.** AWS Budgets
> **B.** Compute Optimizer, using actual utilization metrics to recommend a rightsizing change
> **C.** Cost Anomaly Detection
> **D.** Cost Explorer alone, without Compute Optimizer

**11. [Fill in the Blank] Moderate**

> Savings Plans and Reserved Instances fit ____________, predictable, always-on usage that must not be interrupted.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Meridian Loyalty runs a steady baseline of compute that's expected to keep running regardless of demand fluctuations. What discount mechanism fits best?

> **A.** Spot Instances, for the deepest possible discount
> **B.** Savings Plans or Reserved Instances, since the usage is steady and predictable and must not be interrupted
> **C.** No discount mechanism applies to steady workloads
> **D.** Cost Anomaly Detection, since it manages spend automatically

**13. [Scenario / Judgment] Hard**

> Café Sol's nightly batch reporting job can restart from the beginning if interrupted, and cost is the primary concern. What fits best?

> **A.** Reserved Instances, for the commitment discount
> **B.** Spot Instances, since the workload tolerates interruption and gains the deepest discount as a result
> **C.** On-Demand Instances only, to avoid any risk
> **D.** Savings Plans, since they're the most flexible option

**14. [Scenario / Judgment] Hard**

> A team wants a specific recommendation for whether an over-provisioned RDS or EC2 resource should be downsized, based on real usage data. Which tool actually analyzes that utilization data?

> **A.** AWS Budgets
> **B.** Compute Optimizer, since it uses actual utilization metrics and machine learning to recommend rightsizing
> **C.** Cost Explorer, since it shows overall spend
> **D.** Cost Anomaly Detection, since it uses machine learning

**15. [Scenario / Judgment] Hard**

> Priya wants to catch an unexpected spend spike that's well under any budget threshold the team would have thought to set, simply because it doesn't match the normal spend pattern. What fits best?

> **A.** AWS Budgets, since it can be set to a very low threshold
> **B.** Cost Anomaly Detection, since it learns a normal pattern and alerts on unusual deviations without needing a predefined threshold
> **C.** Compute Optimizer, since it analyzes utilization
> **D.** Savings Plans, since they reduce overall spend

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Savings Plans, Reserved Instances, and Spot Instances all just save money, so it doesn't matter which one you pick." Correct this using this module's content.

> **A.** They're right — all three are fully interchangeable regardless of workload
> **B.** They're different: Savings Plans and RIs require a commitment and fit steady, uninterruptible usage, while Spot offers the deepest discount in exchange for AWS being able to reclaim capacity with short notice — picking Spot for a workload that can't tolerate interruption is a real risk, not just a suboptimal choice
> **C.** Spot Instances require the longest commitment of the three
> **D.** Reserved Instances can be reclaimed by AWS at any time, just like Spot

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes using Cost Explorer alone to get instance-level rightsizing recommendations, arguing "it shows all our spend, so it can tell us what to downsize." Evaluate this using this module's content.

> **A.** Agree — Cost Explorer's spend visualizations are the same as utilization-based rightsizing recommendations
> **B.** Disagree — Cost Explorer visualizes and forecasts spend trends, but it doesn't analyze a resource's actual utilization metrics the way Compute Optimizer does; a specific rightsizing recommendation needs Compute Optimizer's utilization-based analysis, not spend data alone
> **C.** Disagree, but only because Cost Explorer cannot show spend by service
> **D.** Agree, since Compute Optimizer and Cost Explorer are the same tool under different names

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Cost Anomaly Detection can catch a cost problem that AWS Budgets would miss.

> **A.** Cost Anomaly Detection is simply a more sensitive version of Budgets with a lower threshold
> **B.** Budgets only alerts when spend crosses a threshold you defined in advance; an unusual spend spike that stays under every threshold anyone thought to set can still be a real anomaly, and Cost Anomaly Detection's machine learning can flag it by comparing it to the normal historical pattern instead of a fixed number
> **C.** Budgets cannot be configured for percentage-based alerts, only dollar amounts
> **D.** Cost Anomaly Detection requires the same threshold configuration as Budgets, so there's no real difference

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that Spot Instances should be used for every workload because they're the cheapest option available. Argue against this using this module's content.

> **A.** Agree — cost should always be the only factor in instance purchasing decisions
> **B.** Disagree — Spot Instances can be reclaimed by AWS with short notice, so they only fit workloads that are fault-tolerant and flexible about interruption; a workload that must stay running, like a steady production database tier, needs Savings Plans, Reserved Instances, or On-Demand instead
> **C.** Disagree, but only because Spot Instances are more expensive than On-Demand
> **D.** Agree, since Spot Instances are never reclaimed once launched

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as Compute Optimizer shows no rightsizing recommendations, the account's costs are fully optimized and nothing else needs review." Evaluate this claim using this module's content.

> **A.** Agree — Compute Optimizer alone covers every cost optimization angle
> **B.** Disagree — Compute Optimizer only addresses whether individual resources are the right size for their utilization; it says nothing about whether the right discount mechanism (Savings Plans, RIs, or Spot) is being used, whether spend is trending in a concerning direction, or whether an unusual spend anomaly has occurred — those need Cost Explorer, Budgets, and Cost Anomaly Detection respectively
> **C.** Disagree, but only because Compute Optimizer cannot analyze EC2 instances
> **D.** Agree, since rightsizing is the only component of cost optimization that matters

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
