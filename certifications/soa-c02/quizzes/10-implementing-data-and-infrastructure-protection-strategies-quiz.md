**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 10 Knowledge Check**

Implementing Data and Infrastructure Protection Strategies · 20 questions · Practice — not graded

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

> An AWS managed KMS key can be shared across accounts with custom rotation control.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which VPC traffic control operates at the subnet level and supports both Allow and Deny rules?

> **A.** Security Group
> **B.** Network ACL
> **C.** IAM policy
> **D.** KMS key policy

**3. [Fill in the Blank] Easy**

> A ____________ key is created and controlled by you, including its rotation schedule, key policy, and cross-account sharing.

**4. [Multiple Choice] Easy**

> Which AWS service supports built-in automatic rotation for RDS, Redshift, and DocumentDB credentials?

> **A.** Systems Manager Parameter Store
> **B.** AWS Secrets Manager
> **C.** AWS KMS
> **D.** Network ACLs

**5. [True / False] Easy**

> A Security Group can contain explicit Deny rules.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does a customer managed KMS key fit a requirement for cross-account access to an encrypted resource?

> **A.** AWS managed keys already support cross-account sharing by default
> **B.** Customer managed keys let you define the key policy, which can grant access to principals in other accounts — AWS managed keys can't be shared across accounts
> **C.** Cross-account access requires disabling encryption entirely
> **D.** Only Parameter Store supports cross-account access

**7. [Fill in the Blank] Moderate**

> A Security Group is ____________, meaning a response to an allowed inbound request is automatically allowed back out.

**8. [Multiple Choice] Moderate**

> Why can't a Security Group alone block traffic from a specific known-bad IP address while allowing everything else?

> **A.** Security Groups can only be applied to VPCs, not instances
> **B.** Security Groups only support Allow rules — there's no way to explicitly Deny traffic
> **C.** Security Groups are stateless, so blocking wouldn't work
> **D.** Security Groups can only block traffic, never allow it

**9. [True / False] Moderate**

> For a KMS action to succeed, both the key policy and the principal's IAM policy must allow it.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A team needs to store a simple, non-rotating configuration value at the lowest cost, with no automatic rotation requirement. What fits best?

> **A.** AWS Secrets Manager, since it's always the more secure option
> **B.** Systems Manager Parameter Store SecureString — lower cost, no rotation needed
> **C.** A Network ACL, since it can store encrypted values
> **D.** An AWS managed KMS key used directly as a secret store

**11. [Fill in the Blank] Moderate**

> Network ACL rules are evaluated in ____________ order until a matching rule is found.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A principal has an IAM policy granting full `kms:Decrypt` permission, but the KMS key's key policy doesn't grant that principal access. Can they decrypt data with that key?

> **A.** Yes, since the IAM policy alone is sufficient
> **B.** No — both the key policy and the IAM policy must allow the action; the key policy not granting access blocks the request regardless of IAM permissions
> **C.** Yes, since key policies only apply to key administrators
> **D.** It depends on whether the key is an AWS managed key or a customer managed key

**13. [Scenario / Judgment] Hard**

> An instance's inbound traffic on port 443 is allowed, but outbound responses to that same traffic seem to require a separate explicit rule to work. What does this describe?

> **A.** Security Group behavior, since Security Groups are stateless
> **B.** NACL behavior, since NACLs are stateless and require explicit rules for both directions
> **C.** This behavior is impossible in a VPC
> **D.** KMS key policy behavior applied to network traffic

**14. [Scenario / Judgment] Hard**

> A system is being decommissioned, and Priya needs to schedule deletion of the KMS key used to encrypt its data after a waiting period. What kind of key does this require?

> **A.** An AWS managed key, since AWS handles all key lifecycle decisions
> **B.** A customer managed key, since only customer managed keys can be disabled or have deletion scheduled by the customer
> **C.** Neither type of KMS key supports scheduled deletion
> **D.** A Parameter Store SecureString value instead of a KMS key

**15. [Scenario / Judgment] Hard**

> A database credential needs to rotate automatically every 30 days with minimal custom engineering, using AWS's built-in rotation logic. What fits best?

> **A.** Systems Manager Parameter Store SecureString, since it's the lower-cost option
> **B.** AWS Secrets Manager, using its built-in rotation support for the database type
> **C.** A Network ACL rule scheduled to rotate every 30 days
> **D.** An AWS managed KMS key configured for automatic rotation of the credential

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Security Groups and NACLs both do the same job, so it doesn't matter which one you use." Correct this using this module's content.

> **A.** They're right — Security Groups and NACLs are fully interchangeable
> **B.** They're different: Security Groups are stateful, instance-level, and Allow-only, while NACLs are stateless, subnet-level, and support both Allow and Deny rules evaluated in order — a requirement to explicitly block specific traffic can only be met by a NACL
> **C.** NACLs are simply a faster version of Security Groups
> **D.** Security Groups support Deny rules; NACLs do not

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes using Secrets Manager for every stored value in the account, including static configuration values that never change, arguing "more rotation capability is always better." Evaluate this using this module's content.

> **A.** Agree — Secrets Manager should always be used regardless of whether rotation is needed
> **B.** Disagree — Parameter Store SecureString is the lower-cost fit when nothing actually needs to rotate; reaching for Secrets Manager's added cost and complexity for a static value doesn't add security value, it just adds expense
> **C.** Disagree, but only because Secrets Manager cannot store static values at all
> **D.** Agree, since Parameter Store cannot encrypt values at rest

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a scenario requiring cross-account access to an encrypted S3 bucket cannot be satisfied with an AWS managed KMS key.

> **A.** AWS managed keys already support cross-account access by default, so this scenario has no real constraint
> **B.** AWS managed keys are created and controlled entirely by AWS — you don't control their key policy, and they cannot be shared across accounts, so a cross-account access requirement needs a customer managed key where the key policy can grant access to another account's principals
> **C.** S3 cannot use KMS encryption at all, regardless of key type
> **D.** Cross-account access requires disabling KMS encryption entirely

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that since Security Groups are stateful and easier to configure, NACLs are essentially obsolete and should never be used. Argue against this using this module's content.

> **A.** Agree — NACLs serve no purpose that Security Groups don't already cover
> **B.** Disagree — NACLs provide a capability Security Groups fundamentally lack: explicit Deny rules. A requirement to block a specific IP address or CIDR range while allowing other traffic can only be met with a NACL, since Security Groups have no Deny capability at all
> **C.** Disagree, but only because NACLs are required by AWS for every subnet
> **D.** Agree, since NACLs and Security Groups both operate at the instance level

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as a KMS key exists and the resource is encrypted, access is automatically controlled correctly — no additional configuration is needed." Evaluate this claim using this module's content.

> **A.** Agree — encryption alone fully controls who can access the data
> **B.** Disagree — a KMS key's access is controlled by its key policy working alongside IAM policies; a key without a correctly configured key policy could either block legitimate access or, if misconfigured too permissively, fail to restrict access as intended — encryption existing isn't the same as access being correctly controlled
> **C.** Disagree, but only because KMS keys cannot be attached to encrypted resources
> **D.** Agree, since IAM policies are irrelevant once KMS encryption is enabled

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
