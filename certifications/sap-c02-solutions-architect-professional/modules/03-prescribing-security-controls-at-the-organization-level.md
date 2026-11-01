<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](02-architecting-network-connectivity-strategies.md) · [Next module](04-designing-reliable-and-resilient-architectures.md) · [Quiz](../quizzes/03-prescribing-security-controls-at-the-organization-level-quiz.md) · [Slides](../lectures/03-prescribing-security-controls-at-the-organization-level.pptx)
<!-- /hub-navigation -->

# Module 3: Prescribing Security Controls at the Organization Level

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 2 gave Café Sol, Haven & Co., and Ridgeline a way to reach each other. That's a problem on its own now: connectivity without governance means any engineer on any brand's team who can reach the shared Transit Gateway hub can potentially reach further than they should. Security at the associate level meant securing one account — IAM users, roles, security groups, one account's worth of policy. Security at the organization level means deciding what's allowed *before* any individual account's administrator gets a chance to misconfigure it, and proving that decision holds consistently across every account Meridian owns, including ones that don't exist yet.

This module covers Task 1.2: prescribing security controls that apply across an entire AWS Organization, not just within one account.

## Learning objectives

By the end of this module, you should be able to:

- Explain what a Service Control Policy (SCP) does and does not do, and how it differs from an IAM policy
- Describe how AWS Organizations organizational units (OUs) let policies apply to groups of accounts
- Explain what AWS IAM Identity Center provides for centralized, cross-account identity
- Distinguish preventive and detective guardrails, and how AWS Control Tower applies both
- Explain the cross-account role pattern and why it's preferred over sharing long-lived credentials

---

## Service Control Policies: Setting the Outer Boundary

A **Service Control Policy (SCP)** is a policy type in AWS Organizations that sets the maximum available permissions for accounts within an organizational unit (OU) or the whole organization. SCPs are the mechanism Meridian's central security team uses to say "no account in this organization can ever do X," regardless of what any individual account's own IAM policies allow.

The single most important thing to understand about SCPs, and the thing the exam tests hardest: **an SCP never grants permissions by itself.** It only sets a ceiling. A user or role still needs an actual IAM policy granting a permission for that permission to be usable — the SCP just determines whether that IAM policy's grant is allowed to take effect at all. An account with full administrator IAM permissions, sitting under an SCP that denies `ec2:TerminateInstance` organization-wide, still cannot terminate an EC2 instance — the SCP's denial wins, regardless of how permissive the account's own IAM policies are.

> ⚠️ **Exam trap:** a scenario describing "we attached an SCP allowing S3 access, but users still can't access S3" is testing this exact misunderstanding. The fix isn't the SCP — it's that the SCP was never going to grant access on its own; an IAM policy inside the account still has to grant it too. SCPs restrict; they don't provision.

## Organizational Units: Applying Policy to Groups of Accounts

Meridian doesn't want to attach the same SCP individually to Café Sol's account, Haven & Co.'s account, and Ridgeline's future account one at a time — that doesn't scale, and it's easy to miss an account when policy changes. **Organizational units (OUs)** in AWS Organizations let accounts be grouped, and policies attached at the OU level apply to every account inside it, including accounts added later.

A typical structure separates accounts by purpose and risk: a **Security OU** for the accounts running centralized logging and security tooling, holding the strictest SCPs; a **Production OU** (potentially with one child OU per brand) holding each brand's live customer-facing workloads; and a **Sandbox OU** for experimentation, where engineers can safely try things that would be dangerous in production, under looser — but not absent — SCPs. OUs nest, so policy can be layered: an org-wide SCP applies everywhere, a Production-OU SCP adds stricter rules on top for every brand's live environment, and so on.

## AWS IAM Identity Center: One Identity, Many Accounts

Without a centralized identity solution, Sofía's team would need a separate IAM user, with a separate password, in every one of Meridian's AWS accounts — Café Sol's, Haven & Co.'s, and eventually Ridgeline's. That doesn't scale either, and it means offboarding someone requires remembering to remove their access from every account individually.

**AWS IAM Identity Center** (the successor to AWS Single Sign-On) solves this: users sign in once, to one central identity source, and are granted access to specific AWS accounts through **permission sets** — reusable collections of permissions assigned to a user or group for a specific account. Sofía's team gets one set of credentials, one login, and access scoped per account through permission sets rather than per-account IAM users. Adding access to a new account (like Ridgeline's, once it's created) means assigning an existing permission set to it — not creating and distributing new credentials.

## Preventive and Detective Guardrails: AWS Control Tower

