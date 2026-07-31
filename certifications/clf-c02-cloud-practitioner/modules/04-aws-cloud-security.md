# Module 4: AWS Cloud Security

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 2 — Security and Compliance (30% of the exam — the heaviest single domain)
**Estimated study time:** 45 minutes

## Why this matters

Module 1 introduced the Shared Responsibility Model as a preview. This module is where it earns its weight — Domain 2 is the largest single domain on the exam, and nearly every question in it traces back to one question: whose side of the line is this on, AWS's or the customer's? Get comfortable answering that, and most of Domain 2 becomes recognition rather than memorization.

The rest of this module is a practical toolkit for the customer's half of that line — the part you actually control. Cloud security isn't primarily about exotic attacks; it's overwhelmingly about identity (who can do what), configuration (is it locked down correctly), and visibility (would you notice if something went wrong). Everything below maps to one of those three.

## Learning objectives

By the end of this module, you should be able to:

- State the Shared Responsibility Model and correctly sort a given task as AWS's job or yours
- Explain how the responsibility line shifts between self-managed (IaaS) and managed services
- Describe IAM's building blocks — users, groups, roles, and policies — and the principle of least privilege
- Explain AWS root account best practices and why MFA matters everywhere, not just on root
- Distinguish threat detection (GuardDuty) from vulnerability and data scanning (Inspector, Macie)
- Distinguish active defense (WAF, Shield) from encryption (KMS) from the historical audit trail (CloudTrail, Config)
- Explain what AWS Artifact is for
- Avoid the most common cloud-security traps on the exam

---

## The Shared Responsibility Model

This is the single most important security concept on the exam, and the line is simple to state but easy to misjudge under pressure:

- **AWS is responsible for security *of* the cloud** — the physical data centers, the global network, the hardware, and the virtualization layer (the hypervisor) that isolates one customer's resources from another's.
- **You are responsible for security *in* the cloud** — your data, your IAM configuration, patching (where applicable), and your firewall/security-group configuration.

| Task | Whose job |
|---|---|
| Physical security of the data center building | AWS |
| Patching the underlying hypervisor | AWS |
| Maintaining the global network infrastructure | AWS |
| Physically destroying decommissioned hardware | AWS |
| Configuring security groups and network ACLs | Customer |
| Creating and managing IAM users, groups, and permissions | Customer |
| Deciding whether to encrypt data, and managing the keys | Customer |
| Classifying your own data as sensitive or public | Customer |
| Enabling MFA on your account | Customer |

> ⚠️ **Exam trap:** a question describing a misconfigured security group, an unpatched guest OS, or an overly permissive IAM policy is always describing a *customer* failure — never AWS's — no matter how the scenario is dressed up. If a customer clicking a different setting would have fixed it, it's the customer's responsibility.

## Does the Line Move? IaaS vs. Managed Services

The line isn't fixed — it shifts depending on how managed a service is, though one part of it never moves.

On **EC2** (IaaS), the customer patches the guest operating system, configures the instance-level firewall, and manages everything from the OS up. On **Amazon RDS** (a managed database service), AWS takes over patching the database engine and underlying OS — work that would otherwise land on the customer with a self-managed database on EC2.

What *doesn't* change, regardless of how managed the service is: the customer always controls IAM permissions, always owns their data, and always decides what's stored and who can reach it. Moving to a more managed service shrinks how much infrastructure the customer has to maintain — it doesn't erase the customer's side of the line entirely.

> ⚠️ **Exam trap:** "we moved to a managed service, so security is now AWS's job" is a common wrong inference. Managed services shift the *infrastructure* portion of responsibility toward AWS; they never shift IAM, data, or access control off the customer's plate.

## Identity and Access Management (IAM)

IAM controls **who** can do **what**, and it's built from four pieces:

| Piece | What it is |
|---|---|
| User | An identity for a person or application |
| Group | A collection of users that share the same permissions |
| Role | A set of temporary permissions that can be assumed — no long-term credentials attached |
| Policy | The actual document (in JSON) that defines what's allowed or denied |

The organizing principle behind all four is **least privilege** — grant only the permissions a user or role actually needs to do its job, nothing more. A new employee who needs access to a single S3 bucket should get a policy scoped to that one bucket, not broad account access "to be safe."

> ⚠️ **Exam trap:** "least privilege" questions test whether you'll reach for a narrowly scoped policy or a broad one. The exam consistently rewards the narrower answer — over-permissioning is treated as a security failure, not a convenience.

## Root Account Best Practices

Every AWS account has a root user created at signup, and it has unrestricted access to everything in the account — which is exactly why it shouldn't be used for daily work.

- **Enable MFA on root immediately** — this is one of the single most important habits in this entire course.
- **Don't use root for day-to-day tasks.** Create an IAM user or role with only the permissions needed, and use that instead.
- **Lock root away** for the small number of tasks that genuinely require it (like changing a support plan or closing an account), rather than keeping it in daily rotation.

