**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 7**

**Lab Worksheet — Storage**

Activity 1: Sort the Storage Types · Activity 2: Storage Service Hunt

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Sort the Storage Types (20 min)

### How this works

Below is a list of storage needs. For each one, sort it into object, block, or file storage, and name the AWS service. Work on your own first, then we'll build the sort together on the board.

*This is the single most tested skill in this module — sorting a scenario by access pattern before picking a specific service.*

### Sort each need

| # | Storage need | Type (object/block/file) | AWS service |
|---|---|---|---|
| 1 | A production database needs a low-latency virtual hard drive attached to one instance | | |
| 2 | A company wants to back up files, accessed over the web, with virtually unlimited capacity | | |
| 3 | A fleet of ten web servers all need to read and write the same set of shared files at once | | |
| 4 | A static website's images and videos need to be stored and served to visitors | | |
| 5 | An EC2 instance needs a boot volume that persists even when the instance is stopped | | |
| 6 | An application's log-processing servers need a shared, growing file system, no capacity planned in advance | | |

### Does the access pattern change the picture? (discuss as a class)

Look at #1 and #3 again — both need storage attached to compute, but they're different types.

| Question | Your answer |
|---|---|
| How many instances need access to the storage in #1? | |
| How many instances need access to the storage in #3? | |
| Why does that single detail — one instance vs. many — completely change which AWS service is correct? | |

### Think about it

1. Why is "accessed over the web, no traditional file system" the detail that makes something object storage instead of block or file storage?
2. EBS and EFS both attach to EC2 instances. What's the one detail that decides which of the two is correct for a given scenario?
3. Give one real-world example (not from the list above) of data that belongs in S3 specifically because of its access pattern, not just because "it's a file."

---

## Activity 2 — Storage Service Hunt (25 min)

### How this works

Work on your own. For each scenario, write which AWS storage service or S3 storage class fits best — and UNDERLINE the exact phrase that gave it away. We'll go through the answers together as a class afterward.

*Same skill as the compute service hunt from Lecture 6: noticing which phrase is load-bearing is what the real exam question is testing.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the toolkit

| Service / Class | What it's for |
|---|---|
| Amazon S3 | Object storage — virtually unlimited, accessed over the web |
| S3 Standard | Frequently accessed data, millisecond retrieval |
| S3 Standard-IA | Infrequently accessed, still needed fast, lower storage cost |
| S3 Glacier Instant Retrieval | Archive data needing millisecond access |
| S3 Glacier Flexible Retrieval | Archive data, retrieval not urgent (minutes–hours) |
| S3 Glacier Deep Archive | Long-term archive, rarely accessed, cheapest class |
| S3 lifecycle policy | Automatically moves or deletes objects as they age |
| Amazon EBS | Block storage — attached to one instance |
| Amazon EFS | File storage — shared across many instances |
| AWS Storage Gateway | Connects on-premises apps to AWS storage, ongoing |
| AWS Snow Family | Physically ships massive datasets into AWS |
| AWS Backup | Centralized backup policy across many AWS services |

### The scenarios

*Underline the deciding phrase in each scenario as you read it.*

| # | Scenario | Your answer |
|---|---|---|
| 1 | A company needs to store compliance records accessed maybe once a year, and cost is the top priority. | |
| 2 | An architect needs to make sure objects automatically move to cheaper storage as they age, without manual work. | |
| 3 | A company has 80 terabytes of data on-premises and a slow internet connection, and needs it in AWS quickly. | |
| 4 | Ten EC2 instances need to read and write the same set of shared files simultaneously. | |
| 5 | A database instance needs a persistent, low-latency virtual hard drive. | |
| 6 | A company wants archived data that's rarely accessed but, when it is needed, must come back within milliseconds. | |
| 7 | An on-premises application needs to use AWS storage as if it were a local drive, on an ongoing basis. | |
| 8 | A company wants one backup policy covering EBS, RDS, and DynamoDB, instead of five separate settings. | |
| 9 | A media company needs to store and serve video files to a website, with virtually unlimited capacity. | |
| 10 | A company needs archived data that's accessed so rarely, retrieval can take several hours, in exchange for the lowest possible storage cost. | |

### Pick any two and go deeper

For two of the scenarios above, write out why the service or class you picked beats the next most tempting wrong answer.

**Scenario #____ — why this beats the tempting wrong answer:**

**Scenario #____ — why this beats the tempting wrong answer:**

### The shortcut — write this down

**For ANY AWS storage scenario on the exam, ask in this order:**

1. Is this about **whole objects**, accessed over the web? → Amazon S3.
2. Is this about **one instance's disk**? → Amazon EBS.
3. Is this about **many instances sharing files**? → Amazon EFS.
4. Is this about **an on-premises app using AWS storage**? → AWS Storage Gateway.
5. Is this about **massive data, limited bandwidth**? → The AWS Snow Family.
6. Is this about **one backup policy across services**? → AWS Backup.

*Notice the pattern: object, block, file, hybrid, and offline — five questions that resolve almost every storage scenario. Once you've landed on S3, a second question kicks in: how often is it accessed, and how fast does it need to come back? That's what picks the storage class.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Rewrite scenario 4 so the correct answer becomes EBS instead of EFS. What did you have to change? |
| 2 | Explain in your own words why the Snow Family isn't the answer if a company's internet connection is fast and reliable, even for a huge dataset. |
| 3 | Pick one S3 storage class and explain, without notes, the specific trade-off it makes. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 7 + knowledge check (aim 80%+ first attempt) |
| | Sketch the three storage types from memory once, without looking at your notes |
| | Pick one storage service from tonight's toolkit and explain what it does in your own words, no notes |
