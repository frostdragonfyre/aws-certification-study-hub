**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 10 Review Quiz**

Auto Scaling and Monitoring · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|
| | |

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

> Elastic Load Balancing can launch new EC2 instances when traffic increases.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service collects metrics, sets alarms, and builds dashboards for real-time monitoring?
>
> **A.** AWS Trusted Advisor
> **B.** Amazon CloudWatch
> **C.** Elastic Load Balancing
> **D.** EC2 Auto Scaling

**3. [Fill in the Blank] Easy**

> Amazon EC2 Auto Scaling launches and ____________ instances automatically to match demand.

**4. [Multiple Choice] Easy**

> Which ELB type is built for HTTP/HTTPS web traffic and can route based on content like URL path?
>
> **A.** Network Load Balancer
> **B.** Gateway Load Balancer
> **C.** Application Load Balancer
> **D.** Classic Load Balancer

**5. [True / False] Easy**

> Elastic Load Balancing stops sending traffic to a target that fails a health check.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which Auto Scaling group setting caps the number of instances that can ever run at once?
>
> **A.** Minimum capacity
> **B.** Desired capacity
> **C.** Maximum capacity
> **D.** Target capacity

**7. [Fill in the Blank] Moderate**

> A CloudWatch ____________ watches a metric and triggers an action when it crosses a defined threshold.

**8. [Multiple Choice] Moderate**

> Which load balancer type is built for extreme performance, TCP/UDP traffic, and static IP addresses?
>
> **A.** Application Load Balancer
> **B.** Network Load Balancer
> **C.** Gateway Load Balancer
> **D.** Classic Load Balancer

**9. [True / False] Moderate**

> Amazon CloudWatch can directly launch or terminate EC2 instances on its own, without any other service involved.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A Gateway Load Balancer is primarily used for which purpose?
>
> **A.** Routing HTTP traffic based on URL path
> **B.** Deploying and managing third-party virtual network appliances
> **C.** Storing static website content
> **D.** Running scheduled reports

**11. [Fill in the Blank] Moderate**

> CloudWatch ____________ centralizes log data from applications and AWS services for searching and analysis.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Average CPU utilization across an Auto Scaling group has been above 75% for 10 minutes, and an alarm attached to a scaling policy just fired. What happens next?
>
> **A.** Nothing, until a human manually approves it
> **B.** Auto Scaling launches additional instances
> **C.** ELB automatically increases its own capacity
> **D.** CloudWatch deletes the underperforming instances

**13. [Scenario / Judgment] Hard**

> Three of twelve instances behind a load balancer fail their health checks. What does ELB do?
>
> **A.** Sends equal traffic to all twelve instances anyway
> **B.** Stops sending traffic to the three unhealthy instances until they recover
> **C.** Terminates the three unhealthy instances
> **D.** Shuts down the entire load balancer

**14. [Scenario / Judgment] Hard**

> A team wants raw TCP traffic handled with the lowest possible latency and a static IP address. Which load balancer type fits best?
>
> **A.** Application Load Balancer
> **B.** Network Load Balancer
> **C.** Gateway Load Balancer
> **D.** None — load balancers can't provide static IP addresses

**15. [Scenario / Judgment] Hard**

> A CloudWatch alarm is configured to email the on-call engineer when disk space exceeds 90%. Will this alarm launch new capacity automatically?
>
> **A.** Yes, all CloudWatch alarms trigger Auto Scaling automatically
> **B.** No — this alarm's action is a notification, not a scaling policy, so a human still has to act
> **C.** Yes, but only for disk-related alarms
> **D.** No — CloudWatch alarms can never be attached to scaling policies

**16. [Scenario / Judgment] Hard**

> A company runs a fixed number of EC2 instances sized for its busiest historical day, all year round. What's the main downside of this approach?
>
> **A.** There is no downside — fixed capacity is always safer
> **B.** Idle, unused capacity most of the year, paid for regardless of actual demand
> **C.** Fixed capacity is more secure than dynamic scaling
> **D.** ELB cannot distribute traffic to a fixed number of instances

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Elastic Load Balancing and EC2 Auto Scaling do the same job, just with different names." What's the correct correction?
>
> **A.** They're right — the two terms are interchangeable
> **B.** ELB distributes traffic across whatever capacity currently exists; Auto Scaling changes how much capacity exists — two different jobs, almost always named together but never interchangeable
> **C.** Auto Scaling replaced ELB in a recent AWS update
> **D.** ELB only works after Auto Scaling has finished launching instances

**18. [Scenario / Judgment] Very Hard**

> A flash sale is expected to spike traffic 10x with no advance warning, and the company can't staff someone to watch a dashboard at 2 AM. Which combination of services solves this, and how?
>
> **A.** ELB alone — it will add capacity as traffic increases
> **B.** CloudWatch watches metrics, an alarm crossing its threshold triggers Auto Scaling to launch instances, and ELB distributes traffic across all healthy instances — three services, one automated loop
> **C.** Auto Scaling alone — it will automatically detect the traffic spike without any monitoring service
> **D.** Trusted Advisor — it directly manages traffic spikes in real time

**19. [Scenario / Judgment] Very Hard**

> CloudWatch metrics show request count per instance is high, but CPU utilization is normal. Is a CPU-based scaling policy guaranteed to catch this situation?
>
> **A.** Yes, high request count and high CPU always occur together
> **B.** Not necessarily — a scaling policy tied to CPU won't fire if CPU stays normal, even if another metric like request count signals real strain, which is why picking the right metric for a workload matters
> **C.** No — CloudWatch cannot track request count as a metric at all
> **D.** Yes, because ELB will automatically switch the alarm to a different metric

**20. [Scenario / Judgment] Very Hard**

> An Auto Scaling group scales out under load but new instances take a few minutes to fully start their application before they're ready for traffic. What keeps ELB from sending real users to an instance that isn't ready yet?
>
> **A.** Nothing — ELB sends traffic to every instance in the group immediately
> **B.** ELB's health checks withhold traffic from a new instance until it passes, protecting users from hitting a not-yet-ready server
> **C.** Auto Scaling delays launching the instance until it's fully ready
> **D.** CloudWatch blocks all traffic to the group until every instance is healthy

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
