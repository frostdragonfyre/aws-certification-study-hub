**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 5 Knowledge Check**

Implementing High Availability and Resilient Environments · 20 questions · Practice — not graded

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

> An RDS Multi-AZ standby replica can serve read traffic during normal operation.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What does an Availability Zone represent within an AWS Region?

> **A.** A single server rack
> **B.** A physically separate data center (or set of them) with its own power and networking
> **C.** A separate AWS Region entirely
> **D.** A single customer account

**3. [Fill in the Blank] Easy**

> Route 53 ____________ ____________ monitor an endpoint's status and mark it healthy or unhealthy.

**4. [Multiple Choice] Easy**

> Which load balancer type has cross-zone load balancing enabled by default?

> **A.** Network Load Balancer
> **B.** Application Load Balancer
> **C.** Neither has it enabled by default
> **D.** Both require manual configuration with no default

**5. [True / False] Easy**

> Multi-AZ deployment alone protects against an entire AWS Region going down.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What is used to promote a replacement primary automatically when an Aurora writer instance fails?

> **A.** A manually triggered snapshot restore
> **B.** An Aurora Replica, promoted automatically
> **C.** A Route 53 health check
> **D.** A CloudFormation stack update

**7. [Fill in the Blank] Moderate**

> ____________-____________ load balancing distributes traffic evenly across all registered targets in all enabled Availability Zones, not just each zone's own share.

**8. [Multiple Choice] Moderate**

> Why can't Route 53 DNS failover redirect an already-established, in-progress connection instantly?

> **A.** Route 53 health checks are always disabled by default
> **B.** DNS failover changes what address a query resolves to, but clients keep using a cached record until its TTL expires
> **C.** Route 53 cannot be paired with a failover routing policy
> **D.** Route 53 only operates within a single Availability Zone

**9. [True / False] Moderate**

> Without cross-zone load balancing, an NLB node still splits its share of traffic evenly across AZs, regardless of how many targets are actually in each AZ.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A workload has 2 instances in AZ A and 8 in AZ B, behind an NLB with cross-zone load balancing disabled. What happens?

> **A.** Traffic is distributed evenly across all 10 instances regardless of AZ
> **B.** Each of AZ A's 2 instances receives a larger individual share of traffic than each of AZ B's 8 instances
> **C.** AZ B receives no traffic at all
> **D.** The NLB refuses to route traffic until the AZs are balanced

**11. [Fill in the Blank] Moderate**

> An RDS Multi-AZ standby is ____________ until failover; an Aurora Replica serves read traffic continuously beforehand.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A scenario asks how to survive the complete loss of one AWS Region, with a standby stack ready in a second Region. Which mechanism decides which Region's endpoint customers actually reach?

> **A.** ELB cross-zone load balancing
> **B.** Route 53 health checks paired with a failover routing policy
> **C.** RDS Multi-AZ alone
> **D.** Aurora storage replication alone

**13. [Scenario / Judgment] Hard**

> A student claims RDS Multi-AZ and an Aurora Replica-based failover work identically because both involve a second AZ. What's the key difference?

> **A.** There is no difference — they are the same mechanism
> **B.** An RDS Multi-AZ standby does nothing but wait for failover; an Aurora Replica serves read traffic continuously and is promoted only when needed
> **C.** Aurora cannot fail over automatically at all
> **D.** RDS Multi-AZ standbys always serve read traffic, unlike Aurora Replicas

**14. [Scenario / Judgment] Hard**

> An NLB serves a fleet with an uneven number of instances per AZ, and monitoring shows some instances receiving disproportionately more traffic than others. What's the most likely fix?

> **A.** Switch to Route 53 failover routing
> **B.** Enable cross-zone load balancing, since NLBs default to it being off
> **C.** Add an RDS Multi-AZ standby
> **D.** Nothing can be done — NLBs cannot distribute traffic evenly

**15. [Scenario / Judgment] Hard**

> Priya wants Meridian Loyalty's checkout service to keep working if one entire AZ's compute fails, without losing any in-flight database reads capacity. Which combination fits best?

> **A.** RDS Multi-AZ standby alone, since it always serves reads
> **B.** Aurora Replicas across AZs (serving reads continuously, promotable on failure) paired with an ALB or cross-zone-enabled NLB across those same AZs
> **C.** Route 53 health checks alone, since DNS failover happens instantly for any connection type
> **D.** A single-AZ deployment with frequent manual snapshots

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Multi-AZ, Route 53 failover, and cross-zone load balancing are basically interchangeable — pick any one and you're covered against any failure." Correct this using this module's content.

> **A.** They're right — any one mechanism covers every failure scenario
> **B.** They're not interchangeable: Multi-AZ protects against losing a data center, Route 53 failover protects against losing an entire endpoint or Region (at the DNS layer, subject to TTL), and cross-zone load balancing fixes uneven traffic distribution across AZs — each addresses a different failure mode
> **C.** Only Route 53 failover matters; the other two are redundant
> **D.** Cross-zone load balancing replaces the need for Multi-AZ entirely

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues that since Route 53 failover "automatically" redirects traffic, it makes existing in-progress user sessions seamless during a failover event. Evaluate this using this module's content.

> **A.** Agree — Route 53 failover is always instant for every connection
> **B.** Disagree — Route 53 failover changes what a *new* DNS query resolves to; clients holding a cached record continue using it until the TTL expires, so existing connections aren't seamlessly redirected by DNS failover alone
> **C.** Disagree, but only because Route 53 cannot use health checks
> **D.** Agree, since failover routing bypasses DNS caching entirely by design

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a scenario emphasizing "the database needs to keep serving reads even during the replica that will handle failover" points toward Aurora rather than a standard RDS Multi-AZ standby.

> **A.** RDS Multi-AZ standbys can also serve reads, so there's no real distinction
> **B.** An RDS Multi-AZ standby serves no read traffic at all — it exists purely for failover — while an Aurora Replica serves reads continuously and is simply promoted on failure, so a requirement for the failover target to already be doing useful read work points to Aurora
> **C.** Aurora cannot be used with Multi-AZ concepts at all
> **D.** RDS Multi-AZ is strictly newer technology and always the better choice

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping cross-zone load balancing entirely, arguing "Auto Scaling always keeps every AZ perfectly balanced, so it's unnecessary." Argue against this using this module's content.

> **A.** Agree — Auto Scaling guarantees perfectly even instance counts across AZs at all times
> **B.** Disagree — Auto Scaling doesn't guarantee AZs stay perfectly even at every moment (a scale-in, an AZ issue, or timing can leave counts uneven), and without cross-zone load balancing an NLB still splits its share evenly per AZ regardless of actual instance count, creating per-instance hotspots when counts diverge
> **C.** Disagree, but only because cross-zone load balancing is required by AWS for all load balancers
> **D.** Agree, since ALBs and NLBs both default to cross-zone load balancing disabled

**20. [Scenario / Judgment] Very Hard**

> A student says: "If I enable Multi-AZ, add cross-zone load balancing, and set up Route 53 failover, my application literally cannot go down." Evaluate this claim using this module's content.

> **A.** Agree completely — this combination guarantees zero downtime under every possible failure
> **B.** Disagree — these mechanisms each reduce a specific class of failure risk (single-AZ loss, uneven traffic distribution, endpoint/Region-level loss) but none of them, together or alone, is presented in this module as an absolute guarantee against every possible failure mode
> **C.** Disagree, but only because Route 53 failover cannot be combined with Multi-AZ
> **D.** Agree, but only if cross-zone load balancing is disabled instead of enabled

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
