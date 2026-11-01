[Course index](../README.md) · [Read the paired lesson](../modules/04-implementing-scalability-and-elasticity.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 4 Knowledge Check**

Implementing Scalability and Elasticity · 20 questions · Practice — not graded

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

> Target tracking scaling requires manually defining every step adjustment amount.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which scaling approach fits a demand pattern that's known in advance, like a daily lunch-hour spike?

> **A.** Target tracking
> **B.** Step scaling
> **C.** Scheduled scaling
> **D.** Simple scaling only

**3. [Fill in the Blank] Easy**

> AWS ____________ ____________ ____________ extends target tracking and scheduled scaling to services like ECS tasks, DynamoDB capacity, and Aurora read replicas.

**4. [Multiple Choice] Easy**

> What does Aurora Auto Scaling add or remove based on load?

> **A.** EC2 instances
> **B.** Aurora Replicas
> **C.** VPC subnets
> **D.** IAM roles

**5. [True / False] Easy**

> Scheduled scaling and dynamic scaling can be used together on the same Auto Scaling group.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why is target tracking usually the right default for a workload with a fairly steady relationship between load and the chosen metric?

> **A.** It requires manually calculating every scaling adjustment
> **B.** It maintains a target metric value automatically, without needing step sizes defined by hand
> **C.** It only works for scheduled, predictable workloads
> **D.** It cannot be used with CPU utilization as a metric

**7. [Fill in the Blank] Moderate**

> ____________ scaling defines specific, different-sized capacity adjustments depending on how far a metric has breached its threshold.

**8. [Multiple Choice] Moderate**

> Why does Priya add scheduled scaling ahead of Meridian Loyalty's known daily spikes, instead of relying on target tracking alone?

> **A.** Target tracking cannot be used for customer-facing services
> **B.** Dynamic scaling reacts to a metric after it changes, so it's always a step behind a spike that's already predictable — scheduled scaling puts capacity in place beforehand
> **C.** Scheduled scaling is required for all Auto Scaling groups
> **D.** Target tracking only works for database workloads

**9. [True / False] Moderate**

> Step scaling can apply a different-sized capacity change depending on how large the threshold breach is.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A workload's demand is genuinely unpredictable — no known schedule, no reliable pattern. Which scaling approach fits?

> **A.** Scheduled scaling, since it handles all demand patterns
> **B.** Dynamic scaling (target tracking or step), since it reacts to the actual metric rather than a fixed time
> **C.** No scaling approach can handle unpredictable demand
> **D.** Manual scaling only, since automation cannot react to unpredictable load

**11. [Fill in the Blank] Moderate**

> Auto Scaling policies that react to a metric changing in real time, rather than a fixed schedule, are called ____________ scaling.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A scenario describes a workload that just needs to "keep average CPU utilization near 50%," with no mention of different responses to different breach sizes. Which policy fits best?

> **A.** Step scaling, since it's always more precise
> **B.** Target tracking — it's the simplest fit for maintaining a metric near a target value, and the scenario doesn't call for the granular control step scaling provides
> **C.** Scheduled scaling, since CPU utilization is always predictable
> **D.** Simple scaling, since it's the only option for CPU-based metrics

**13. [Scenario / Judgment] Hard**

> A workload needs a small capacity increase for a minor threshold breach, but a much larger increase if the breach is severe. Which policy fits, and why not target tracking?

> **A.** Target tracking, since it can define different step sizes for different breach magnitudes
> **B.** Step scaling — it explicitly defines different-sized responses to different-sized breaches, which target tracking's single target-value approach doesn't provide
> **C.** Scheduled scaling, since severity should always be handled on a fixed schedule
> **D.** Neither approach can handle varying breach severity

**14. [Scenario / Judgment] Hard**

> Priya wants Meridian Loyalty's Aurora cluster to add read replicas during the same lunch-hour spike that scales its EC2 fleet. What should she use?

> **A.** EC2 Auto Scaling, since it also manages database read replicas
> **B.** Aurora Auto Scaling, which adds and removes Aurora Replicas based on load using the same target tracking concept applied to database read capacity
> **C.** AWS Schema Conversion Tool, since it manages database scaling
> **D.** Nothing — Aurora clusters cannot scale read capacity automatically

**15. [Scenario / Judgment] Hard**

> A student argues that scheduled scaling and dynamic scaling are mutually exclusive — a workload must choose one or the other. What's the flaw?

> **A.** There is no flaw — only one scaling type can ever be active
> **B.** They can be layered together: scheduled scaling handles a known baseline pattern, while dynamic scaling handles unpredictable variation on top of that baseline, at the same time
> **C.** Dynamic scaling automatically disables any scheduled scaling action
> **D.** Scheduled scaling can only be used on databases, never on EC2 Auto Scaling groups

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Scaling is scaling — target tracking, step scaling, and scheduled scaling all just add more capacity, so it doesn't matter which one you pick." Correct this using this module's content.

> **A.** They're right — any of the three produces an identical outcome in every scenario
> **B.** They're different: target tracking maintains a metric automatically, step scaling defines different-sized responses to different-sized breaches, and scheduled scaling puts capacity in place ahead of a known pattern instead of reacting to a metric at all — matching the right one to the actual demand shape is the real skill, not simply "adding capacity"
> **C.** Step scaling and scheduled scaling are the same mechanism under two names
> **D.** Target tracking can only be used for scheduled, predictable workloads

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes using step scaling for every Auto Scaling group by default, arguing "more control is always better." Evaluate this using this module's content.

> **A.** Agree — step scaling should always be the default regardless of the workload
> **B.** Disagree — target tracking is the simpler, usually correct default for a workload with a steady relationship between load and the metric; reaching for step scaling's added configuration when it isn't needed is unnecessary complexity, not extra safety
> **C.** Disagree, but only because step scaling is technically incompatible with EC2 Auto Scaling groups
> **D.** Agree, since target tracking cannot be configured for CPU-based metrics

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why relying on target tracking alone — without scheduled scaling — would leave Meridian Loyalty's checkout service under-provisioned right as its known lunch-hour spike begins.

> **A.** Target tracking scales instantly, before any metric ever changes, so this scenario can't happen
> **B.** Target tracking is dynamic — it reacts only after the metric (like CPU) actually rises, so during the first minutes of a sudden, predictable spike, capacity is still catching up; scheduled scaling puts the needed capacity in place ahead of time, before the spike ever starts
> **C.** Target tracking cannot be used for customer-facing workloads at all
> **D.** Scheduled scaling and target tracking cannot coexist, so this comparison is invalid

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes scaling Meridian Loyalty's Aurora read capacity manually, checking a dashboard every hour and adjusting replica count by hand. Argue against this using this module's content.

> **A.** Agree — manual checks are always more reliable than automation
> **B.** Disagree — Aurora Auto Scaling already adds and removes Aurora Replicas automatically based on load, using the same target tracking concept as EC2; hourly manual checks would react far slower than an automated policy and require ongoing human effort for a problem Application Auto Scaling already solves
> **C.** Disagree, but only because Aurora Replicas cannot be added or removed at all
> **D.** Agree, since Aurora Auto Scaling only works with DynamoDB, not Aurora clusters

**20. [Scenario / Judgment] Very Hard**

> A student says: "Application Auto Scaling is just EC2 Auto Scaling with a different name." Evaluate this using this module's content.

> **A.** Agree — they are identical services under two names
> **B.** Disagree — Application Auto Scaling extends the same target tracking and scheduled scaling concepts to other services entirely, like ECS tasks, DynamoDB capacity, and Aurora read replicas, none of which are EC2 instances — the underlying concepts carry over, but the service and what it scales are different
> **C.** Disagree, but only because Application Auto Scaling cannot use target tracking
> **D.** Agree, since ECS, DynamoDB, and Aurora are all technically EC2 instances

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
