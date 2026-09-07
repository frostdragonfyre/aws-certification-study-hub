**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 11 Knowledge Check**

Automating Your Architecture · 20 questions · Practice — not graded

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

> A CloudFormation template describes desired AWS resources in a text file, rather than requiring them to be built manually through the console.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What is a CloudFormation stack?
>
> **A.** The text file describing desired resources
> **B.** The deployed, managed collection of resources created from a template
> **C.** A type of EC2 instance
> **D.** A billing report

**3. [Fill in the Blank] Easy**

> A CloudFormation ____________ set previews exactly what a stack update will do before it's applied.

**4. [Multiple Choice] Easy**

> Which Systems Manager capability provides secure shell access to an EC2 instance without opening an inbound SSH port?
>
> **A.** Patch Manager
> **B.** Session Manager
> **C.** Parameter Store
> **D.** Automation

**5. [True / False] Easy**

> AWS Elastic Beanstalk requires you to write a full CloudFormation template before deploying an application.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What happens when a CloudFormation stack is deleted?
>
> **A.** Nothing — stacks cannot be deleted once created
> **B.** Every resource the stack created is deleted, in the correct dependency order
> **C.** Only the template file is removed; resources remain
> **D.** Resources are paused, not deleted

**7. [Fill in the Blank] Moderate**

> AWS Systems Manager's ____________ Manager automates applying OS and software patches across a fleet of instances.

**8. [Multiple Choice] Moderate**

> Which of the following is a genuine benefit of infrastructure as code, according to this module?
>
> **A.** It eliminates the need for any AWS resources at all
> **B.** It's version-controllable, repeatable, and self-documenting
> **C.** It only works for a single AWS Region
> **D.** It removes the need for a change set before updates

**9. [True / False] Moderate**

> A change set can show that a stack update would replace a resource entirely, rather than update it in place.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does AWS Elastic Beanstalk primarily ask the person deploying to provide?
>
> **A.** A complete CloudFormation template
> **B.** Application code
> **C.** A fully pre-configured VPC
> **D.** A Systems Manager Automation document

**11. [Fill in the Blank] Moderate**

> Elastic Beanstalk still runs on real underlying resources like EC2 and ____________ — it isn't a separate compute model.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> The café wants to redeploy its exact current architecture — VPC, subnets, ALB, Auto Scaling group, RDS Multi-AZ — in a second Region for disaster recovery. Which tool best fits this specific need?
>
> **A.** AWS Elastic Beanstalk, since it deploys applications quickly
> **B.** AWS CloudFormation, since the architecture is already precisely designed and needs to be reproduced exactly
> **C.** AWS Systems Manager Automation alone
> **D.** Manually reconfiguring each resource by hand in the new Region

**13. [Scenario / Judgment] Hard**

> A team applies a CloudFormation stack update without reviewing a change set first, and the update unexpectedly replaces their production RDS database. What could have caught this in advance?
>
> **A.** Nothing — this risk cannot be detected beforehand
> **B.** Reviewing the change set, which would have shown the database resource would be replaced, not updated in place
> **C.** Elastic Beanstalk would have prevented this automatically
> **D.** Change sets only apply to EC2 resources, not RDS

**14. [Scenario / Judgment] Hard**

> A small team without a dedicated infrastructure engineer wants to get a new application running on AWS as quickly as possible, and is comfortable with AWS-managed defaults for the underlying infrastructure. What fits best?
>
> **A.** AWS CloudFormation, written from scratch
> **B.** AWS Elastic Beanstalk
> **C.** Manually provisioning each resource through the console
> **D.** AWS Systems Manager Automation

**15. [Scenario / Judgment] Hard**

> An administrator wants every EC2 instance in a growing fleet patched on a regular schedule, without manually logging into each one. Which Systems Manager capability fits?
>
> **A.** Session Manager
> **B.** Patch Manager
> **C.** Parameter Store
> **D.** CloudFormation change sets

**16. [Scenario / Judgment] Hard**

> Why does a version-controlled CloudFormation template answer "what is our production setup right now?" more reliably than checking the console?
>
> **A.** The console is always inaccurate
> **B.** The template is the actual, current, reviewable description of what was declared and deployed, with a change history — rather than relying on someone accurately remembering or re-discovering months of accumulated manual console changes
> **C.** CloudFormation templates cannot be wrong once written
> **D.** The console cannot display resource configurations at all

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Elastic Beanstalk and CloudFormation solve completely different problems, since Beanstalk doesn't use CloudFormation-style infrastructure at all." Evaluate this claim.
>
> **A.** True — Beanstalk uses an entirely separate, non-AWS compute model
> **B.** False in the way stated — Beanstalk still provisions real, familiar AWS resources like EC2 and load balancers; the actual difference is who manages the provisioning decisions (Beanstalk automates them, CloudFormation makes them explicit), not the underlying resource types
> **C.** True, because Beanstalk applications never touch EC2
> **D.** False, because Beanstalk and CloudFormation are the exact same service with different names

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues that Session Manager is "just a nice-to-have" compared to traditional SSH access. What's the strongest counterargument using this module's content?
>
> **A.** There is no meaningful difference between the two approaches
> **B.** Session Manager removes the need to open an inbound SSH port at all, manages access entirely through IAM instead of distributed SSH keys, and can log every session for audit — closing off a category of exposure that an open SSH port carries, not just a convenience improvement
> **C.** SSH is always more secure than Session Manager
> **D.** Session Manager only works with Elastic Beanstalk applications

**19. [Scenario / Judgment] Very Hard**

> Connect this module to Module 10. Why does a large, dynamically-scaling Auto Scaling group make Systems Manager more valuable, not just convenient?
>
> **A.** Systems Manager has no particular relevance to Auto Scaling groups
> **B.** As instances are added and removed automatically, they may not have fixed, individually memorized identities — patching, accessing, and automating tasks across a fleet like that by hand doesn't scale, which is exactly the operational gap Systems Manager's fleet-wide tools (Patch Manager, Automation, Session Manager) close
> **C.** Auto Scaling groups automatically include Systems Manager with no additional value provided
> **D.** Systems Manager replaces the need for Auto Scaling entirely

**20. [Scenario / Judgment] Very Hard**

> A team debates whether to build the café's V6 architecture with CloudFormation or by continuing to configure resources by hand "since it already works." What's the strongest argument for CloudFormation even though the current manual setup is functional?
>
> **A.** Manual configuration is always broken and unusable
> **B.** A working manual setup today doesn't make it repeatable, reviewable, or safely reproducible in a second Region — CloudFormation captures the design as a versioned artifact that can be redeployed, audited, and safely updated (via change sets) rather than depending on institutional memory of how it was clicked together
> **C.** CloudFormation is required by AWS for any production workload
> **D.** There is no real advantage; the two approaches are equivalent in practice

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
