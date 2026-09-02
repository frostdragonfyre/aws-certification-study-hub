**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 6 Knowledge Check**

Cost Optimization and Visibility Strategies · 20 questions · Practice — not graded

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

> AWS Cost Explorer supports both historical cost analysis and basic near-term forecasting.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service provides the most comprehensive, granular billing data export, typically delivered to an S3 bucket?
>
> **A.** AWS Cost Explorer
> **B.** AWS Cost and Usage Report (CUR)
> **C.** AWS Budgets
> **D.** AWS Cost Anomaly Detection

**3. [Fill in the Blank] Easy**

> AWS ____________ lets you define a cost or usage threshold and get notified proactively when actual or forecasted spend crosses it.

**4. [Multiple Choice] Easy**

> What does a budget action do?
>
> **A.** Nothing beyond sending a notification
> **B.** Triggers an automated response, like applying an SCP, when a budget threshold is breached
> **C.** Automatically lowers AWS list prices
> **D.** Replaces the need for consolidated billing

**5. [True / False] Easy**

> AWS Cost Anomaly Detection only alerts when a fixed dollar threshold has been crossed.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which tool is best suited for interactive, exploratory analysis through AWS's own console interface?
>
> **A.** AWS Cost and Usage Report
> **B.** AWS Cost Explorer
> **C.** A raw S3 export with no interface
> **D.** AWS Config

**7. [Fill in the Blank] Moderate**

> AWS Cost Anomaly Detection uses ____________ ____________ to learn an account's or service's normal spending pattern.

**8. [Multiple Choice] Moderate**

> A finance team wants to build fully custom cost dashboards outside of AWS, using their own BI tooling. What should feed that tooling?
>
> **A.** AWS Cost Explorer's console view alone
> **B.** AWS Cost and Usage Report (CUR) data
> **C.** AWS Budgets notifications
> **D.** AWS Cost Anomaly Detection alerts alone

**9. [True / False] Moderate**

> A budget can be scoped to an account, an OU, a specific tag value, or the whole organization.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What is the key difference between AWS Budgets and AWS Cost Anomaly Detection?
>
> **A.** They are functionally identical
> **B.** Budgets alert on a fixed threshold being crossed; Cost Anomaly Detection alerts on spend that deviates from a learned normal pattern, regardless of any fixed threshold
> **C.** Budgets use machine learning; Cost Anomaly Detection uses fixed thresholds
> **D.** Only one of the two can be used at a time

**11. [Fill in the Blank] Moderate**

> AWS Cost Explorer can filter and group cost data by account, service, Region, or ____________, such as Meridian's Brand tag from Module 5.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A misconfigured resource in Café Sol's account starts costing noticeably more per day than its historical pattern, but the total is still comfortably under Café Sol's monthly budget. Which tool would actually catch this?
>
> **A.** AWS Budgets alone
> **B.** AWS Cost Anomaly Detection, since it evaluates the spending pattern, not just a static threshold
> **C.** AWS Cost Explorer's forecasting feature alone
> **D.** Nothing would catch this until the monthly bill arrives

**13. [Scenario / Judgment] Hard**

> Meridian wants a Sandbox account that blows through its monthly budget to automatically have further resource creation restricted, without requiring someone to manually intervene. What accomplishes this?
>
> **A.** A budget action applying an SCP when the threshold is breached
> **B.** AWS Cost Explorer's forecasting feature
> **C.** A Cost and Usage Report
> **D.** Cost Anomaly Detection alone, with no budget involved

**14. [Scenario / Judgment] Hard**

> An analyst wants to explore how Haven & Co.'s spend has trended over the last six months and get a rough forecast for next quarter, using AWS's own console. What fits best?
>
> **A.** AWS Cost and Usage Report, downloaded and processed manually
> **B.** AWS Cost Explorer
> **C.** AWS Budgets
> **D.** AWS Cost Anomaly Detection

**15. [Scenario / Judgment] Hard**

> Meridian's finance team needs to build a chargeback report allocating cost back to each brand at a level of line-item detail Cost Explorer's interface doesn't expose. What should they use?
>
> **A.** AWS Cost Explorer alone
> **B.** The AWS Cost and Usage Report, likely queried afterward with a tool like Amazon Athena
> **C.** AWS Budgets notifications
> **D.** Cost Anomaly Detection alerts

**16. [Scenario / Judgment] Hard**

> A reviewer proposes relying only on AWS Budgets, arguing that any cost problem worth catching will eventually cross a defined threshold. What's the flaw in this reasoning, per this module?
>
> **A.** There is no flaw — Budgets alone is always sufficient
> **B.** A gradual or unusual spend pattern can look anomalous well before crossing any fixed threshold, and by the time a threshold is crossed, the issue may have already accumulated unnecessary cost — Cost Anomaly Detection catches this earlier
> **C.** AWS Budgets cannot be scoped to a tag, only to an account
> **D.** Budgets and Cost Anomaly Detection cannot both be used in the same organization

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Cost Explorer and the Cost and Usage Report do the same thing, so we only need one." Correct this using this module's content.
>
> **A.** They're right — the two are fully redundant
> **B.** Cost Explorer is for interactive, exploratory analysis through AWS's own console interface; CUR is the complete, granular raw data export intended for custom reporting and external BI tooling. They serve complementary purposes, not the same one
> **C.** CUR is only for AWS internal use and isn't available to customers
> **D.** Cost Explorer replaces the need for any billing data export entirely

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since Meridian already has consolidated billing and tag policies from Module 5, cost visibility is already solved — this module's tools are redundant." Evaluate this using this module's content.
>
> **A.** Agree — consolidated billing and tagging alone provide everything needed
> **B.** Disagree — consolidated billing and tagging make cost data available and attributable, but don't provide exploration (Cost Explorer), granular custom reporting (CUR), proactive threshold alerting (Budgets), or pattern-based anomaly detection; this module turns that raw, tagged billing data into something actually actionable
> **C.** Disagree, but only because tag policies don't actually work as described in Module 5
> **D.** Agree, since Cost Explorer and CUR duplicate what consolidated billing already shows

**19. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Meridian scopes a separate AWS Budget to each brand's OU using the Brand tag, rather than relying on a single organization-wide budget alone.
>
> **A.** A single org-wide budget is technically impossible to create
> **B.** A single org-wide budget could mask one brand's overspend if another brand is under budget at the same time, and wouldn't notify the specific team responsible; per-brand budgets scoped by tag alert the right team directly, closer to the source of the actual spend
> **C.** Per-brand budgets are required by AWS Organizations for every account
> **D.** There is no difference between the two approaches

**20. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping AWS Budgets entirely and relying only on Cost Anomaly Detection, arguing pattern-based detection is strictly better than fixed thresholds. Argue against this using this module's content.
>
> **A.** Agree — fixed thresholds serve no purpose once anomaly detection is in place
> **B.** Disagree — a budget threshold enforces a specific, known business constraint (like a Sandbox account's approved monthly spend limit) and can trigger budget actions automatically; anomaly detection catches unusual patterns but doesn't know or enforce a specific dollar limit an organization has actually decided on. The two serve different, complementary purposes
> **C.** Disagree, but only because Cost Anomaly Detection is not a real AWS service
> **D.** Agree, since budget actions can be triggered by Cost Anomaly Detection directly with no budget required

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*