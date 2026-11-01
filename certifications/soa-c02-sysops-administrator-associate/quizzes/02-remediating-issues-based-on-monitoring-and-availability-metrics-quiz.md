[Course index](../README.md) · [Read the paired lesson](../modules/02-remediating-issues-based-on-monitoring-and-availability-metrics.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 2 Knowledge Check**

Remediating Issues Based on Monitoring and Availability Metrics · 20 questions · Practice — not graded

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

> The "recover" EC2 alarm action restarts the operating system in place, on the same underlying hardware.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which EC2 status check does "recover" address?

> **A.** Instance status check
> **B.** System status check
> **C.** Auto Scaling health check
> **D.** ELB target health check

**3. [Fill in the Blank] Easy**

> Amazon ____________ can route a CloudWatch alarm's state change to a target, such as a Systems Manager Automation runbook.

**4. [Multiple Choice] Easy**

> Which requirement must an instance meet for the "recover" alarm action to be available?

> **A.** It must be instance store-backed
> **B.** It must be EBS-backed and on a supported instance type
> **C.** It must be part of an Auto Scaling group
> **D.** It must have detailed monitoring enabled

**5. [True / False] Easy**

> An Auto Scaling policy and a built-in EC2 alarm action solve the same problem in the same way.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does "recover" preserve the instance's ID, private IP, and attached EBS volumes?

> **A.** It creates a brand-new instance with the same name
> **B.** It moves the instance to new, healthy underlying hardware while keeping its identity and storage intact
> **C.** It restarts the operating system without changing hardware
> **D.** It terminates the instance and relies on Auto Scaling to replace it

**7. [Fill in the Blank] Moderate**

> A documented, repeatable sequence of steps that can restart a service, run a script, or patch a package is an AWS Systems Manager ____________ runbook.

**8. [Multiple Choice] Moderate**

> A single instance in an Auto Scaling group fails its instance status check because a hung application isn't responding. What's the appropriate response?

> **A.** An Auto Scaling policy, since only capacity changes can fix a hung application
> **B.** Reboot that instance, or let the Auto Scaling group's own health check replace it — this is a single unhealthy instance, not a load problem
> **C.** Recover, since instance status check failures always require moving to new hardware
> **D.** Nothing — instance status check failures resolve themselves automatically

**9. [True / False] Moderate**

> Built-in EC2 alarm actions can restart a specific application service without rebooting the whole operating system.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Why does Priya use an Auto Scaling policy, not a "reboot" alarm action, when checkout service load increases?

> **A.** Reboot actions are always disabled on instances in an Auto Scaling group
> **B.** Increased load isn't an unhealthy-instance problem — it's a capacity problem, which a scaling policy addresses by changing how many instances exist
> **C.** Auto Scaling policies can only decrease capacity, never increase it
> **D.** Rebooting an instance always increases its capacity to handle load

**11. [Fill in the Blank] Moderate**

> An instance that is ____________-backed, rather than EBS-backed, cannot use the "recover" alarm action.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A checkout service instance fails its system status check — the underlying hardware has a problem, not the instance's own configuration. The instance is EBS-backed on a supported instance type. What's the best built-in response?

> **A.** Reboot, since restarting the OS fixes hardware problems
> **B.** Recover — it moves the instance to healthy hardware while preserving its instance ID, IP, and EBS volumes
> **C.** Terminate, since system status check failures always require full replacement
> **D.** Nothing — system status check failures cannot be remediated

**13. [Scenario / Judgment] Hard**

> An instance store-backed instance on an unsupported instance family fails its system status check. What's the issue with attempting "recover"?

> **A.** There is no issue — recover works identically for every instance type and storage configuration
> **B.** Recover isn't available for instance store-backed instances or unsupported instance types, since recovery depends on moving the instance's storage to new hardware — a different remediation path, such as replacement through an Auto Scaling group, is needed
> **C.** Recover only works for instance store-backed instances, never EBS-backed ones
> **D.** System status check failures on unsupported instance types resolve without any action

**14. [Scenario / Judgment] Hard**

> Priya wants a hung application service restarted automatically the moment a specific error pattern appears in the logs, without rebooting the whole instance or paging anyone. What should she build?

> **A.** A built-in EC2 "reboot" alarm action, since it's the closest fixed option
> **B.** An EventBridge rule triggered by the alarm, invoking a Systems Manager Automation runbook that restarts just that service
> **C.** An Auto Scaling policy, since scaling always resolves application-level issues
> **D.** Nothing can automate a fix more specific than reboot

**15. [Scenario / Judgment] Hard**

> A student argues that Auto Scaling policies and EC2 alarm actions are interchangeable, since both are triggered by CloudWatch alarms. What's the flaw?

> **A.** There is no flaw — they are fully interchangeable in every scenario
> **B.** An EC2 alarm action fixes one specific unhealthy instance; an Auto Scaling policy changes the group's overall capacity in response to load — they address different kinds of problems despite both reacting to alarms
> **C.** Auto Scaling policies cannot be triggered by CloudWatch alarms
> **D.** EC2 alarm actions can only be used within Auto Scaling groups

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Module 1 built the alarms, so Module 2 is really just about making more alarms." Correct this using this module's content.

> **A.** They're right — Module 2 is entirely about creating additional alarms
> **B.** Module 2 doesn't create more alarms — it connects the alarms Module 1 already built to actual remediation: built-in EC2 actions like recover and reboot, Auto Scaling policies for capacity, and EventBridge triggering Systems Manager Automation for anything more specific — turning signal into action
> **C.** Module 2 replaces every alarm from Module 1 with a new one
> **D.** There is no meaningful difference between an alarm and a remediation action

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes setting every EC2 alarm's action to "recover," arguing it's the safest universal choice. Evaluate this using this module's content.

> **A.** Agree — recover is always the correct action regardless of the failure or instance configuration
> **B.** Disagree — recover only fits a system status check failure on an EBS-backed, supported instance type; an instance status check failure calls for reboot instead, and an instance store-backed or unsupported instance can't use recover at all, requiring a different remediation path
> **C.** Disagree, but only because recover is technically disabled by default on all instances
> **D.** Agree, since reboot and terminate no longer exist as valid alarm actions

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why EventBridge plus a Systems Manager Automation runbook can remediate a problem that no built-in EC2 alarm action ever could.

> **A.** Built-in alarm actions already cover every possible remediation scenario, so this situation can't happen
> **B.** Built-in EC2 alarm actions are limited to a fixed set — recover, reboot, stop, terminate — that act on the whole instance; an Automation runbook is a scripted, arbitrary sequence of steps that can target something specific, like restarting one service, which none of the fixed actions can do
> **C.** EventBridge can only trigger other CloudWatch alarms, not Automation runbooks
> **D.** Systems Manager Automation cannot be triggered by EventBridge under any circumstances

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping Auto Scaling entirely and just setting every instance's alarm action to "reboot" whenever load increases, arguing "rebooting clears whatever's slowing it down." Argue against this using this module's content.

> **A.** Agree — rebooting is always an effective response to increased load
> **B.** Disagree — increased load isn't an unhealthy-instance problem that rebooting fixes; it's a capacity problem, and the correct response is an Auto Scaling policy that changes how many instances exist to handle the actual demand, not restarting instances that were never unhealthy to begin with
> **C.** Disagree, but only because reboot actions are technically incompatible with load-based alarms
> **D.** Agree, since Auto Scaling policies cannot respond to CloudWatch alarms

**20. [Scenario / Judgment] Very Hard**

> A student says: "Recover, reboot, Auto Scaling, and Systems Manager Automation are four ways of doing the same thing." Evaluate this using this module's content.

> **A.** Agree — all four produce an identical outcome in every scenario
> **B.** Disagree — recover fixes hardware-level failure while preserving identity, reboot fixes an OS-level hang in place, Auto Scaling changes capacity in response to load, and Systems Manager Automation via EventBridge handles arbitrary, specific remediation beyond any fixed action — four genuinely different tools matched to four different problems
> **C.** Disagree, but only because Auto Scaling and Systems Manager Automation are the same service
> **D.** Agree, since all four require exactly the same instance configuration to use

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
