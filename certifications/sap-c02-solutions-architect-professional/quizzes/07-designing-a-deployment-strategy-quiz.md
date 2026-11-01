[Course index](../README.md) · [Read the paired lesson](../modules/07-designing-a-deployment-strategy.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 7 Knowledge Check**

Designing a Deployment Strategy · 20 questions · Practice — not graded

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

> An in-place deployment causes downtime during the deployment window.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which deployment strategy stands up an entirely new, parallel environment and cuts traffic over, often instantly?
>
> **A.** In-place
> **B.** Rolling
> **C.** Blue/green
> **D.** None of the above

**3. [Fill in the Blank] Easy**

> AWS ____________ orchestrates the overall release process as a series of stages — source, build, test, deploy.

**4. [Multiple Choice] Easy**

> Which AWS service compiles source code, runs tests, and produces deployable build artifacts?
>
> **A.** AWS CodePipeline
> **B.** AWS CodeBuild
> **C.** AWS CodeDeploy
> **D.** AWS CloudFormation

**5. [True / False] Easy**

> A canary deployment shifts all traffic to the new version at once.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which deployment strategy updates instances in batches, keeping the application available throughout without a dedicated second environment?
>
> **A.** In-place
> **B.** Rolling
> **C.** Blue/green
> **D.** Canary

**7. [Fill in the Blank] Moderate**

> ____________ ____________ ____________, using AWS CloudFormation or the AWS CDK, defines infrastructure in version-controlled templates or code rather than manual console configuration.

**8. [Multiple Choice] Moderate**

> What does AWS CodeDeploy natively support, beyond just executing a deployment?
>
> **A.** Compiling source code
> **B.** Several deployment strategies, including in-place and blue/green, through its own deployment configuration
> **C.** Creating VPCs
> **D.** Writing CloudFormation templates automatically

**9. [True / False] Moderate**

> Rolling deployment requires the old and new application versions to be compatible with each other for the duration of the rollout.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Why does rollback take just as long as the original deployment in an in-place strategy?
>
> **A.** It doesn't — in-place rollback is always instant
> **B.** Because rolling back means redeploying the previous version from scratch, the same process as the original deployment
> **C.** Because in-place deployments don't support rollback at all
> **D.** Because a second environment must be built first

**11. [Fill in the Blank] Moderate**

> A deployment pipeline deploying across account boundaries uses a ____________-____________ role, the same pattern introduced in Module 3.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Meridian Loyalty touches real guest reward balances, and a bad release needs to be caught while affecting only a small fraction of guests. Which deployment strategy fits best?
>
> **A.** In-place
> **B.** Rolling
> **C.** Canary
> **D.** Blue/green, since it's always the safest option regardless of scenario

**13. [Scenario / Judgment] Hard**

> A pipeline in Meridian's tooling account needs to deploy resources into Café Sol's account. What's the correct mechanism, consistent with Module 3?
>
> **A.** A shared IAM user with long-lived credentials stored in the tooling account
> **B.** A cross-account role in Café Sol's account, assumed by the pipeline's role in the tooling account, scoped to exactly what deployment requires
> **C.** Disabling IAM in Café Sol's account for the duration of the deployment
> **D.** An SCP granting deployment permissions directly

**14. [Scenario / Judgment] Hard**

> A team wants development, staging, and production environments for Meridian Loyalty to stay consistent without manually reproducing configuration in each one. What addresses this?
>
> **A.** Manually documenting the steps in a wiki page
> **B.** Infrastructure as Code — CloudFormation or CDK templates deployed through the same pipeline as the application
> **C.** A blue/green deployment strategy alone
> **D.** AWS CodeBuild alone, without any infrastructure definition

**15. [Scenario / Judgment] Hard**

> A scenario requires the fastest possible rollback, with two fully separate, complete environments available at all times. Which strategy fits best?
>
> **A.** Rolling
> **B.** In-place
> **C.** Blue/green
> **D.** Canary, since it's always safer than blue/green

**16. [Scenario / Judgment] Hard**

> A reviewer proposes skipping CodeBuild and having CodeDeploy compile and test the application directly. What's the issue with this, per this module?
>
> **A.** There is no issue — CodeDeploy and CodeBuild are interchangeable
> **B.** CodeBuild's role is specifically compiling code, running tests, and producing build artifacts — CodeDeploy handles deployment to compute targets; conflating the two skips the module's described division of responsibility within the pipeline
> **C.** CodeDeploy cannot be used in the same pipeline as CodeBuild under any circumstances
> **D.** CodePipeline requires CodeBuild to be removed before CodeDeploy can run

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Blue/green and canary are basically the same thing." Correct this using this module's content.
>
> **A.** They're right — the two are functionally identical
> **B.** Blue/green typically cuts traffic over all at once to a fully separate, parallel environment, with rollback meaning an instant switch back; canary gradually shifts a small, increasing percentage of traffic to the new version specifically to limit exposure to a bad release before it affects most users. The gradual, monitored exposure is the meaningful difference
> **C.** Canary requires two full environments and blue/green does not
> **D.** Blue/green is only used for infrastructure, never for application code

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since blue/green gives instant rollback and is the safest strategy, Meridian Loyalty should always use it instead of canary." Evaluate this using this module's content.
>
> **A.** Agree without qualification — blue/green is strictly better in every case
> **B.** Disagree — blue/green's cutover is typically all-or-nothing once traffic shifts, so a bad release still affects the full user base immediately, whereas canary's gradual shift is specifically what limits exposure before a bad release is caught. Given Meridian Loyalty touches real guest balances, limiting exposure matters more than cutover speed alone
> **C.** Disagree, but only because blue/green cannot technically be automated with CodeDeploy
> **D.** Agree, since canary deployments cannot be rolled back at all

**19. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Meridian Loyalty's infrastructure is defined with CloudFormation or CDK and deployed through the same pipeline as its application code, rather than being built once manually and left alone.
>
> **A.** Manually built infrastructure is technically impossible to create for a new solution
> **B.** Manual, one-time setup invites drift between environments and accounts over time, and leaves no reviewable, version-controlled record of infrastructure changes; deploying infrastructure through the same pipeline as application code keeps development, staging, and each brand's production environment consistent by construction, with the same audit trail as any other change
> **C.** CloudFormation templates cannot be modified after their first deployment
> **D.** There is no real benefit — manual setup and Infrastructure as Code produce identical outcomes

**20. [Scenario / Judgment] Very Hard**

> A stakeholder proposes storing a long-lived IAM user's access keys for each brand account directly in the deployment pipeline's configuration, arguing it's simpler than setting up cross-account roles. Argue against this using this module's and Module 3's content.
>
> **A.** Agree — long-lived keys stored in pipeline configuration are simpler and equally secure
> **B.** Disagree — long-lived shared credentials are hard to rotate, hard to audit per actual use, and a single leak (e.g. from the pipeline configuration itself) would compromise every account the credential touches; a cross-account role issues short-lived, individually logged temporary credentials scoped exactly to what deployment requires, which is the pattern this module and Module 3 both build on
> **C.** Disagree, but only because AWS technically prevents storing access keys in pipeline configuration
> **D.** Agree, since cross-account roles are being deprecated by AWS

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