> ⚠️ **Exam trap:** a scenario describing someone using root credentials for routine work is describing a best-practice violation, not a tool-selection question. The "fix" is a practice change (stop using root day-to-day, enable MFA, use IAM instead), not a specific AWS service.

## Detecting Threats: Amazon GuardDuty

GuardDuty continuously monitors an account for suspicious or malicious behavior — for example, an EC2 instance suddenly communicating with a known malicious IP address — using automated threat intelligence. It answers the question "is something bad happening *right now*," which distinguishes it from the scanning services below, which look for weaknesses *before* something happens.

## Scanning for Weaknesses: Inspector and Macie

Two services scan for different kinds of problems before they become incidents:

- **Amazon Inspector** scans EC2 instances and container images for known software vulnerabilities.
- **Amazon Macie** uses machine learning to scan Amazon S3 for sensitive data — like personally identifiable information — that may have ended up somewhere it shouldn't be.

> ⚠️ **Exam trap:** GuardDuty, Inspector, and Macie get mixed up constantly. GuardDuty detects behavior happening now; Inspector scans for known vulnerabilities in compute; Macie scans for sensitive data in storage. Three different jobs, three different tenses (now vs. before vs. what's actually stored).

## Defending Public-Facing Applications: WAF and Shield

- **AWS WAF** filters malicious web traffic in front of an application — the standard answer for something like repeated SQL injection attempts through a login form.
- **AWS Shield** protects against DDoS (distributed denial-of-service) attacks — the standard answer for a massive volumetric traffic flood meant to take a service offline.

## Encrypting Data: AWS KMS

AWS Key Management Service (KMS) creates and manages the encryption keys used to protect data at rest. The exam cue is control: when a scenario specifically wants the ability to control and rotate encryption keys, KMS is the answer.

## Proving Compliance: AWS Artifact

AWS Artifact provides on-demand access to AWS's own compliance reports and certifications (like SOC reports or HIPAA eligibility documentation) — useful when a customer needs to prove to an *external* auditor that AWS itself meets a given compliance standard, without waiting on a support ticket.

## The Audit Trail: CloudTrail and Config

Two services answer "what happened, and who did it":

- **AWS CloudTrail** logs *who* called which API, when, and from where.
- **AWS Config** tracks *what* a resource's configuration looked like over time.

A question asking for a historical record of exactly when a security group changed, and by whom, is really asking for both — Config for the "what changed and when," CloudTrail for the "who did it."

## Defense in Depth

No single control should be the only thing standing between an account and a breach. A well-designed account stacks several of the tools above together — IAM for access control, security groups for network-level filtering, WAF and Shield for public-facing defense, KMS for data protection, and CloudTrail/Config/GuardDuty for visibility — so that one failed or misconfigured layer doesn't mean total exposure. This layering is a deliberate design choice, not paranoia, and it's the same instinct behind spreading an application across multiple Availability Zones in Module 3: don't let any single point carry all the risk.

---

## What to skip

You don't need to write actual IAM policy JSON from scratch, configure a real WAF rule set, or memorize every field GuardDuty can flag — that hands-on depth belongs to the Solutions Architect Associate exam. For Cloud Practitioner, focus on matching a scenario to the right service and correctly sorting a task as AWS's responsibility or the customer's.

## Key takeaways

- The Shared Responsibility Model splits security into "of the cloud" (AWS: physical, hardware, network, hypervisor) and "in the cloud" (you: data, IAM, patching where applicable, configuration) — misconfiguration is always the customer's responsibility.
- The responsibility line moves based on how managed a service is, but IAM, data, and access control never move to AWS's side, no matter how managed the service is.
- IAM is built from users, groups, roles, and policies, organized around the principle of least privilege.
- Root account credentials should be locked away with MFA enabled and reserved for rare tasks — daily work belongs to an IAM user or role.
- GuardDuty detects threats happening now; Inspector scans compute for known vulnerabilities; Macie scans S3 for sensitive data — three different jobs, easy to conflate.
- WAF blocks malicious web traffic; Shield protects against DDoS; KMS manages encryption keys — defense and encryption are different jobs from detection and scanning.
- AWS Artifact provides compliance proof; CloudTrail and Config together provide the historical audit trail of who did what and what changed.

## Further reading

- [AWS Identity and Access Management](https://aws.amazon.com/iam/) — official IAM documentation, including least-privilege guidance.
- [Shared Responsibility Model](https://aws.amazon.com/compliance/shared-responsibility-model/) — AWS's own explanation, useful for double-checking the line for a specific service.
- [AWS Security, Identity, and Compliance services](https://aws.amazon.com/products/security/) — a full list of the services introduced in this module, for anyone who wants to go deeper before the Solutions Architect Associate exam.

*Service capabilities mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 3 — AWS Global Infrastructure Overview](03-aws-global-infrastructure-overview.md) · **Next:** [Module 5 — Networking and Content Delivery](05-networking-and-content-delivery.md) · **Quiz:** [Module 4 Quiz](../quizzes/04-aws-cloud-security-quiz.md) · **Activity:** [Module 4 Activity](../labs/04-aws-cloud-security-activity.md)
