**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 9 Knowledge Check**

Implementing and Managing Security and Compliance Policies · 20 questions · Practice — not graded

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

> A Service Control Policy can grant a principal permission to perform an action, even without an IAM policy allowing it.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What does an IAM policy do?

> **A.** Sets a maximum permissions boundary for an entire organizational unit
> **B.** Grants permissions to a user, group, or role
> **C.** Continuously evaluates resource configuration
> **D.** Aggregates findings from other security services

**3. [Fill in the Blank] Easy**

> AWS ____________ continuously records resource configuration and evaluates it against defined rules.

**4. [Multiple Choice] Easy**

> What does AWS Security Hub primarily do?

> **A.** Generates its own independent threat detection findings
> **B.** Aggregates findings from services like GuardDuty, Config, and Inspector into one view
> **C.** Grants IAM permissions across accounts
> **D.** Replaces the need for GuardDuty and Config entirely

**5. [True / False] Easy**

> AWS Config rules can trigger automatic remediation through SSM Automation.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> An SCP applied to an OU denies `s3:DeleteBucket`. A user in that OU has an IAM policy explicitly allowing `s3:DeleteBucket`. What happens?

> **A.** The user can delete the bucket, since their IAM policy allows it
> **B.** The user cannot delete the bucket — the SCP sets a boundary that the IAM policy cannot exceed
> **C.** The SCP and IAM policy cancel out, so the action requires a separate approval
> **D.** SCPs and IAM policies cannot apply to the same action

**7. [Fill in the Blank] Moderate**

> A ____________ ____________ ____________ (SCP) is managed through AWS Organizations and applied to an account or organizational unit.

**8. [Multiple Choice] Moderate**

> How is AWS Config's evaluation different from CloudFormation drift detection?

> **A.** They are functionally identical
> **B.** Config evaluates resources against organization-wide compliance rules regardless of how they were created; drift detection compares resources only against a specific CloudFormation stack's template
> **C.** Drift detection can trigger automatic remediation, but Config cannot
> **D.** Config only works for resources created through CloudFormation

**9. [True / False] Moderate**

> Enabling Security Hub alone, without GuardDuty, Config, or Inspector actually running, will still generate threat detection findings.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A company needs every account in an OU permanently blocked from disabling CloudTrail, regardless of any individual account's IAM configuration. What fits?

> **A.** An IAM policy attached to every user in every account
> **B.** A Service Control Policy applied at the OU level
> **C.** An AWS Config rule with no remediation
> **D.** Security Hub compliance scoring

**11. [Fill in the Blank] Moderate**

> Security Hub scores accounts against compliance ____________ like the CIS AWS Foundations Benchmark or PCI DSS.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A user has no IAM policy granting `ec2:TerminateInstance`, but no SCP denies it either. Can the user terminate an EC2 instance?

> **A.** Yes, since no SCP is blocking the action
> **B.** No — without an IAM policy actually granting the permission, the action is denied by default, regardless of what any SCP allows
> **C.** Yes, since SCPs are the only thing that matters for permissions
> **D.** It depends entirely on the account's Config rules

**13. [Scenario / Judgment] Hard**

> Meridian wants non-compliant S3 buckets (missing encryption) automatically fixed the moment they're detected, without a person manually intervening. What combination fits?

> **A.** An SCP denying bucket creation entirely
> **B.** An AWS Config rule detecting the non-compliant configuration, paired with SSM Automation remediation triggered by Config
> **C.** IAM policies alone, since they can automatically fix misconfigured buckets
> **D.** Security Hub, since it can independently remediate non-compliant resources

**14. [Scenario / Judgment] Hard**

> A security team wants one dashboard showing GuardDuty threat findings, Config compliance results, and Inspector vulnerability scans across 40 accounts, without checking each service's console per account. What fits?

> **A.** AWS Config alone, since it already includes GuardDuty and Inspector data
> **B.** AWS Security Hub, aggregating findings from all three services into one standardized view
> **C.** A Service Control Policy, since it applies across all 40 accounts
> **D.** IAM Access Analyzer, since it covers every security finding type

**15. [Scenario / Judgment] Hard**

> A resource was compliant with a Config rule when it was created but later became non-compliant after a manual change. When would Config detect this?

> **A.** Never — Config only evaluates resources at creation time
> **B.** On an ongoing basis — Config continuously evaluates resource configuration, not just at a single point in time
> **C.** Only if the resource was created through CloudFormation
> **D.** Only if Security Hub is also enabled

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "SCPs and IAM policies do the same job — they both control what a user can do." Correct this using this module's content.

> **A.** They're right — SCPs and IAM policies are functionally interchangeable
> **B.** They're different: an IAM policy is what actually grants permissions to a principal, while an SCP only ever restricts — it sets a maximum boundary and can never grant permission on its own; a principal needs both an allowing IAM policy and no blocking SCP
> **C.** SCPs grant permissions and IAM policies restrict them — the student has the roles reversed but the concepts right
> **D.** Neither SCPs nor IAM policies actually affect what a user can do

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues that since Security Hub is enabled organization-wide, GuardDuty and Config no longer need to be enabled in each account. Evaluate this using this module's content.

> **A.** Agree — Security Hub replaces the need for the underlying detection services entirely
> **B.** Disagree — Security Hub aggregates and scores findings that GuardDuty, Config, and other services generate; without those services actually running, there's no underlying detection or configuration evaluation for Security Hub to aggregate
> **C.** Disagree, but only because Security Hub cannot be enabled organization-wide
> **D.** Agree, since GuardDuty and Config duplicate exactly what Security Hub already does independently

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why an SCP denying `iam:CreateUser` at the OU level cannot be bypassed by an account administrator granting themselves that permission through an IAM policy.

> **A.** IAM policies always take precedence over SCPs, so this bypass would work
> **B.** An SCP sets the maximum available permissions for every principal in the account — no IAM policy, no matter how permissive, can grant a permission the SCP has denied, since the SCP is an outer boundary, not something an in-account policy can override
> **C.** SCPs and IAM policies operate on completely unrelated resource types, so there's no conflict
> **D.** This would only fail if Security Hub was also enabled in the account

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes relying solely on Config rules (detection) without ever pairing them with SSM Automation remediation, arguing "knowing about a problem is enough." Argue against this using this module's content.

> **A.** Agree — detection alone is always sufficient for compliance
> **B.** Disagree — Config rules flag non-compliance but don't fix it on their own; without remediation paired in (through SSM Automation), a non-compliant resource stays non-compliant until a person manually intervenes, which is exactly the manual, repeatable-but-not-automated work Domain 3 was about eliminating
> **C.** Disagree, but only because Config cannot detect non-compliance without remediation configured
> **D.** Agree, since SSM Automation cannot be triggered by Config rules

**20. [Scenario / Judgment] Very Hard**

> A student says: "If Security Hub shows a high compliance score, the organization's actual security posture must be strong." Evaluate this claim using this module's content.

> **A.** Agree completely — a high Security Hub score is a complete guarantee of security
> **B.** Disagree — Security Hub's score reflects what the underlying services (GuardDuty, Config, Inspector) actually report; if those services aren't enabled everywhere, aren't configured for the right rules, or don't cover a particular risk, the aggregated score can look strong while real gaps go undetected
> **C.** Disagree, but only because Security Hub scores are randomly generated
> **D.** Agree, since Security Hub independently verifies every possible security risk beyond what any other service checks

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
