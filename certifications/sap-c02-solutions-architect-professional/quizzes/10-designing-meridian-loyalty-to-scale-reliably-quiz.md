**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 10 Knowledge Check**

Designing Meridian Loyalty to Scale Reliably · 20 questions · Practice — not graded

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

> Elasticity specifically requires that scaling happen automatically, in both directions, in response to real demand.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which Auto Scaling policy type is the right fit for a "double points weekend" promotion whose exact start time Sofía already knows?
>
> **A.** Target tracking scaling
> **B.** Scheduled scaling
> **C.** Manual scaling only
> **D.** No scaling is needed for known events

**3. [Fill in the Blank] Easy**

> Amazon ____________ sits between the point-earning event source and the database writer, absorbing a burst into a rate the downstream system can sustain.

**4. [Multiple Choice] Easy**

> Which DynamoDB capacity mode is the safer starting point for a brand-new workload with no traffic history yet?
>
> **A.** Provisioned capacity with no Auto Scaling
> **B.** On-demand capacity mode
> **C.** Reserved capacity
> **D.** DynamoDB does not support variable capacity

**5. [True / False] Easy**

> A system that can only be resized manually by an engineer, with no automatic behavior, is elastic.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does Meridian Loyalty's design use both target tracking and scheduled scaling, rather than just one?

> **A.** Scheduled scaling handles known, calendar-driven spikes proactively, while target tracking handles organic, unpredictable fluctuation reactively — different traffic shapes need different policy types
> **B.** Target tracking is deprecated and scheduled scaling is its replacement
> **C.** AWS requires at least two scaling policies per Auto Scaling group
> **D.** Only scheduled scaling actually removes capacity when demand drops

**7. [Fill in the Blank] Moderate**

> Amazon ____________ sits in front of Aurora, serving hot guest-balance reads from memory instead of hitting the database for every check.

**8. [Multiple Choice] Moderate**

> What is the main trade-off of provisioned capacity with Auto Scaling compared to on-demand, for DynamoDB?

> **A.** It costs more per request but requires no capacity planning at all
> **B.** It costs less per request once traffic is predictable, but still reacts to a target metric, so a truly instantaneous extreme spike can outrun it
> **C.** It cannot be used with Auto Scaling at all
> **D.** It offers no cost advantage over on-demand under any circumstances

**9. [True / False] Moderate**

> SQS decoupling eliminates the underlying traffic spike entirely, rather than absorbing it into a sustainable rate.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Why is ElastiCache proportionally valuable during a campaign weekend specifically?

> **A.** Because campaign weekends generate mostly writes, not reads
> **B.** Because the same guest-balance data gets checked repeatedly by the same guests, exactly the access pattern a cache is built to absorb
> **C.** Because ElastiCache replaces the need for Aurora entirely
> **D.** Because caching only helps with DynamoDB, not Aurora

**11. [Fill in the Blank] Moderate**

> A system's ability to handle growth at all, by adding resources, is called ____________ — distinct from the ability to do so automatically in both directions.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A new solution's traffic fluctuates unpredictably day to day, with no known campaign schedule. Which Auto Scaling policy type fits best on its own?

> **A.** Scheduled scaling alone
> **B.** Target tracking scaling, reacting to real-time demand
> **C.** No scaling policy is needed
> **D.** Manual resizing performed by an engineer each morning

**13. [Scenario / Judgment] Hard**

> A reviewer proposes writing every point-earning event synchronously and directly to the database, arguing it's simpler than adding a queue. What risk does this introduce during a traffic spike?

> **A.** No risk — synchronous writes are always safer
> **B.** The database, and the guest-facing request itself, are exposed directly to the size of the spike, rather than having it absorbed into a sustainable rate by a queue
> **C.** SQS cannot be used with DynamoDB under any circumstances
> **D.** Synchronous writes are required for any AWS architecture

**14. [Scenario / Judgment] Hard**

> Meridian Loyalty's event table has now run for a year with well-understood, steady daily traffic and known campaign timing. What does this module's reasoning suggest reconsidering?

