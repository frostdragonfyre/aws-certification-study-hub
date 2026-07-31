**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 4**

**Lab Worksheet — Cloud Security**

Activity 1: Shared Responsibility Sort · Activity 2: Security Tool Hunt

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Sort the Shared Responsibility Model (20 min)

### How this works

Below is a list of security and infrastructure tasks. For each one, mark whether it's **AWS's job** ("security OF the cloud") or **your job** ("security IN the cloud"). Work on your own first, then we'll compare answers as a class.

*This is the single most tested concept in Domain 2. Get comfortable with the line between the two columns — almost every security question on the exam is really asking "which side of this line are we on?"*

### Sort each item

| # | Task | AWS's job | Your job |
|---|---|---|---|
| 1 | Physical security of the data center building | | |
| 2 | Patching the underlying hypervisor | | |
| 3 | Configuring security groups and network ACLs | | |
| 4 | Deciding whether to encrypt your data, and managing the keys | | |
| 5 | Maintaining the global network infrastructure (cabling, routers) | | |
| 6 | Creating and managing IAM users, groups, and permissions | | |
| 7 | Patching the guest operating system on an EC2 instance | | |
| 8 | Physically destroying decommissioned hard drives | | |
| 9 | Classifying your own data as sensitive, confidential, or public | | |
| 10 | Enabling MFA on your account | | |
| 11 | Powering and cooling the facilities | | |
| 12 | Configuring the OS-level firewall on your own instance | | |

### Does the line move? (discuss as a class)

Look at #7 — patching the guest operating system. That's true for a **self-managed database on EC2**. Now consider **Amazon RDS**, a managed database service.

| Question | Your answer |
|---|---|
| Who patches the database engine and underlying OS in RDS? | |
| Who still controls who can log in and what data lives in the tables? | |
| So does moving to a managed service shrink your responsibility, or just move where the line sits? | |

### Think about it

1. Name one item from the list above that surprised you — one you assumed was AWS's job but is actually yours (or vice versa).
2. "Security groups" showed up in the list. Whose job is configuring them, and why does that make sense given who actually knows what your application needs to talk to?
3. A company got breached because an S3 bucket was accidentally left public. Whose side of the line does that fall on — AWS's or the customer's?

---

## Activity 2 — Security Tool Hunt (25 min)

### How this works

Work on your own. For each scenario, write which AWS security service or practice fits best — and UNDERLINE the exact phrase that gave it away. We'll go through the answers together as a class afterward.

*Same skill as the support-plan hunt from Lecture 2 and the Region-picking hunt from Lecture 3: noticing which phrase is load-bearing is what the real exam question is testing.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the toolkit

| Service / Practice | What it's for |
|---|---|
| IAM (users, groups, roles, policies) | Controls WHO can do WHAT |
| MFA | An extra proof of identity beyond a password |
| Amazon GuardDuty | Detects suspicious or malicious activity/behavior automatically |
| Amazon Inspector | Scans EC2 instances and container images for known vulnerabilities |
| Amazon Macie | Scans S3 for sensitive data like PII, using machine learning |
| AWS WAF | Filters malicious web traffic (e.g., SQL injection) in front of an application |
| AWS Shield | Protects against DDoS attacks |
| AWS KMS | Creates and manages encryption keys |
| AWS Artifact | On-demand access to AWS's compliance reports and certifications |
| AWS Config | Tracks WHAT a resource's configuration looked like over time |
| AWS CloudTrail | Logs WHO called which API, when, and from where |
| AWS Organizations SCPs | Sets the maximum permissions an entire account can have *(callback to Lecture 2)* |

### The scenarios

*Underline the deciding phrase in each scenario as you read it.*

| # | Scenario | Your answer |
|---|---|---|
| 1 | A new employee needs access to only one S3 bucket, nothing else in the account. | |
| 2 | The security team wants an extra layer of protection on every login, beyond just a password. | |
| 3 | A company wants to know immediately if an EC2 instance suddenly starts communicating with a known malicious IP address. | |
| 4 | Before a product launch, the team wants to scan their EC2 fleet for known software vulnerabilities. | |
| 5 | A company suspects an S3 bucket may contain customer social security numbers that were never supposed to be stored there. | |
| 6 | An e-commerce site keeps getting hit with SQL injection attempts through its login form. | |
| 7 | A gaming company's servers are experiencing a massive volumetric traffic flood meant to take the service offline. | |
| 8 | A healthcare company needs to prove to an auditor that AWS itself is HIPAA-eligible, without waiting on an AWS support ticket. | |
| 9 | A company wants every database's data encrypted at rest, with the ability to control and rotate the encryption keys themselves. | |
| 10 | A security lead wants a historical record of exactly when a security group's rules were changed, and by whom. | |
| 11 | A CFO's root account credentials are being used for day-to-day work — including reading news articles between tasks. | |

### Pick any two and go deeper

For two of the scenarios above, write out why the service you picked beats the next most tempting wrong answer.

**Scenario #____ — why this beats the tempting wrong answer:**

**Scenario #____ — why this beats the tempting wrong answer:**

### The shortcut — write this down

**For ANY AWS security scenario on the exam, ask in this order:**

1. Is this about **who** can access something? → IAM.
2. Is this about **detecting** a threat or unusual behavior after the fact? → GuardDuty.
3. Is this about **scanning** for a known weakness before something goes wrong? → Inspector (instances/images) or Macie (sensitive data in S3).
4. Is this about **blocking** an attack on a public-facing app? → WAF (malicious requests) or Shield (DDoS floods).
5. Is this about **proving** compliance to someone outside your company? → AWS Artifact.
6. Is this about **encrypting** data or managing keys? → KMS.
7. Is this about **who did what, and when**? → CloudTrail (the "who") and Config (the "what changed" over time) — often named together.

*Notice the pattern: IAM is about permission, GuardDuty is about live threat detection, Inspector/Macie are about scanning, WAF/Shield are about defense, Artifact is about proof, KMS is about protecting the data itself, and CloudTrail/Config are about the historical record. Seven different jobs — the exam is testing whether you can tell them apart, not just recognize the names.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Rewrite scenario 3 so the correct answer becomes Inspector instead of GuardDuty. What did you have to change? |
| 2 | The root account rule everyone breaks: what SHOULD scenario 11's CFO be doing instead, day to day? |
| 3 | Explain in your own words why "the customer is always responsible for IAM" is true even for a fully-managed service like RDS or Lambda. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 4 + knowledge check (aim 80%+ first attempt) |
| | If you have a personal AWS account: confirm MFA is enabled on your root user right now — this is the single most important account habit in this whole course |
| | Pick one security service from tonight's toolkit and explain what it does in your own words, no notes |
