[Course index](../README.md) · [Read the paired lesson](../modules/16-modernizing-whats-been-migrated.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 16 Knowledge Check**

Modernizing What's Been Migrated · 20 questions · Practice — not graded

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

> Migrating a workload and modernizing it in the same cutover reduces overall risk, because it's only one change instead of two.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service runs containers without requiring the team to manage the underlying EC2 instances?

> **A.** AWS Application Migration Service
> **B.** AWS Fargate
> **C.** AWS Schema Conversion Tool
> **D.** AWS Database Migration Service

**3. [Fill in the Blank] Easy**

> The exam-preferred sequencing for an existing workload is often described as crawl, ____________, run — migrate, stabilize, then modernize.

**4. [Multiple Choice] Easy**

> What should trigger the reporting server's refactored, event-driven design, instead of a fixed nightly schedule?

> **A.** A CloudWatch alarm on CPU utilization
> **B.** New data landing in Amazon S3
> **C.** A manual button click each morning
> **D.** A Savings Plans renewal date

**5. [True / False] Easy**

> Containerizing a workload with Amazon ECS on Fargate requires first rewriting the application as a set of microservices.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why did Module 15's rehost of the point-of-sale system leave the architecture unchanged rather than modernizing it during the move?

> **A.** Modernizing during the same cutover as the migration would combine two different kinds of risk into one change, with no clean way to tell which one caused a problem
> **B.** The point-of-sale system cannot technically be modernized
> **C.** AWS Application Migration Service only works on unmodified systems, permanently
> **D.** Modernizing during a migration is always faster than modernizing afterward

**7. [Fill in the Blank] Moderate**

> A read-heavy workload with repeated queries against an existing database often just needs a ____________ in front of it, such as Amazon ElastiCache, rather than a new database engine.

**8. [Multiple Choice] Moderate**

> Why does the inventory database stay on Amazon RDS instead of moving to a purpose-built database like DynamoDB?

> **A.** RDS is the only database AWS supports
> **B.** Its access pattern hasn't changed since the replatform, so forcing a different database model adds complexity without a real benefit
> **C.** DynamoDB cannot store inventory data
> **D.** Purpose-built databases are always slower than relational ones

**9. [True / False] Moderate**

> Containerizing the point-of-sale system with ECS on Fargate means the team no longer has to patch or scale the underlying compute themselves.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What is the actual problem with the reporting server's current design, according to this module?

> **A.** Its database engine is fundamentally incompatible with AWS
> **B.** It runs on a fixed schedule instead of in response to new data, wasting runs and depending on a server being available at a set time
> **C.** It has no database at all
> **D.** It was never migrated to AWS in Module 15

**11. [Fill in the Blank] Moderate**

> A workload with a genuinely different access pattern than a relational engine handles well — high-volume key-value lookups at scale, for example — is a legitimate case for a ____________ database like Amazon DynamoDB.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A team proposes migrating Ridgeline's reporting server to AWS and redesigning it as an event-driven serverless system in the same cutover weekend. What's the concern?

> **A.** There is no concern — combining the two saves time with no real downside
> **B.** Combining migration and modernization in one cutover means an outage or bug could come from either the move or the redesign, with no clean way to isolate which — the exam-preferred approach separates them
> **C.** Event-driven designs cannot be deployed to AWS under any circumstances
> **D.** Modernization must always happen before migration, never after

**13. [Scenario / Judgment] Hard**

> A reviewer suggests moving the inventory database from RDS to DynamoDB simply because "DynamoDB is more modern." What's the flaw?

> **A.** DynamoDB cannot be used for any workload migrated from on-premises
> **B.** The access pattern hasn't changed — moving to a purpose-built database should be driven by a genuine pattern mismatch, not by one database being newer
> **C.** RDS is always the correct choice regardless of workload
> **D.** There is no flaw; newer is always better

**14. [Scenario / Judgment] Hard**

> Sofía wants the point-of-sale system to stop requiring EC2 patching and manual scaling, without rewriting the application as microservices. What should she use?

> **A.** A full refactor to a microservices architecture
> **B.** Amazon ECS on AWS Fargate — containerize the existing application without a rewrite
> **C.** AWS Schema Conversion Tool
> **D.** A second rehost via AWS Application Migration Service

**15. [Scenario / Judgment] Hard**

> A student argues that every legacy database performance problem should be solved by adopting a purpose-built database. What's missing from this reasoning?

> **A.** Nothing — a purpose-built database is always the correct fix for a slow database
> **B.** A cache in front of the existing database, or recognizing the real bottleneck isn't the database at all — as with the reporting server's fixed schedule — often fits better than replacing the database engine
> **C.** Purpose-built databases are never appropriate under any circumstances
> **D.** Only relational databases can ever have performance problems

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Domain 4 is really just two migrations back to back — Module 15 moved Ridgeline, Module 16 moves it again." Correct this using this module's content.

> **A.** They're right — Module 16 is a second migration of the same systems
> **B.** Module 15 moved Ridgeline's systems to AWS largely unchanged; Module 16 doesn't move them again — it modernizes systems that are now stable in AWS, using different tools (ECS on Fargate, event-driven Lambda, caching or purpose-built databases) aimed at a different goal
> **C.** Module 16 undoes everything Module 15 did
> **D.** There is no meaningful difference between migration and modernization tools

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since containerizing the point-of-sale system worked well, every system in Ridgeline's portfolio should be containerized next." Evaluate this using this module's content.

> **A.** Agree — containerizing should always be applied to every system regardless of fit
> **B.** Disagree — modernization should match the actual bottleneck per system; the reporting server's real problem is a fixed schedule, not its packaging, and the inventory database's access pattern hasn't changed, so neither needs containerizing to solve the problem it actually has
> **C.** Disagree, but only because containers are technically incompatible with databases
> **D.** Agree, since Fargate is required for every AWS workload

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why refactoring the reporting server's nightly batch job to be event-driven solves its actual problem, when simply moving the same scheduled job onto a more powerful EC2 instance would not.

> **A.** A more powerful EC2 instance would run the job faster on the same fixed schedule, but the underlying problem — wasted runs when no new data arrived, and a dependency on a server being available at a set time — stays exactly the same; only triggering the job from the actual event (new data landing in Amazon S3) removes that dependency
> **B.** A more powerful EC2 instance solves the problem completely and is the recommended fix
> **C.** The reporting server has no scheduling problem at all
> **D.** Event-driven designs are only cosmetic and change nothing about when the job runs

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping the migrate-then-modernize sequencing entirely for a future acquisition, arguing "waiting to stabilize before modernizing just slows us down." Argue against this using this module's content.

> **A.** Agree — modernizing during the same cutover as the migration is always faster with no added risk
> **B.** Disagree — combining migration and modernization into one cutover means any outage or bug could come from either change, with no clean way to isolate the cause; migrating first and modernizing once the system is stable, using real operating data to guide what's worth changing, is the exam-preferred approach precisely because it reduces that risk
> **C.** Disagree, but only because modernization is technically impossible immediately after a migration
> **D.** Agree, since stabilization periods serve no real purpose

**20. [Scenario / Judgment] Very Hard**

> Looking back across the whole SAP-C02 track, a student says: "Domain 2, Domain 3, and Domain 4 basically taught the same design skills three times." Evaluate this using this module's content and the earlier domains'.

> **A.** Agree — all three domains cover identical scenarios with different labels
> **B.** Disagree — Domain 2 designed Meridian Loyalty new, with no existing constraints; Domain 3 improved Café Sol, a system already stable in AWS, using real operating history; Domain 4 migrated and modernized Ridgeline, a system that had never touched the cloud at all, requiring an entirely different toolset (MGN, DMS, SCT, then ECS, Lambda, purpose-built databases) that neither earlier domain needed
> **C.** Domain 2 and Domain 3 are identical, but Domain 4 is unrelated to both
> **D.** Each domain replaces everything the previous one covered

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
