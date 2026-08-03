**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 3 Review Quiz**

Securing Access · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|
| | |

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

> By default, a newly created IAM user can perform no actions until permissions are explicitly granted.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which IAM identity type is assumed temporarily rather than owned permanently by one person?
>
> **A.** IAM user
> **B.** IAM group
> **C.** IAM role
> **D.** IAM account

**3. [Fill in the Blank] Easy**

> IAM ____________ are collections of users that share the same access needs and have no credentials of their own.

**4. [Multiple Choice] Easy**

> Which security principle means granting exactly the access needed and nothing more?
>
> **A.** Defense in depth
> **B.** Least privilege
> **C.** Shared responsibility
> **D.** Default deny

**5. [True / False] Easy**

> A policy is a JSON document that explicitly states what's allowed or denied.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> An EC2 instance needs to read objects from an S3 bucket. What's the best-practice way to grant that access?
>
> **A.** Hardcode an IAM user's access keys into the application
> **B.** Attach an IAM role to the EC2 instance
> **C.** Share the root user's credentials with the instance
> **D.** Make the S3 bucket fully public

**7. [Fill in the Blank] Moderate**

> If any applicable policy explicitly ____________ an action, that decision overrides any other policy that allows it.

**8. [Multiple Choice] Moderate**

> Which policy type attaches directly to a resource, like an S3 bucket, rather than to a user, group, or role?
>
> **A.** Managed policy
> **B.** Inline policy
> **C.** Identity-based policy
> **D.** Resource-based policy

**9. [True / False] Moderate**

> An AWS managed policy is embedded in a single identity and can't be reused elsewhere.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Under the shared responsibility model, who is responsible for a misconfigured IAM policy that grants too much access?
>
> **A.** AWS
> **B.** The customer
> **C.** Both equally, always
> **D.** Neither — misconfiguration isn't covered by the shared responsibility model

**11. [Fill in the Blank] Moderate**

> A policy embedded directly in a single identity, rather than saved as a reusable document, is called an ____________ policy.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A Lambda function needs temporary, auto-rotated credentials to write to a DynamoDB table. Which IAM identity type fits best?
>
> **A.** IAM user
> **B.** IAM group
> **C.** IAM role
> **D.** Root user

**13. [Scenario / Judgment] Hard**

> A user's identity-based policy allows read access to an S3 bucket, but the bucket's own resource-based policy explicitly denies access to that user. Can the user read the bucket?
>
> **A.** Yes — identity-based policies always take priority
> **B.** No — the explicit deny in the resource-based policy overrides the identity-based allow
> **C.** Yes, but only through the console, not the API
> **D.** It depends on which policy was created first

**14. [Scenario / Judgment] Hard**

> A team updates one AWS managed policy that's attached to twelve different IAM users. What happens to those twelve users' permissions?
>
> **A.** Nothing changes until each user's policy is manually reattached
> **B.** All twelve users' permissions update immediately, since they all reference the same policy
> **C.** Only new users added after the update are affected
> **D.** Managed policies can't be updated once attached to more than one user

**15. [Scenario / Judgment] Hard**

> A small nonprofit wants every volunteer to log in with the same shared IAM user to save on setup time. What's the main risk?
>
> **A.** There is no risk — shared credentials are a standard AWS best practice
> **B.** Individual accountability is lost, and the shared password is harder to rotate safely if compromised
> **C.** IAM doesn't allow more than one person to use the same user at different times
> **D.** Shared IAM users are technically impossible to create

**16. [Scenario / Judgment] Hard**

> A group has an attached policy allowing S3 read access. A new employee is added to that group. What access does the new employee have immediately?
>
> **A.** None, until an administrator manually attaches the policy to their individual account
> **B.** The same S3 read access as every other member of the group, automatically
> **C.** Only read access to buckets they personally created
> **D.** Full administrator access, since group membership grants broad permissions by default

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A short-term project needs five contractors to have identical access to a set of AWS resources for four months, with contractors likely to be swapped out mid-project. Which approach best follows AWS security principles?
>
> **A.** One shared IAM user for all five contractors, with the required policies attached directly to that user
> **B.** Five individual IAM users, all placed in one IAM group, with the required policies attached to the group
> **C.** Five individual IAM users, each with the required policies attached directly to their own account
> **D.** One shared IAM user placed in an IAM group, with policies attached to the group

**18. [Scenario / Judgment] Very Hard**

> Using the scenario from question 17: why is option C (individual users with individually-attached policies) not the *best* choice, even though it would technically work?
>
> **A.** It's not possible to attach the same policy to more than one individual user
> **B.** It works, but doesn't scale well — adding or removing a contractor means manually updating policies on every affected user instead of updating one group
> **C.** Individual IAM users are less secure than shared ones
> **D.** AWS charges extra for each individual IAM user beyond the first

**19. [Scenario / Judgment] Very Hard**

> A student says: "default deny in IAM means AWS blocks anything that looks suspicious." What's the correct correction?
>
> **A.** They're right — that's exactly what default deny means
> **B.** Default deny means no action is allowed unless a policy explicitly grants it — it's not about detecting suspicious behavior, it's the baseline state of every identity before any policy is attached
> **C.** Default deny only applies to the root user
> **D.** Default deny was replaced by a newer AWS feature and no longer applies

**20. [Scenario / Judgment] Very Hard**

> An architecture has an S3 bucket with no bucket policy at all, and an IAM user with a policy explicitly allowing read access to that bucket. Can the user read the bucket?
>
> **A.** No — a resource-based policy is always required for any access to succeed
> **B.** Yes — with no resource-based policy present to deny it, the identity-based allow is sufficient
> **C.** No — buckets without a bucket policy are always fully inaccessible
> **D.** It depends on whether the bucket has versioning enabled

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
