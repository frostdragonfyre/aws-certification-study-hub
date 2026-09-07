**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 3 Knowledge Check**

Prescribing Security Controls at the Organization Level · 20 questions · Practice — not graded

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

> A Service Control Policy (SCP) can grant a permission to a user on its own, without any IAM policy inside the account.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What does an organizational unit (OU) in AWS Organizations allow?
>
> **A.** Policies to be attached to a group of accounts at once, including accounts added later
> **B.** IAM users to be shared across multiple AWS accounts
> **C.** SCPs to grant permissions directly to users
> **D.** Cross-account roles to bypass trust policies

**3. [Fill in the Blank] Easy**

> AWS ____________ ____________ provides one central sign-on for users, granting access to specific AWS accounts through permission sets.

**4. [Multiple Choice] Easy**

> Which type of guardrail blocks an action from happening at all?
>
> **A.** Detective
> **B.** Preventive
> **C.** Reactive
> **D.** Corrective

**5. [True / False] Easy**

> A cross-account IAM role is assumed using long-lived access keys that never expire.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> An account has an IAM policy granting full S3 access, but sits under an SCP that denies all S3 actions organization-wide. What happens when a user in that account tries to access S3?
>
> **A.** Access is granted, since the IAM policy allows it
> **B.** Access is denied, since the SCP sets the outer boundary and the IAM policy can't exceed it
> **C.** Access depends on which was created first, the SCP or the IAM policy
> **D.** SCPs and IAM policies cannot both apply to the same account

**7. [Fill in the Blank] Moderate**

> A ____________ guardrail continuously evaluates accounts for compliance and flags violations after the fact, without blocking the action itself.

**8. [Multiple Choice] Moderate**

> What API call does a principal use to obtain temporary credentials for a cross-account IAM role?
>
> **A.** iam:CreateRole
> **B.** sts:AssumeRole
> **C.** organizations:AttachPolicy
> **D.** sso:CreatePermissionSet

**9. [True / False] Moderate**

> AWS Control Tower's guardrails include both preventive guardrails, implemented using SCPs, and detective guardrails, implemented using AWS Config rules.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Why does IAM Identity Center use permission sets instead of separate IAM users in every account?
>
> **A.** Permission sets are required by AWS Organizations before any account can be created
> **B.** Permission sets let one central identity be granted scoped access to specific accounts, instead of managing a separate user and password per account
> **C.** Permission sets replace the need for SCPs entirely
> **D.** Permission sets only work within a single AWS account

**11. [Fill in the Blank] Moderate**

> The permissions of a cross-account role are defined by the role itself; whether another account's principal is allowed to assume it at all is defined by the role's ____________ policy.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Meridian's security team wants to guarantee that CloudTrail logging can never be disabled in any governed account, no matter how permissive that account's own IAM policies are. Which control fits?
>
> **A.** A detective guardrail, since it will flag the change after it happens
> **B.** A preventive guardrail, implemented using an SCP, since it blocks the action outright
> **C.** An IAM Identity Center permission set
> **D.** A cross-account role with read-only permissions

**13. [Scenario / Judgment] Hard**

> A monitoring tool in Meridian's Security OU account needs to read CloudWatch metrics from Café Sol's account. What's the correct mechanism?
>
> **A.** Create an IAM user in Café Sol's account and share its long-lived access keys with the Security account
> **B.** A cross-account IAM role in Café Sol's account, with a trust policy allowing the Security account's principal to assume it
> **C.** An SCP granting CloudWatch read access
> **D.** Disable IAM entirely between the two accounts

**14. [Scenario / Judgment] Hard**

> Meridian wants an S3 bucket that becomes publicly accessible to be flagged for review, but doesn't need it blocked outright since some legitimate use cases require temporary public access. What best fits?
>
> **A.** A preventive guardrail blocking all public S3 access
> **B.** A detective guardrail flagging public S3 buckets after the fact
> **C.** An SCP denying s3:PutBucketPolicy organization-wide
> **D.** Removing S3 access from all accounts entirely

**15. [Scenario / Judgment] Hard**

> Ridgeline's future AWS account is expected to join Meridian's organization later this year. Where should Meridian's baseline SCPs be attached so they automatically apply to Ridgeline's account without additional configuration once it's created?
>
> **A.** Directly to Café Sol's account only
> **B.** To the relevant organizational unit that Ridgeline's account will be placed into
> **C.** SCPs cannot be applied until after an account already exists and is manually configured
> **D.** To an IAM Identity Center permission set

**16. [Scenario / Judgment] Hard**

> A new engineer joins Sofía's team and needs scoped access to Café Sol's and Haven & Co.'s accounts, but not Ridgeline's (not yet in AWS). Using this module's content, what's the correct way to grant this?
>
> **A.** Create a separate IAM user with its own password in each of the two accounts
> **B.** Add the engineer in IAM Identity Center and assign the appropriate permission sets for Café Sol's and Haven & Co.'s accounts only
> **C.** Share the root account credentials for both accounts
> **D.** Attach an SCP granting the engineer access

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "We attached an SCP allowing full S3 access to our Production OU, so now every account in that OU has S3 access." Correct this using this module's content.
>
> **A.** They're right — attaching an SCP is sufficient on its own to grant access
> **B.** An SCP only sets the maximum available permissions — it never grants access by itself. Each account still needs its own IAM policy actually granting S3 permissions to a user or role; the SCP only determines whether that grant is allowed to take effect
> **C.** SCPs only apply to individual IAM users, never to accounts
> **D.** SCPs and S3 permissions are unrelated to each other

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Preventive guardrails alone are enough — we don't need detective guardrails, since anything worth stopping can just be blocked outright." Argue against this using this module's content.
>
> **A.** Agree — detective guardrails serve no real purpose if preventive guardrails exist
> **B.** Disagree — some issues, like a resource's configuration drifting out of compliance over time, can't practically be prevented up front the way a single blocked action can; detective guardrails catch and flag these after the fact so they can be remediated, which is a genuinely different job than prevention
> **C.** Disagree, but only because preventive guardrails don't actually work
> **D.** Agree, since AWS Control Tower only supports one guardrail type at a time

**19. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Meridian uses cross-account IAM roles instead of creating an IAM user in each account and sharing its access keys with the accounts that need access.
>
> **A.** IAM users cannot be created in AWS accounts that belong to an organization
> **B.** Shared long-lived access keys are hard to rotate, hard to audit per-user, and a single leak compromises every account that credential touches; cross-account roles issue short-lived temporary credentials via sts:AssumeRole, individually logged in CloudTrail, with permissions scoped exactly to the role
> **C.** Cross-account roles are only a cosmetic difference with no real security benefit over shared keys
> **D.** SCPs make IAM users obsolete, so this distinction doesn't matter

**20. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping OUs entirely and attaching every SCP directly to each of Meridian's individual accounts, arguing it gives more precise control. Argue against this approach using this module's content.
>
> **A.** Agree — per-account SCPs are always more precise and preferable
> **B.** Disagree — per-account attachment doesn't scale as Meridian adds brands, requires remembering to attach policy to every new account individually, and is easy to get inconsistent across accounts; OUs let policy apply to groups of accounts automatically, including ones added later
> **C.** Disagree, but only because SCPs cannot be attached to individual accounts under any circumstances
> **D.** Agree, since OUs are being deprecated by AWS Organizations

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
