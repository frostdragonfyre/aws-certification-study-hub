<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](04-implementing-scalability-and-elasticity.md) · [Next module](06-implementing-backup-and-restore-strategies.md) · [Quiz](../quizzes/05-implementing-high-availability-and-resilient-environments-quiz.md) · [Slides](../lectures/05-implementing-high-availability-and-resilient-environments.pptx)
<!-- /hub-navigation -->

# Module 5: Implementing High Availability and Resilient Environments

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Module 4 made sure Meridian's infrastructure has enough capacity when demand grows. This module asks a harder question: what happens when a piece of that capacity simply stops working? Task 2.2 is about surviving failure, not just load — a single instance, a single Availability Zone, even a whole AWS Region can go down, and Priya needs Meridian Loyalty, Café Sol, and Ridgeline Diner Co. to keep serving customers through all three.

## Learning objectives

By the end of this module, you should be able to:

- Explain what Multi-AZ deployments actually protect against, and what they don't
- Distinguish an RDS Multi-AZ standby from an Aurora Replica used for failover
- Describe how Route 53 health checks and DNS failover redirect traffic away from an unhealthy endpoint
- Explain what Elastic Load Balancing cross-zone load balancing changes about traffic distribution
- Design a resilient architecture for a stated availability requirement

---

## Multi-AZ: Surviving the Loss of a Data Center

An Availability Zone is a physically separate data center (or set of them) within a Region — separate power, separate networking, separate physical location, close enough for low-latency replication but far enough apart that one AZ's failure doesn't take out another. **Multi-AZ** deployment means running redundant resources across at least two of these AZs, so the failure of one doesn't take down the whole application.

For **Amazon RDS**, Multi-AZ works by maintaining a synchronous standby replica in a second AZ. That standby isn't available for read traffic — it exists purely for failover. If the primary fails, or during planned maintenance, RDS automatically fails over to the standby, updating the DNS endpoint so the application keeps using the same connection string without any manual intervention.

**Amazon Aurora** takes a related but different approach: Aurora storage is already replicated across three AZs automatically, and instead of a passive standby, Aurora typically uses **Aurora Replicas** — read replicas that can also serve read traffic day to day, with one promoted automatically to primary if the writer fails. The distinction matters for the exam: an RDS Multi-AZ standby does nothing but wait; an Aurora Replica is doing useful work (serving reads) right up until the moment it's needed for failover.

> ⚠️ **Exam trap:** Multi-AZ protects against the failure of a data center — power, networking, hardware in one AZ. It does **not** protect against a Region-wide event, and it does not, by itself, add read capacity the way a read replica does (an RDS standby can't serve reads at all). A scenario asking about surviving an entire Region going down needs cross-Region replication or a multi-Region architecture, not Multi-AZ alone.

## Route 53 Health Checks and DNS Failover

Multi-AZ handles failure inside a single database or a single load-balanced fleet. But what routes traffic away from an endpoint that's failed entirely — a whole Region, a whole application stack, not just one component of it?

**Route 53 health checks** monitor an endpoint — an IP address, a domain, or the status of a CloudWatch alarm — at a regular interval, and mark it healthy or unhealthy based on whether it responds correctly. Paired with a **failover routing policy**, Route 53 uses that health check to decide which record to return: it answers DNS queries with the primary endpoint's address as long as the primary is healthy, and automatically switches to returning the secondary endpoint's address the moment the primary's health check fails — no application code change, no manual DNS update.

This is the mechanism behind an active-passive multi-Region architecture: Ridgeline Diner Co.'s primary stack runs in one Region, a warm or cold standby sits in another, and Route 53 health checks decide, continuously and automatically, which one customers actually reach.

> ⚠️ **Exam trap:** Route 53 failover routing is a DNS-level mechanism — it changes which IP address a query resolves to, and clients only pick up the change once their cached DNS record expires (governed by the record's TTL). It doesn't fail over an in-progress connection, and a scenario emphasizing near-instant failover for existing connections is describing something below the DNS layer (like an ELB or a database endpoint failover), not Route 53 health checks by themselves.

## ELB Cross-Zone Load Balancing

Within a single Region, an Elastic Load Balancer already distributes traffic across the AZs it's configured for. **Cross-zone load balancing** changes what "distribute across AZs" actually means at the instance level: with it enabled, each load balancer node distributes traffic evenly across *all* registered targets in *all* enabled AZs, not just the targets in its own AZ.

Without cross-zone load balancing, if AZ A has 2 instances and AZ B has 8, each load balancer node still splits its share of traffic evenly across the AZs — meaning each of AZ A's 2 instances gets a much bigger slice of traffic than each of AZ B's 8 instances get individually. Cross-zone load balancing spreads that traffic evenly across all 10 instances regardless of which AZ they're in, avoiding the uneven-hotspot problem an imbalanced fleet would otherwise create.

> ⚠️ **Exam trap:** Application Load Balancers have cross-zone load balancing enabled by default and it can't be turned off at the load balancer level; Network Load Balancers have it disabled by default and it must be turned on explicitly (and it may carry a data transfer charge across AZs). A scenario describing uneven per-instance load with an NLB, where AZs have different instance counts, is very likely pointing at enabling cross-zone load balancing.

## Putting It Together: A Resilient Meridian Loyalty

Priya's resilience strategy for Meridian Loyalty layers all three mechanisms:

- **Aurora Multi-AZ** (Aurora Replicas across AZs) so a single AZ's database failure fails over automatically, with replicas already doing useful read work beforehand.
- **Cross-zone load balancing** on the Application Load Balancer in front of the checkout service, so traffic stays even across AZs even if Auto Scaling temporarily leaves one AZ with more instances than another.
- **Route 53 health checks and failover routing** watching the whole stack, ready to redirect traffic to a standby Region if something bigger than a single AZ ever goes wrong.

## What to skip

You don't need to memorize Route 53 health check configuration syntax or the exact cross-zone data transfer pricing — that's implementation depth beyond this exam. What matters is knowing what each mechanism actually protects against (AZ failure vs. Region failure vs. uneven traffic distribution) and matching the right one to the scenario's actual failure mode.

## Key takeaways

- Multi-AZ protects against the loss of a single data center; it does not protect against a Region-wide failure and, for RDS, the standby serves no read traffic.
- An RDS Multi-AZ standby is passive until failover; an Aurora Replica serves reads continuously and is promoted on failover — same goal, different mechanism.
- Route 53 health checks and DNS failover redirect traffic at the DNS layer, governed by record TTL — they don't fail over an existing connection instantly.
- Cross-zone load balancing spreads traffic evenly across all targets in all AZs, not just each AZ's own share; ALBs default to on, NLBs default to off.
- This is Domain 2's second task — surviving failure. Module 6 covers the third: recovering data after something goes wrong despite all of this.

## Further reading

- [High Availability (Multi-AZ) for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html) — synchronous standby and automatic failover.
- [Amazon Aurora High Availability](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraHighAvailability.html) — Aurora Replicas and automatic failover.
- [Route 53 Health Checks and DNS Failover](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html) — health checks paired with failover routing policy.
- [Cross-Zone Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/cross-zone-load-balancing.html) — even traffic distribution across all targets in all AZs.
