**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 8 Review Quiz**

Databases · 20 questions · Practice — not graded

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

> Amazon RDS is a managed relational database service supporting engines like MySQL, PostgreSQL, and SQL Server.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS database service is fully managed NoSQL, built for massive scale and single-digit-millisecond latency?
>
> **A.** Amazon RDS
> **B.** Amazon DynamoDB
> **C.** Amazon Redshift
> **D.** Amazon Aurora

**3. [Fill in the Blank] Easy**

> A ____________ database organizes data into tables with defined schemas and relationships, queried using SQL.

**4. [Multiple Choice] Easy**

> Which service is purpose-built for analytical queries (OLAP) across large historical datasets?
>
> **A.** Amazon RDS
> **B.** Amazon DynamoDB
> **C.** Amazon Redshift
> **D.** Amazon Aurora

**5. [True / False] Easy**

> Amazon Aurora is a completely separate product from RDS, with its own dedicated console.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which RDS feature maintains a synchronous standby database in another Availability Zone, with automatic failover?
>
> **A.** Read replicas
> **B.** Multi-AZ deployment
> **C.** Aurora Serverless
> **D.** Snapshot restore

**7. [Fill in the Blank] Moderate**

> ____________ replicas offload read traffic to additional database copies, helping scale read-heavy workloads.

**8. [Multiple Choice] Moderate**

> Which type of workload does OLTP describe?
>
> **A.** Few large analytical queries
> **B.** Lots of small, fast transactional operations
> **C.** Batch data warehousing
> **D.** Offline bulk data transfer

**9. [True / False] Moderate**

> DynamoDB requires a fixed schema, just like a relational database.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> AWS positions Amazon Aurora as offering what, compared to standard RDS engines?
>
> **A.** Lower cost only
> **B.** Higher performance and availability
> **C.** NoSQL flexibility
> **D.** Built-in data warehousing

**11. [Fill in the Blank] Moderate**

> The unmanaged-versus-managed distinction, applied to databases, is exactly why Amazon ____________ exists — to remove the operational burden of running a relational database yourself.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A company needs complex joins across related tables with strict consistency. Relational or NoSQL?
>
> **A.** NoSQL
> **B.** Relational

**13. [Scenario / Judgment] Hard**

> A mobile app needs massive scale with simple, fast key-based lookups, and user profiles vary a lot in structure. What's the best fit?
>
> **A.** Amazon RDS
> **B.** Amazon DynamoDB
> **C.** Amazon Redshift
> **D.** Amazon Aurora

**14. [Scenario / Judgment] Hard**

> Leadership wants quarterly sales trend reports across five years of historical data. What's the best fit?
>
> **A.** Amazon RDS
> **B.** Amazon DynamoDB
> **C.** Amazon Redshift
> **D.** Read replicas

**15. [Scenario / Judgment] Hard**

> A team wants MySQL compatibility, but with better performance and availability than a standard RDS instance. What's the best fit?
>
> **A.** Amazon DynamoDB
> **B.** Amazon Redshift
> **C.** Amazon Aurora
> **D.** Read replicas

**16. [Scenario / Judgment] Hard**

> Read traffic is overwhelming a single RDS instance, but writes stay low. What's the best fix?
>
> **A.** Enable Multi-AZ
> **B.** Add read replicas
> **C.** Migrate to DynamoDB
> **D.** Migrate to Redshift

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> An architect argues a scenario needing complex multi-table joins should use DynamoDB "because it's more scalable." What's the correct pushback?
>
> **A.** They're right — always pick the most scalable option available
> **B.** DynamoDB trades away complex relational joins for scale and flexibility — a scenario needing enforced relationships and joins belongs on RDS or Aurora, regardless of scalability claims
> **C.** DynamoDB supports joins just as well as RDS does
> **D.** Scalability alone should always decide the database choice

**18. [Scenario / Judgment] Very Hard**

> A company has three needs: (1) an order database that can't go down, (2) a shopping cart needing massive scale, and (3) sales analytics across years of data. In order, which services match?
>
> **A.** RDS/Aurora with Multi-AZ, DynamoDB, Redshift
> **B.** DynamoDB, Redshift, RDS
> **C.** Redshift, RDS, DynamoDB
> **D.** RDS, DynamoDB, RDS

**19. [Scenario / Judgment] Very Hard**

> A company mistakenly believes "RDS" and "Aurora" are two separate, competing categories of database. What's the correct clarification?
>
> **A.** They're right — always pick Aurora since it's newer
> **B.** Aurora is an engine option available within RDS — not a separate category — offering higher performance and availability than the standard engines
> **C.** RDS is being deprecated in favor of Aurora
> **D.** Aurora only supports NoSQL workloads

**20. [Scenario / Judgment] Very Hard**

> A company's database was fine at launch but is now struggling with both failover risk AND read-traffic overload as the business grew. What's the correct combined fix?
>
> **A.** Just add more read replicas
> **B.** Just enable Multi-AZ
> **C.** Enable Multi-AZ for failover protection AND add read replicas for read scaling — they solve two different problems
> **D.** Migrate everything to DynamoDB

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
