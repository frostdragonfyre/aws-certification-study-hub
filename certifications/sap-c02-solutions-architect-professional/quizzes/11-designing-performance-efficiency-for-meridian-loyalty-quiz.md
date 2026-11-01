[Course index](../README.md) · [Read the paired lesson](../modules/11-designing-performance-efficiency-for-meridian-loyalty.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 11 Knowledge Check**

Designing Performance Efficiency for Meridian Loyalty · 20 questions · Practice — not graded

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

> Instance family selection should follow a workload's actual resource bottleneck, not default to general purpose reflexively.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which instance family fits Meridian Loyalty's overnight, CPU-bound tier-recalculation batch job?
>
> **A.** General purpose
> **B.** Compute optimized
> **C.** Memory optimized
> **D.** Storage optimized

**3. [Fill in the Blank] Easy**

> AWS ____________ processors offer meaningfully better price-performance than comparable x86 instances for compatible workloads.

**4. [Multiple Choice] Easy**

> Which service caches HTTP/HTTPS content at edge locations close to guests?
>
> **A.** AWS Global Accelerator
> **B.** Amazon CloudFront
> **C.** Amazon Aurora
> **D.** AWS Auto Scaling

**5. [True / False] Easy**

> Aurora Read Replicas and Amazon ElastiCache solve the exact same problem in the exact same way.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does running Meridian Loyalty's ordinary web tier on a memory-optimized instance waste money?

> **A.** Memory-optimized instances cannot run web applications at all
> **B.** The web tier's typical request handling doesn't lean heavily on RAM, so the extra memory capacity goes unused while still being paid for
> **C.** Memory-optimized instances are always slower than general purpose
> **D.** AWS prohibits running web tiers on memory-optimized instances

**7. [Fill in the Blank] Moderate**

> Amazon Aurora ____________ ____________ are additional read-only copies of the database that reporting queries run against instead of the primary.

**8. [Multiple Choice] Moderate**

> Which service is the right fit for Meridian Loyalty's live, uncacheable point-redemption API calls that must reach the origin every time?

> **A.** Amazon CloudFront alone
> **B.** AWS Global Accelerator
> **C.** Amazon S3 Transfer Acceleration
> **D.** AWS Auto Scaling

**9. [True / False] Moderate**

> Global Accelerator works for TCP and UDP traffic generally, not just HTTP/HTTPS.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> How does isolating reporting queries onto Aurora Read Replicas benefit Meridian Loyalty's transactional workload?

> **A.** It has no effect on the transactional workload
> **B.** The transactional path keeps its full capacity, undisturbed by a long-running analytical query competing for the same database resources
> **C.** It eliminates the need for the primary database entirely
> **D.** It automatically caches guest balances in memory

**11. [Fill in the Blank] Moderate**

> Amazon CloudFront fits content that can be ____________; AWS Global Accelerator fits traffic that must reach the actual application every time.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A new solution runs a workload that holds a large dataset entirely in memory for fast in-application analytics. Which instance family fits best?

> **A.** General purpose
> **B.** Compute optimized
> **C.** Memory optimized
> **D.** No EC2 instance family can support this workload

**13. [Scenario / Judgment] Hard**

> A reviewer proposes using Global Accelerator for Meridian Loyalty's static assets instead of CloudFront, arguing "it's AWS's premium performance service, so it should always be preferred." What's the flaw?

> **A.** There is no flaw — Global Accelerator should always be preferred over CloudFront
> **B.** Static assets are cacheable content, which is exactly what CloudFront is built to cache at edge locations; Global Accelerator is the right fit for live, uncacheable traffic instead — "premium" doesn't mean "always the right choice regardless of fit"
> **C.** Global Accelerator cannot be used for any guest-facing traffic
> **D.** CloudFront cannot cache any content originating from Meridian Loyalty's servers

**14. [Scenario / Judgment] Hard**

> Meridian's operations team wants to run a large reporting query without affecting guests actively earning and redeeming points at that moment. What should they use?

> **A.** Run the query directly against the primary database
> **B.** Run the query against an Aurora Read Replica, isolating the analytical load from the transactional primary
> **C.** Pause the application until the query finishes
> **D.** Run the query against ElastiCache instead of Aurora

**15. [Scenario / Judgment] Hard**

> A student says Graviton processors are strictly better for every workload with no trade-off to consider. What's missing from this claim?

> **A.** Nothing — Graviton is unconditionally better for every workload
> **B.** Graviton's price-performance advantage applies specifically to compatible workloads — ones without dependencies on x86-only libraries — so compatibility is the actual condition, not a universal guarantee
> **C.** Graviton cannot be used with Auto Scaling groups
> **D.** Graviton only works with memory-optimized instance families

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student argues: "Module 10 already covered performance since it covered scaling." Correct this using this module's content and Module 10's.

> **A.** They're right — scaling and performance efficiency are identical concerns
> **B.** Module 10 covered handling more load without breaking — elasticity, decoupling, capacity modes; this module covers being fast for the load already being handled — matching compute to workload, getting content close to guests, and isolating analytical queries from transactional ones. Related, but different questions
> **C.** Module 10 only applies to Café Sol, never to performance concerns
> **D.** This module replaces Module 10's content entirely

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since CloudFront and Global Accelerator both improve performance for guest traffic, only one is ever needed for a given architecture." Evaluate this using this module's content.

> **A.** Agree — using both together is always redundant
> **B.** Disagree — they solve different problems for different kinds of traffic; a well-designed guest-facing architecture, like Meridian Loyalty's, often uses CloudFront for cacheable content and Global Accelerator for live, uncacheable API calls at the same time, not as a choice between them
> **C.** Disagree, but only because CloudFront cannot serve any dynamic content
> **D.** Agree, since Global Accelerator includes all of CloudFront's caching functionality

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Aurora Read Replicas and ElastiCache are described as solving different problems, even though both sit "in front of" or "alongside" the primary database to reduce its load.

> **A.** They're actually the same solution to the same problem, just with different names
> **B.** ElastiCache serves the same hot data to many repeated requests from memory — a caching problem; Read Replicas isolate an entirely different kind of workload, long-running analytical queries, from competing with transactional traffic at all — a workload-isolation problem, not a caching one
> **C.** ElastiCache only works with DynamoDB, never with Aurora, making the comparison meaningless
> **D.** Read Replicas eliminate the need for ElastiCache in every architecture

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes running Meridian's monthly brand-level reporting queries directly against the production primary database during business hours, arguing "it's just one query, how much load could it add?" Argue against this using this module's content.

> **A.** Agree — a single query never meaningfully affects database performance
> **B.** Disagree — a reporting query that scans large amounts of data competes with real guest transactions for the same database capacity; even one such query can measurably affect the transactional path, which is exactly why this module isolates that workload onto a Read Replica instead
> **C.** Disagree, but only because Aurora prohibits running analytical queries against the primary by policy
> **D.** Agree, since reporting queries and transactional queries never use the same database resources

**20. [Scenario / Judgment] Very Hard**

> A student says: "Performance efficiency just means using the most powerful resources available everywhere." Evaluate this using this module's content.

> **A.** Agree — the most powerful resources always produce the best performance efficiency
> **B.** Disagree — this module's entire approach is matching the resource to the actual workload characteristic: instance family to the real bottleneck, CloudFront or Global Accelerator to whether content is cacheable, Read Replicas to isolate analytical load. Reflexively over-provisioning the most powerful option everywhere wastes money without improving the performance that actually matters
> **C.** Disagree, but only because AWS limits how powerful a resource can be
> **D.** Agree, since this module recommends the largest instance size for every tier

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
