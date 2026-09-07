**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Modules 1 & 2 Review Quiz**

Welcome to Cloud Architecting + Introducing Cloud Architecting · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|
| | |

*Instructions: Answer every question. Questions get harder as you go — the last several are exam-style judgment questions where more than one answer looks reasonable. For those, pick the BEST answer and be ready to defend it out loud.*

*Note: AWS Academy's own Module 1 has no formal knowledge check — it's an orientation module. This quiz reviews Module 1 alongside Module 2's official 10-question knowledge check content, expanded to our usual 20-question format.*

| **Question types** | **What to do** |
|---|---|
| Multiple Choice | Circle one letter. |
| True / False | Circle TRUE or FALSE. |
| Fill in the Blank | Write your answer on the line. |
| Scenario / Judgment | Circle the BEST answer. Note WHY the others fail. |

---

## Easy Questions

**1. [True / False] Easy**

> The challenge labs in this course are built around a single, running fictional business case rather than a new example every time.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which café staff member has some programming background and drives the family's interest in AWS?
>
> **A.** Frank
> **B.** Martha
> **C.** Sofía
> **D.** Nikhil

**3. [Fill in the Blank] Easy**

> AWS began selling its own internal fix for its architecture problems externally in the year ____________.

**4. [Multiple Choice] Easy**

> Which was the first AWS service Amazon launched externally, in 2006?
>
> **A.** Amazon EC2
> **B.** Amazon S3
> **C.** Amazon SQS
> **D.** Amazon RDS

**5. [True / False] Easy**

> A Region is made up of two or more Availability Zones.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which cloud computing role is described as a generalist who often manages a production environment directly?
>
> **A.** Developer
> **B.** IT leader
> **C.** IT professional
> **D.** Cloud architect

**7. [Fill in the Blank] Moderate**

> Regions launched before March 20, 2019 are enabled by ____________ on every account; newer Regions must be manually enabled.

**8. [Multiple Choice] Moderate**

> A workload needs single-digit-millisecond latency for real-time gaming, in a city with no nearby AWS Region. What's designed for exactly this?
>
> **A.** Regional edge caches
> **B.** Local Zones
> **C.** AWS GovCloud
> **D.** Availability Zones

**9. [True / False] Moderate**

> AWS automatically replicates your data to other Regions unless you opt out.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which best practice specifically protects against paying for permanent capacity sized for a rare demand peak?
>
> **A.** Design for failure
> **B.** Decouple components
> **C.** Implement elasticity
> **D.** Automate wherever possible

**11. [Fill in the Blank] Moderate**

> A system that meets its technical needs but ignores the actual business use case is ____________, not well-architected.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A team wants to evaluate whether a proposed design can recover from an Availability Zone failure. Which Well-Architected pillar are they really applying?
>
> **A.** Cost Optimization
> **B.** Reliability
> **C.** Performance Efficiency
> **D.** Operational Excellence

**13. [Scenario / Judgment] Hard**

> A company must keep certain customer data within a specific country by law. Which of the four Region-selection factors is driving this decision?
>
> **A.** Latency
> **B.** Price
> **C.** Compliance
> **D.** Service availability

**14. [Scenario / Judgment] Hard**

> An architect designs a system that's technically elegant, highly available, and secure — but costs far more than the business can ever justify. What went wrong?
>
> **A.** Nothing — technical excellence is the only thing that matters
> **B.** The design met the technical needs but ignored the business use case, so it isn't actually well-architected
> **C.** The Well-Architected Framework doesn't apply to cost-sensitive businesses
> **D.** This is a Security pillar failure, not a Cost Optimization one

**15. [Scenario / Judgment] Hard**

> A CloudFront request is served from a regional edge cache instead of an edge location. What does that most likely mean?
>
> **A.** The content is popular enough to stay permanently at every edge location
> **B.** The content isn't accessed frequently enough to remain cached at an edge location, so the regional edge cache absorbs it instead
> **C.** The edge location network is down
> **D.** Regional edge caches only serve traffic within a single Availability Zone

**16. [Scenario / Judgment] Hard**

> A student says: "the café's architecture evolves the same way this course is structured — one layer at a time, driven by a real, growing need." Is this a fair reading of Module 1's evolving café table?
>
> **A.** No — the café's architecture changes were random, unrelated to the course structure
> **B.** Yes — each version of the café's architecture (V1 through V7) was driven by a specific new business need, in roughly the order this course covers those same concepts
> **C.** No — the café's architecture only changed once, in V1
> **D.** Yes, but only because AWS requires all case studies to follow this pattern

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "the Well-Architected Framework's six pillars from CLF-C02 and the version used in this course are different frameworks." What's the correct correction?
>
> **A.** They're right — this course uses a completely different framework
> **B.** Same six pillars, same framework — what changes is how it's used: CLF-C02 taught you to recognize the names, this course teaches you to use it as an active evaluation tool on real designs
> **C.** This course only uses three of the six pillars
> **D.** The pillars were renamed for the Solutions Architect exam

**18. [Scenario / Judgment] Very Hard**

> A workload's data must never leave a specific country, must serve users with minimal latency in that same country, and depends on a fairly new AWS service. Which combination of factors is actually in play, and which one could override the others?
>
> **A.** Only latency matters; price and compliance are irrelevant
> **B.** Compliance, latency, and service availability are all in play — compliance can override the other two even if a closer or cheaper Region would otherwise be preferred
> **C.** Only service availability matters, since the service is new
> **D.** Price is always the deciding factor regardless of the other three

**19. [Scenario / Judgment] Very Hard**

> A team treats "best practices" as a fixed list of exactly ten AWS services to always use, regardless of the situation. What's the flaw in this approach?
>
> **A.** There's no flaw — best practices are always the same ten services
> **B.** Best practices are tested-at-scale patterns that protect against specific failure modes — the pattern matters more than any specific service, and the right service can change depending on the situation
> **C.** Best practices only apply to Amazon's own internal systems, not customer workloads
> **D.** AWS discourages the use of best practices outside of guided labs

**20. [Scenario / Judgment] Very Hard**

> Why did AWS's founding story (Amazon's own 2000s scaling struggle) matter enough to include in a course about cloud architecting, rather than just being interesting trivia?
>
> **A.** It's purely historical interest with no connection to the course content
> **B.** It's the origin case study for the entire discipline — the unplanned, siloed architecture that slowed Amazon down is the exact failure mode cloud architecting best practices, the Well-Architected Framework, and deliberate resource placement all exist to prevent
> **C.** It only matters for understanding AWS's pricing history
> **D.** It explains why AWS chose its Region names

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
