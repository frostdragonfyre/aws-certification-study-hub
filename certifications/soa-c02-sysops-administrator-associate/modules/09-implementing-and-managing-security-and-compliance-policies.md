<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](08-automating-manual-and-repeatable-processes.md) · [Next module](10-implementing-data-and-infrastructure-protection-strategies.md) · [Quiz](../quizzes/09-implementing-and-managing-security-and-compliance-policies-quiz.md) · [Slides](../lectures/09-implementing-and-managing-security-and-compliance-policies.pptx)
<!-- /hub-navigation -->

# Module 9: Implementing and Managing Security and Compliance Policies

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Domain 3 made sure Meridian's infrastructure gets created consistently and operates without constant manual intervention. Domain 4 asks whether that infrastructure is actually secure and compliant — not just once, at launch, but continuously, across every account Meridian operates. This module opens Domain 4 with Task 4.1: setting the guardrails that define what's allowed, and continuously checking whether reality still matches them.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish an IAM policy from a Service Control Policy, and explain what each one actually controls
- Explain how AWS Config continuously evaluates resource configuration against defined rules
- Describe how Config rules can trigger automatic remediation
- Explain what AWS Security Hub aggregates, and what it doesn't replace
- Design a security and compliance strategy for a stated multi-account requirement

---

## IAM Policies vs. Service Control Policies

Both IAM policies and Service Control Policies (SCPs) look similar — JSON documents with Allow and Deny statements — which is exactly why they're easy to confuse. They control fundamentally different things.

An **IAM policy** (attached to a user, group, or role) is what actually **grants** permissions — without an IAM policy allowing an action, a principal can't perform it, full stop. A **Service Control Policy**, managed through **AWS Organizations** and applied to an account or an organizational unit (OU), does something different: it sets the **maximum available permissions** for every principal in that account, but an SCP **never grants permissions on its own** — it can only restrict what IAM policies within the account are allowed to grant.

This means a principal needs *both* an IAM policy that allows an action *and* no SCP that denies it. An SCP that denies `s3:DeleteBucket` for an entire OU blocks every principal in every account under that OU from deleting a bucket, no matter how permissive their individual IAM policies are — the SCP is an outer boundary, not a grant.

> ⚠️ **Exam trap:** a scenario describing an organization-wide restriction — "no account in this OU should ever be able to disable CloudTrail" or "block all accounts from using non-approved Regions" — is describing an **SCP**, applied at the Organizations level, not an IAM policy attached to individual users or roles. Conversely, a scenario asking to grant a specific user permission to perform an action is an **IAM policy** question — SCPs alone can never grant anyone permission to do anything.

## AWS Config: Continuous Compliance Evaluation

A resource that was compliant at launch doesn't necessarily stay that way — someone widens a security group, disables encryption on a new S3 bucket, or launches an EC2 instance without required tags. **AWS Config** continuously records resource configuration changes and evaluates them against **Config rules** — either AWS-managed (like requiring S3 buckets to have encryption enabled) or custom rules backed by a Lambda function — flagging each resource as **compliant** or **non-compliant** on an ongoing basis, not just at a single point in time.

This is a different kind of check than CloudFormation drift detection: drift detection compares resources against a specific CloudFormation template; Config evaluates resources against organization-wide compliance rules, regardless of whether they were created through CloudFormation at all.

Critically, Config rules can be paired with **automatic remediation** — when a resource is found non-compliant, Config can trigger an SSM Automation runbook (the same mechanism from Module 8) to fix it, closing the loop from detection to correction without a person in between.

> ⚠️ **Exam trap:** a scenario asking how to continuously verify that resources across the organization stay compliant with a security standard — not just at creation, but on an ongoing basis — is describing **AWS Config rules**, not CloudFormation drift detection (which only compares against a specific stack's template) and not a one-time manual audit. If the scenario adds that non-compliant resources should be fixed automatically, that's Config paired with SSM Automation remediation.

## Security Hub: One View, Many Sources

Meridian's accounts generate security signal from multiple places — GuardDuty findings, Config compliance results, Inspector vulnerability scans, IAM Access Analyzer results — and checking each service's own console separately doesn't scale across dozens of accounts. **AWS Security Hub** aggregates findings from these services (and partner security tools) into a single, standardized view, and scores accounts against compliance **standards** like CIS AWS Foundations Benchmark or PCI DSS.

What Security Hub does *not* do is replace the underlying detection services — it doesn't generate its own threat findings the way GuardDuty does, and it doesn't independently evaluate resource configuration the way Config does. Security Hub is an aggregation and scoring layer sitting on top of those services, not a substitute for turning them on in the first place.

> ⚠️ **Exam trap:** a scenario asking how to get a single, consolidated view of security findings from GuardDuty, Config, and Inspector across many accounts is describing **Security Hub**. But a scenario implying that enabling Security Hub alone — without GuardDuty, Config, or Inspector actually running — would still generate threat detection or configuration findings is a misunderstanding: Security Hub aggregates and scores what those services report, it doesn't generate that detection itself.

## Putting It Together: Security and Compliance at Meridian

Priya's strategy, opening Domain 4:

- **SCPs** at the Organizations level enforcing hard boundaries — no disabling CloudTrail, no launching resources outside approved Regions — regardless of what any individual account's IAM policies allow.
- **IAM policies** granting the specific, least-privilege permissions each team actually needs, within whatever boundary the SCPs allow.
- **AWS Config rules** continuously evaluating every account for required encryption, tagging, and configuration standards, with **automatic remediation** through SSM Automation for well-understood fixes.
- **Security Hub** aggregating GuardDuty, Config, and Inspector findings across every Meridian account into one dashboard, scored against the CIS AWS Foundations Benchmark.

## What to skip

You don't need to memorize every AWS-managed Config rule or the full CIS Benchmark control list — that's implementation depth beyond this exam. What matters is knowing that SCPs restrict but never grant, that Config evaluates compliance continuously (and can trigger remediation), and that Security Hub aggregates and scores findings rather than generating them itself.

## Key takeaways

- IAM policies grant permissions; SCPs set a maximum boundary and can only restrict, never grant — a principal needs both an allowing IAM policy and no blocking SCP.
- AWS Config continuously evaluates resource configuration against rules, distinct from CloudFormation drift detection, and can trigger automatic remediation through SSM Automation.
- Security Hub aggregates and scores findings from GuardDuty, Config, Inspector, and more — it doesn't replace those services or generate detection on its own.
- This opens Domain 4 — security and compliance policy. Module 10 covers the second half: protecting data and infrastructure directly.

## Further reading

- [Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) — maximum available permissions at the organization level.
- [What Is AWS Config?](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) — continuous configuration recording and rule evaluation.
- [Remediating Noncompliant AWS Config Rules with AWS Systems Manager Automation](https://docs.aws.amazon.com/config/latest/developerguide/remediation.html) — closing the loop from detection to fix.
- [What Is AWS Security Hub?](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) — aggregating findings and compliance standards.
