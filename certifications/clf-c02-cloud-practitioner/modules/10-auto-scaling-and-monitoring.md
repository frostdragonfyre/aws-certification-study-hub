# Module 10: Auto Scaling and Monitoring

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 3 — Cloud Technology and Services
**Estimated study time:** 45 minutes

## Why this matters

This is the last new-content module of Cloud Foundations, and it's a fitting place to end, because it's where three ideas that have been circling this whole course — spreading load across resources, watching what's actually happening, and adjusting capacity automatically — finally combine into one working system. Module 6 introduced Elastic Load Balancing and Auto Scaling briefly; Module 9 leaned on both as the practical expression of the Reliability pillar. Tonight is where each one gets its own real depth, plus the monitoring service that ties them together.

Three services, three jobs: **Elastic Load Balancing** distributes traffic, **Amazon CloudWatch** watches what's happening, and **Amazon EC2 Auto Scaling** adjusts capacity based on what CloudWatch sees. Used together, they're how a real production architecture handles changing demand without a human manually reacting to every spike and dip.

## Learning objectives

By the end of this module, you should be able to:

- Explain how Elastic Load Balancing distributes traffic across EC2 instances
- Explain how Amazon CloudWatch monitors AWS resources and applications in real time
- Explain how Amazon EC2 Auto Scaling launches and terminates instances in response to workload changes
- Describe how ELB, CloudWatch, and Auto Scaling work together as a dynamically scalable architecture
- Avoid the most common scaling and monitoring traps on the exam

---

## Elastic Load Balancing: Distributing Traffic

**Elastic Load Balancing (ELB)** automatically distributes incoming application traffic across multiple targets — EC2 instances, containers, or IP addresses — in one or more Availability Zones. A load balancer continuously runs **health checks** against its targets, and automatically stops sending traffic to any target that fails one, routing around unhealthy resources without any manual intervention.

AWS offers a few load balancer types for different traffic patterns, though for CLF-C02 the important thing is the concept, not the full feature comparison:

| Load balancer type | Best for |
|---|---|
| Application Load Balancer (ALB) | HTTP/HTTPS web traffic, routing based on content (like URL path) |
| Network Load Balancer (NLB) | Extreme performance, TCP/UDP traffic, static IP addresses |
| Gateway Load Balancer (GWLB) | Deploying and managing third-party virtual network appliances |

> ⚠️ **Exam trap:** ELB distributes traffic across *existing* capacity — it doesn't create or remove instances. If a scenario is about changing *how many* instances exist, that's Auto Scaling's job, covered below. ELB and Auto Scaling are named together constantly, but they solve two different problems.

## Amazon CloudWatch: Monitoring in Real Time

**Amazon CloudWatch** is AWS's monitoring service — it collects and tracks **metrics** (like CPU utilization, network traffic, or request counts), collects and stores **logs**, and lets you set **alarms** that trigger an action when a metric crosses a threshold you define. CloudWatch is how you actually *know* what's happening across your AWS resources and applications, in real time, instead of finding out from an angry customer.

The core building blocks:

- **Metrics** — numerical data points tracked over time (CPU utilization, request latency, error counts)
- **Alarms** — watch a metric and trigger an action (like a notification, or an Auto Scaling event) when it crosses a defined threshold
- **Dashboards** — customizable visual displays of metrics, useful for at-a-glance monitoring
- **Logs** — CloudWatch Logs centralizes log data from applications and AWS services for searching and analysis

> ⚠️ **Exam trap:** CloudWatch *observes and alerts* — it doesn't take direct action on its own beyond triggering something else (like an alarm notification or an Auto Scaling policy). A scenario asking "which service monitors CPU utilization and can trigger a scaling event when it gets too high" is really describing CloudWatch and Auto Scaling working together, not CloudWatch acting alone.

## Amazon EC2 Auto Scaling: Adjusting Capacity Automatically

**Amazon EC2 Auto Scaling** automatically launches or terminates EC2 instances to match actual demand, keeping an application available and performant while avoiding the cost of paying for idle, unused capacity. It's the practical answer to Module 9's "stop guessing your capacity needs" design principle.

Auto Scaling works through an **Auto Scaling group**, which you configure with:

- **Minimum capacity** — never scales below this number of instances
- **Desired capacity** — the target number of instances under normal conditions
- **Maximum capacity** — never scales above this number, capping cost

Auto Scaling groups typically respond to **CloudWatch alarms** — for example, an alarm that fires when average CPU utilization across the group exceeds 70% can trigger a **scaling policy** that launches additional instances. When demand drops, a corresponding policy can terminate instances back down toward the desired capacity.

> ⚠️ **Exam trap:** Auto Scaling changes *how many* instances exist; it doesn't distribute traffic between them. That's ELB's job. A scenario describing both — capacity that grows and shrinks, AND traffic spread evenly across whatever currently exists — is describing Auto Scaling and ELB working together, not one service doing both jobs.

## The Three Working Together: A Dynamically Scalable Architecture

Here's how the three services actually connect in a real architecture:

1. **CloudWatch** continuously watches metrics like CPU utilization across an EC2 fleet.
2. When a CloudWatch **alarm** crosses its threshold (say, average CPU above 70% for 5 minutes), it triggers an **Auto Scaling** policy.
3. **Auto Scaling** launches new instances into the **Auto Scaling group**, up to the configured maximum.
4. The new instances automatically register with the **Elastic Load Balancer**, which begins routing traffic to them once they pass health checks.
5. When demand drops, the same loop runs in reverse — CloudWatch detects low utilization, Auto Scaling terminates instances back toward the desired capacity, and ELB simply stops routing traffic to instances that are no longer there.

This loop is what "dynamically scalable architecture" actually means: no human watching a dashboard and manually launching instances at 2 AM during a traffic spike — the system reacts to real conditions on its own.

---

## What to skip

You don't need to write actual CloudWatch alarm thresholds, configure a real Auto Scaling policy's exact math, or compare every load balancer type's full feature set — that hands-on depth belongs to the Solutions Architect Associate exam. For Cloud Practitioner, focus on knowing what job each of the three services does, and recognizing when a scenario needs one, two, or all three together.

## Key takeaways

- Elastic Load Balancing distributes traffic across existing targets and routes around unhealthy ones via health checks — it does not change how many targets exist.
- Amazon CloudWatch monitors metrics, stores logs, and triggers alarms when thresholds are crossed — it observes and alerts, rather than directly resizing infrastructure itself.
- Amazon EC2 Auto Scaling launches and terminates instances to match demand, typically triggered by CloudWatch alarms, within a configured minimum/desired/maximum range.
- The three work together in a loop: CloudWatch watches, Auto Scaling adjusts capacity in response, and ELB spreads traffic across whatever capacity currently exists.
- This module completes AWS Academy Cloud Foundations — every Domain 3 service from Modules 3 through 10 has now been covered, and you're ready for CCP exam review.

## Further reading

- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/) — load balancer types and health check concepts.
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) — metrics, alarms, dashboards, and logs overview.
- [Amazon EC2 Auto Scaling](https://aws.amazon.com/ec2/autoscaling/) — Auto Scaling groups and scaling policy concepts.

*Service capabilities mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 9 — Cloud Architecture](09-cloud-architecture.md) · **Quiz:** [Module 10 Quiz](../quizzes/10-auto-scaling-and-monitoring-quiz.md) · **Activity:** [Module 10 Activity](../labs/10-auto-scaling-and-monitoring-activity.md)

**Foundations complete.** This is the last module in the sequence — see the [CCP Exam Review guide](../ccp-exam-review.md) for how the ten modules map to the exam's four domains, plus links to official AWS practice resources.
