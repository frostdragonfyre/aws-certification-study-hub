# Module 10: Implementing Monitoring, Elasticity, and High Availability

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 45 minutes

## Why this matters

CLF-C02 introduced CloudWatch, Elastic Load Balancing, and Auto Scaling at a conceptual level: what each one is, in a sentence. This module goes back to all three, but at the depth an architect actually needs — not "what is Auto Scaling" but "which scaling policy fits this traffic pattern, and how does a load balancer's health check actually decide an instance is unhealthy."

The business trigger is the café's V5 milestone: handle an expected traffic increase while staying highly available and resilient to failure, by adding a load balancer, implementing Auto Scaling on the EC2 instances, and distributing compute and database instances across two Availability Zones. Every piece of that sentence gets built out fully in this module. Frank and Martha's café has been featured in a local news segment, and Sofía is bracing for a traffic spike neither she nor the current single EC2 instance is ready for.

## Learning objectives

By the end of this module, you should be able to:

- Explain what CloudWatch actually monitors, and the difference between a metric and an alarm
- Describe how an Application Load Balancer distributes traffic and determines instance health
- Compare Auto Scaling's scaling policy types and match each to a traffic pattern
- Explain why Multi-AZ deployment is required for genuine high availability
- Diagnose a described availability or scaling problem using this module's concepts

---

## Amazon CloudWatch: Seeing What's Actually Happening

You can't scale, fail over, or fix what you can't see. **Amazon CloudWatch** is AWS's monitoring and observability service — it collects **metrics** (numeric data points over time, like CPU utilization or request count), **logs** (the actual output your application and AWS services produce), and lets you set **alarms** that watch a metric and trigger an action when it crosses a threshold you define.

The distinction worth being precise about: CloudWatch *observes and alerts* — it does not, by itself, scale anything or fail anything over. A CloudWatch alarm firing because CPU utilization crossed 70% doesn't launch a new EC2 instance on its own; it can, however, notify Auto Scaling to do exactly that. CloudWatch is the sensor; other services are what act on what it reports.

A few CloudWatch details the exam expects:

- **Standard metrics** (like EC2 CPU utilization) are collected automatically, no setup required, at 5-minute intervals by default; **detailed monitoring** drops that to 1-minute intervals, at additional cost.
- **CloudWatch Logs** centralizes log data from EC2, Lambda, and most other AWS services — useful for debugging after the fact, not just watching a live number.
- An **alarm** has three possible states: OK (within threshold), ALARM (threshold breached), and INSUFFICIENT_DATA (not enough data yet to evaluate) — a scenario mentioning an alarm that "hasn't triggered but also isn't reporting OK" is describing this third state.

## Elastic Load Balancing: Distributing the Traffic

A single EC2 instance is a single point of failure by definition — if it fails, or is simply too busy, every request aimed at it fails or slows down with it. **Elastic Load Balancing (ELB)** distributes incoming traffic across multiple targets, most commonly EC2 instances spread across multiple Availability Zones, so no single instance (or single AZ) is a single point of failure for the whole application.

AWS offers a few load balancer types, but for a typical web application like the café's, the one to know well is the **Application Load Balancer (ALB)** — it operates at the application layer (HTTP/HTTPS), can route based on the actual content of a request (like the URL path), and is the default choice for web traffic. (A Network Load Balancer operates lower in the stack, for extreme performance and static IP needs; recognize the name, but the ALB is this module's focus.)

### How an ALB actually decides where traffic goes

An ALB routes requests to a **target group** — a set of registered targets (typically EC2 instances) that the load balancer distributes traffic across. The mechanism that keeps this safe is the **health check**: the ALB periodically sends a request (commonly a simple HTTP GET to a defined path) to each registered target, and any target that fails enough consecutive health checks is marked unhealthy and automatically removed from rotation — no more traffic sent its way until it starts passing health checks again.

> ⚠️ **Exam trap:** an unhealthy target being removed from a load balancer's rotation is *automatic* and doesn't require Auto Scaling at all — the load balancer manages routing around a bad target on its own. Auto Scaling's separate job is deciding whether to launch a *replacement* instance, which is a related but distinct action.

## EC2 Auto Scaling: Adding and Removing Capacity

**EC2 Auto Scaling** automatically adjusts the number of running EC2 instances to match demand — adding instances when load increases, removing them when it drops, within a range you define. This is the mechanism that actually delivers **elasticity**: acquiring resources when needed, releasing them when not, so the café doesn't pay for capacity sized for a rare traffic spike around the clock.