> **A.** Nothing — on-demand should be kept indefinitely regardless of traffic predictability
> **B.** Moving from on-demand to provisioned capacity with Auto Scaling, since traffic is now predictable enough to capture meaningfully lower per-request cost
> **C.** Removing Auto Scaling entirely once traffic is predictable
> **D.** Switching from DynamoDB to Aurora, since predictability makes NoSQL unnecessary

**15. [Scenario / Judgment] Hard**

> A student says an architecture that can theoretically handle 10x traffic, but requires an engineer to manually launch new instances, is "elastic." Correct this using this module's definitions.

> **A.** They're correct — any ability to handle more load counts as elastic
> **B.** That architecture is scalable, not elastic — elasticity specifically requires the scaling to happen automatically, in response to demand, including scaling back down, not through manual intervention
> **C.** Elasticity and scalability are the same thing, so the distinction doesn't matter
> **D.** Only DynamoDB-based architectures can be considered elastic

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student argues: "Module 8 already covered reliability, so this module is redundant." Correct this using this module's content and Module 8's.

> **A.** They're right — the two modules cover identical content
> **B.** Module 8 covered surviving a disaster — RTO/RPO, DR strategy, cross-Region replication; this module covers surviving success — scaling behavior under a traffic spike that isn't a disaster at all, a different reliability concern entirely
> **C.** Module 8 only applies to Café Sol, never to Meridian Loyalty
> **D.** This module replaces Module 8's content entirely

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since on-demand DynamoDB capacity requires no planning at all, it should always be used regardless of how predictable traffic becomes." Evaluate this using this module's content.

> **A.** Agree — on-demand should always be used regardless of traffic predictability
> **B.** Disagree — on-demand's simplicity is valuable for new or unpredictable workloads, but provisioned capacity with Auto Scaling costs meaningfully less per request once traffic is well understood; sticking with on-demand indefinitely leaves real cost savings on the table without a corresponding benefit
> **C.** Disagree, but only because on-demand doesn't actually support automatic scaling
> **D.** Agree, since provisioned capacity cannot use Auto Scaling under any circumstances

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Sofía uses scheduled scaling for Meridian Loyalty's known campaign weekends instead of relying on target tracking alone.

> **A.** Target tracking cannot be used for planned events under any circumstances
> **B.** Target tracking reacts to load only after it's already climbing, which can mean scrambling to catch up; scheduled scaling adds capacity proactively, minutes before a known campaign goes live, avoiding that reactive lag entirely for demand that's already predictable
> **C.** Scheduled scaling is required by AWS for every Auto Scaling group
> **D.** There is no meaningful difference between the two for known events

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping ElastiCache entirely, arguing Aurora can just be scaled up with a larger instance class during campaign weekends instead. Argue against this using this module's content.

> **A.** Agree — a larger instance class is always a better solution than caching
> **B.** Disagree — most of the read traffic during a campaign is the same guests repeatedly checking the same balance, exactly the pattern a cache absorbs from memory; scaling the database instance up addresses total capacity but still pays the cost of serving the same repeated reads from disk-backed storage rather than eliminating that redundant load
> **C.** Disagree, but only because Aurora cannot be resized under any circumstances
> **D.** Agree, since ElastiCache cannot be used alongside Aurora

**20. [Scenario / Judgment] Very Hard**

> A student says: "Elasticity, decoupling, and capacity mode are three separate, unrelated decisions." Evaluate this using this module's content.

> **A.** Agree — none of these decisions relate to each other in any way
> **B.** Disagree — all three are facets of the same underlying goal, handling variable demand without manual intervention or overpaying for idle capacity: elasticity governs the compute tier, SQS decoupling protects the write path from a spike, and DynamoDB's capacity mode governs how the data tier itself absorbs that same variability. They're one coherent scaling strategy, not three unrelated choices
> **C.** Disagree, but only because AWS bundles all three into a single service
> **D.** Agree, since compute, messaging, and data storage never interact in a real architecture

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
