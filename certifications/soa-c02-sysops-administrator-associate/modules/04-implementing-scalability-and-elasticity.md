# Module 4: Implementing Scalability and Elasticity

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Domain 1 kept Priya informed and gave her a way to fix what breaks. Domain 2 asks a different question: does Meridian's infrastructure survive its own success — and its own failures? This module opens Domain 2 with Task 2.1: matching the right scaling mechanism to the actual shape of demand, so capacity shows up exactly when it's needed and not a wasteful moment before or after.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish target tracking, step, and simple scaling policies, and match each to the scenario it fits
- Explain when scheduled scaling fits better than any dynamic policy
- Describe how Aurora Auto Scaling adds and removes read replicas based on load
- Explain how Application Auto Scaling extends the same scaling concepts beyond EC2
- Design a complete scaling strategy for a stated demand pattern

---

## Target Tracking vs. Step Scaling

An Auto Scaling policy decides how many instances exist, based on a metric — but there's more than one way to translate "the metric changed" into "add or remove this many instances."

**Target tracking scaling** is the simplest and most common approach: you set a target value for a metric — like keeping average CPU utilization at 50% — and Auto Scaling calculates and applies whatever adjustments keep the metric near that target, automatically, without you defining the actual step sizes. For most workloads with a fairly steady relationship between load and the chosen metric, target tracking is the right default.

**Step scaling** gives more granular control for workloads where a small breach and a large breach of the threshold genuinely call for different responses: it lets you define specific step adjustments — for example, add 2 instances if CPU is 10–20% over the threshold, but add 5 instances if it's more than 20% over. This fits a demand pattern where the *size* of the problem, not just its existence, should change the response.

> ⚠️ **Exam trap:** a scenario that just says "keep CPU near 50%" or "maintain a target metric value" is describing target tracking — the simplest fit, and usually the right answer unless the scenario specifically calls for different-sized responses to different-sized breaches. Reaching for step scaling by default, when target tracking would do the same job with less configuration, is a common wrong answer on the exam.

## Scheduled Scaling vs. Dynamic Scaling

Target tracking and step scaling are both **dynamic** — they react to a metric changing in real time. But not every scaling need is driven by something Auto Scaling has to detect first.

**Scheduled scaling** sets capacity changes for specific, known times — Meridian Loyalty's checkout service reliably sees a large, predictable spike every day at lunch and again in the evening, tied to when people actually shop, not to any metric Auto Scaling would need to react to after the fact. A scheduled scaling action that adds capacity ten minutes before that known spike, every day, means the capacity is already there when demand arrives — dynamic scaling reacting to the spike as it happens would always be playing catch-up.

Dynamic scaling remains the right fit for demand that isn't predictable on a schedule — a sudden press mention, an unpredictable batch of orders. The two aren't mutually exclusive: Priya runs scheduled scaling for Meridian Loyalty's known daily pattern, layered with target tracking to handle whatever unpredictable variation happens on top of that baseline.

> ⚠️ **Exam trap:** a scenario describing a demand pattern that's known in advance — a daily, weekly, or otherwise predictable schedule — is pointing at scheduled scaling, not a dynamic policy tuned to react faster. Dynamic scaling, however well-tuned, always reacts after a metric crosses a threshold; scheduled scaling has capacity in place before demand ever arrives.

## Scaling Beyond EC2

Auto Scaling for EC2 instances is the most familiar case, but the same scaling concepts apply well beyond it through **Application Auto Scaling**, which extends target tracking and scheduled scaling to services like Amazon ECS tasks, DynamoDB read/write capacity, and Aurora read replicas.

**Aurora Auto Scaling** specifically adds and removes **Aurora Replicas** based on load, using the same target tracking concept applied to a database's read capacity rather than a fleet of EC2 instances — Meridian Loyalty's Aurora cluster can scale its number of read replicas up during the same lunch-hour spike that scales its EC2 fleet, using the same underlying pattern in a different service.

## Putting It Together: Scaling Meridian Loyalty's Checkout Service

Priya's scaling strategy for the checkout service:

- **Scheduled scaling** adding baseline capacity ahead of the known daily lunch and evening spikes — capacity is in place before demand arrives, not reacting after.
- **Target tracking** layered on top, holding average CPU near a set target for whatever unpredictable variation happens beyond the known pattern.
- **Aurora Auto Scaling** adding read replicas to the backing database during the same predictable and unpredictable load, using the same target tracking concept applied to database read capacity.

## What to skip

You don't need to memorize the exact CloudWatch metric math behind target tracking or every Application Auto Scaling-supported service — that's implementation depth beyond this exam. What matters is matching target tracking vs. step scaling to the scenario, recognizing when scheduled scaling fits better than any dynamic policy, and knowing that the same scaling concepts extend beyond EC2 through Application Auto Scaling.

## Key takeaways

- Target tracking maintains a metric near a target value automatically; step scaling defines specific, different-sized responses to different-sized threshold breaches.
- Scheduled scaling fits a demand pattern that's known in advance; dynamic scaling (target tracking or step) reacts to a metric after it changes, which means it's always a step behind for predictable spikes.
- Scheduled and dynamic scaling aren't mutually exclusive — a known baseline pattern and unpredictable variation on top of it can both be handled at once.
- Application Auto Scaling extends the same target tracking and scheduled scaling concepts to services like ECS, DynamoDB, and Aurora read replicas, not just EC2.
- This is Domain 2's first task — capacity that matches demand. Module 5 covers the second: what happens when a piece of that capacity actually fails.

## Further reading

- [Target Tracking Scaling Policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-target-tracking.html) — maintaining a metric at a target value.
- [Step and Simple Scaling Policies](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-scaling-simple-step.html) — granular, breach-size-aware scaling.
- [Scheduled Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-scheduled-scaling.html) — capacity changes for known, predictable times.
- [Aurora Auto Scaling](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Integrating.AutoScaling.html) — adding and removing Aurora Replicas based on load.
