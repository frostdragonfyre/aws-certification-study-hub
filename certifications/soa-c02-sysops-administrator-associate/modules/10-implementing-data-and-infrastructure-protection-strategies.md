# Module 10: Implementing Data and Infrastructure Protection Strategies

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Module 9 set the guardrails for who can do what, and made sure Meridian stays compliant with them continuously. This module gets more concrete: protecting the data itself, controlling network traffic at every layer, and keeping secrets out of code and config files. This is Domain 4's second and final task, closing out Domain 4.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish an AWS managed key from a customer managed key in AWS KMS
- Explain how a KMS key policy and an IAM policy work together to control key access
- Distinguish Security Groups from Network ACLs, and know when each fits
- Distinguish AWS Secrets Manager from Systems Manager Parameter Store
- Design a data and network protection strategy for a stated requirement

---

## KMS: AWS Managed Keys vs. Customer Managed Keys

**AWS Key Management Service (KMS)** manages the encryption keys behind encryption at rest for services like S3, EBS, and RDS. Not every key is the same, though: an **AWS managed key** is created and managed entirely by AWS on your behalf — you don't control its rotation schedule (AWS rotates it automatically, roughly yearly) or its key policy, and you can't share it across accounts. A **customer managed key (CMK)** is created and controlled by you: you define the key policy, choose whether rotation is automatic or manual, can disable or schedule deletion of the key, and can share it across accounts for cross-account access to encrypted resources.

Access to a KMS key is controlled by its **key policy** — a resource-based policy attached directly to the key — working alongside any IAM policy the principal has. Similar to the IAM-and-SCP relationship from Module 9, both have to allow the action: the key policy has to permit the principal's access to the key, and the principal's IAM policy has to permit the KMS action, for a request to actually succeed.

> ⚠️ **Exam trap:** a scenario requiring cross-account access to an encrypted resource, custom key rotation control, or the ability to disable or schedule deletion of a key is describing a **customer managed key**, not an AWS managed key — AWS managed keys can't be shared across accounts or have their rotation customized. And a scenario where a principal has full IAM permissions for a KMS action but is still denied access is pointing at the **key policy** not granting that access — both the key policy and the IAM policy have to allow it.

## Security Groups vs. Network ACLs

Both Security Groups and Network ACLs control traffic in and out of a VPC, and both are frequently confused because they sound like they do the same job. They operate at different layers with fundamentally different behavior.

A **Security Group** operates at the **instance level**, is **stateful** (a response to an allowed inbound request is automatically allowed back out, with no separate outbound rule needed), and can only contain **Allow** rules — there's no way to explicitly deny traffic with a Security Group, only omit an Allow. A **Network ACL (NACL)** operates at the **subnet level**, is **stateless** (inbound and outbound traffic each need their own explicit rule, since a response isn't automatically allowed), and supports both **Allow and Deny** rules, evaluated **in numbered order** until a match is found.

This difference in capability matters directly: if Priya needs to explicitly block traffic from a specific known-bad IP address while still allowing everything else, a Security Group can't do that — it has no Deny capability. A NACL, with a low-numbered Deny rule for that IP followed by a broader Allow rule, can.

> ⚠️ **Exam trap:** a scenario needing to explicitly **block** a specific IP address or CIDR range, while allowing other traffic, is describing a **NACL** — Security Groups have no Deny rules at all, only Allow. And a scenario where an instance's inbound and outbound traffic seem to behave asymmetrically — inbound is opened but outbound to the same destination doesn't automatically work — is pointing at NACL statelessness, since Security Groups (stateful) wouldn't cause that behavior.

## Secrets Manager vs. Systems Manager Parameter Store

Both **AWS Secrets Manager** and **Systems Manager Parameter Store** (in its `SecureString` type) can store sensitive values encrypted, and both are reasonable places to keep a value out of code. They diverge in one significant capability.

**Secrets Manager** is purpose-built for credentials that need to be rotated: it supports **automatic rotation** on a schedule, with built-in rotation logic for RDS, Redshift, and DocumentDB credentials (and a Lambda function for custom rotation logic elsewhere) — the secret's value changes on its own, and dependent applications retrieve the current value at runtime rather than relying on something that was hardcoded or cached indefinitely. **Parameter Store SecureString** stores an encrypted value too, at a lower cost, but has no built-in automatic rotation of its own — rotating a Parameter Store value means writing and scheduling that logic yourself (or integrating with Secrets Manager for the rotation piece).

> ⚠️ **Exam trap:** a scenario emphasizing that a database credential (or another secret) needs to be **rotated automatically on a schedule**, with minimal custom engineering, is describing **Secrets Manager**. A scenario storing a simple, non-rotating configuration value or secret where cost is the deciding factor is often better fit by **Parameter Store SecureString** — reaching for Secrets Manager's added cost and complexity when nothing actually needs to rotate isn't the efficient choice.

## Putting It Together: Protecting Meridian's Data and Network

Priya's protection strategy, closing out Domain 4:

- **Customer managed KMS keys** for Meridian Loyalty's and Ridgeline's databases, giving Priya control over rotation, cross-account sharing with the security team's audit account, and the ability to schedule key deletion if a system is decommissioned.
- **Security Groups** as the default instance-level control for normal allow-listed traffic, with **NACLs** layered at the subnet level specifically to explicitly block a small list of known-bad IP ranges.
- **Secrets Manager** for RDS credentials across all three systems, with automatic rotation configured — no hardcoded database passwords anywhere in application code.
- **Parameter Store SecureString** for simpler, non-rotating configuration values, keeping cost down where Secrets Manager's rotation capability isn't actually needed.

## What to skip

You don't need to memorize KMS's exact key policy JSON syntax or every NACL rule evaluation edge case — that's implementation depth beyond this exam. What matters is knowing AWS managed vs. customer managed key capabilities, Security Group vs. NACL statefulness and Allow/Deny behavior, and when Secrets Manager's rotation justifies its use over Parameter Store.

## Key takeaways

- A customer managed KMS key gives you control over rotation, cross-account sharing, and deletion; an AWS managed key doesn't — and both a key policy and an IAM policy must allow an action for it to succeed.
- Security Groups are stateful, instance-level, Allow-only; NACLs are stateless, subnet-level, and support both Allow and Deny rules evaluated in order.
- Secrets Manager supports automatic rotation for credentials that need it; Parameter Store SecureString is the lower-cost option when nothing needs to rotate.
- This closes Domain 4: Module 9 set the guardrails and continuous compliance checks, and Module 10 protected the data and network traffic directly.

## Further reading

- [AWS KMS Concepts: Customer Keys and AWS Keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-mgmt) — AWS managed vs. customer managed keys.
- [Key Policies in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) — how key policies and IAM policies work together.
- [Security Groups vs. Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-comparison.html) — a direct side-by-side comparison.
- [AWS Secrets Manager Rotation](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) — automatic rotation for supported and custom secrets.
