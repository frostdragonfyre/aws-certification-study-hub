# Module 5: Designing a Multi-Account AWS Environment

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Every module so far has quietly assumed Meridian already has a sensible account structure — a Security OU here, a Production OU there, an account for Café Sol, an account for Haven & Co. It's time to actually design that structure deliberately, rather than assume it into existence. This module closes out Domain 1 by covering how the accounts themselves get created and organized, how activity across all of them gets logged in one place, how resources get tagged consistently enough to actually track cost and ownership, and how billing gets consolidated across every brand Meridian owns.

This is Task 1.4: designing the multi-account environment itself — the foundation everything in Modules 2 through 4 was quietly built on top of.

## Learning objectives

By the end of this module, you should be able to:

- Describe the foundational accounts a Control Tower landing zone establishes, and what each one is responsible for
- Explain what AWS Control Tower's Account Factory automates when provisioning a new account
- Explain what AWS Organizations tag policies enforce, and why consistent tagging matters at scale
- Describe how an organization trail centralizes CloudTrail logging across every account
- Explain how AWS Organizations consolidates billing across accounts while preserving per-account cost visibility

---

## The Landing Zone: Foundational Accounts

A **landing zone** is the governed multi-account environment a new AWS Organization starts from — not just any collection of accounts, but a deliberately structured one with a small number of foundational accounts already in place before any brand's workload account is created:

- The **management account** (sometimes called the payer account) is where the AWS Organization itself lives — it's used to create and manage member accounts, consolidate billing, and apply organization-wide policy. It's intentionally kept nearly empty of actual workloads, since compromising the management account would threaten the entire organization.
- A **Log Archive account** exists solely to receive and store logs — CloudTrail events, Config history, and similar audit data — from every other account in the organization, in one centralized, access-restricted location.
- An **Audit account** (sometimes combined with, sometimes separate from, Log Archive) holds security tooling with read access across the organization, used by the security team to review and investigate activity without needing standing access inside each brand's own workload accounts.

Meridian's Security OU from Module 3 is exactly where these foundational accounts live — Log Archive and Audit specifically, separate from the Production OU holding Café Sol's and Haven & Co.'s actual customer-facing workloads.

> ⚠️ **Exam trap:** a scenario emphasizing that workload accounts should never hold long-term audit logs, or that security review shouldn't require standing access inside every workload account, is describing the Log Archive/Audit account separation — not a permissions problem to solve with more granular IAM policy inside each workload account.

## AWS Control Tower Account Factory: Provisioning New Accounts Consistently

Every time Meridian adds a new brand — the way Ridgeline was added last quarter — a new AWS account has to be created, and that new account needs the same baseline guardrails, network configuration, and logging setup as every other account in its OU, applied consistently and without depending on someone remembering every manual step.

**AWS Control Tower's Account Factory** automates exactly this: provisioning a new account that's pre-configured with the landing zone's baseline — the right OU placement, the applicable SCPs and Control Tower guardrails from Module 3, standard networking, and logging already wired to the Log Archive account — from the moment it's created, rather than being manually configured (and potentially misconfigured, or forgotten) after the fact.

This matters specifically for Ridgeline's eventual AWS account: when it's created, Account Factory ensures it inherits Meridian's baseline automatically, the same way an OU-level SCP or backup policy does — one more piece of "governed by default, not governed by remembering to configure it correctly."

## Tag Policies: Enforcing Consistent Resource Tagging

Without a consistent tagging standard, cost allocation and ownership tracking across Meridian's three brands becomes guesswork — one team tags resources with `Environment=prod`, another with `env: production`, and neither AWS Cost Explorer nor an automated cleanup script can reliably tell that they mean the same thing.

