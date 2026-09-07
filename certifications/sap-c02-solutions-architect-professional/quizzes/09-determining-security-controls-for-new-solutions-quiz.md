**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 9 Knowledge Check**

Determining Security Controls for New Solutions · 20 questions · Practice — not graded

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

> Meridian Loyalty's security requirements were derived from an inventory of the data it actually handles, not a generic "add every security service" instinct.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which service should store Meridian Loyalty's database password, given that it needs to rotate automatically?
>
> **A.** Amazon S3
> **B.** AWS Secrets Manager
> **C.** Amazon CloudWatch
> **D.** AWS Config

**3. [Fill in the Blank] Easy**

> AWS ____________ ____________ is enabled automatically, at no additional cost, for every AWS resource, defending against common network and transport layer DDoS attacks.

**4. [Multiple Choice] Easy**

> Which service inspects application-layer traffic and blocks specific attack patterns like SQL injection and cross-site scripting?

> **A.** AWS Shield Standard
> **B.** AWS WAF
> **C.** Amazon GuardDuty
> **D.** AWS Secrets Manager

**5. [True / False] Easy**

> Meridian Loyalty's guest rewards platform stores payment card numbers directly.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why is Systems Manager Parameter Store a valid choice for Meridian Loyalty's static, non-sensitive configuration values instead of Secrets Manager?

> **A.** Parameter Store cannot store encrypted values at all
> **B.** Those values don't need automatic rotation, and Parameter Store is cheaper when rotation isn't the actual requirement
> **C.** Secrets Manager cannot be used for configuration values under any circumstances
> **D.** Parameter Store is the only service that supports KMS encryption

**7. [Fill in the Blank] Moderate**

> AWS ____________ ____________ already constrains what Meridian Loyalty's account can do, the moment the account is provisioned inside the organization — no new setup required for this workload.

**8. [Multiple Choice] Moderate**

> Which combination is the right starting point for protecting Meridian Loyalty's public-facing guest portal at launch?

> **A.** Shield Advanced alone
> **B.** Shield Standard (automatic) plus AWS WAF
> **C.** GuardDuty alone
> **D.** No additional protection is needed since Shield Standard already covers application-layer attacks

**9. [True / False] Moderate**

> Amazon GuardDuty, enabled organization-wide in Module 3, starts monitoring Meridian Loyalty's account automatically, without a separate enablement step.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does AWS Shield Advanced add beyond what Shield Standard already provides?

> **A.** The first DDoS protection of any kind for the resource
> **B.** Enhanced detection for sophisticated attacks, cost protection during an attack, and 24/7 access to the AWS DDoS Response Team
> **C.** Automatic secret rotation
> **D.** Application-layer rule-based traffic inspection

**11. [Fill in the Blank] Moderate**

> Meridian Loyalty's three concrete security requirements are encryption for guest data, secure credential storage and rotation, and protection for its ____________ ____________ portal.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A reviewer proposes enabling Shield Advanced on every Meridian Loyalty resource on day one, "just to be safe." What does this module's reasoning suggest?

> **A.** This is correct — Shield Advanced should always be enabled everywhere by default
> **B.** Shield Standard plus WAF is the right starting point; Shield Advanced's added cost is worth it if the workload later becomes a specific, high-value DDoS target — not reflexively, for every public-facing workload on day one
> **C.** Shield Advanced is free, so there's no reason not to enable it everywhere
> **D.** Shield Advanced replaces the need for WAF entirely

**13. [Scenario / Judgment] Hard**

> A new solution needs a credential that must rotate automatically on a schedule, using a built-in rotation Lambda for a supported database. Which service fits?

> **A.** Systems Manager Parameter Store
> **B.** AWS Secrets Manager
> **C.** Amazon S3 with versioning
> **D.** AWS Config

**14. [Scenario / Judgment] Hard**

> Sofía wants Meridian Loyalty's findings to appear in the same organization-wide security dashboard Module 3 already built, without setting up a second dashboard. What accomplishes this?

