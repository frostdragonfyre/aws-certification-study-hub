**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 7 Review Quiz**

Storage · 20 questions · Practice — not graded

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

> Object storage (Amazon S3) stores whole files with metadata and is accessed over the web, not mounted like a traditional file system.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service provides block storage attached to a single EC2 instance?
>
> **A.** Amazon S3
> **B.** Amazon EFS
> **C.** Amazon EBS
> **D.** AWS Storage Gateway

**3. [Fill in the Blank] Easy**

> Amazon ____________ provides a shared file system that multiple EC2 instances can mount and access simultaneously.

**4. [Multiple Choice] Easy**

> Which S3 storage class is the cheapest, with retrieval taking hours?
>
> **A.** S3 Standard
> **B.** S3 Standard-IA
> **C.** S3 Glacier Instant Retrieval
> **D.** S3 Glacier Deep Archive

**5. [True / False] Easy**

> An S3 lifecycle policy requires someone to manually move objects between storage classes.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which service physically ships a device to a customer to transfer massive datasets when bandwidth is limited?
>
> **A.** AWS Storage Gateway
> **B.** The AWS Snow Family
> **C.** AWS Backup
> **D.** Amazon EFS

**7. [Fill in the Blank] Moderate**

> AWS ____________ connects an on-premises environment to AWS storage on an ongoing basis.

**8. [Multiple Choice] Moderate**

> Which service centralizes backup policy across many AWS services, like EBS, RDS, and DynamoDB?
>
> **A.** AWS Config
> **B.** AWS Backup
> **C.** AWS Artifact
> **D.** AWS CloudTrail

**9. [True / False] Moderate**

> An EBS volume can be simultaneously attached to and used by multiple EC2 instances at once, just like EFS.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which S3 storage class offers millisecond retrieval, even though it's an archive tier?
>
> **A.** S3 Glacier Flexible Retrieval
> **B.** S3 Glacier Deep Archive
> **C.** S3 Glacier Instant Retrieval
> **D.** S3 One Zone-IA

**11. [Fill in the Blank] Moderate**

> S3 durability is described as 99.999999999% — commonly referred to as ____________ nines.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A company needs to store compliance records accessed maybe once a year, and cost is the top priority. Which storage class fits best?
>
> **A.** S3 Standard
> **B.** S3 Standard-IA
> **C.** S3 Glacier Deep Archive
> **D.** Amazon EFS

**13. [Scenario / Judgment] Hard**

> Ten EC2 instances need to read and write the same set of shared files at once. What's the best fit?
>
> **A.** Amazon EBS
> **B.** Amazon EFS
> **C.** Amazon S3
> **D.** The AWS Snow Family

**14. [Scenario / Judgment] Hard**

> A company has 80 terabytes of data on-premises, a slow internet connection, and needs it moved into AWS quickly. What's the best fit?
>
> **A.** A standard online transfer
> **B.** The AWS Snow Family
> **C.** AWS Storage Gateway
> **D.** Amazon EFS

**15. [Scenario / Judgment] Hard**

> A database needs a persistent, low-latency virtual hard drive attached to a single instance. What's the best fit?
>
> **A.** Amazon S3
> **B.** Amazon EFS
> **C.** Amazon EBS
> **D.** AWS Storage Gateway

**16. [Scenario / Judgment] Hard**

> A company wants one consistent backup policy instead of five separate settings across services. What's the best fit?
>
> **A.** AWS Config
> **B.** AWS Backup
> **C.** An S3 lifecycle policy
> **D.** AWS CloudTrail

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> Data is rarely accessed but must come back within milliseconds when it is needed. Which storage class fits, and why isn't Deep Archive the answer?
>
> **A.** Deep Archive, since it's the cheapest option available
> **B.** S3 Glacier Instant Retrieval — it keeps millisecond access despite being an archive tier; Deep Archive takes hours to retrieve
> **C.** S3 Standard, since speed should always win regardless of cost
> **D.** S3 One Zone-IA, since it's a reasonable middle ground

**18. [Scenario / Judgment] Very Hard**

> A company wants object storage for website media, block storage for its database, file storage for shared editing files, and one consistent backup policy across everything. Match all four needs to services, in order.
>
> **A.** S3, EBS, EFS, AWS Backup
> **B.** EFS, S3, EBS, AWS Config
> **C.** S3, EFS, EBS, AWS Backup
> **D.** EBS, S3, EFS, AWS CloudTrail

**19. [Scenario / Judgment] Very Hard**

> An architect claims: "Since our data is important, it should stay in S3 Standard forever." What's the correct pushback?
>
> **A.** They're right — important data should always stay in Standard
> **B.** Storage class should be based on access frequency and retrieval urgency, not importance — critical compliance data can still belong in Glacier Deep Archive if it's rarely accessed
> **C.** Important data should move to EBS instead of S3
> **D.** Importance determines durability, not storage class, so the claim doesn't apply either way

**20. [Scenario / Judgment] Very Hard**

> A company configures individual backup schedules for EBS, RDS, and DynamoDB separately, and one gets forgotten during a team reorganization. What's the architectural lesson, and the fix?
>
> **A.** Nothing can be done — backups must always be configured manually per service
> **B.** Per-service backup configuration has a real failure mode — someone can always forget one; the fix is AWS Backup's centralized, consistent policy across all resource types
> **C.** Switch everything to S3 to avoid needing backups entirely
> **D.** Backups aren't necessary once data is already stored durably

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
