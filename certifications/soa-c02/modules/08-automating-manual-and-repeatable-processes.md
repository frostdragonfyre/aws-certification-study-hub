# Module 8: Automating Manual and Repeatable Processes

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Module 7 made sure Meridian's infrastructure gets created consistently. This module asks what happens after it exists: the routine, repeatable operational work — patching, cleanup, maintenance windows — that someone currently does by hand, on a schedule, the same way every time. That's exactly the kind of work that shouldn't need a human doing it manually. This is Domain 3's second and final task, closing out Domain 3.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish AWS Systems Manager Automation from Run Command, and know when each fits
- Explain how EventBridge scheduled rules trigger automation on a recurring basis
- Distinguish a rate expression from a cron expression, and know when each fits
- Explain when custom Lambda logic is the right tool instead of a built-in Automation runbook
- Design an automated maintenance workflow for a stated repeatable process

---

## Systems Manager Automation vs. Run Command

AWS Systems Manager offers two related but distinctly different ways to act on managed instances, and they answer different questions.

**Run Command** executes a specific command or script on one or more managed instances immediately, on demand — install a package right now, restart a service right now, pull a log file right now. It's ad hoc: a single action, run once, targeted at whatever instances you specify at the moment you run it.

**Systems Manager Automation** runs a documented, multi-step workflow called a **runbook** — a predefined sequence of actions, potentially spanning multiple AWS services, with approval steps, rollback behavior, and built-in AWS-provided runbooks for common operational tasks like patching an AMI, restarting an unresponsive EC2 instance, or taking a snapshot before a risky change. An Automation runbook can be triggered manually, on a schedule, or in response to an event — and unlike Run Command, it's built for a workflow that needs to be documented, repeatable, and consistent every time it runs.

> ⚠️ **Exam trap:** a scenario describing a one-off, immediate action on specific instances — "run this command on these servers right now" — is describing **Run Command**. A scenario describing a documented, multi-step, repeatable operational process — especially one that needs to run the same way every time, on a schedule, or as part of a larger remediation workflow — is describing **Systems Manager Automation**. Reaching for Run Command when the actual need is a repeatable, auditable runbook is a common wrong turn.

## EventBridge Scheduled Rules: Automation on a Schedule

Module 2 covered EventBridge reacting to an *event* — something happening that triggers a response. But not all automation is reactive. Routine maintenance — a nightly cleanup Lambda function, a weekly patch window, a monthly cost report — needs to run on a **schedule**, whether or not anything unusual has happened.

**EventBridge scheduled rules** trigger a target (a Lambda function, an SSM Automation runbook, and more) at specified times, using one of two expression types. A **rate expression** (like `rate(1 day)` or `rate(12 hours)`) fires at a fixed, recurring interval starting from whenever the rule was created — simple, and the right fit when all that matters is "every X amount of time." A **cron expression** (like `cron(0 2 * * ? *)`) fires at specific, calendar-based times — a particular hour, day of the week, or day of the month — the right fit when the schedule has to match a real-world constraint, like "every Sunday at 2 AM" or "the first of the month."

> ⚠️ **Exam trap:** a scenario asking for something to run "every 6 hours" or "every 3 days" — a simple, fixed interval with no calendar-specific requirement — is describing a **rate expression**. A scenario asking for something to run "every Sunday at 2 AM" or "on the last day of the month" — a schedule tied to specific calendar times — is describing a **cron expression**. Using cron for a simple fixed interval works but adds unnecessary complexity; using rate for a calendar-specific requirement often can't express what's actually needed at all.

## When Lambda Is the Right Tool Instead of a Built-In Runbook

Systems Manager Automation ships with AWS-provided runbooks for many common tasks, but not every operational process fits a built-in action. When the automation needs custom logic — calling an internal API, transforming data in a specific way, making a decision based on business rules that don't map to a standard AWS action — **AWS Lambda** is the right tool: a function containing exactly the custom code the process needs, triggered by EventBridge (scheduled or event-driven) or invoked as a step within a larger Automation runbook.

Priya uses this distinction directly: patching Meridian's EC2 fleet uses a built-in SSM Automation runbook (`AWS-RunPatchBaseline`) on a scheduled EventBridge rule — no custom code needed, since patching is already a well-defined, standard action. But archiving Café Sol's old order records from DynamoDB to S3 in a specific business-defined format, on the first of every month, needs custom logic no built-in runbook provides — that's a Lambda function, triggered by an EventBridge scheduled rule.

> ⚠️ **Exam trap:** a scenario describing a standard, well-known operational task — patching, restarting, snapshotting — is usually pointing at a **built-in SSM Automation runbook**, not custom code. A scenario describing business-specific logic, custom data transformation, or an action with no standard AWS-provided runbook is pointing at **Lambda**. Writing custom Lambda code to replicate what a built-in runbook already does is unnecessary engineering effort.

## Putting It Together: Automating Meridian's Routine Operations

Priya's automation strategy, closing out Domain 3:

- **SSM Automation runbooks** for documented, repeatable operational workflows — patching, instance recovery, pre-change snapshots — instead of Run Command's one-off, ad hoc actions.
- **EventBridge scheduled rules** triggering those runbooks and maintenance Lambda functions: **rate expressions** for simple fixed intervals (a cleanup job every 12 hours), **cron expressions** for calendar-specific timing (a patch window every Sunday at 2 AM).
- **Lambda functions** reserved for genuinely custom logic — Café Sol's monthly archival job — while standard tasks use AWS's built-in runbooks instead of reinventing them in code.

## What to skip

You don't need to memorize the full cron expression syntax or every AWS-provided Automation runbook by name — that's implementation depth beyond this exam. What matters is knowing when Automation fits better than Run Command, when a rate expression fits better than a cron expression, and recognizing when custom Lambda logic is actually necessary versus reinventing a built-in runbook.

## Key takeaways

- Run Command executes an immediate, ad hoc action; Systems Manager Automation runs a documented, repeatable, multi-step runbook — pick based on whether the action needs to be one-off or standardized and repeatable.
- EventBridge scheduled rules trigger automation on a recurring basis, using either a rate expression (simple fixed intervals) or a cron expression (calendar-specific timing).
- Lambda is the right tool for genuinely custom automation logic; a standard operational task usually already has a built-in SSM Automation runbook that doesn't need to be replicated in code.
- This closes Domain 3: Module 7 made resource creation consistent, and Module 8 made the routine operational work around that infrastructure automated instead of manual.

## Further reading

- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) — runbooks, built-in documents, and workflow steps.
- [AWS Systems Manager Run Command](https://docs.aws.amazon.com/systems-manager/latest/userguide/execute-remote-commands.html) — ad hoc command execution on managed instances.
- [Creating an Amazon EventBridge Rule That Runs on a Schedule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-create-rule-schedule.html) — rate and cron expressions.
- [Schedule Expressions for Rules](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-scheduled-rule-pattern.html) — rate() and cron() syntax reference.
