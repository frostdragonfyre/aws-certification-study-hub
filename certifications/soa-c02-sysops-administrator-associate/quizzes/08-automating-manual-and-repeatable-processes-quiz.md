**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 8 Knowledge Check**

Automating Manual and Repeatable Processes · 20 questions · Practice — not graded

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

> Run Command is designed for immediate, ad hoc actions rather than documented, repeatable workflows.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What is a Systems Manager Automation workflow called?

> **A.** A run command
> **B.** A runbook
> **C.** A change set
> **D.** A stack instance

**3. [Fill in the Blank] Easy**

> A ____________ expression fires at a fixed, recurring interval, like every 12 hours.

**4. [Multiple Choice] Easy**

> Which expression type fits a schedule like "every Sunday at 2 AM"?

> **A.** A rate expression
> **B.** A cron expression
> **C.** Neither can express a specific day and time
> **D.** A change set expression

**5. [True / False] Easy**

> AWS Lambda is generally the right tool for a standard operational task that already has a built-in SSM Automation runbook.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> A scenario says: "restart this specific service on these three servers right now." What fits best?

> **A.** Systems Manager Automation, since every action should be documented
> **B.** Run Command — an immediate, ad hoc action on specified instances
> **C.** An EventBridge scheduled rule
> **D.** A CloudFormation change set

**7. [Fill in the Blank] Moderate**

> A ____________ expression fires at specific, calendar-based times, like the first of the month.

**8. [Multiple Choice] Moderate**

> Why does patching Meridian's EC2 fleet use a built-in SSM Automation runbook instead of custom Lambda code?

> **A.** Lambda cannot be triggered by EventBridge
> **B.** Patching is a well-defined, standard action already covered by an AWS-provided runbook, so writing custom code would be unnecessary engineering effort
> **C.** SSM Automation cannot run on a schedule
> **D.** Built-in runbooks cannot include rollback behavior

**9. [True / False] Moderate**

> A cron expression can express a fixed, simple interval like "every 6 hours" just as easily as a rate expression.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Café Sol needs old order records archived from DynamoDB to S3 in a specific business-defined format, once a month. What fits best?

> **A.** A built-in SSM Automation runbook, since archiving is a standard AWS action
> **B.** A Lambda function with the custom transformation logic, triggered by an EventBridge scheduled rule
> **C.** Run Command, executed manually each month
> **D.** A CloudFormation StackSet

**11. [Fill in the Blank] Moderate**

> Systems Manager ____________ runs a documented, multi-step workflow, potentially including approval steps and rollback behavior.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A team wants a process that runs the exact same documented sequence of steps every time, with approval gates, and can be triggered manually, on a schedule, or by an event. What AWS feature is being described?

> **A.** Run Command
> **B.** Systems Manager Automation, using a runbook
> **C.** A CloudFormation change set
> **D.** AWS Service Catalog

**13. [Scenario / Judgment] Hard**

> A scenario needs a Lambda function to run every 3 days, with no requirement tied to a specific day of the week or calendar date. What schedule expression fits best?

> **A.** A cron expression, since it's always more precise
> **B.** A rate expression — `rate(3 days)` — the simplest fit for a fixed interval with no calendar-specific requirement
> **C.** Neither expression type can express a multi-day interval
> **D.** A change set expression

**14. [Scenario / Judgment] Hard**

> A team writes a custom Lambda function to patch EC2 instances, duplicating logic that `AWS-RunPatchBaseline` already provides as a built-in Automation runbook. What's the issue?

> **A.** There is no issue — custom code is always preferable
> **B.** This is unnecessary engineering effort — a standard, well-known task like patching already has a built-in runbook, and reinventing it in custom code adds maintenance burden with no real benefit
> **C.** Lambda cannot patch EC2 instances under any circumstances
> **D.** SSM Automation runbooks cannot patch EC2 instances at all

**15. [Scenario / Judgment] Hard**

> An engineer needs to pull a specific log file from 5 servers immediately to debug a live issue, with no need for this to be repeatable or scheduled. What fits best?

> **A.** Systems Manager Automation, since it's always the more powerful option
> **B.** Run Command — an immediate, targeted, one-off action
> **C.** An EventBridge cron expression
> **D.** AWS Service Catalog

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Run Command and Systems Manager Automation are the same thing — they both run actions on instances." Correct this using this module's content.

> **A.** They're right — there's no meaningful difference between the two
> **B.** They're different: Run Command executes an immediate, ad hoc action on specified instances, while Automation runs a documented, multi-step, repeatable runbook that can include approvals and rollback — one is for "right now," the other is for "the same way, every time"
> **C.** Automation is simply a faster version of Run Command
> **D.** Run Command supports rollback behavior; Automation does not

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes using a cron expression for every scheduled automation, arguing "cron is more powerful, so it's always the better choice." Evaluate this using this module's content.

> **A.** Agree — cron should always be used regardless of the schedule's actual requirements
> **B.** Disagree — a rate expression is the simpler, more appropriate fit for a fixed interval with no calendar-specific requirement; reaching for cron's added complexity when it isn't needed doesn't add value, it just adds unnecessary configuration
> **C.** Disagree, but only because cron expressions cannot be used with EventBridge
> **D.** Agree, since rate expressions cannot trigger Lambda functions

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why writing a custom Lambda function to restart an unresponsive EC2 instance would usually be the wrong call.

> **A.** Lambda functions cannot interact with EC2 instances under any circumstances
> **B.** Restarting an unresponsive instance is a well-known, standard operational task already covered by an AWS-provided SSM Automation runbook, so custom Lambda code would be duplicating something that already exists and adding unnecessary maintenance burden
> **C.** SSM Automation runbooks cannot be triggered by EventBridge, so Lambda is required
> **D.** Custom Lambda code is always the more reliable choice regardless of what built-in options exist

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that since Module 2 already covered EventBridge triggering SSM Automation for remediation, tonight's scheduled-rule content is redundant. Argue against this using this module's content.

> **A.** Agree — scheduled rules and event-pattern rules are the same mechanism with no meaningful difference
> **B.** Disagree — Module 2's EventBridge use was reactive, triggered by something going wrong; tonight's scheduled rules are proactive, running routine maintenance on a recurring basis whether or not anything unusual has happened — the trigger mechanism is shared, but the purpose and the schedule-vs-event-pattern distinction are different enough to need their own treatment
> **C.** Agree, since EventBridge can only be used for one purpose at a time
> **D.** Disagree, but only because Module 2 never mentioned EventBridge

**20. [Scenario / Judgment] Very Hard**

> A student says: "Automation is just for emergencies — routine maintenance should always be done manually so a human can double-check it." Evaluate this using this module's content.

> **A.** Agree — manual execution is always safer than automation for routine tasks
> **B.** Disagree — routine, repeatable processes like patching, cleanup, and scheduled archival are exactly the kind of work that shouldn't need a human doing it the same way every time; SSM Automation runbooks and EventBridge scheduled rules exist specifically to make that routine work consistent and hands-off, not just for emergency remediation
> **C.** Disagree, but only because Systems Manager Automation cannot run without human approval at every step
> **D.** Agree, since EventBridge scheduled rules are only used for security incidents

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
