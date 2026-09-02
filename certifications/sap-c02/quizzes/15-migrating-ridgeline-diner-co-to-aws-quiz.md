**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 15 Knowledge Check**

Migrating Ridgeline Diner Co. to AWS · 20 questions · Practice — not graded

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

> A real migration portfolio should apply the same migration strategy to every system, for consistency.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which migration strategy fits Ridgeline's internal scheduling tool, which nobody has opened in over a year?

> **A.** Refactor
> **B.** Retire
> **C.** Repurchase
> **D.** Relocate

**3. [Fill in the Blank] Easy**

> AWS ____________ ____________ ____________ (MGN) automates a rehost by continuously replicating a server's disk state to AWS.

**4. [Multiple Choice] Easy**

> Which tool is required, in addition to DMS, for a heterogeneous database migration?

> **A.** AWS Application Migration Service
> **B.** AWS Schema Conversion Tool
> **C.** Amazon Compute Optimizer
> **D.** AWS Resilience Hub

**5. [True / False] Easy**

> A homogeneous database migration moves data between two different database engines.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why is the point-of-sale system a rehost candidate rather than a refactor candidate?

> **A.** It's critical and well-understood, with no time pressure to redesign it before Ridgeline needs to be operating normally on AWS — speed and low risk matter more here than modernization
> **B.** Rehosting is always the correct choice for every system regardless of characteristics
> **C.** The point-of-sale system has no business value
> **D.** Refactoring is impossible for point-of-sale systems

**7. [Fill in the Blank] Moderate**

> A ____________ database migration moves data between the same database engine, requiring only AWS DMS with no schema conversion.

**8. [Multiple Choice] Moderate**

> Why does the inventory database get replatformed onto RDS rather than rehosted as-is?

> **A.** It benefits meaningfully from a managed service — automated backups, patching, Multi-AZ — without needing a full application redesign
> **B.** RDS is always required for any database, regardless of benefit
> **C.** Replatforming is the only strategy AWS supports for databases
> **D.** The inventory database has no meaningful benefit from managed services

**9. [True / False] Moderate**

> AWS Schema Conversion Tool is an optional step for a heterogeneous migration that can be skipped without consequence.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What minimizes the actual downtime window during an MGN-based rehost cutover?

> **A.** MGN has already been continuously replicating the server's disk state to AWS before cutover, rather than starting the copy at cutover time
> **B.** MGN eliminates the need for any cutover window at all
> **C.** MGN only works for databases, not full servers
> **D.** MGN requires the source server to be shut down for a week before migration

**11. [Fill in the Blank] Moderate**

> A ____________ database migration moves data between different database engines, requiring the Schema Conversion Tool before DMS handles the data.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Ridgeline's reporting server runs on aging, hard-to-maintain custom software the team has wanted to modernize for years, and isn't the most time-urgent system to move. Which strategy fits best?

> **A.** Retire, since old software should always be turned off
> **B.** Refactor — it's the system worth a real redesign, once the more urgent moves are complete
> **C.** Rehost, to avoid any change at all
> **D.** Repurchase, since no SaaS alternative is mentioned

**13. [Scenario / Judgment] Hard**

> A reviewer proposes migrating Ridgeline's on-premises Oracle database to Amazon Aurora using DMS alone, skipping the Schema Conversion Tool. What's the risk?

> **A.** There is no risk — DMS alone always handles engine changes automatically
> **B.** Oracle to Aurora is a heterogeneous migration; DMS doesn't translate schemas, data types, or stored procedures between different engines, so skipping SCT would leave the target schema incompatible with the source
> **C.** SCT is only needed for homogeneous migrations, not heterogeneous ones
> **D.** Aurora cannot be a migration target under any circumstances

**14. [Scenario / Judgment] Hard**

> Sofía wants Ridgeline's point-of-sale system moved to AWS with minimal downtime and minimal redesign risk, as fast as possible. What should she use?