> **A.** A brand-new, separate Security Hub instance just for Meridian Loyalty
> **B.** AWS Security Hub, which already aggregates findings organization-wide, including from Meridian Loyalty's account automatically
> **C.** Manually exporting GuardDuty findings by hand each week
> **D.** A custom CloudWatch dashboard built from scratch

**15. [Scenario / Judgment] Hard**

> A student argues that because Meridian Loyalty handles personal guest data, it needs the same PCI-DSS-scope controls as a payment processor. What's the flaw in this reasoning?

> **A.** There is no flaw — every workload needs PCI-DSS-scope controls regardless of what it handles
> **B.** Meridian Loyalty never touches payment card data at all — card numbers stay inside each brand's existing point-of-sale systems — so PCI-DSS scope isn't the actual requirement; strong protection for personal data is
> **C.** PCI-DSS only applies to AWS-native services, so it's irrelevant regardless
> **D.** Meridian Loyalty should ignore data protection entirely since it isn't in PCI scope

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Module 3 already covered security, so this module is redundant." Correct this using this module's content and Module 3's.

> **A.** They're right — the two modules cover identical content
> **B.** Module 3 built organization-wide guardrails — SCPs, org-wide GuardDuty, aggregated Security Hub — that apply automatically to every account; this module is the per-workload decision those guardrails support, made for Meridian Loyalty specifically, and it plugs directly into Module 3's tooling rather than duplicating it
> **C.** Module 3 only applies to Café Sol and Haven & Co., never to new solutions
> **D.** This module replaces Module 3's content entirely

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Secrets Manager is strictly better than Parameter Store, so it should always be used for every stored value regardless of cost." Evaluate this using this module's content.

> **A.** Agree — Secrets Manager should always be chosen regardless of the actual requirement
> **B.** Disagree — the two solve different problems; Secrets Manager's advantage is automatic rotation, which matters for credentials like a database password, but for static configuration values that don't need rotation, Parameter Store is the cheaper, equally valid choice. Reaching for Secrets Manager by default isn't matching the tool to the requirement
> **C.** Disagree, but only because Parameter Store doesn't support encryption
> **D.** Agree, since Parameter Store cannot store any secret values at all

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why WAF and Shield Advanced are often both worth having for a well-protected internet-facing workload, rather than one instead of the other.

> **A.** They do the same job, so only one is ever needed
> **B.** They solve different problems — WAF inspects application-layer traffic for specific attack patterns like SQL injection, while Shield Advanced adds enhanced detection and response for large-scale, sophisticated DDoS attacks; a workload facing both kinds of threats benefits from both, not a choice between them
> **C.** Shield Advanced already includes all of WAF's functionality, making WAF redundant whenever Shield Advanced is enabled
> **D.** WAF is only relevant for DDoS attacks, the same as Shield Advanced

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes that Meridian Loyalty's team build its own custom threat-monitoring system instead of relying on Module 3's organization-wide GuardDuty and Security Hub. Argue against this using this module's content.

> **A.** Agree — a custom system is always preferable to organization-wide tooling
> **B.** Disagree — GuardDuty and Security Hub already apply to Meridian Loyalty's account automatically the moment it's provisioned inside the organization, at no extra setup; building a parallel system would duplicate coverage Module 3 already provides, rather than adding anything new
> **C.** Disagree, but only because AWS prohibits custom threat-monitoring systems entirely
> **D.** Agree, since GuardDuty and Security Hub don't apply to newly created accounts

**20. [Scenario / Judgment] Very Hard**

> A student says: "Since Meridian Loyalty needs strong security, every possible AWS security service should be enabled for it, regardless of what it actually handles." Evaluate this using this module's content.

> **A.** Agree — more security services always means better security, regardless of fit
> **B.** Disagree — this module's entire approach is deriving requirements from what the workload actually handles: encryption and access control for the personal data it holds, rotation where credentials actually need it, WAF and Shield sized to its actual public exposure. Adding unrelated controls (like PCI-DSS-scope tooling for data Meridian Loyalty never touches) doesn't improve security, it just adds cost and complexity without addressing an actual risk
> **C.** Disagree, but only because AWS limits how many security services one account can enable
> **D.** Agree, since this module recommends enabling every AWS security service for every workload

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
