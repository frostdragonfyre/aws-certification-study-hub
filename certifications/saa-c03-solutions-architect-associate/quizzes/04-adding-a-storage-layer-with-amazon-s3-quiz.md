**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 4 Review Quiz**

Adding a Storage Layer with Amazon S3 · 20 questions · Practice — not graded

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

> Amazon S3 stores data as objects inside buckets, not as files inside a traditional folder hierarchy.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What's the unique identifier used to retrieve a specific object from an S3 bucket?
>
> **A.** File path
> **B.** Key
> **C.** Instance ID
> **D.** ARN only

**3. [Fill in the Blank] Easy**

> S3 is built for extremely high ____________ — the near-certainty that a stored object won't be lost.

**4. [Multiple Choice] Easy**

> Which S3 feature keeps every prior version of an object instead of overwriting it?
>
> **A.** Lifecycle policy
> **B.** Versioning
> **C.** Intelligent-Tiering
> **D.** Block Public Access

**5. [True / False] Easy**

> A newly created S3 bucket is publicly accessible by default.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which storage class automatically moves objects between tiers when the access pattern is unknown or changing?
>
> **A.** S3 Standard
> **B.** S3 Glacier
> **C.** S3 Intelligent-Tiering
> **D.** S3 One Zone-IA

**7. [Fill in the Blank] Moderate**

> A(n) ____________ policy automatically transitions objects between storage classes, or expires them, based on rules you define.

**8. [Multiple Choice] Moderate**

> Which of the following best describes the difference between durability and availability in S3?
>
> **A.** They mean the same thing
> **B.** Durability is whether data survives at all; availability is whether you can access it right now
> **C.** Durability only applies to Glacier; availability only applies to Standard
> **D.** Availability is about cost; durability is about speed

**9. [True / False] Moderate**

> S3 Standard-IA and S3 One Zone-IA both charge a retrieval fee, but One Zone-IA stores data in only one Availability Zone.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does S3 use to serve static website content, such as a homepage, when a visitor requests the site's root URL?
>
> **A.** A load balancer
> **B.** An index document
> **C.** An IAM role
> **D.** A lifecycle policy

**11. [Fill in the Blank] Moderate**

> Amazon S3's Block Public Access setting can block public access even if a bucket ____________ would otherwise allow it.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A company stores rarely accessed compliance records that must be retained for seven years, with no need for fast retrieval. Which storage class fits best?
>
> **A.** S3 Standard
> **B.** S3 Intelligent-Tiering
> **C.** S3 Glacier
> **D.** S3 Standard-IA

**13. [Scenario / Judgment] Hard**

> An object in a versioning-enabled bucket gets overwritten by mistake every few days by an automated process. What's the likely consequence if no lifecycle policy is in place?
>
> **A.** Nothing — S3 automatically deletes old versions after 24 hours
> **B.** The bucket's storage footprint for that object grows with every overwrite, since each version is kept in full
> **C.** Versioning prevents any overwrites from happening at all
> **D.** The object becomes read-only after the first overwrite

**14. [Scenario / Judgment] Hard**

> A team enables static website hosting on an S3 bucket, but visitors report the site doesn't load and they get an access denied error. What's the most likely cause?
>
> **A.** S3 doesn't support static website hosting
> **B.** Block Public Access or the bucket policy isn't configured to allow the public read access the site needs
> **C.** The bucket needs an IAM role attached to serve web traffic
> **D.** Versioning must be disabled before static hosting will work

**15. [Scenario / Judgment] Hard**

> A photo-sharing app expects some images to go viral unpredictably, while others are viewed rarely — and there's no way to know in advance which will be which. Which storage approach best fits?
>
> **A.** Manually move each photo between storage classes based on guesses about future popularity
> **B.** Store everything in S3 Glacier for the lowest possible cost
> **C.** Use S3 Intelligent-Tiering to let AWS move objects automatically based on actual observed access
> **D.** Store everything in S3 One Zone-IA

**16. [Scenario / Judgment] Hard**

> A company migrates from on-premises file servers to S3 and assumes their existing nested folder structure will be preserved exactly as a real directory tree. What should they understand about how S3 actually works?
>
> **A.** S3 has no concept of folders at all, even visually
> **B.** S3 displays keys containing slashes as if they were folders, but underneath it's a flat namespace of keys, not a true nested directory structure
> **C.** S3 requires converting every folder into a separate bucket
> **D.** S3 only supports one level of folder nesting

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "cheaper S3 storage classes mean my data is more likely to be lost." What's the correct correction?
>
> **A.** They're right — cheaper classes sacrifice durability for cost
> **B.** Durability stays extremely high across S3 storage classes; what actually changes between classes is availability and retrieval speed, not the likelihood of data loss
> **C.** Only S3 Standard offers any durability guarantee at all
> **D.** Durability only matters for objects larger than 1 GB

**18. [Scenario / Judgment] Very Hard**

> An architecture team wants log files to start in S3 Standard, move to Standard-IA after 30 days, move to Glacier after 90 days, and delete entirely after 2 years — without anyone manually managing it. What single feature accomplishes this?
>
> **A.** Versioning
> **B.** A lifecycle policy with multiple transition and expiration rules
> **C.** Block Public Access
> **D.** A separate bucket for each storage class, moved manually every month

**19. [Scenario / Judgment] Very Hard**

> A bucket hosting a static website needs its HTML and CSS files to be publicly readable, but a separate folder of internal draft files in the same bucket should stay private. What's the best approach?
>
> **A.** Make the entire bucket public, since S3 buckets can't have mixed public/private content
> **B.** Grant public read access only to the specific objects or prefix that need it, while leaving Block Public Access protections in place for the rest
> **C.** Create a new IAM user for every website visitor
> **D.** Enable versioning, which automatically separates public and private content

**20. [Scenario / Judgment] Very Hard**

> Why did the café's architecture eventually need to move beyond S3 static website hosting once online ordering was introduced?
>
> **A.** S3 can no longer host static content once a business grows past a certain size
> **B.** Online ordering requires dynamic content and server-side processing (handling orders, checking inventory), which static hosting was never built to do — a compute layer became necessary, not because S3 got worse
> **C.** S3 static website hosting has a hard limit of 100 total objects per bucket
> **D.** AWS deprecated static website hosting after 2020

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
