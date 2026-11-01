<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](12-designing-meridian-loyaltys-cost-strategy.md) · [Next module](14-improving-reliability-performance-and-cost.md) · [Quiz](../quizzes/13-continuously-improving-an-existing-solution-quiz.md) · [Slides](../lectures/13-continuously-improving-an-existing-solution.pptx)
<!-- /hub-navigation -->

# Module 13: Continuously Improving an Existing Solution — Operational Excellence and Security

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Domain 2 built Meridian Loyalty from nothing, one deliberate decision at a time. Domain 3 asks a different question: what about the architecture that's already running? Café Sol's original system — the one built across Modules 1 through 16 of SAA-C03 — has been live for six months under Meridian's ownership now, handling real orders every day, and it was never revisited with everything Frank, Martha, and Sofía have learned since. This module is Domain 3, Tasks 3.1 and 3.2: conducting a formal review of an existing solution, and improving it — operationally and from a security standpoint — without a rebuild.

## Learning objectives

By the end of this module, you should be able to:

- Explain what a AWS Well-Architected Framework review actually produces, and how it differs from Trusted Advisor
- Identify operational excellence gaps in an existing architecture and the AWS tools that address them
- Use AWS IAM Access Analyzer to find unused permissions and unintended external access in an existing environment
- Distinguish IAM Access Analyzer's purpose from GuardDuty's
- Design a continuous improvement plan for a stated existing-solution scenario

---

## Conducting a Formal Review of Café Sol's Architecture

Café Sol's system has run well for six months — but "runs well" and "reviewed against current best practice" aren't the same claim, and Domain 3 is built around making that distinction concrete.

The **AWS Well-Architected Tool** walks an existing workload through a structured, six-pillar review — operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability — producing a specific list of gaps against best practices for that particular architecture, prioritized by risk. It's a point-in-time (or periodic) deep review, conducted deliberately, that Sofía runs against Café Sol's actual design.

**AWS Trusted Advisor** is different: it continuously scans an account against a broad set of automated checks — cost, security, fault tolerance, performance, and service limits — surfacing specific, actionable findings (an open security group, an idle load balancer, an approaching service quota) in near real time, without anyone needing to schedule anything.

Both matter here, and they're not substitutes for each other: the **Well-Architected review** is how Sofía discovers that Café Sol's original design, reasonable in isolation, never accounted for multi-brand realities; **Trusted Advisor** is what keeps catching the smaller, ongoing issues in between formal reviews.

> ⚠️ **Exam trap:** the exam expects you to know that the Well-Architected Tool is a structured, deliberate review producing a prioritized improvement plan against an architecture's actual design choices, while Trusted Advisor is continuous, automated, and check-based — not a substitute for a real architectural review, but not something a periodic review replaces either. A well-run continuous improvement program uses both.

## Operational Excellence: Turning Runbooks into Automation

The Well-Architected review's operational excellence findings for Café Sol turn up something predictable: several manual runbooks — restarting a stuck order-processing job, rotating a credential, scaling up ahead of a known lunch rush — that Frank or Martha's team still perform by hand, the same way they did when Café Sol was a single independent café.

**AWS Systems Manager Automation** converts a manual runbook into a defined, repeatable automation document — the same steps, executed consistently, without depending on the one person who remembers exactly how to do it. **AWS Config**, tracking configuration changes and evaluating resources against defined rules, catches drift — a security group opened temporarily for a fix and never closed back up — before it becomes a real incident rather than after.

Neither tool rebuilds Café Sol's architecture. Both make the architecture that already works, work more consistently, with fewer steps that depend on one specific person's memory.

## Improving Security Posture: AWS IAM Access Analyzer

Six months of ordinary operation tends to leave residue: IAM roles created for a project that finished, permissions granted broadly because narrowing them took more time under a deadline, an S3 bucket policy that technically allows more access than anyone intended.

**AWS IAM Access Analyzer** finds exactly this: it identifies resources shared with an external entity (an S3 bucket, an IAM role, a KMS key reachable from outside the intended boundary) and, through its unused access findings, flags permissions granted but never actually used — the accumulated slack in a real, lived-in environment. Sofía runs it against Café Sol's account and gets a concrete list: a forgotten cross-account role from a vendor integration that ended months ago, an IAM policy still granting write access nobody has used in that time.

This is a different tool from **Amazon GuardDuty**, which detects active threats — unusual API activity, a compromised credential being used maliciously — in near real time. Access Analyzer looks at what's *possible* given current permissions and public exposure, regardless of whether anything malicious is actually happening; GuardDuty looks for signs that something malicious *is* happening. Both matter for security posture, but they answer different questions.

> ⚠️ **Exam trap:** "unused permissions" and "unintended external access" point to IAM Access Analyzer — a permissions-and-exposure question. "Active malicious behavior" or "a compromised credential in use" points to GuardDuty — a threat-detection question. Confusing the two means reaching for threat detection when the actual problem is permission hygiene, or vice versa.

## Putting It Together: Café Sol's Continuous Improvement Plan

Sofía's improvement plan for Café Sol's existing architecture:

- **A Well-Architected Tool review**, producing a prioritized list of gaps against Café Sol's actual six-month-old design — supplemented by **Trusted Advisor**'s continuous, automated checks in between reviews.
- **Systems Manager Automation** converting the team's manual runbooks into consistent, repeatable procedures; **AWS Config** catching configuration drift before it becomes an incident.
- **IAM Access Analyzer** clearing out accumulated unused permissions and unintended external access, distinct from **GuardDuty**'s ongoing watch for active threats.

## What to skip

You don't need to memorize the Well-Architected Framework's full pillar-by-pillar question list or Access Analyzer's exact finding-type taxonomy — that's implementation depth beyond this exam. What matters is telling a structured review apart from continuous automated checking, knowing what Systems Manager Automation and Config actually catch, and telling permission hygiene (Access Analyzer) apart from threat detection (GuardDuty).

## Key takeaways

- The Well-Architected Tool produces a structured, prioritized review of an existing architecture's design; Trusted Advisor continuously surfaces automated checks — a well-run program uses both, not one instead of the other.
- Systems Manager Automation converts manual runbooks into consistent, repeatable procedures; AWS Config catches configuration drift before it becomes an incident.
- IAM Access Analyzer identifies unused permissions and unintended external access — a permissions-and-exposure question — distinct from GuardDuty's active threat detection.
- An existing solution that "runs well" hasn't necessarily been reviewed against current best practice — continuous improvement is a deliberate, ongoing process, not a one-time check.
- Domain 3 revisits what Domain 2 built new — the same underlying concerns (operational excellence, security, and more to come), applied to something already running instead of something being designed from scratch.

## Further reading

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — the six pillars and the review process.
- [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) — continuous, automated account checks.
- [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) — converting manual runbooks into repeatable procedures.
- [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) — unused access and external resource sharing.
