**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 13 Knowledge Check**

Continuously Improving an Existing Solution — Operational Excellence and Security · 20 questions · Practice — not graded

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

> An architecture that "runs well" has necessarily already been reviewed against current AWS best practice.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which tool walks an existing workload through a structured, six-pillar review producing a prioritized list of gaps?
>
> **A.** AWS Trusted Advisor
> **B.** AWS Well-Architected Tool
> **C.** Amazon GuardDuty
> **D.** AWS Config

**3. [Fill in the Blank] Easy**

> AWS ____________ ____________ continuously scans an account against automated checks — cost, security, fault tolerance, performance, and service limits.

**4. [Multiple Choice] Easy**

> Which service converts a manual runbook into a defined, repeatable automation document?
>
> **A.** AWS Config
> **B.** AWS Systems Manager Automation
> **C.** Amazon GuardDuty
> **D.** IAM Access Analyzer

**5. [True / False] Easy**

> IAM Access Analyzer and Amazon GuardDuty answer the exact same security question.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What does AWS Config catch that's relevant to Café Sol's operational excellence?

> **A.** Active malicious API activity
> **B.** Configuration drift — like a security group opened temporarily for a fix and never closed back up — before it becomes an incident
> **C.** Unused IAM permissions
> **D.** Service quota limits approaching their maximum

**7. [Fill in the Blank] Moderate**

> AWS IAM ____________ ____________ identifies unused permissions and unintended external access to resources like S3 buckets or IAM roles.

**8. [Multiple Choice] Moderate**

> Why does a well-run continuous improvement program use both the Well-Architected Tool and Trusted Advisor, rather than just one?

> **A.** They are legally required to be used together
> **B.** The Well-Architected Tool is a structured, deliberate review of an architecture's actual design; Trusted Advisor continuously surfaces automated checks in between those reviews — different cadences, different depth
> **C.** Trusted Advisor cannot be used without first running a Well-Architected review
> **D.** The Well-Architected Tool only works for brand-new workloads, never existing ones

**9. [True / False] Moderate**

> A forgotten cross-account role from a vendor integration that ended months ago is exactly the kind of finding IAM Access Analyzer is built to surface.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does Amazon GuardDuty detect, as distinguished from IAM Access Analyzer in this module?

> **A.** Unused IAM permissions granted but never exercised
> **B.** Active threats — unusual API activity, a compromised credential being used maliciously — in near real time
> **C.** Configuration drift in resource settings
> **D.** Service quota limits approaching their maximum

**11. [Fill in the Blank] Moderate**

> AWS Systems Manager ____________ converts a manual runbook into a defined, repeatable procedure that doesn't depend on one specific person's memory.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Sofía wants a deliberate, prioritized list of gaps in Café Sol's existing architecture, evaluated against current best practices across all six pillars. Which tool produces this?

> **A.** Amazon GuardDuty
> **B.** The AWS Well-Architected Tool
> **C.** AWS Systems Manager Automation
> **D.** Amazon CloudWatch alone

**13. [Scenario / Judgment] Hard**

> A reviewer proposes skipping the Well-Architected review entirely, arguing "Trusted Advisor already checks everything automatically." What's the flaw in this reasoning?

> **A.** There is no flaw — Trusted Advisor makes a Well-Architected review unnecessary
> **B.** Trusted Advisor surfaces specific, automated checks, but it doesn't produce the kind of structured, deliberate review of an architecture's actual design decisions that the Well-Architected Tool does — they serve different purposes, not one replacing the other
> **C.** Trusted Advisor cannot run against any existing workload
> **D.** The Well-Architected Tool and Trusted Advisor check for identical findings, making either one redundant

**14. [Scenario / Judgment] Hard**

> Frank's team has been manually restarting a stuck order-processing job the same way for six months. What does this module's reasoning suggest as the right fix?

> **A.** Leave it manual, since it has worked so far
> **B.** Convert it into a Systems Manager Automation document, so the same steps run consistently without depending on one specific person's memory
> **C.** Disable the order-processing job entirely
> **D.** Assign a second person to memorize the same manual steps as backup

**15. [Scenario / Judgment] Hard**

> A student says an IAM policy that grants write access nobody has used in six months isn't a real security concern "since nothing bad has happened yet." What's the flaw in this reasoning?

> **A.** There is no flaw — unused permissions are never a risk
> **B.** Unused but still-granted permissions represent accumulated exposure — a wider attack surface than necessary — even without an active incident, which is exactly what IAM Access Analyzer's unused access findings are built to surface and reduce
> **C.** GuardDuty would have already flagged this if it were a real concern
> **D.** IAM permissions expire automatically after six months regardless of use

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student argues: "Domain 3 is just Domain 2 repeated for no reason." Correct this using this module's content and Domain 2's.

> **A.** They're right — the two domains cover identical content
> **B.** Domain 2 designed a brand-new solution, Meridian Loyalty, from nothing; Domain 3 applies related concerns — like operational excellence and security — to an existing solution, Café Sol, that's already running and was never revisited against current best practice. Same underlying concerns, genuinely different starting point
> **C.** Domain 2 only applies to Meridian Loyalty and Domain 3 only applies to Café Sol, with no conceptual relationship at all
> **D.** Domain 3 replaces everything Domain 2 covered

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since IAM Access Analyzer and GuardDuty are both IAM/security-related tools, running one makes the other redundant." Evaluate this using this module's content.

> **A.** Agree — only one of the two is ever needed
> **B.** Disagree — Access Analyzer answers what's possible given current permissions and public exposure, regardless of whether anything malicious is happening; GuardDuty answers whether something malicious is actively happening. Both matter for a complete security posture, addressing different questions
> **C.** Disagree, but only because GuardDuty cannot be used alongside IAM at all
> **D.** Agree, since Access Analyzer includes all of GuardDuty's threat-detection capability

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a Well-Architected review specifically was needed to discover that Café Sol's original design "never accounted for multi-brand realities," rather than Trusted Advisor catching this on its own.

> **A.** Trusted Advisor would have caught this eventually given enough time
> **B.** Trusted Advisor surfaces specific, automated, check-based findings — not a judgment about whether an architecture's original design assumptions still fit a changed business context; that kind of structural, design-level gap is exactly what a deliberate Well-Architected review is built to surface, not an automated check
> **C.** Multi-brand realities are outside the scope of any AWS tool
> **D.** There is no meaningful difference between what each tool can discover

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes that since Café Sol "runs well" after six months, no further review is needed. Argue against this using this module's content.

> **A.** Agree — a system that runs without incident needs no further review
> **B.** Disagree — "runs well" and "reviewed against current best practice" are different claims; six months of ordinary operation under a changed ownership structure (multi-brand, Meridian-wide guardrails) is exactly the situation likely to have accumulated operational and security gaps that a deliberate review, not just uptime, would surface
> **C.** Disagree, but only because AWS requires quarterly reviews by policy
> **D.** Agree, since continuous improvement only applies to solutions that have already failed

**20. [Scenario / Judgment] Very Hard**

> A student says: "Continuous improvement just means fixing things after they break." Evaluate this using this module's content.

> **A.** Agree — continuous improvement is purely reactive, addressing failures after they occur
> **B.** Disagree — this module's tools are largely proactive: a Well-Architected review finds design gaps before they cause an incident, Config catches drift before it becomes a problem, and Access Analyzer finds unused access before it's exploited. Continuous improvement is about surfacing gaps ahead of failure, not just responding after one
> **C.** Disagree, but only because AWS tools cannot detect problems before they occur
> **D.** Agree, since this module only covers incident response tooling

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