**AWS Organizations tag policies** solve this at the organization level: a tag policy defines the allowed tag keys and values (for example, requiring a `CostCenter` tag with one of a specific set of values, and a `Brand` tag identifying which of Meridian's brands a resource belongs to), and can report on — or in stricter configurations, help prevent — resources that don't comply. Attached at the OU level like SCPs and backup policies, a tag policy keeps tagging consistent across every account without depending on each brand's team independently agreeing on a convention.

Consistent tagging is what makes the next two topics actually work: centralized logging is far less useful if you can't tell which brand's resource generated a given log entry, and consolidated billing is far less useful if costs can't be broken down by brand.

## Organization Trail: One CloudTrail, Every Account

SAA-C03 covered CloudTrail within a single account. At the organization level, **an organization trail**, created once from the management account, automatically captures CloudTrail events from every account in the organization — including accounts created later, like Ridgeline's — and delivers them to a single, centralized S3 bucket, typically in the Log Archive account established as part of the landing zone.

This means Meridian's security team never has to remember to enable CloudTrail in a new account, never has to aggregate logs from multiple accounts manually, and gets one consistent, tamper-resistant record of activity across the entire organization — member accounts can't disable or modify the organization trail's configuration, only the management account can.

## Consolidated Billing: One Bill, Per-Brand Visibility

**AWS Organizations consolidated billing** combines usage from every member account into a single bill, paid by the management account, while still preserving the ability to see costs broken down per account — and, with consistent tagging in place, per brand, per environment, or by whatever cost dimension actually matters to Meridian's finance team. This also lets Meridian take advantage of volume pricing discounts and Reserved Instance or Savings Plan sharing across accounts, since usage is aggregated for pricing purposes even though it's tracked separately for visibility.

## Putting It Together: Meridian's Multi-Account Environment Design

Sofía's design for the multi-account environment itself, closing out Domain 1:

- A **landing zone** with a management account, a Log Archive account, and an Audit account, all inside the Security OU — kept separate from the Production and Sandbox OUs holding actual brand workloads.
- **Account Factory** provisioning any new brand's account (Ridgeline's, and whichever brand Meridian acquires next) pre-configured with the correct OU placement, SCPs, guardrails, and logging from day one.
- **Tag policies** requiring a `Brand` and `CostCenter` tag on resources organization-wide, making per-brand cost and ownership tracking possible in the first place.
- An **organization trail** delivering CloudTrail events from every account — Café Sol's, Haven & Co.'s, and eventually Ridgeline's — to the Log Archive account automatically.
- **Consolidated billing** giving Meridian's finance team one invoice, with cost visibility broken down per brand using the tag policy's `Brand` tag.

## What to skip

You don't need to memorize Control Tower's exact account provisioning workflow steps or write tag policy JSON syntax from scratch — that's implementation depth beyond this exam. What matters is knowing what a landing zone's foundational accounts are for, what Account Factory automates, why tag policies matter for cost and log clarity, what an organization trail centralizes, and how consolidated billing works.

## Key takeaways

- A landing zone's foundational accounts — management, Log Archive, and Audit — exist to keep organization administration, log storage, and security review separate from actual brand workloads.
- AWS Control Tower's Account Factory provisions new accounts pre-configured with the landing zone's baseline guardrails, networking, and logging, rather than requiring manual, error-prone setup after the fact.
- AWS Organizations tag policies enforce consistent tag keys and values across accounts, which is what makes accurate cost allocation and log attribution possible at scale.
- An organization trail, created from the management account, automatically captures CloudTrail events from every account — including ones created later — into one centralized, tamper-resistant log location.
- Consolidated billing combines usage into a single bill for pricing benefits, while preserving per-account (and, with tagging, per-brand) cost visibility.

## Further reading

- [AWS Control Tower: What Is a Landing Zone?](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) — foundational OUs and accounts.
- [AWS Control Tower Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) — automated, pre-configured account provisioning.
- [AWS Organizations Tag Policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_tag-policies.html) — enforcing consistent resource tagging across accounts.
- [AWS CloudTrail Organization Trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) — centralized, org-wide event logging.
- [Consolidated Billing for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_billing.html) — one bill, per-account visibility, and shared pricing benefits.
