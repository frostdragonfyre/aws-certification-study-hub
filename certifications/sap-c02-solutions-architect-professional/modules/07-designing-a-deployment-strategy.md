# Module 7: Designing a Deployment Strategy

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Domain 1 finished the organizational foundation — connectivity, governance, reliability tooling, account structure, and cost visibility, all in place across Meridian. Domain 2 is where that foundation actually gets used: designing new solutions from scratch. The first one is **Meridian Loyalty** — a brand-new guest rewards platform, shared across Café Sol, Haven & Co., and eventually Ridgeline, that doesn't exist anywhere yet. Nothing about it inherits legacy decisions the way Café Sol's SAA-C03-era architecture does; every choice here is being made fresh.

This module covers the first thing a new solution needs before a single line of its code reaches production: a deployment strategy. Not just "how do we deploy" but "how do we deploy repeatedly, safely, and with a real plan for when a release goes wrong."

## Learning objectives

By the end of this module, you should be able to:

- Compare in-place, rolling, blue/green, and canary deployment strategies, and the trade-off each makes between deployment speed, risk, and rollback time
- Explain how AWS CodePipeline, CodeBuild, and CodeDeploy work together to automate a deployment
- Explain why Infrastructure as Code (via AWS CloudFormation or the AWS CDK) matters for deploying consistently across environments and accounts
- Describe how a deployment pipeline deploys safely across account boundaries, using the cross-account role pattern from Module 3
- Recommend a deployment strategy for a stated business requirement

---

## Four Deployment Strategies: Speed, Risk, and Rollback

Every deployment strategy makes the same fundamental trade-off differently: how fast the new version goes live, how much risk that speed carries, and how quickly you can undo it if something's wrong.

- **In-place deployment** updates existing servers directly, in one action — every instance running the old version is replaced (or updated) essentially at once. It's the fastest and simplest to set up, but it causes downtime during the deployment window, and rollback means redeploying the previous version from scratch, which takes just as long as the original deployment did.
- **Rolling deployment** updates instances in batches — a portion of the fleet at a time — so the application stays available throughout, without a dedicated second environment. The cost is that old and new versions run simultaneously during the rollout, which requires the two versions to be compatible with each other (and with whatever data or API contract they share) for as long as the rollout takes.
- **Blue/green deployment** stands up an entirely new, parallel environment (green) running the new version, fully tested, alongside the existing environment (blue) still serving live traffic. Cutover happens by shifting traffic — often instantly, via a load balancer or DNS change — from blue to green. Rollback is just as fast: shift traffic back to blue, which is still fully intact and untouched. This is the safest option, but it costs the most, since two complete environments run in parallel, at least temporarily.
- **Canary deployment** is a controlled variant of blue/green: instead of cutting all traffic over at once, a small percentage of traffic is shifted to the new version first, monitored closely, and gradually increased if metrics stay healthy. This limits the blast radius of a bad release to a small fraction of users before it's caught, at the cost of a slower, more gradual rollout than a full blue/green cutover.

> ⚠️ **Exam trap:** "we need zero downtime, and we need to detect a bad release before it affects most users" is describing canary, not blue/green — blue/green's cutover is typically all-or-nothing once traffic shifts, while canary's gradual traffic shift is specifically what limits exposure to a bad release. "We need the fastest possible rollback with two fully separate environments" is blue/green. Read for whether gradual, limited exposure is actually the requirement, or whether an instant, complete cutover is.

## Automating Deployment: CodePipeline, CodeBuild, and CodeDeploy

Manually running any of these four strategies by hand doesn't scale, and it reintroduces exactly the kind of "forgot a step" risk Domain 1's tooling was built to eliminate. AWS provides three services that work together to automate deployment end to end:

- **AWS CodePipeline** orchestrates the overall release process as a series of stages — source, build, test, deploy — automatically moving a change through each stage in order, and stopping the pipeline if any stage fails.
- **AWS CodeBuild** compiles source code, runs tests, and produces deployable build artifacts, as one stage within that pipeline.
- **AWS CodeDeploy** handles the actual deployment to compute targets (EC2 instances, on-premises servers, ECS, or Lambda), and natively supports several of the strategies above — including in-place and blue/green deployments — through its own deployment configuration, rather than requiring that logic to be built by hand.

For Meridian Loyalty, this means a change merged to the main branch moves through CodePipeline automatically: CodeBuild compiles and tests it, and CodeDeploy executes the actual rollout using whichever strategy the pipeline is configured for — with no manual step in between that could be skipped or done inconsistently.

## Infrastructure as Code: Deploying Consistently, Not Just Repeatedly