**AWS Control Tower** sets up and manages a multi-account environment — a "landing zone" — with a baseline set of guardrails applied automatically. Guardrails come in two types, and the exam expects you to tell them apart:

- **Preventive guardrails** stop an action from happening at all, implemented under the hood using SCPs. If a preventive guardrail disallows disabling CloudTrail logging, no user in any governed account — however permissive their own IAM policy — can actually disable it.
- **Detective guardrails** don't block anything; they continuously evaluate accounts for compliance (implemented using AWS Config rules) and flag or report on violations after the fact. A detective guardrail can identify that an S3 bucket was made public, without having prevented it from happening.

Both matter, and for different reasons: preventive guardrails stop the worst mistakes outright, while detective guardrails catch the things that can't practically be prevented in advance (like a resource configuration drifting out of compliance over time) so they can be remediated.

> ⚠️ **Exam trap:** "must be blocked from ever happening" is preventive. "Must be detected and reported if it happens" is detective. A scenario asking for *both* — block what can be blocked, and report on everything else — is describing Control Tower's actual default behavior, not an either/or choice.

## Cross-Account Roles: Access Without Shared Credentials

Once Meridian's accounts are connected and centrally governed, engineers and automated processes still need an actual mechanism to act across account boundaries — for example, a monitoring tool in the Security OU account that needs to read CloudWatch metrics from Café Sol's account. The wrong way to do this is creating an IAM user in Café Sol's account and sharing its long-lived access keys with the Security account. Long-lived shared credentials are hard to rotate, hard to audit per-user, and a single leak compromises every account that credential set touches.

The correct pattern is a **cross-account IAM role**: Café Sol's account creates a role with a trust policy allowing a specific principal (a role or account) in the Security account to assume it, and that role's own permissions define exactly what the assumed session can do. The Security account's principal calls `sts:AssumeRole`, receives short-lived temporary credentials scoped to that role, and those credentials expire automatically. No long-lived secret is ever shared between accounts, every assumption is individually logged in CloudTrail, and the permissions granted are exactly and only what the role defines — nothing more.

## Putting It Together: Meridian's Organization-Level Security Design

Sofía's security control design for Meridian combines every piece from this module:

- An OU structure with a **Security OU**, a **Production OU** (with Café Sol and Haven & Co. as member accounts today, Ridgeline to follow), and a **Sandbox OU**, each with SCPs scoped to its actual risk level.
- **AWS Control Tower** managing the landing zone, with preventive guardrails blocking the highest-risk misconfigurations outright (like disabling account-level logging) and detective guardrails flagging everything else that can't practically be prevented up front (like an S3 bucket becoming public).
- **AWS IAM Identity Center** as the single sign-on source for every Meridian engineer, with permission sets scoped per account — so Sofía's team gets exactly the access each person needs in each brand's account, from one login.
- **Cross-account IAM roles** for every legitimate need to act across account boundaries — like the Security OU's monitoring tooling reading metrics from each brand's account — with no long-lived credentials shared between accounts anywhere in the design.

## What to skip

You don't need to memorize specific Control Tower guardrail names or write SCP JSON syntax from scratch — that's implementation depth beyond this exam. What matters is the SCP-doesn't-grant-permissions distinction, how OUs let policy scale across accounts, what Identity Center actually centralizes, preventive versus detective guardrails, and why cross-account roles replace shared credentials.

## Key takeaways

- SCPs set a maximum permission ceiling for accounts in an OU or organization; they never grant permissions on their own — an IAM policy inside the account still has to grant the actual permission.
- Organizational units let policy apply to groups of accounts, including accounts added later, instead of requiring per-account policy management.
- AWS IAM Identity Center provides one central sign-on, with permission sets scoping exactly what each user can do in each assigned account.
- Preventive guardrails (SCP-based) block an action outright; detective guardrails (AWS Config–based) flag violations after the fact. AWS Control Tower applies both as part of managing a multi-account landing zone.
- Cross-account IAM roles, assumed via `sts:AssumeRole` for short-lived temporary credentials, are the correct way to grant access across account boundaries — never long-lived shared credentials.

## Further reading

- [AWS Organizations: Service Control Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) — how SCPs set permission boundaries across an organization.
- [AWS IAM Identity Center User Guide](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) — centralized identity and permission sets.
- [AWS Control Tower How It Works](https://docs.aws.amazon.com/controltower/latest/userguide/how-control-tower-works.html) — preventive and detective guardrails in a managed landing zone.
- [IAM Roles for Cross-Account Access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) — the `sts:AssumeRole` pattern.
