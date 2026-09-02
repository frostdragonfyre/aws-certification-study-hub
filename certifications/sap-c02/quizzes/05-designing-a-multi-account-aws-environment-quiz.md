**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 5 Knowledge Check**

Designing a Multi-Account AWS Environment · 20 questions · Practice — not graded

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

> The management account in a landing zone is intentionally kept nearly empty of actual workloads.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which foundational account exists solely to receive and store logs from every other account in the organization?
>
> **A.** The management account
> **B.** The Log Archive account
> **C.** The Sandbox account
> **D.** The Production account

**3. [Fill in the Blank] Easy**

> AWS Control Tower's ____________ ____________ automates provisioning a new account pre-configured with the landing zone's baseline.

**4. [Multiple Choice] Easy**

> What does an AWS Organizations tag policy define?
>
> **A.** Which AWS Regions an account can use
> **B.** The allowed tag keys and values for resources across accounts
> **C.** The maximum number of accounts an organization can have
> **D.** Which IAM users can assume a cross-account role

**5. [True / False] Easy**

> An organization trail must be individually enabled in each new account before it starts capturing CloudTrail events there.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What does AWS Organizations consolidated billing combine into a single bill?
>
> **A.** Only the management account's own usage
> **B.** Usage from every member account in the organization
> **C.** Only accounts in the Production OU
> **D.** Only accounts that explicitly opt in to billing consolidation

**7. [Fill in the Blank] Moderate**

> The Audit account, often paired with the Log Archive account, holds security tooling with ____________ access across the organization for review and investigation.

**8. [Multiple Choice] Moderate**

> Why does consistent tagging matter for centralized logging specifically?
>
> **A.** It doesn't — tagging and logging are unrelated
> **B.** Without consistent tags, it's difficult to tell which brand's resource generated a given log entry, even with all logs centralized in one place
> **C.** Tags replace the need for an organization trail entirely
> **D.** Tags are required before CloudTrail can be enabled at all

**9. [True / False] Moderate**

> Only the management account can disable or modify an organization trail's configuration — member accounts cannot.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What pricing benefit does consolidated billing provide beyond one invoice?
>
> **A.** It eliminates the need for AWS Backup policies
> **B.** Usage can be aggregated for volume pricing discounts and Reserved Instance or Savings Plan sharing, while still tracked separately for visibility
> **C.** It automatically grants every account administrator access to every other account
> **D.** It removes the need for organizational units

**11. [Fill in the Blank] Moderate**

> A ____________ ____________ is the governed multi-account environment an AWS Organization starts from, including its foundational accounts.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Meridian's security team wants to review activity across every brand's account without needing standing access inside each one individually. Which foundational account is built for this?
>
> **A.** The management account
> **B.** The Audit account
> **C.** A Sandbox account
> **D.** Any brand's own production account

**13. [Scenario / Judgment] Hard**

> When Ridgeline's AWS account is created, Meridian wants it to automatically inherit the correct OU placement, SCPs, guardrails, and logging setup, without manual post-creation configuration. What accomplishes this?
>
> **A.** AWS Control Tower's Account Factory
> **B.** A VPC peering connection
> **C.** An IAM Identity Center permission set
> **D.** Manually configuring the account after creation, following a checklist

**14. [Scenario / Judgment] Hard**

> Meridian's finance team wants to see AWS costs broken down by brand, even though usage across all brands is billed together under the management account. What makes this possible?
>
> **A.** Consolidated billing alone, without any tagging
> **B.** A tag policy enforcing a consistent Brand tag, combined with consolidated billing's per-account (and per-tag) visibility
> **C.** Creating a separate AWS Organization for each brand
> **D.** Cost visibility per brand is not possible under consolidated billing

**15. [Scenario / Judgment] Hard**

> One brand's team tags resources with "env: production" while another uses "Environment=prod," and automated cost reports can't reliably group them together. What addresses this?
>
> **A.** An SCP denying resource creation
> **B.** An AWS Organizations tag policy defining the allowed tag keys and values consistently across accounts
> **C.** A cross-account IAM role
> **D.** Consolidated billing alone, without any tag policy

**16. [Scenario / Judgment] Hard**

> A reviewer suggests storing each account's CloudTrail logs only within that same account, reasoning that it's simpler. What's the strongest argument against this, using this module's content?
>
> **A.** CloudTrail cannot technically run inside a workload account at all
> **B.** Storing logs only within the account that generated them means security review requires standing access inside every workload account, and a compromised account could tamper with its own audit trail — a centralized Log Archive account, populated by an organization trail, avoids both problems
> **C.** There is no real downside to this approach
> **D.** Organization trails are more expensive than per-account trails in every case

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Once Control Tower's Account Factory creates a new account, our job is done — nothing else needs to happen." Correct this using this module's content and Module 3's.
>
> **A.** They're right — Account Factory handles everything permanently with no further action needed
> **B.** Account Factory establishes the correct baseline at creation — OU placement, SCPs, guardrails, and logging — but ongoing governance (tag policy compliance, resilience assessment, security review via the Audit account) continues throughout the account's life; provisioning correctly isn't the same as staying correctly governed forever
> **C.** Account Factory only creates accounts and applies no baseline configuration at all
> **D.** Nothing about Account Factory relates to any content from Module 3

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Consolidated billing means every account can see every other account's detailed cost breakdown, so this raises a data exposure concern." Evaluate this using this module's content.
>
> **A.** Agree — consolidated billing has no access controls at all
> **B.** The concern conflates billing consolidation for the invoice and pricing benefits with unrestricted visibility; consolidated billing preserves per-account cost visibility rather than exposing every account's detail to every other account, and access to that visibility is still governed separately, like any other AWS resource
> **C.** Disagree, but only because consolidated billing is optional and Meridian shouldn't use it
> **D.** Agree, and the only fix is a separate AWS Organization per brand

**19. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Meridian keeps the management account "nearly empty of actual workloads" rather than just running Café Sol's production systems there directly, since it's already the organization's central account.
>
> **A.** AWS technically forbids running any workload in a management account
> **B.** The management account can create and manage every member account and apply organization-wide policy; compromising it would threaten the entire organization, so keeping it free of workloads limits what's exposed if it's ever compromised, and keeps its blast radius separate from any single brand's production risk
> **C.** There is no real reason — it's simply convention with no security rationale
> **D.** Workloads run faster in member accounts than in the management account for technical reasons

**20. [Scenario / Judgment] Very Hard**

> A stakeholder proposes giving every brand's team direct access to create and configure their own new AWS accounts as needed, without going through Account Factory, arguing it's faster. Argue against this using this module's and Module 3's content.
>
> **A.** Agree — speed should always be prioritized over consistency in account creation
> **B.** Disagree — an account created outside Account Factory risks missing correct OU placement, applicable SCPs and guardrails, and logging wired to the Log Archive account from day one; exactly the "governed by default, not governed by remembering to configure it correctly" principle this module and Module 3 both build toward
> **C.** Disagree, but only because AWS technically prevents creating accounts outside Account Factory
> **D.** Agree, since OU placement and SCPs can always be added perfectly correctly after the fact with no risk

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*