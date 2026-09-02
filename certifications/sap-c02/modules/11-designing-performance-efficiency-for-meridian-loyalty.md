# Module 11: Designing Performance Efficiency for Meridian Loyalty

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 10 made sure Meridian Loyalty doesn't fall over under load. This module makes sure it's actually fast — for a guest opening the app from a hotel in another city, for the operations team pulling a reporting query in the middle of a busy evening, and for every request in between. This is Task 2.5: performance efficiency, the part of the exam that asks you to match the right resource to the right job, not just add more of everything.

## Learning objectives

By the end of this module, you should be able to:

- Match an EC2 instance family to a workload's actual resource profile, rather than defaulting to general purpose
- Explain the cost/performance trade-off Graviton processors offer for compatible workloads
- Choose between Amazon CloudFront and AWS Global Accelerator for a given performance requirement
- Explain how Aurora read replicas offload reporting queries from the transactional path
- Design a complete performance efficiency strategy for a stated new-solution scenario

---

## Choosing the Right Compute for Meridian Loyalty

Meridian Loyalty runs on EC2 instances behind its Auto Scaling groups from Module 10 — but which instance family those groups actually launch is its own decision, and the exam expects you to match the family to what the workload actually does, not reach for general purpose by default.

- **General purpose** instances balance compute, memory, and networking, fitting Meridian Loyalty's typical web and application tier — the day-to-day request handling that doesn't lean heavily toward one resource.
- **Compute optimized** instances favor CPU over memory, fitting workloads with genuinely CPU-bound processing — for Meridian Loyalty, that's the batch job that recalculates point-earning tiers across every guest overnight.
- **Memory optimized** instances favor RAM over CPU, fitting workloads that hold large datasets in memory — a use case Meridian Loyalty doesn't currently have, but would if it ever ran a large in-memory analytics job itself, rather than relying on a managed service for that.

Separately from family, **AWS Graviton** processors (available across several of these families) offer meaningfully better price-performance than comparable x86 instances for compatible workloads — Meridian Loyalty's application, built without dependencies on x86-only libraries, runs on Graviton at lower cost for the same performance.

> ⚠️ **Exam trap:** the exam expects you to read what a workload's bottleneck actually is — CPU-bound, memory-bound, or balanced — and match the instance family to that, not assume bigger and more expensive is automatically better. Running Meridian Loyalty's ordinary web tier on a memory-optimized instance wastes money on RAM the workload doesn't need.

## Getting Guests Close to Their Data

Meridian Loyalty's guests open the app from wherever they happen to be — a hotel guest checking Haven & Co. points from another city, a Café Sol regular checking in from home. Two AWS services get traffic closer to where it needs to go, and they solve different problems.

- **Amazon CloudFront** is a content delivery network that caches HTTP/HTTPS content — static assets, and cacheable API responses — at edge locations close to guests, reducing both latency and the load on Meridian Loyalty's origin servers.
- **AWS Global Accelerator** improves performance for traffic that reaches an application's actual origin every time — using AWS's global network and static anycast IP addresses to route each guest to the closest healthy endpoint, and failing over automatically if a Region becomes unhealthy. It works for TCP and UDP traffic generally, not just HTTP/HTTPS, and it's valuable specifically when content can't be cached (real-time API calls that must reach the live application).

For Meridian Loyalty: **CloudFront** fits the app's static assets and cacheable balance-check responses. **Global Accelerator** fits the guest portal's live, uncacheable API traffic — the actual point-redemption calls that must reach the origin every time, still benefiting from AWS's backbone network and automatic failover.

> ⚠️ **Exam trap:** "content can be cached" points to CloudFront. "Traffic must reach the actual application every time, and needs a static IP or non-HTTP protocol support" points to Global Accelerator. They aren't competing options for the same problem — a well-designed guest-facing architecture often uses both, for different parts of the traffic.

## Offloading Reporting from the Transactional Path

Module 10's ElastiCache handled a different problem — the same guest checking the same balance repeatedly during a spike. Meridian's operations team has a separate need: pulling reporting queries — points earned by brand this month, redemption trends — that scan large amounts of data and would compete with real guest transactions for the same database capacity if run directly against the primary.

**Aurora Read Replicas** solve this specifically: additional read-only copies of the database, kept current through Aurora's native replication, that reporting queries run against instead of the primary. The transactional path — guests earning and redeeming points — keeps its full capacity, undisturbed by a long-running analytical query someone on the operations team just kicked off.

This is a different tool from ElastiCache, solving a different problem: ElastiCache serves the same hot data to many repeated requests from memory; read replicas isolate a different *kind* of workload — analytical, not repeated-lookup — from competing with transactional traffic at all.

## Putting It Together: Meridian Loyalty's Performance Strategy

Sofía's complete performance efficiency design for Meridian Loyalty:

- **Instance families matched to actual workload**: general purpose for the web/application tier, compute optimized for the overnight tier-recalculation batch job, Graviton wherever compatibility allows for better price-performance.
- **CloudFront** caching static assets and cacheable balance-check responses at the edge, close to guests wherever they are.
- **Global Accelerator** routing live, uncacheable API traffic — actual point redemptions — to the closest healthy endpoint over AWS's backbone network.
- **Aurora Read Replicas** absorbing the operations team's reporting queries, keeping that analytical load off the transactional primary entirely.

## What to skip

You don't need to memorize every EC2 instance family's exact vCPU-to-memory ratio or CloudFront's full edge location list — that's implementation depth beyond this exam. What matters is matching an instance family to a workload's actual bottleneck, choosing between CloudFront and Global Accelerator based on whether traffic is cacheable, and recognizing when a reporting workload needs isolating from a transactional one.

## Key takeaways

- Instance family selection should follow the workload's actual bottleneck — CPU-bound, memory-bound, or balanced — not default to general purpose or over-provision reflexively.
- Graviton processors offer better price-performance than comparable x86 instances for compatible workloads, at no functional downside for those workloads.
- CloudFront fits cacheable content; Global Accelerator fits live, uncacheable traffic needing a static IP or non-HTTP protocol support — a well-designed architecture often uses both.
- Aurora Read Replicas isolate analytical/reporting workloads from the transactional primary, a different problem from ElastiCache's repeated-hot-read caching.
- Performance efficiency, like every Domain 2 decision so far, comes from matching the right tool to the actual workload characteristic — not adding more resources reflexively.

## Further reading

- [Amazon EC2 Instance Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) — general purpose, compute optimized, and memory optimized families.
- [AWS Graviton Processor](https://aws.amazon.com/ec2/graviton/) — price-performance for compatible workloads.
- [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) — edge caching for HTTP/HTTPS content.
- [AWS Global Accelerator Developer Guide](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) — static IPs and routing for live traffic.
- [Amazon Aurora Replicas](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.Replication.html) — offloading read traffic from the primary.
