[Course index](../README.md) · [Read the paired lesson](../modules/15-implementing-compute-and-storage-performance-optimization.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 15 Knowledge Check**

Implementing Compute and Storage Performance Optimization · 20 questions · Practice — not graded

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

> Instance Store data survives an EC2 instance stop or termination.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which EBS volume type is the cost-effective default with a solid baseline of IOPS and throughput?

> **A.** Provisioned IOPS SSD (io2)
> **B.** General Purpose SSD (gp3)
> **C.** Instance Store
> **D.** Magnetic (standard)

**3. [Fill in the Blank] Easy**

> S3 ____________ fits data accessed frequently, at the highest per-GB cost of the commonly used storage classes.

**4. [Multiple Choice] Easy**

> Which AWS service sits in front of a database to serve repeated, read-heavy queries from memory?

> **A.** Amazon Compute Optimizer
> **B.** Amazon ElastiCache
> **C.** AWS Budgets
> **D.** Amazon S3 Glacier

**5. [True / False] Easy**

> An S3 lifecycle policy can automatically transition an object to a cheaper storage class as it ages.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does Instance Store deliver higher performance than EBS for some workloads?

> **A.** It uses a slower but cheaper disk technology
> **B.** It's physically attached to the same host as the instance, with no network hop involved
> **C.** Instance Store is actually a type of EBS volume
> **D.** It automatically replicates data across Availability Zones

**7. [Fill in the Blank] Moderate**

> S3 Standard-____________ costs less than S3 Standard but still offers millisecond retrieval, fitting data accessed infrequently but needed immediately when it is.

**8. [Multiple Choice] Moderate**

> A database is under load from the same handful of queries being run repeatedly, returning largely the same results. What's the appropriate fix?

> **A.** Resize the database to a larger instance type
> **B.** Add ElastiCache in front of the database to absorb the repeated, read-heavy queries
> **C.** Migrate to a completely different database engine
> **D.** Switch the database's storage to Instance Store

**9. [True / False] Moderate**

> Provisioned IOPS SSD (io2) is typically reserved for demanding database workloads needing consistently high, predictable IOPS.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Data that's essentially archival, where a retrieval delay of minutes to hours is acceptable, fits which S3 storage class family?

> **A.** S3 Standard
> **B.** S3 Standard-IA
> **C.** S3 Glacier
> **D.** None — archival data cannot be stored in S3

**11. [Fill in the Blank] Moderate**

> A ____________ policy automates moving an S3 object between storage classes as it ages, without manual intervention.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Café Sol runs a batch-processing job that regenerates its scratch data every run and never needs that data to survive an instance replacement. What storage fits best?

> **A.** EBS Provisioned IOPS (io2), for maximum durability
> **B.** Instance Store, since the data is reproducible and doesn't need to persist
> **C.** S3 Glacier, for the lowest cost
> **D.** EBS General Purpose SSD (gp3), as the safe default

**13. [Scenario / Judgment] Hard**

> Meridian Loyalty's database tier needs consistently high, predictable IOPS at low latency for demanding transactional workloads. What EBS volume type fits best?

> **A.** Instance Store, for the highest raw performance
> **B.** Provisioned IOPS SSD (io2), built for consistently high, predictable IOPS
> **C.** S3 Standard, since it's the most cost-effective
> **D.** General Purpose SSD (gp3) alone, since it always matches io2 performance

**14. [Scenario / Judgment] Hard**

> Ridgeline's order records are accessed frequently for the first 30 days, rarely after that, and almost never after a year, though a small chance of an audit request remains. What storage design fits best?

> **A.** Keep everything in S3 Standard indefinitely, regardless of access pattern
> **B.** An S3 lifecycle policy moving records to Standard-IA after 30 days and to Glacier after a year, automating the transition as access drops off
> **C.** Delete the records after 30 days to save cost
> **D.** Store everything in Glacier from the start, regardless of the frequent access in the first 30 days

**15. [Scenario / Judgment] Hard**

> A team notices their database's CPU and memory usage are actually fine, but response times are still slow due to the same read queries running over and over. What should they try before resizing the database?

> **A.** Resize the database anyway, since slow response times always mean it's undersized
> **B.** Add a caching layer like ElastiCache to absorb the repeated read queries, since the underlying resource usage isn't actually the bottleneck
> **C.** Switch the database's underlying storage to Instance Store
> **D.** Migrate the database to S3

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Instance Store and EBS are basically the same thing, so it doesn't matter which one you pick for a database's primary storage." Correct this using this module's content.

> **A.** They're right — the two are fully interchangeable for any workload
> **B.** They're different: Instance Store is ephemeral and loses data on stop, terminate, or hardware failure, while EBS is persistent and survives the instance's lifecycle — a database's primary storage needs to survive, making Instance Store the wrong choice regardless of its raw performance advantage
> **C.** EBS is ephemeral; Instance Store is persistent
> **D.** Instance Store is simply a slower version of EBS with no other differences

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes storing all of Ridgeline's data in S3 Glacier from day one, arguing "it's the cheapest option, so it should always be used." Evaluate this using this module's content.

> **A.** Agree — Glacier should always be used regardless of access pattern
> **B.** Disagree — Glacier trades away instant access for its low cost, with retrieval taking minutes to hours; data accessed frequently or needing immediate retrieval belongs in S3 Standard or Standard-IA instead, and using Glacier for actively accessed data would create real retrieval delays
> **C.** Disagree, but only because Glacier cannot store more than a few files
> **D.** Agree, since S3 Standard and Standard-IA no longer exist

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why adding ElastiCache can fix a performance problem that resizing the database wouldn't.

> **A.** ElastiCache and database resizing always produce identical results
> **B.** If the bottleneck is repeated, read-heavy queries returning largely the same data, the database is spending capacity re-computing or re-fetching the same answers — a cache absorbs that repeated load directly, while a bigger database instance would still redo the same redundant work, just with more headroom before it becomes a problem again
> **C.** Resizing a database is always cheaper than adding a cache
> **D.** ElastiCache replaces the need for a database entirely

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that Provisioned IOPS SSD (io2) should be the default for every EBS volume because it delivers the highest guaranteed performance. Argue against this using this module's content.

> **A.** Agree — io2 has no downside compared to gp3
> **B.** Disagree — gp3 is the cost-effective default with a solid baseline of IOPS and throughput sufficient for most workloads; io2's higher, more consistent IOPS is built for demanding workloads where gp3's baseline genuinely isn't enough, not as a blanket default
> **C.** Disagree, but only because io2 cannot be attached to EC2 instances
> **D.** Agree, since gp3 offers no baseline performance at all

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as data is stored somewhere in AWS, the storage choice doesn't really affect performance or cost." Evaluate this claim using this module's content.

> **A.** Agree — all AWS storage options perform and cost identically
> **B.** Disagree — Instance Store versus EBS trades performance and persistence very differently, EBS volume types trade baseline versus provisioned IOPS, and S3 storage classes trade retrieval speed against cost — the right choice in each case depends on the specific access pattern and durability requirement, not a one-size-fits-all default
> **C.** Disagree, but only because AWS has just one storage option
> **D.** Agree, since cost and performance are unrelated to storage choice in AWS

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
