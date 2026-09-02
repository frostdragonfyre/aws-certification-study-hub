# Module 7: Provisioning and Maintaining Cloud Resources

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Domain 2 made sure Meridian's infrastructure survives demand, failure, and data loss. Domain 3 asks a different question: how does that infrastructure get created and kept consistent in the first place — across dozens of resources, multiple accounts, and a growing number of people who need to provision something without becoming an infrastructure expert first. This module opens Domain 3 with Task 3.1: provisioning cloud resources at scale and keeping them from silently drifting away from how they were defined.

## Learning objectives

By the end of this module, you should be able to:

- Explain what a CloudFormation stack is and how a template drives it
- Describe how CloudFormation StackSets deploy the same template across multiple accounts and Regions
- Explain what drift detection finds, and what it does not automatically fix
- Describe how AWS Service Catalog lets non-admins provision approved resources safely
- Design a provisioning strategy for a stated multi-account, self-service requirement

---

## CloudFormation: One Template, One Stack

**AWS CloudFormation** turns infrastructure into code: a **template** (JSON or YAML) declares the resources an application needs — EC2 instances, an RDS database, IAM roles, a VPC — and CloudFormation creates, updates, or deletes all of them together as a single unit called a **stack**. Instead of manually clicking through consoles or running one-off CLI commands, the template becomes the single source of truth for what the infrastructure should look like.

Updating a stack isn't a black box: a **change set** previews exactly what CloudFormation would add, modify, or replace before anything actually happens — including flagging any change that would require replacing a resource entirely (which can mean data loss for something like a database) rather than updating it in place. Reviewing a change set before executing it is how Priya avoids an update that looks harmless in the template but would actually tear down and recreate a running resource.

> ⚠️ **Exam trap:** a scenario describing an update that needs to be reviewed for safety before it's applied — especially one where a resource replacement would cause unacceptable downtime or data loss — is pointing at reviewing a **change set**, not just running the update directly. Skipping that review is exactly how an update quietly recreates a resource nobody meant to touch.

## StackSets: The Same Template, Many Accounts and Regions

A single CloudFormation stack lives in one account and one Region. But Meridian's baseline — a standard VPC layout, a required set of IAM roles, a mandatory CloudTrail configuration — needs to exist identically across every account in the organization and every Region those accounts operate in. Deploying that by hand, account by account, is exactly the kind of manual, error-prone process Domain 3 is about eliminating.

**CloudFormation StackSets** solve this directly: a single StackSet deploys and manages a CloudFormation template as a set of **stack instances** across many accounts and Regions at once, from one administrator account. Updating the StackSet's template propagates that change to every stack instance, keeping the baseline consistent everywhere without a person manually repeating the same deployment dozens of times.

> ⚠️ **Exam trap:** a scenario asking to deploy or update the same set of resources consistently across multiple AWS accounts or Regions is describing a job for **StackSets**, not a plan to deploy individual CloudFormation stacks account by account. A single stack is scoped to one account and one Region — StackSets are the mechanism that scales a template out across many of both at once.

## Drift Detection: Finding What Changed Outside CloudFormation

Once a stack is deployed, nothing stops someone from going into the console and manually changing a resource CloudFormation created — widening a security group rule, resizing an EBS volume, changing a tag. When that happens, the actual resource no longer matches what the template says it should be. This mismatch is called **drift**.

**Drift detection** compares a stack's actual resource configuration against the template's expected configuration and reports which resources have drifted and exactly what changed. Critically, drift detection is a **read-only comparison** — it identifies drift, it does not undo it. Fixing drifted resources means either manually reverting the out-of-band change, or updating the stack (which may or may not bring a drifted resource back in line, depending on what changed).

> ⚠️ **Exam trap:** a scenario describing resources that no longer match their CloudFormation template, where someone assumes CloudFormation "automatically" reconciles the difference, is describing a misunderstanding of drift detection. Drift detection finds and reports the mismatch — it does not automatically remediate it. Treating drift detection as a fix, rather than a diagnostic step that still requires action, is the trap.

## Service Catalog: Self-Service Without Losing Control

Not everyone who needs to provision a resource should need CloudFormation template-writing skills or account-level permissions to create arbitrary infrastructure. **AWS Service Catalog** solves this by letting administrators package approved CloudFormation templates as **products**, organized into **portfolios**, and grant specific users or teams permission to launch only those pre-approved products — with the underlying configuration (instance sizes, required tags, security settings) locked to what's already been vetted.

A developer on Café Sol's team who needs a standard, pre-configured application server doesn't need IAM permissions to create EC2 instances directly; they need permission to launch a specific Service Catalog product, which then provisions exactly the vetted configuration behind the scenes.

> ⚠️ **Exam trap:** a scenario asking how to let non-administrative users provision infrastructure themselves, without giving them broad IAM permissions to create arbitrary resources, is describing **AWS Service Catalog** — self-service provisioning restricted to pre-approved, pre-configured products, not a change to the users' underlying IAM permissions.

## Putting It Together: Provisioning at Meridian

Priya's provisioning strategy, opening Domain 3:

- **CloudFormation templates** as the source of truth for every standard resource pattern, with **change sets** reviewed before any update that could replace a resource.
- **StackSets** deploying Meridian's baseline VPC, IAM roles, and CloudTrail configuration identically across every account and Region in the organization.
- **Drift detection** run on a schedule against critical stacks, so an out-of-band console change gets caught and addressed instead of silently persisting.
- **Service Catalog** portfolios giving Café Sol's and Ridgeline's developers self-service access to pre-approved application server and database products, without broad provisioning permissions.

## What to skip

You don't need to memorize CloudFormation's full intrinsic function syntax or every StackSets deployment option — that's implementation depth beyond this exam. What matters is knowing what a change set previews, that StackSets scale a template across accounts and Regions, that drift detection reports but doesn't fix, and that Service Catalog is the self-service mechanism for non-admin provisioning.

## Key takeaways

- A CloudFormation template defines a stack's resources; a change set previews an update before it runs, flagging any replacement that could cause data loss.
- StackSets deploy and manage the same template as stack instances across many accounts and Regions from one place — a single stack is scoped to one account and one Region.
- Drift detection identifies where actual resources no longer match their template, but it's read-only — it doesn't automatically remediate the mismatch.
- Service Catalog lets non-admins provision pre-approved, pre-configured resources through portfolios and products, without needing broad IAM provisioning permissions.
- This opens Domain 3 — provisioning and maintaining resources at scale. Module 8 covers the second half: automating the manual, repeatable processes around that infrastructure.

## Further reading

- [What Is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) — templates, stacks, and change sets.
- [Working with CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) — deploying across accounts and Regions.
- [Detecting Unmanaged Configuration Changes to Stacks and Resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) — how drift detection works.
- [What Is AWS Service Catalog?](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/introduction.html) — portfolios, products, and self-service provisioning.
