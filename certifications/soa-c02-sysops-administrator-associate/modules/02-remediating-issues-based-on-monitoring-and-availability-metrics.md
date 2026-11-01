<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](01-implementing-metrics-alarms-and-filters.md) · [Next module](03-maintaining-and-troubleshooting-logging-solutions.md) · [Quiz](../quizzes/02-remediating-issues-based-on-monitoring-and-availability-metrics-quiz.md) · [Slides](../lectures/02-remediating-issues-based-on-monitoring-and-availability-metrics.pptx)
<!-- /hub-navigation -->

# Module 2: Remediating Issues Based on Monitoring and Availability Metrics

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Module 1 gave Priya the signal — metrics, alarms, and log-based filters that reliably surface a real problem. An alarm that just pages a human every time is still useful, but it doesn't scale, and it means someone is always on the hook to type the same fix at 2 a.m. This module is Domain 1, Task 1.2: turning a monitoring signal into an action AWS takes automatically, before a human has to.

## Learning objectives

By the end of this module, you should be able to:

- Match an EC2 status check failure to the correct built-in alarm action — recover, reboot, or replace
- Explain what "recover" actually does, and the conditions under which it isn't available
- Distinguish an EC2 alarm action from an Auto Scaling response to the same alarm
- Describe how EventBridge and AWS Systems Manager Automation extend remediation beyond what a built-in alarm action can do
- Design a complete remediation strategy for a stated availability scenario

---

## Matching the Alarm Action to the Actual Failure

An EC2 instance reports two status checks: **system status check** (the underlying hardware and network the instance runs on) and **instance status check** (the operating system and the instance itself). A CloudWatch alarm on either of these can trigger a **built-in EC2 alarm action** — and which action fits depends entirely on which check actually failed.

**Recover** moves the instance to new, healthy underlying hardware, preserving its instance ID, private IP address, Elastic IP, and attached EBS volumes — it's the fit for a **system status check failure**, where the problem is the hardware Meridian Loyalty's instance happens to be running on, not anything about the instance's own configuration. **Reboot** restarts the operating system in place — appropriate for an **instance status check failure** where the OS or application has genuinely hung, but the underlying hardware is fine. **Stop** and **terminate** are available too, but they're a much bigger hammer — appropriate mainly when an instance is part of an Auto Scaling group and the group itself will replace it, not for a single standalone instance you actually need to keep running.

> ⚠️ **Exam trap:** "recover" isn't available for every instance. It only works for a supported subset of instance types, and it requires an EBS-backed instance — an instance store-backed instance can't be recovered this way, because recovery depends on being able to move the instance's storage to new hardware. A scenario describing an instance store-backed instance, or an unsupported instance family, with a system status check failure needs a different remediation path — often replacing the instance entirely, through an Auto Scaling group if it's in one.

## EC2 Alarm Action vs. Auto Scaling Response

A built-in EC2 alarm action and an Auto Scaling policy can look similar — both react to a CloudWatch alarm — but they solve different problems. A **recover** or **reboot** alarm action responds to that specific instance being unhealthy, and acts on that one instance. An **Auto Scaling policy**, by contrast, responds to a *load* signal — like average CPU utilization across the group — by changing how many instances exist, not by fixing any one of them.

If Meridian Loyalty's checkout service instances are part of an Auto Scaling group, and one specific instance fails its status checks, that's an alarm-action problem (recover or reboot that instance, or let the ASG's own health check replace it). If the checkout service overall is under heavier load than its current capacity handles well, that's a scaling problem, solved by an Auto Scaling policy adding capacity — not by rebooting anything.

## Extending Remediation with EventBridge and Systems Manager Automation

Built-in EC2 alarm actions only cover a narrow set of fixed responses (recover, reboot, stop, terminate) to EC2-specific status checks. Most real remediation needs are broader than that — restarting a hung application service without rebooting the whole OS, rotating a credential, remediating an AWS Config rule violation, or opening a support case automatically.

**Amazon EventBridge** can route a CloudWatch alarm's state change (for example, entering ALARM) to a target that takes real action — most usefully, an **AWS Systems Manager Automation** runbook. An Automation runbook is a documented, repeatable sequence of steps (built from AWS-provided or custom automation documents) that can restart a specific service, run a script, patch a package, or take any other scripted remediation action — well beyond what a fixed EC2 alarm action can do.

Priya builds exactly this for Meridian Loyalty: a CloudWatch alarm watching for a specific application error pattern (from Module 1's metric filter) triggers an EventBridge rule, which invokes a Systems Manager Automation runbook that restarts the application service on the affected instance — without needing anyone paged for a fix that's genuinely routine.

> ⚠️ **Exam trap:** a scenario describing remediation that goes beyond EC2's fixed alarm actions — restarting a specific service, running a custom script, remediating a configuration drift — is describing EventBridge triggering Systems Manager Automation, not a built-in EC2 alarm action. Built-in alarm actions are fast and simple but genuinely limited to recover, reboot, stop, and terminate; anything more specific than that needs an actual automation runbook behind it.

## Putting It Together: Remediating Meridian Loyalty's Checkout Service

Priya's remediation strategy for the checkout service:

- A **system status check failure** alarm action set to **recover** — the checkout instances are EBS-backed and on a supported instance type, so recovery preserves the instance ID and IP without anyone paged.
- An **Auto Scaling policy** handling load-driven capacity changes separately from any individual instance's health — scaling is not a status-check remediation.
- An **EventBridge rule**, triggered by the Module 1 application-error alarm, invoking a **Systems Manager Automation runbook** that restarts the application service — covering the routine failure that no built-in alarm action can reach.

## What to skip

You don't need to memorize the full list of instance types that support recovery or every Systems Manager Automation document AWS provides out of the box — that's implementation depth beyond this exam. What matters is matching recover vs. reboot vs. replace to the actual failure, knowing recovery's EBS-backed and instance-type requirements, and recognizing when a scenario needs EventBridge plus Systems Manager Automation instead of a built-in alarm action.

## Key takeaways

- Recover fits a system status check failure and preserves the instance's identity; reboot fits an instance status check failure where the OS or application has hung.
- Recovery requires an EBS-backed instance on a supported instance type — it isn't available for instance store-backed instances or every instance family.
- An EC2 alarm action fixes one unhealthy instance; an Auto Scaling policy changes capacity in response to load — they solve different problems even though both react to alarms.
- EventBridge routing a CloudWatch alarm to a Systems Manager Automation runbook extends remediation well beyond the fixed set of built-in EC2 alarm actions.
- This is Domain 1's second task, turning Module 1's signal into automatic action — Module 3 covers the third and final piece of Domain 1, logging.

## Further reading

- [Recover Your Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-recover.html) — what EC2 instance recovery does and its requirements.
- [Creating Amazon CloudWatch Alarms That Take EC2 Actions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/UsingAlarmActions.html) — recover, reboot, stop, and terminate alarm actions.
- [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) — routing events, including alarm state changes, to targets.
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation.html) — automation runbooks for remediation.