A deployment strategy handles *application* code — but Meridian Loyalty's actual infrastructure (its VPC, its compute, its database) needs to exist consistently across environments too: a development environment, a staging environment, and production, and potentially replicated per brand. Manually clicking through the console to build each environment invites exactly the kind of drift Domain 1 spent five modules trying to prevent at the organizational level.

**Infrastructure as Code (IaC)** — using **AWS CloudFormation** or the **AWS Cloud Development Kit (CDK)** — defines infrastructure in version-controlled templates or code, so an environment can be created, updated, or torn down by deploying that same definition rather than manually reproducing it. CloudFormation templates (or CDK code, which synthesizes down to CloudFormation) become part of the same pipeline as the application code: a change to the infrastructure definition goes through source control, build, and deployment, the same as any other change, with the same audit trail and the same ability to review before it ships.

This matters specifically for Meridian Loyalty because it's meant to run consistently in more than one brand's account eventually — IaC is what makes "deploy the same infrastructure into Ridgeline's account once it's ready" a template parameter change, not a manual rebuild from memory.

## Deploying Across Account Boundaries

Meridian Loyalty's pipeline doesn't run inside Café Sol's or Haven & Co.'s account directly — following the landing zone pattern from Module 5, it runs from a dedicated deployment/tooling account, and needs to actually deploy resources into each brand's account from there.

This is exactly the cross-account role pattern from Module 3: the pipeline's role in the tooling account assumes a role in each target brand account — Café Sol's, Haven & Co.'s, and eventually Ridgeline's — scoped to exactly the permissions a deployment needs (creating and updating the specific resources Meridian Loyalty uses), and nothing more. No long-lived credentials are stored per brand account, every cross-account deployment action is logged via CloudTrail, and a compromised pipeline can't silently gain broader access than its role explicitly grants.

## Putting It Together: Meridian Loyalty's Deployment Strategy

Sofía's deployment design for Meridian Loyalty, the first new solution in this course:

- **Canary deployment**, chosen specifically because Meridian Loyalty touches real guest reward balances — a bad release needs to be caught while affecting a small fraction of guests, not all of them at once, which rules out a full blue/green cutover as the primary strategy.
- **CodePipeline, CodeBuild, and CodeDeploy** automating the entire release process, with CodeDeploy's native canary configuration handling the gradual traffic shift and automatic rollback if health metrics degrade.
- **CloudFormation** (or CDK) defining Meridian Loyalty's infrastructure, deployed through the same pipeline as the application code, so development, staging, and each brand's production environment stay consistent by construction rather than by discipline.
- A **cross-account role** from the tooling account's pipeline into each brand's account, scoped narrowly to what deploying Meridian Loyalty actually requires.

## What to skip

You don't need to memorize CodeDeploy's exact configuration file syntax or CloudFormation's full template schema — that's implementation depth beyond this exam. What matters is comparing the four deployment strategies' trade-offs, knowing what each of CodePipeline/CodeBuild/CodeDeploy is responsible for, why IaC matters for cross-environment consistency, and how cross-account deployment uses the role pattern from Module 3.

## Key takeaways

- In-place is fastest but causes downtime and slow rollback; rolling avoids downtime but runs mixed versions simultaneously; blue/green gives instant cutover and rollback at double the running cost; canary limits a bad release's blast radius through gradual, monitored traffic shifting.
- AWS CodePipeline orchestrates the release process end to end; CodeBuild compiles and tests; CodeDeploy executes the actual deployment and natively supports several deployment strategies.
- Infrastructure as Code (CloudFormation or CDK) keeps environments consistent across dev, staging, and production — and across brand accounts — by deploying a shared definition rather than manually reproducing it.
- Deploying across account boundaries uses the cross-account role pattern from Module 3: a pipeline in a tooling account assumes narrowly scoped roles in each target account, with no long-lived shared credentials.
- Meridian Loyalty's strategy: canary deployment (given real guest balances are at stake), automated by CodePipeline/CodeBuild/CodeDeploy, infrastructure defined as code, deployed across brand accounts via cross-account roles.

## Further reading

- [AWS Whitepaper: Blue/Green Deployments on AWS](https://docs.aws.amazon.com/whitepapers/latest/blue-green-deployments/welcome.html) — deployment strategy trade-offs in depth.
- [AWS CodePipeline User Guide](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) and [AWS CodeDeploy User Guide](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) — pipeline orchestration and deployment configurations, including canary and blue/green.
- [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) — Infrastructure as Code fundamentals.
- [Cross-Account Deployment Patterns](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html) — the same cross-account role pattern from Module 3, applied to deployment pipelines.