An Auto Scaling group is defined with a **minimum**, **desired**, and **maximum** capacity, and a **launch template** describing exactly what a new instance should look like (AMI, instance type, security groups, and so on) when Auto Scaling needs to create one.

### Scaling policy types

How Auto Scaling actually decides *when* to add or remove capacity comes down to a choice of policy type, and the exam expects you to match each to the right situation:

| Policy type | How it works | Best for |
|---|---|---|
| Target tracking | You pick a metric and a target value (e.g., "keep average CPU at 50%"); Auto Scaling adjusts capacity automatically to hold that target | Most workloads — the simplest, most commonly recommended approach |
| Step scaling | You define specific scaling actions triggered by CloudWatch alarm thresholds, with different step sizes for different severity levels | Traffic patterns needing finer-grained control than a single target value |
| Scheduled scaling | Capacity changes at specific, known times | Predictable patterns — a lunch rush, a known marketing event, a recurring end-of-month spike |

For the café's news-segment traffic spike, target tracking on CPU utilization is the simplest, most defensible choice — the exact spike size and timing aren't known in advance, which rules out scheduled scaling, and there's no need yet for step scaling's finer-grained tiers.

> ⚠️ **Exam trap:** Auto Scaling and Elastic Load Balancing are frequently described together but are not the same service and do not do the same job. Auto Scaling adds and removes instances; ELB distributes traffic across whichever instances currently exist. They're commonly paired — a new instance Auto Scaling launches gets automatically registered with the load balancer's target group — but one doesn't replace the other, and a question testing "which service adds capacity" versus "which service distributes traffic" is testing this exact distinction.

## Multi-AZ: High Availability, Not Just More Capacity

Everything above can be built entirely within a single Availability Zone — and if that AZ fails, none of it matters. **High availability** means designing so a system keeps operating through the failure of a component, and for the café's V5 milestone, that means the load balancer's targets and the database itself both need to span at least two AZs, not just exist as multiple instances that all happen to be in the same one.

This connects directly back to Module 7: a subnet lives in exactly one AZ, so achieving this means the Auto Scaling group's instances launch across subnets in multiple AZs, and the ALB itself is configured to route to targets in each of them. For the database tier, RDS offers **Multi-AZ deployments** — a synchronous standby copy of the database in a second AZ, with automatic failover if the primary fails. It's worth being precise about what Multi-AZ *doesn't* do: it solves availability, not read scaling. A **read replica** is the separate RDS feature that offloads read traffic to additional copies — confusing Multi-AZ with read replicas is one of the most common mistakes on this exam, because both involve "another copy of the database," for two entirely different reasons.

## Putting It Together: The Café's V5 Architecture

With CloudWatch, an Application Load Balancer, EC2 Auto Scaling, and Multi-AZ RDS, the café's V5 architecture actually delivers what that milestone promised: an ALB spreads incoming traffic across EC2 instances in two AZs; a target-tracking Auto Scaling policy adds instances automatically as CloudWatch reports rising CPU utilization during the news-segment traffic spike, and removes them once it settles back down; and RDS Multi-AZ means a single database-layer AZ failure doesn't take the whole application down. No single instance, and no single AZ, is a single point of failure anymore.

## What to skip

You don't need to hand-calculate CloudWatch alarm evaluation periods, configure Network Load Balancer specifics, or memorize every Auto Scaling lifecycle hook — those are implementation depth past what the associate exam tests. What matters is the vocabulary (metric vs. alarm, target group vs. health check, the three scaling policy types, Multi-AZ vs. read replica) and matching a described scenario to the right concept.

## Key takeaways

- CloudWatch observes and alerts (metrics, logs, alarms); it doesn't scale or fail anything over by itself — it triggers other services that do.
- An Application Load Balancer distributes traffic to a target group and automatically routes around targets that fail their health checks.
- EC2 Auto Scaling adds and removes instances to match demand, using a minimum/desired/maximum capacity range and a launch template.
- Target tracking, step scaling, and scheduled scaling are three different Auto Scaling policy types, each fitting a different traffic pattern.
- High availability requires spanning at least two Availability Zones — for compute (Auto Scaling instances across AZs, behind an ALB) and for the database (RDS Multi-AZ).
- RDS Multi-AZ solves availability through automatic failover; it does not scale reads — that's what read replicas are for. Don't confuse the two.

## Further reading

- [Amazon CloudWatch User Guide](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) — metrics, alarms, and logs in full detail.
- [Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) — target groups and health checks in depth.
- [EC2 Auto Scaling User Guide](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) — all scaling policy types with configuration examples.

---

**Next:** [Module 11 — Automating Your Architecture](11-automating-your-architecture.md)
