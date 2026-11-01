[Course index](../README.md) · [Read the paired lesson](../modules/10-implementing-monitoring-elasticity-and-high-availability.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 10 Knowledge Check**

Implementing Monitoring, Elasticity, and High Availability · 20 questions · Practice — not graded

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

> CloudWatch can trigger other services to act, but it does not scale or fail anything over by itself.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS component periodically checks whether a registered EC2 instance is healthy, and removes it from rotation if it fails?
>
> **A.** CloudWatch alarm
> **B.** Load balancer health check
> **C.** Auto Scaling launch template
> **D.** RDS read replica

**3. [Fill in the Blank] Easy**

> An Auto Scaling group is defined with a minimum, desired, and ____________ capacity.

**4. [Multiple Choice] Easy**

> Which RDS feature provides a synchronous standby copy of a database in a second Availability Zone with automatic failover?
>
> **A.** Read replica
> **B.** Multi-AZ deployment
> **C.** Auto Scaling
> **D.** CloudWatch Logs

**5. [True / False] Easy**

> A single EC2 instance, with no load balancer or Auto Scaling, is a single point of failure.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which Auto Scaling policy type is best for a known, predictable event like a recurring lunch-hour traffic pattern?
>
> **A.** Target tracking
> **B.** Step scaling
> **C.** Scheduled scaling
> **D.** Manual scaling

**7. [Fill in the Blank] Moderate**

> An RDS ____________ offloads read traffic to additional database copies, and is a different feature from Multi-AZ.

**8. [Multiple Choice] Moderate**

> An Auto Scaling target tracking policy is set to keep average CPU utilization at 50%. What does Auto Scaling do as CPU rises above 50%?
>
> **A.** Nothing — target tracking only monitors, it doesn't act
> **B.** Automatically adds capacity to bring average CPU back toward the target
> **C.** Automatically removes capacity
> **D.** Sends an email but takes no automated action

**9. [True / False] Moderate**

> RDS Multi-AZ is primarily a solution for scaling read traffic across more database copies.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does an Auto Scaling launch template define?
>
> **A.** The load balancer's health check path
> **B.** What a new EC2 instance should look like when Auto Scaling creates one — AMI, instance type, security groups, etc.
> **C.** The CloudWatch alarm threshold
> **D.** The RDS failover schedule

**11. [Fill in the Blank] Moderate**

> An Application Load Balancer routes requests to targets registered in a ____________ group.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> The café expects a one-time traffic spike from a local news segment airing at an unknown, unannounced time. Which Auto Scaling policy type fits best?
>
> **A.** Scheduled scaling, since the event is known in advance
> **B.** Target tracking, since the exact timing and size of the spike aren't known in advance
> **C.** No scaling policy is needed, since Auto Scaling only supports scheduled events
> **D.** Step scaling is the only option that supports unpredictable events
>
**13. [Scenario / Judgment] Hard**

> A team believes that adding a load balancer alone makes their application highly available. What's missing from this reasoning?
>
> **A.** Nothing — a load balancer alone is sufficient for high availability
> **B.** If every target behind the load balancer is still in a single Availability Zone, an AZ failure takes down the whole application regardless of the load balancer
> **C.** Load balancers automatically span every AZ in a Region with no configuration needed
> **D.** High availability only applies to the database layer, not compute

**14. [Scenario / Judgment] Hard**

> An EC2 instance behind an ALB starts failing its health checks. What happens next, assuming no Auto Scaling group is involved?
>
> **A.** The ALB automatically terminates the instance
> **B.** The ALB stops routing traffic to that instance until it passes health checks again — no new instance is launched
> **C.** Nothing happens until a human manually intervenes
> **D.** The ALB automatically replaces the instance with a new one

**15. [Scenario / Judgment] Hard**

> A team wants finer-grained control than a single target value — different scaling actions for different severity thresholds (e.g., add 1 instance at 60% CPU, add 3 at 85% CPU). Which policy type fits?
>
> **A.** Target tracking
> **B.** Step scaling
> **C.** Scheduled scaling
> **D.** This isn't possible with EC2 Auto Scaling

**16. [Scenario / Judgment] Hard**

> A CloudWatch alarm shows a state of INSUFFICIENT_DATA rather than OK or ALARM. What does this mean?
>
> **A.** The alarm has definitively failed and needs to be recreated
> **B.** The metric's threshold has been breached
> **C.** There isn't yet enough data for the alarm to evaluate its condition
> **D.** The associated resource has been deleted

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Auto Scaling and Elastic Load Balancing are basically the same service since they're always used together." Correct this using this module's content.
>
> **A.** They're right — the two are functionally identical
> **B.** They're commonly paired but do different jobs: Auto Scaling adds and removes instances to match demand, while ELB distributes traffic across whichever instances currently exist — a new Auto Scaling instance gets registered with the load balancer's target group, but neither service replaces the other
> **C.** Elastic Load Balancing replaced Auto Scaling and it's now deprecated
> **D.** Auto Scaling only works if Elastic Load Balancing is disabled

**18. [Scenario / Judgment] Very Hard**

> A design uses RDS Multi-AZ and reports that read-heavy query performance hasn't improved at all. What's the correct diagnosis?
>
> **A.** Multi-AZ is broken and should be reconfigured
> **B.** Multi-AZ solves availability through failover, not read scaling — a read replica is the correct feature for improving read-heavy query performance, and the two are not interchangeable
> **C.** RDS doesn't support performance improvements under any configuration
> **D.** Multi-AZ automatically improves read performance after 24 hours

**19. [Scenario / Judgment] Very Hard**

> Connect this module to Module 7. Why does achieving true high availability for the café's compute layer require more than just "run more EC2 instances"?
>
> **A.** More instances alone is always sufficient for high availability
> **B.** Because a subnet lives in exactly one Availability Zone (Module 7), running many instances that are all still in the same AZ's subnet doesn't protect against that AZ failing — the instances (and the subnets they launch into) must actually span multiple AZs for the redundancy to be real
> **C.** High availability has nothing to do with subnets or Availability Zones
> **D.** Running more instances always automatically distributes them across AZs

**20. [Scenario / Judgment] Very Hard**

> Walk through why CloudWatch, ELB, and Auto Scaling are described in this module as three separate services working together rather than one combined feature. What would be lost by treating them as interchangeable?
>
> **A.** Nothing would be lost — they're functionally identical
> **B.** Each has a distinct job — CloudWatch observes and alerts, ELB distributes traffic and removes unhealthy targets from rotation, Auto Scaling adds/removes capacity based on demand — treating them as interchangeable would obscure which one to reach for when diagnosing a specific symptom, which is exactly how the exam tests this module
> **C.** They are actually the same underlying service with three different names
> **D.** Only Auto Scaling matters; the other two are optional add-ons with no real function

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
