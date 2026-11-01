[Course index](../README.md) · [Read the paired lesson](../modules/16-planning-for-disaster.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 16 Knowledge Check**

Planning for Disaster · 20 questions · Practice — not graded

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

> Recovery Time Objective (RTO) measures how long a system can be down before the business impact is unacceptable.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which DR strategy has nothing running in the secondary Region day-to-day, relying entirely on restoring from backups when disaster strikes?
>
> **A.** Pilot Light
> **B.** Backup and Restore
> **C.** Warm Standby
> **D.** Multi-Site Active/Active

**3. [Fill in the Blank] Easy**

> ____________ measures how much data, expressed as a window of time, an organization can afford to lose.

**4. [Multiple Choice] Easy**

> Which DR strategy runs the full environment simultaneously in both Regions, actively serving live traffic in each?
>
> **A.** Pilot Light
> **B.** Backup and Restore
> **C.** Warm Standby
> **D.** Multi-Site Active/Active

**5. [True / False] Easy**

> Multi-Site Active/Active is generally the cheapest of the four DR strategies.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which AWS service supports health checks and automatic failover routing between Regions?
>
> **A.** AWS Backup
> **B.** Amazon Route 53
> **C.** AWS CloudFormation
> **D.** AWS Systems Manager

**7. [Fill in the Blank] Moderate**

> In the Pilot Light strategy, a small core piece — commonly a database kept continuously in sync — stays "____________" while the rest of the environment is scaled down.

**8. [Multiple Choice] Moderate**

> What does AWS Backup centralize?
>
> **A.** DNS routing decisions
> **B.** Backup policies across multiple AWS services, including cross-Region copies
> **C.** CloudFormation stack updates
> **D.** Load balancer health checks

**9. [True / False] Moderate**

> A tighter RTO/RPO requirement generally costs more to achieve.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> In the Warm Standby strategy, what is running in the secondary Region?
>
> **A.** Nothing at all
> **B.** Only a replicated database, with no application tier
> **C.** A scaled-down but fully functional copy of the complete environment
> **D.** The full-capacity production environment

**11. [Fill in the Blank] Moderate**

> The DR strategy that sits between Pilot Light and Multi-Site Active/Active, running a scaled-down but functional copy of the environment continuously, is called ____________ ____________.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Frank says the café can tolerate being offline for at most 2 hours. Which metric is this describing?
>
> **A.** RPO
> **B.** RTO
> **C.** Both equally
> **D.** Neither

**13. [Scenario / Judgment] Hard**

> The café says it can afford to lose at most 15 minutes of order data in a disaster. Which metric is this describing?
>
> **A.** RPO
> **B.** RTO
> **C.** Both equally
> **D.** Neither

**14. [Scenario / Judgment] Hard**

> A scenario states: "We can be down for most of a day; minimize cost above all." What's the best-fit DR strategy?
>
> **A.** Multi-Site Active/Active
> **B.** Backup and Restore
> **C.** Warm Standby
> **D.** Pilot Light

**15. [Scenario / Judgment] Hard**

> A scenario states: "We cannot tolerate any real downtime at all; cost is not the primary concern." What's the best-fit DR strategy?
>
> **A.** Backup and Restore
> **B.** Pilot Light
> **C.** Multi-Site Active/Active
> **D.** None of these strategies can achieve near-zero RTO

**16. [Scenario / Judgment] Hard**

> A team picks Pilot Light for a system that needs to be back up within a few minutes, assuming Pilot Light is "close enough" to Warm Standby. What's the flaw in this choice?
>
> **A.** There is no flaw
> **B.** Pilot Light's RTO is tens of minutes, since the application and web tier aren't running and must be scaled up first — Warm Standby's already-running, scaled-down environment recovers meaningfully faster
> **C.** Pilot Light and Warm Standby are functionally identical
> **D.** Warm Standby is always cheaper than Pilot Light

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "RTO and RPO both measure downtime, just in different words." Correct this using this module's content.
>
> **A.** They're right — the two terms are redundant
> **B.** RTO measures downtime — how long until systems are back up; RPO measures data loss as a window of time — how much data since the last good backup or replica is acceptable to lose. They measure genuinely different things
> **C.** RPO measures downtime and RTO measures data loss — the opposite of what most people assume
> **D.** Both terms actually measure cost, not time

**18. [Scenario / Judgment] Very Hard**

> Connect this module to Module 11. CloudFormation templates support deploying the same stack to a second Region. How does that connect to this module's DR strategies?
>
> **A.** There is no connection between the two modules
> **B.** The same template that captures the café's architecture (Module 11) is exactly what stands up infrastructure in the secondary Region for Pilot Light, Warm Standby, or Backup and Restore, without re-clicking months of console configuration during an actual disaster
> **C.** CloudFormation is only relevant to the Multi-Site Active/Active strategy
> **D.** CloudFormation templates cannot be deployed to a second Region

**19. [Scenario / Judgment] Very Hard**

> A team believes Route 53 failover happens instantly with zero configuration required, simply because a secondary Region exists. What's missing from this understanding?
>
> **A.** Nothing is missing — this is accurate
> **B.** Route 53 requires health checks configured against the primary endpoint and failover routing set up in advance — it doesn't automatically discover that a secondary Region exists or should receive traffic without that configuration
> **C.** Route 53 only operates within a single Region and cannot support failover at all
> **D.** Failover always requires a manual DNS change no matter how Route 53 is configured

**20. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Every workload should use Multi-Site Active/Active, since it has the best RTO/RPO." Argue against this using this module's content.
>
> **A.** Agree — Multi-Site Active/Active is always the correct choice
> **B.** The right strategy is determined by the actual stated business RTO/RPO requirement, not by defaulting to the fastest and most expensive option — a workload that can tolerate hours of downtime doesn't need to pay for full active/active capacity running in two Regions at all times
> **C.** Multi-Site Active/Active is actually the cheapest of the four strategies
> **D.** RTO/RPO requirements are irrelevant to choosing a DR strategy

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
