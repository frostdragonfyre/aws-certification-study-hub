<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](05-designing-a-multi-account-aws-environment.md) · [Next module](07-designing-a-deployment-strategy.md) · [Quiz](../quizzes/06-cost-optimization-and-visibility-strategies-quiz.md) · [Slides](../lectures/06-cost-optimization-and-visibility-strategies.pptx)
<!-- /hub-navigation -->

# Module 6: Cost Optimization and Visibility Strategies

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 5 gave Meridian one consolidated bill and a `Brand` tag on every resource — necessary, but still just raw ingredients. A single invoice and consistent tags don't, by themselves, tell Sofía whether Café Sol's spend this month is normal or alarming, whether Haven & Co. is running EC2 instances sized for traffic they no longer get, or whether an entire brand's cost trajectory is quietly heading somewhere finance needs to know about before the bill arrives. This module is about turning consolidated, tagged billing data into something Meridian can actually act on — and closes out Domain 1.

## Learning objectives

By the end of this module, you should be able to:

- Explain what AWS Cost Explorer is used for, and how it differs from a Cost and Usage Report
- Describe what an AWS Cost and Usage Report (CUR) provides that Cost Explorer doesn't
- Explain how AWS Budgets supports proactive, threshold-based cost control, including budget actions
- Explain how AWS Cost Anomaly Detection differs from a budget threshold
- Recommend the right cost visibility or optimization tool for a stated organizational scenario

---

## AWS Cost Explorer: Visualizing and Analyzing Spend