> **A.** AWS Schema Conversion Tool
> **B.** AWS Application Migration Service, for an automated rehost
> **C.** A full refactor to a cloud-native architecture
> **D.** AWS Compute Optimizer

**15. [Scenario / Judgment] Hard**

> A student argues that rehosting everything in Ridgeline's portfolio would be the safest overall approach. What's missing from this reasoning?

> **A.** Nothing — rehosting everything is always the safest and best approach
> **B.** Rehosting everything ignores real modernization opportunity for systems, like the inventory database, that would meaningfully benefit from a managed service without a full redesign — a strategy should be matched per system, not applied uniformly
> **C.** Rehosting is technically impossible for more than one system at a time
> **D.** Only refactoring is ever an acceptable migration strategy

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Domain 4 is just Domain 3 with different AWS service names." Correct this using this module's content and Domain 3's.

> **A.** They're right — the two domains cover identical content with different labels
> **B.** Domain 3 improved systems that were already running in AWS; Domain 4 migrates a system, Ridgeline, that has never touched the cloud at all — a genuinely different starting point requiring migration-specific tools like MGN, DMS, and SCT that Domain 3 never needed
> **C.** Domain 3 only applies to Café Sol and Domain 4 only applies to Ridgeline, with no conceptual relationship
> **D.** Domain 4 replaces everything Domain 3 covered

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since refactoring produces the most cloud-native, modern result, it should be the default strategy for every system in a migration portfolio." Evaluate this using this module's content.

> **A.** Agree — refactoring should always be the default regardless of system characteristics
> **B.** Disagree — refactoring is the right call for systems with the most to gain from redesign and time to do it safely, like the reporting server; applying it to a time-critical, well-understood system like the point-of-sale system would trade unnecessary risk and delay for a modernization benefit that system doesn't urgently need
> **C.** Disagree, but only because refactoring is technically impossible for any system Ridgeline owns
> **D.** Agree, since rehosting is never an acceptable strategy under any circumstances

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why the inventory database's migration to RDS for SQL Server is homogeneous even though it involves moving from a self-managed, on-premises server to a fully managed AWS service.

> **A.** It's actually heterogeneous, because moving from on-premises to a managed service always counts as an engine change
> **B.** Homogeneous vs. heterogeneous is about whether the database ENGINE changes (SQL Server to SQL Server, in this case), not about whether the hosting model changes (self-managed to managed); moving to a managed service without changing the engine is still homogeneous, and DMS alone is sufficient
> **C.** RDS can only be a target for heterogeneous migrations
> **D.** There is no such thing as a homogeneous migration to a managed service

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping AWS Application Migration Service entirely for the point-of-sale system, arguing "we can just manually rebuild the server on EC2 from scratch after taking it offline." Argue against this using this module's content.

> **A.** Agree — manually rebuilding from scratch is always faster than using MGN
> **B.** Disagree — MGN continuously replicates the server's disk state to AWS ahead of time, so cutover only requires launching an already-current copy; manually rebuilding from scratch after taking the system offline means the actual downtime window includes the entire rebuild, not just a brief cutover
> **C.** Disagree, but only because manual rebuilds are technically prohibited by AWS
> **D.** Agree, since MGN cannot be used for point-of-sale systems specifically

**20. [Scenario / Judgment] Very Hard**

> A student says: "Since Ridgeline's four systems all end up on AWS eventually, the specific strategy chosen for each one doesn't really matter." Evaluate this using this module's content.

> **A.** Agree — the end state is identical regardless of which strategy gets each system there
> **B.** Disagree — the strategy chosen determines risk, timeline, and ongoing benefit: retiring the unused tool avoids wasted migration effort entirely, rehosting the point-of-sale system minimizes downtime and risk for a time-critical system, replatforming the inventory database captures managed-service benefits, and refactoring the reporting server captures the modernization value only a redesign provides. Reaching the same AWS account by different paths produces very different outcomes
> **C.** Disagree, but only because AWS charges different prices depending on strategy
> **D.** Agree, since all four strategies produce technically identical architectures

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
