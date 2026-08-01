**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 10**

**Lab Worksheet — Auto Scaling and Monitoring**

Activity 1: Elastic Load Balancing Use Cases · Activity 2: Amazon CloudWatch Examples

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Elastic Load Balancing Use Cases (20 min)

### How this works

Below are eight real-shaped scenarios. For each one, decide what ELB concept from tonight's lecture applies — which load balancer type fits best, or whether the scenario is actually testing health checks or the ELB-vs-Auto-Scaling distinction instead. Work on your own first, then we'll build the review together on the board.

*This mirrors AWS Academy's own Elastic Load Balancing activity for this module — it's about matching real traffic patterns to the right concept, not just reciting definitions.*

### The scenarios

| # | Scenario | Load balancer type or ELB concept | Why (one sentence) |
|---|---|---|---|
| 1 | A web app receives HTTP traffic and needs requests routed to different backend services based on the URL path (`/images`, `/api`, `/checkout`). | | |
| 2 | A gaming company needs extremely low latency and a static IP address for millions of concurrent TCP connections. | | |
| 3 | Three of twelve EC2 instances behind a load balancer stop responding to health checks. | | |
| 4 | A security team wants to deploy a fleet of third-party firewall appliances that all inbound traffic must pass through first. | | |
| 5 | Traffic to an application doubles overnight, and the team assumes the load balancer will "add more capacity" to handle it. | | |
| 6 | An e-commerce site wants to route `/mobile` traffic to one set of instances and `/desktop` traffic to another, based on the request itself. | | |
| 7 | A finance company needs to handle a sudden burst of raw TCP traffic with the lowest possible latency, no HTTP-layer routing needed. | | |
| 8 | A new instance just launched by Auto Scaling hasn't passed its first health check yet. | | |

### Think about it

1. Scenario 5 describes a common misconception. What's actually wrong with the assumption in that scenario, and which service is really responsible for "adding more capacity"?
2. Scenario 8 — should the load balancer send traffic to that brand-new instance right away? Why or why not?
3. Pick one scenario above where an Application Load Balancer would be the wrong choice. Explain what's wrong with it, in your own words.

---

## Activity 2 — Amazon CloudWatch Examples (25 min)

### How this works

Work on your own. Below are sample CloudWatch-style metrics and alarms (written out, since we don't have live console access tonight). For each one, decide what CloudWatch is actually telling you, and whether it would plausibly trigger an Auto Scaling action. We'll go through the answers together as a class afterward.

*Same skill as the Trusted Advisor recommendations from Lecture 9: noticing which phrase is load-bearing is what the real exam question is testing.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the loop

| Step | What happens |
|---|---|
| Watch | CloudWatch collects a metric (CPU, request count, latency, etc.) |
| Trigger | A CloudWatch alarm fires when the metric crosses a defined threshold |
| Act | The alarm triggers an Auto Scaling policy — launch or terminate instances |
| Distribute | ELB routes traffic across whatever capacity currently exists, once new instances pass health checks |

### The examples

*Underline the deciding phrase in each example as you read it.*

| # | CloudWatch example | What's happening | Would this plausibly trigger Auto Scaling? |
|---|---|---|---|
| 1 | "Average CPU utilization across the Auto Scaling group has been above 75% for the last 10 minutes." | | |
| 2 | "A CloudWatch dashboard shows request latency has been flat and normal all week." | | |
| 3 | "A CloudWatch Logs search shows a spike in HTTP 500 errors in the last hour." | | |
| 4 | "Average CPU utilization across the group has dropped below 15% for the last 20 minutes." | | |
| 5 | "A CloudWatch alarm is configured to notify the on-call engineer by email when disk space exceeds 90%." | | |
| 6 | "Network traffic in has increased 8x in the last 5 minutes, with no alarm currently configured for it." | | |
| 7 | "A CloudWatch alarm fires when average CPU exceeds 70% for 5 minutes, and is attached to a scaling policy." | | |
| 8 | "CloudWatch metrics show request count per instance is high, but CPU utilization is normal." | | |

### Pick any two and go deeper

For two of the examples above, write out what you'd say to a client or manager explaining what's happening and what (if anything) should be done about it, in plain language (no jargon).

**Example #____ — plain-language explanation:**

**Example #____ — plain-language explanation:**

### The shortcut — write this down

**For ANY CloudWatch scenario on the exam, ask in this order:**

1. Is this describing a **metric being collected**? → CloudWatch is watching.
2. Is this describing **a threshold being crossed and an action firing**? → That's an alarm.
3. Does the action **change the number of running instances**? → That's Auto Scaling, triggered by the alarm.
4. Does the action **just notify a person**? → CloudWatch is alerting, not scaling — a human still has to act.
5. Is traffic being **spread across instances** rather than the instance count changing? → That's ELB, not CloudWatch or Auto Scaling at all.

*Notice the pattern: a metric alone is just CloudWatch watching. An alarm is CloudWatch plus a threshold. Only when that alarm is attached to a scaling policy does Auto Scaling actually act — a metric or alarm on its own never guarantees a scaling event happened.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Write one new CloudWatch metric-and-alarm example of your own that would plausibly trigger Auto Scaling, and one that plausibly wouldn't. |
| 2 | Explain in your own words why an alarm needs to be attached to a scaling policy before it can actually launch or terminate instances. |
| 3 | Pick one example from the list and explain which piece of tonight's toolkit — ELB, CloudWatch, or Auto Scaling — is NOT involved at all. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 10 + knowledge check (aim 80%+ first attempt), including the "Scale and Load Balance Your Architecture" lab |
| | Sketch the scaling loop from memory once, without looking at your notes: watch → trigger → act → distribute |
| | If you haven't scheduled your AWS Certified Cloud Practitioner exam yet, do it this week — Foundations is complete after tonight |