**AWS Cost Explorer** is the primary tool for visually exploring AWS cost and usage data — filtering and grouping by account, service, Region, or (critically, given Module 5's tag policy) by tag, like Meridian's `Brand` tag. It supports both historical analysis ("how has Haven & Co.'s spend trended over the last six months?") and basic forecasting of near-term future costs based on historical patterns.

Cost Explorer is built for interactive, exploratory analysis — a person asking questions and drilling into the answers through a console interface. It's the right tool when Sofía or Meridian's finance team wants to understand a trend or investigate a specific question, but it's not built for large-scale, fully custom data processing outside AWS's own interface.

## AWS Cost and Usage Report: The Complete, Granular Export

When Cost Explorer's built-in views aren't enough — when Meridian's finance team wants to build fully custom reports, feed cost data into their own business intelligence tooling, or do analysis at a level of granularity Cost Explorer's interface doesn't expose — the **AWS Cost and Usage Report (CUR)** is the answer. CUR delivers the most comprehensive, granular billing dataset AWS provides, as files (commonly delivered to an S3 bucket, often queried afterward with a tool like Amazon Athena), covering every line item of usage and cost across the organization.

The relationship between the two is complementary, not competing: Cost Explorer is for interactive exploration through AWS's own interface; CUR is the raw data underneath, for when an organization needs to build something more custom on top of it — a finance team's own dashboards, chargeback reports allocating cost back to each brand, or integration with external BI tools.

> ⚠️ **Exam trap:** a scenario describing "we need to build custom cost dashboards outside of AWS" or "we need the most granular line-item billing data available" is pointing at CUR, not Cost Explorer. A scenario describing "an analyst wants to explore and visualize trends interactively" is pointing at Cost Explorer, not requiring a raw CUR export.

## AWS Budgets: Proactive, Threshold-Based Control

Cost Explorer and CUR are both fundamentally look-backward-or-look-at-current-state tools — even Cost Explorer's forecasting is a projection, not an alert. **AWS Budgets** flips this around: you define a budget — a cost or usage threshold, scoped to an account, an OU, a specific tag value, or the whole organization — and get notified proactively when actual or forecasted spend crosses it, rather than discovering the overage after the bill arrives.

Budgets can go further than notification alone: **budget actions** let a budget trigger an automated response when a threshold is breached — for example, applying an SCP that restricts further resource creation in a Sandbox account that's blown through its monthly budget, without requiring someone to manually intervene the moment the alert fires.

For Meridian, this means each brand's OU can have its own budget, scoped with the `Brand` tag from Module 5, alerting the right team — not just Meridian's central finance team — the moment that specific brand's spend trajectory looks like it's heading somewhere unplanned.

## AWS Cost Anomaly Detection: Catching Unusual Spend Patterns

A fixed budget threshold catches spend that crosses a known line — but it doesn't catch a sudden, unusual spike that's still well under the monthly budget, or a gradual pattern that doesn't look like normal usage even though no single threshold has been crossed. **AWS Cost Anomaly Detection** uses machine learning to learn an account's or service's normal spending pattern, and alerts when actual spend deviates from that learned pattern in a way that looks anomalous — regardless of whether any fixed threshold was ever crossed.

This matters for a concrete Meridian scenario: if a misconfigured resource in Café Sol's account suddenly starts costing meaningfully more per day than its historical pattern, but the total is still comfortably under Café Sol's monthly budget, a fixed budget threshold wouldn't catch it — Cost Anomaly Detection would, because it's evaluating the *pattern*, not just a static number.

> ⚠️ **Exam trap:** "alert us if spend crosses this specific dollar amount" is AWS Budgets. "Alert us if spend looks unusual compared to normal patterns, even if it hasn't crossed a set number" is Cost Anomaly Detection. The two are complementary, not redundant — a scenario can reasonably call for both.

## Putting It Together: Meridian's Cost Optimization and Visibility Strategy

Sofía's cost strategy for Meridian, closing out Domain 1:

- **AWS Cost Explorer** available to Meridian's finance team and each brand's engineering leads, filtered by the `Brand` tag from Module 5, for interactive exploration and near-term forecasting.
- **AWS Cost and Usage Reports** delivered to a central S3 bucket (in the Log Archive account's general pattern of centralized, restricted storage), feeding Meridian's own finance BI tooling for custom chargeback reporting per brand.
- **AWS Budgets**, one per brand's OU, scoped with the `Brand` tag, with budget actions configured on the Sandbox OU specifically to automatically restrict further spend if an experimentation account blows through its threshold.
- **AWS Cost Anomaly Detection** running across the organization, catching unusual spend patterns in any brand's account before they accumulate into a budget-threshold-crossing amount that a fixed alert would eventually catch anyway, but later.

## What to skip

You don't need to memorize CUR's exact file schema or write Cost Explorer API calls from scratch — that's implementation depth beyond this exam. What matters is knowing when Cost Explorer's interactive interface is the right tool versus when CUR's raw export is required, how Budgets' threshold-based proactive alerting (and budget actions) works, and how Cost Anomaly Detection's pattern-based approach differs from a fixed threshold.

## Key takeaways

- AWS Cost Explorer is for interactive visualization, exploration, and near-term forecasting of cost and usage data, filterable by account, service, Region, and tag.
- AWS Cost and Usage Reports provide the most granular, complete billing dataset AWS offers, intended for custom reporting and BI tooling beyond what Cost Explorer's interface exposes.
- AWS Budgets provides proactive, threshold-based alerting — and, through budget actions, automated responses — scoped to an account, OU, tag, or the whole organization.
- AWS Cost Anomaly Detection uses machine learning to catch unusual spend patterns that deviate from historical norms, independent of whether any fixed threshold was crossed.
- Meridian's strategy combines all four: Cost Explorer for exploration, CUR for custom reporting, Budgets for proactive per-brand thresholds (with budget actions for Sandbox), and Cost Anomaly Detection for pattern-based catches a fixed threshold would miss or catch too late.

## Further reading

- [AWS Cost Explorer User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html) — interactive cost and usage analysis.
- [AWS Cost and Usage Report User Guide](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) — the most granular billing data export AWS provides.
- [AWS Budgets User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-managing-costs.html) — thresholds, alerts, and budget actions.
- [AWS Cost Anomaly Detection User Guide](https://docs.aws.amazon.com/cost-management/latest/userguide/manage-ad.html) — machine-learning-based spend pattern anomaly alerting.
