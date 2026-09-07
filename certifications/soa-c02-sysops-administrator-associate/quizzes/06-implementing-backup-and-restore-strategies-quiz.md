**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 6 Knowledge Check**

Implementing Backup and Restore Strategies · 20 questions · Practice — not graded

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

> RPO measures how much downtime a business can tolerate.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What does AWS Backup let you define to centralize schedule, retention, and lifecycle rules across services?

> **A.** A security group
> **B.** A backup plan
> **C.** A launch template
> **D.** A trail

**3. [Fill in the Blank] Easy**

> ____________ ____________ ____________ (RDS) are deleted along with the database instance by default, unless a final snapshot is requested.

**4. [Multiple Choice] Easy**

> Which RDS backup mechanism persists indefinitely, independent of the source instance's lifecycle?

> **A.** Automated backups
> **B.** Manual snapshots
> **C.** Transaction logs only
> **D.** Neither persists after instance deletion

**5. [True / False] Easy**

> AWS Backup supports cross-Region and cross-account backup copies as part of the same backup plan.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> A stated requirement says "the system must be back online within 30 minutes of a failure." What is this describing?

> **A.** RPO
> **B.** RTO
> **C.** A backup retention period
> **D.** A snapshot lifecycle rule

**7. [Fill in the Blank] Moderate**

> ____________ ____________ (RPO) measures how much data loss, expressed as time, a business can accept.

**8. [Multiple Choice] Moderate**

> Why does AWS Backup's centralized policy model fix the problem of inconsistent, per-team backup configuration?

> **A.** It removes the need for backups entirely
> **B.** One backup plan assigns schedule, retention, and lifecycle rules across services by tag or resource ID, instead of each service being configured independently
> **C.** It only works for a single AWS service at a time
> **D.** It disables manual snapshots so nothing can be missed

**9. [True / False] Moderate**

> RDS automated backups enable point-in-time recovery to any second within the retention period.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A team needs a database backup that will still exist even after the database instance itself is deleted, with no automatic expiration tied to the instance. What fits?

> **A.** Automated backups, since they always survive instance deletion
> **B.** A manual snapshot, or an automated backup deletion request with backups explicitly retained
> **C.** Nothing — RDS backups cannot survive instance deletion
> **D.** VPC Flow Logs

**11. [Fill in the Blank] Moderate**

> A tight ____________ (measuring downtime) typically requires a pre-provisioned standby, not a from-scratch restore from a cold snapshot.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A stakeholder says "the business can tolerate losing at most 15 minutes of data." Which requirement is this, and what design implication follows?

> **A.** RTO — it requires a pre-provisioned standby
> **B.** RPO — it requires backup frequency (or continuous replication) tight enough to bound data loss to 15 minutes
> **C.** Neither RTO nor RPO — this describes a retention period
> **D.** RTO — it requires increasing snapshot retention to 15 days

**13. [Scenario / Judgment] Hard**

> Priya deletes an RDS instance without requesting a final snapshot, assuming the automated backups would remain available. What actually happens?

> **A.** The automated backups persist indefinitely regardless of the deletion request
> **B.** The automated backups are deleted along with the instance, since they're tied to the instance's lifecycle by default
> **C.** RDS automatically converts them to manual snapshots
> **D.** Only the transaction logs are deleted; daily backups remain

**14. [Scenario / Judgment] Hard**

> A scenario emphasizes that backups must survive a Region-wide event that also takes out the primary data. What's the fix?

> **A.** Increase the RDS backup retention period
> **B.** Cross-Region backup copies through AWS Backup, so backups don't live only in the same Region as the primary data
> **C.** Switch from automated backups to manual snapshots only
> **D.** Nothing — no backup mechanism can survive a Region-wide event

**15. [Scenario / Judgment] Hard**

> A team wants to back up EBS volumes, DynamoDB tables, and EFS file systems on one consistent schedule and retention policy, assigned by tag, without configuring each service separately. What fits?

> **A.** Manually configuring each service's native backup feature one at a time
> **B.** A single AWS Backup plan, with resources assigned by tag across all three services
> **C.** RDS automated backups, since they cover all AWS storage services
> **D.** VPC Flow Logs, since they capture resource-level activity

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "RTO and RPO are basically the same thing — they both just mean 'how fast can we recover.'" Correct this using this module's content.

> **A.** They're right — RTO and RPO measure the exact same thing
> **B.** They're different: RPO measures acceptable data loss (a point in time), RTO measures acceptable downtime (a duration) — a tight RPO drives backup frequency, a tight RTO drives restore speed and standby readiness, and conflating them leads to solving the wrong half of a requirement
> **C.** RPO measures downtime and RTO measures data loss — the student just has the names swapped, but the concepts are correctly grouped
> **D.** Neither term applies to backup and restore strategy at all

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes relying only on RDS automated backups, with default settings, as the sole backup strategy before a risky schema migration. Evaluate this using this module's content.

> **A.** Agree — automated backups with default settings are sufficient for any risky operation
> **B.** Disagree — automated backups are tied to the instance's lifecycle and deleted by default if the instance is deleted, so a backup that must survive independently (like one taken deliberately before a risky change) calls for a manual snapshot instead, or explicit backup retention
> **C.** Disagree, but only because automated backups cannot be restored at all
> **D.** Agree, since manual snapshots are strictly worse than automated backups in every case

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a scenario stating both "recover to any point within the last 35 days" and "the backup must still exist after the instance is deleted" cannot be satisfied by automated backups alone.

> **A.** Automated backups already satisfy both requirements simultaneously with no changes needed
> **B.** Automated backups provide the point-in-time recovery capability, but by default they're deleted with the instance — satisfying the second requirement needs a manual snapshot, or an explicit request to retain backups at deletion time, layered on top of automated backups
> **C.** Neither requirement can be satisfied by any RDS backup mechanism
> **D.** Manual snapshots provide point-in-time recovery to any second, making automated backups unnecessary

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that since Meridian already has Multi-AZ (from Module 5) for high availability, a separate backup and restore strategy is redundant. Argue against this using this module's content.

> **A.** Agree — Multi-AZ already provides everything a backup strategy would provide
> **B.** Disagree — Multi-AZ protects against infrastructure failure (a data center going down), not against a bad deployment, corrupted data, or a mistaken deletion, which gets replicated to the standby just as fast as to the primary; only a separate backup and restore strategy protects against that class of failure
> **C.** Disagree, but only because Multi-AZ is incompatible with RDS
> **D.** Agree, since RPO and RTO only apply to systems without Multi-AZ

**20. [Scenario / Judgment] Very Hard**

> A student says: "Backup strategy is just a technical decision — pick whatever AWS feature sounds the most robust." Evaluate this using this module's content.

> **A.** Agree — the most feature-rich backup mechanism is always the correct choice regardless of context
> **B.** Disagree — the right mechanism is driven by a business requirement first (a stated RTO and RPO), and the technical choice (automated backups vs. manual snapshots, AWS Backup plan design, cross-Region copies) follows from matching that requirement, not from picking the most impressive-sounding feature
> **C.** Disagree, but only because AWS Backup cannot be configured without a support contract
> **D.** Agree, since RTO and RPO are only relevant to networking decisions, not backup and restore

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
