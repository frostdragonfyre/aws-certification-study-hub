**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 7 Knowledge Check**

Provisioning and Maintaining Cloud Resources · 20 questions · Practice — not graded

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

> A single CloudFormation stack can be scoped to more than one AWS account at once.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What does a CloudFormation change set do?

> **A.** Immediately applies an update with no preview
> **B.** Previews exactly what would be added, modified, or replaced before the update runs
> **C.** Permanently deletes a stack
> **D.** Detects drift automatically

**3. [Fill in the Blank] Easy**

> CloudFormation ____________ deploy and manage the same template across many accounts and Regions from one place.

**4. [Multiple Choice] Easy**

> What does drift detection do when it finds a mismatch between a stack and its actual resources?

> **A.** Automatically reverts the resource to match the template
> **B.** Reports the mismatch — it does not automatically fix it
> **C.** Deletes the drifted resource
> **D.** Silently ignores the mismatch

**5. [True / False] Easy**

> AWS Service Catalog lets administrators restrict self-service provisioning to pre-approved products.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why should Priya review a change set before applying a CloudFormation update?

> **A.** Change sets are required before any stack can be created
> **B.** It flags whether an update would replace a resource entirely, which could mean data loss for something like a database
> **C.** Change sets automatically fix drifted resources
> **D.** Change sets are only relevant for StackSets, not individual stacks

**7. [Fill in the Blank] Moderate**

> A ____________ is a single CloudFormation deployment within one account and one Region.

**8. [Multiple Choice] Moderate**

> Why do StackSets fit Meridian's need for a consistent baseline VPC and IAM role setup across every account and Region?

> **A.** A single CloudFormation stack already spans every account and Region automatically
> **B.** A StackSet deploys and updates the same template as stack instances across many accounts and Regions at once, instead of repeating manual deployments
> **C.** StackSets only work within a single account
> **D.** StackSets replace the need for CloudFormation templates entirely

**9. [True / False] Moderate**

> Someone manually changing a CloudFormation-managed resource in the console, outside of a stack update, creates drift.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A developer needs to launch a pre-configured application server without being granted IAM permissions to create EC2 instances directly. What fits?

> **A.** Granting the developer full EC2 permissions
> **B.** A Service Catalog product the developer is permitted to launch, provisioning the vetted configuration behind the scenes
> **C.** A CloudFormation StackSet deployed to their personal account
> **D.** Drift detection configured for their account

**11. [Fill in the Blank] Moderate**

> Service Catalog organizes approved CloudFormation templates as ____________, grouped into portfolios.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A scenario describes an update that, if applied directly, would replace a running RDS instance and cause data loss — but this wasn't caught until after the update ran. What step would have caught it beforehand?

> **A.** Running drift detection before the update
> **B.** Reviewing the change set, which would have flagged the replacement before execution
> **C.** Deploying the change through a StackSet instead of a single stack
> **D.** Nothing could have caught this in advance

**13. [Scenario / Judgment] Hard**

> Meridian needs the same CloudTrail configuration deployed identically to 40 accounts across 3 Regions, updated centrally whenever the baseline changes. What fits best?

> **A.** 120 individual CloudFormation stacks, deployed and updated by hand
> **B.** A single CloudFormation StackSet, with stack instances across all 40 accounts and 3 Regions
> **C.** AWS Service Catalog, since it manages multi-account deployments
> **D.** Drift detection, since it can deploy new resources

**14. [Scenario / Judgment] Hard**

> A team assumes that because CloudFormation "manages" their resources, any manual console change made to those resources is automatically detected and reverted in real time. What's wrong with this assumption?

> **A.** Nothing — CloudFormation does revert manual changes automatically
> **B.** Drift detection has to be run (on demand or on a schedule) to find the mismatch, and even then it only reports drift — it doesn't automatically fix it
> **C.** CloudFormation prevents any manual console changes from being possible at all
> **D.** Manual changes are impossible unless made through a change set

**15. [Scenario / Judgment] Hard**

> Priya wants Café Sol's developers to be able to provision a standard application server themselves, without giving them permission to create arbitrary EC2 instances or modify security groups directly. What fits?

> **A.** Granting broad IAM EC2 permissions, then trusting developers to follow a written policy
> **B.** A Service Catalog portfolio containing a pre-approved application server product, with developers granted permission only to launch that product
> **C.** A CloudFormation StackSet deployed to each developer's personal sandbox account
> **D.** Drift detection configured to alert if a developer creates an unauthorized resource

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "CloudFormation stacks, StackSets, and Service Catalog are all just different names for the same thing — deploying resources." Correct this using this module's content.

> **A.** They're right — all three do exactly the same job with no meaningful difference
> **B.** They're different: a stack deploys a template in one account and Region, a StackSet scales that same template across many accounts and Regions, and Service Catalog restricts *who* can self-service provision *which* pre-approved templates — scope, reach, and access control are three separate problems
> **C.** StackSets and Service Catalog are identical; only plain stacks are different
> **D.** Service Catalog replaces the need for CloudFormation templates entirely

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues that running drift detection once, at initial stack creation, is sufficient ongoing protection against configuration drift. Evaluate this using this module's content.

> **A.** Agree — drift detection at creation time covers the stack's entire lifecycle
> **B.** Disagree — drift can occur at any point after deployment, whenever someone makes an out-of-band change, so drift detection needs to run on an ongoing basis (on demand or scheduled) against live stacks, not just once at creation
> **C.** Disagree, but only because drift detection cannot run more than once per stack
> **D.** Agree, since CloudFormation stacks cannot be modified after creation

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why granting a non-administrative team direct IAM permissions to create EC2 instances is a worse fit than Service Catalog for a self-service provisioning need.

> **A.** IAM permissions and Service Catalog products are functionally identical, so it doesn't matter which is used
> **B.** Direct IAM permissions let the team create arbitrary, unvetted resource configurations, while Service Catalog restricts them to pre-approved, pre-configured products — achieving self-service without losing control over what actually gets provisioned
> **C.** IAM permissions are strictly more secure than Service Catalog in every scenario
> **D.** Service Catalog cannot be used by non-administrative users under any configuration

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping change set review entirely for "routine" CloudFormation updates, arguing it slows down deployments unnecessarily. Argue against this using this module's content.

> **A.** Agree — change sets are unnecessary overhead for any update
> **B.** Disagree — a change set is what reveals whether an update would replace a resource (with possible data loss) before it happens; an update that looks routine in the template can still trigger a replacement, and skipping the preview removes the only chance to catch that beforehand
> **C.** Disagree, but only because change sets are required by AWS for every update with no exceptions
> **D.** Agree, since resource replacement can always be undone after the fact

**20. [Scenario / Judgment] Very Hard**

> A student says: "Once you use StackSets, you no longer need Service Catalog, since StackSets already handle deploying resources across the organization." Evaluate this using this module's content.

> **A.** Agree — StackSets make Service Catalog completely redundant
> **B.** Disagree — StackSets solve deploying the *same* template consistently across many accounts and Regions (an administrator-driven push), while Service Catalog solves letting *specific non-admin users* self-service provision from a restricted, pre-approved catalog — different problems, often used together
> **C.** Disagree, but only because StackSets cannot deploy to more than one account
> **D.** Agree, since Service Catalog and StackSets both require the same IAM permissions

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
