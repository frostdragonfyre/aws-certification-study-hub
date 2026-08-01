**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 9 Review Quiz**

Cloud Architecture · 20 questions · Practice — not graded

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

> The AWS Well-Architected Framework has six pillars.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which of these is NOT one of the six Well-Architected pillars?
>
> **A.** Security
> **B.** Reliability
> **C.** Scalability
> **D.** Sustainability

**3. [Fill in the Blank] Easy**

> The pillar focused on running and monitoring systems and continuously improving processes is ____________ Excellence.

**4. [Multiple Choice] Easy**

> Which AWS tool provides real-time guidance across five categories to help provision resources following best practices?
>
> **A.** AWS Config
> **B.** AWS Trusted Advisor
> **C.** Amazon CloudWatch
> **D.** The AWS Well-Architected Tool only

**5. [True / False] Easy**

> "Test systems at production scale" is one of the six Well-Architected pillars.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which general design principle is about using elasticity instead of over-provisioning for a peak that may never come?
>
> **A.** Drive architectures using data
> **B.** Stop guessing your capacity needs
> **C.** Improve through game days
> **D.** Allow for evolutionary architectures

**7. [Fill in the Blank] Moderate**

> Trusted Advisor's ____________ checks are available to every account for free; the full set requires a Business or Enterprise support plan.

**8. [Multiple Choice] Moderate**

> Which pillar is about the ability to recover from failure and meet demand?
>
> **A.** Performance Efficiency
> **B.** Reliability
> **C.** Cost Optimization
> **D.** Security

**9. [True / False] Moderate**

> High availability and disaster recovery cover the exact same scope of failure.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which design principle involves simulating real failures in production-like environments to find weaknesses before they cause real incidents?
>
> **A.** Drive architectures using data
> **B.** Automate to make architectural experimentation easier
> **C.** Improve through game days
> **D.** Test systems at production scale

**11. [Fill in the Blank] Moderate**

> Trusted Advisor's Fault Tolerance category most closely maps to the Well-Architected ____________ pillar.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A database has no Multi-AZ enabled. Is this a high-availability gap or a disaster-recovery gap?
>
> **A.** Disaster recovery
> **B.** High availability

**13. [Scenario / Judgment] Hard**

> An account is nearing its EC2 vCPU quota for a Region. Which Trusted Advisor category flags this?
>
> **A.** Cost Optimization
> **B.** Security
> **C.** Service Limits
> **D.** Fault Tolerance

**14. [Scenario / Judgment] Hard**

> A team wants to know if any security groups allow unrestricted access from the internet. Which Trusted Advisor category applies?
>
> **A.** Performance
> **B.** Security
> **C.** Fault Tolerance
> **D.** Cost Optimization

**15. [Scenario / Judgment] Hard**

> A company only ever optimizes for Cost Optimization and ignores the other five pillars. What's the risk?
>
> **A.** No risk — cost is always the top priority for every workload
> **B.** Other pillars like Reliability or Security may get silently neglected — a well-architected system balances trade-offs across all six pillars
> **C.** This is exactly what "well-architected" means
> **D.** The Well-Architected Framework doesn't apply to cost-focused companies

**16. [Scenario / Judgment] Hard**

> A team asks: "should we invest in full disaster recovery, multi-Region, for this workload?" What should decide the answer?
>
> **A.** Always yes — more redundancy is always better, regardless of cost
> **B.** Whether the workload can tolerate a Region-level event going unrecovered — DR is a deliberate, expensive step up from standard high availability
> **C.** Never — DR is unnecessary once multiple Availability Zones are in use
> **D.** Whether the company has a Business support plan

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "design principles and pillars are basically the same list, just worded differently." What's the correct correction?
>
> **A.** They're right — there's no real difference
> **B.** Pillars are WHAT a system should be good at (categories); design principles are HOW you design well (habits that cut across multiple pillars at once) — genuinely different kinds of lists
> **C.** Design principles replaced the pillars in a recent update
> **D.** Pillars only apply to the Reliability pillar

**18. [Scenario / Judgment] Very Hard**

> A Trusted Advisor scan flags: (1) an idle load balancer, (2) an RDS instance without Multi-AZ, and (3) MFA not enabled on root. In order, which categories match?
>
> **A.** Cost Optimization, Fault Tolerance, Security
> **B.** Security, Cost Optimization, Fault Tolerance
> **C.** Fault Tolerance, Security, Cost Optimization
> **D.** Performance, Security, Fault Tolerance

**19. [Scenario / Judgment] Very Hard**

> A company has multiple Availability Zones configured for its application, but has never tested what actually happens during a real AZ failure. Which design principle addresses this gap specifically?
>
> **A.** Stop guessing your capacity needs
> **B.** Improve through game days
> **C.** Drive architectures using data
> **D.** Allow for evolutionary architectures

**20. [Scenario / Judgment] Very Hard**

> Does every AWS account automatically get full Trusted Advisor checks across all five categories?
>
> **A.** Yes, always, for free, regardless of support plan
> **B.** No — core checks are free for all accounts, but full checks across all categories require a Business or Enterprise support plan
> **C.** Only Enterprise accounts get any Trusted Advisor access at all
> **D.** Trusted Advisor requires a separate paid subscription, unrelated to support plans

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
