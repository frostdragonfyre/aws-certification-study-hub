**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 9 Knowledge Check**

Securing User, Application, and Data Access · 20 questions · Practice — not graded

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

> Amazon Cognito is designed to authenticate the end users of an application, not to manage administrative access to AWS itself.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which Cognito component handles customer sign-up, sign-in, and password resets?
>
> **A.** Identity pool
> **B.** User pool
> **C.** IAM role
> **D.** Resource-based policy

**3. [Fill in the Blank] Easy**

> AWS Secrets Manager can automatically ____________ a secret's value on a schedule, without manual work.

**4. [Multiple Choice] Easy**

> Which AWS service is primarily responsible for creating and managing encryption keys used to protect data at rest?
>
> **A.** AWS Secrets Manager
> **B.** Amazon Cognito
> **C.** AWS KMS
> **D.** AWS IAM

**5. [True / False] Easy**

> Hardcoding database credentials directly into application code is a recommended AWS best practice.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> A café's website needs to let customers create accounts and log in. What is the correct approach?
>
> **A.** Create an individual IAM user for each customer
> **B.** Use Amazon Cognito user pools for customer authentication
> **C.** Give every customer the same shared IAM user
> **D.** Require customers to have their own AWS account

**7. [Fill in the Blank] Moderate**

> A Cognito ____________ pool grants temporary, limited AWS credentials to an application's users, including guests.

**8. [Multiple Choice] Moderate**

> Which service is the free alternative to Secrets Manager for configuration values that don't need automatic rotation?
>
> **A.** AWS Systems Manager Parameter Store
> **B.** Amazon Cognito
> **C.** AWS KMS
> **D.** IAM Access Analyzer

**9. [True / False] Moderate**

> A customer managed KMS key provides stronger encryption than an AWS managed key.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does "envelope encryption" describe in AWS KMS?
>
> **A.** Encrypting an email before sending it
> **B.** Using a data key to encrypt the actual data locally, then encrypting that data key with a KMS key
> **C.** Wrapping a KMS key inside another KMS key indefinitely
> **D.** A type of network encryption unrelated to KMS

**11. [Fill in the Blank] Moderate**

> Encryption ____________ (like TLS/HTTPS) protects data while it moves across a network, distinct from encryption at rest.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A café's EC2 web tier currently has RDS database credentials hardcoded in its configuration file. What's the recommended fix, and why?
>
> **A.** Leave it as is — hardcoding is the simplest approach and simplicity is always best
> **B.** Move the credentials into AWS Secrets Manager, so the application retrieves them at runtime instead of storing them in code, with the option of automatic rotation
> **C.** Move the credentials into a public S3 bucket for easy access
> **D.** Email the credentials to the development team instead of storing them anywhere

**13. [Scenario / Judgment] Hard**

> A mobile app needs logged-in users to upload photos directly to an S3 bucket without embedding AWS credentials in the app itself. Which Cognito component makes this possible?
>
> **A.** User pool alone
> **B.** Identity pool, typically combined with a user pool for authentication first
> **C.** IAM user created per mobile device
> **D.** AWS Secrets Manager
>
**14. [Scenario / Judgment] Hard**

> A design requires an RDS database password to rotate automatically every 30 days with no manual intervention. Which service directly supports this out of the box?
>
> **A.** AWS Secrets Manager
> **B.** Systems Manager Parameter Store (standard tier)
> **C.** Amazon Cognito
> **D.** AWS IAM

**15. [Scenario / Judgment] Hard**

> A company enables default encryption on an S3 bucket using an AWS managed key, then later decides they need to control exactly who can use that key and revoke access at will. What should they switch to?
>
> **A.** There's no way to gain that level of control in AWS
> **B.** A customer managed KMS key, which they create and control, including its access policy and lifecycle
> **C.** Turning off encryption entirely
> **D.** Amazon Cognito identity pools

**16. [Scenario / Judgment] Hard**

> Why is creating an individual IAM user for every customer of a public-facing application considered the wrong approach, beyond just being unworkable at scale?
>
> **A.** IAM users are actually designed for exactly this use case
> **B.** IAM users are built for managing AWS resources, not for general public authentication — customers should never need any level of AWS access at all
> **C.** IAM has a hard limit of ten users per account
> **D.** IAM users cannot have passwords, only access keys

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Cognito user pools and identity pools do the same thing, so you only need one." Correct this using this module's content.
>
> **A.** They're right — the two are interchangeable
> **B.** They solve different problems: user pools handle authentication (who is this person, via sign-in tokens), while identity pools handle authorization (temporary AWS credentials) — they're commonly used together precisely because they're not redundant
> **C.** Identity pools replaced user pools and user pools are deprecated
> **D.** User pools are only for mobile apps, and identity pools are only for web apps

**18. [Scenario / Judgment] Very Hard**

> A design stores customer data encrypted at rest via KMS, and all traffic between the client and the application is sent over plain HTTP. Is this design's data protection complete?
>
> **A.** Yes — encryption at rest is the only protection that matters
> **B.** No — encryption at rest and encryption in transit are different protections; without TLS/HTTPS, data is exposed while moving across the network even though it's protected while stored
> **C.** No, because KMS also requires HTTPS to function at all
> **D.** Yes, as long as the S3 bucket is private

**19. [Scenario / Judgment] Very Hard**

> A team debates Secrets Manager versus Parameter Store for a set of application configuration values that are not sensitive and never change automatically. Which is the more cost-appropriate choice, and why?
>
> **A.** Secrets Manager, because it's always the more secure option regardless of cost
> **B.** Parameter Store, because its free tier fits non-sensitive values that don't need automatic rotation — Secrets Manager's per-secret cost is better justified for credentials that actually need rotation
> **C.** Neither — configuration values should always be hardcoded
> **D.** Secrets Manager, because Parameter Store cannot store any string values

**20. [Scenario / Judgment] Very Hard**

> Connect this module back to Module 3. A café administrator needs to manage AWS resources through the console, while a café customer needs to log into the ordering website. Explain why the same identity system can't serve both, using this module's core distinction.
>
> **A.** It can — both should just be IAM users
> **B.** IAM is built to manage access to AWS itself, for people and services administering the account; Cognito is built to authenticate an application's end users, who should never need any AWS access at all — conflating the two would either over-grant customers AWS access or force administrators through a system not built for managing AWS permissions
> **C.** Cognito is simply a newer replacement for IAM in every use case
> **D.** The distinction is only a licensing difference, not a functional one

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
