# Module 1: Implementing Metrics, Alarms, and Filters

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Priya Anand is Meridian Retail Group's Cloud Operations Lead — the person who keeps Meridian Loyalty, Café Sol, and Ridgeline Diner Co. running now that Sofía's team has designed, improved, and migrated them. Priya's first responsibility isn't fixing problems; it's knowing about them before a customer does. This module is Domain 1, Task 1.1: building the metrics, alarms, and log-based filters that turn "something's wrong" into an actual, actionable signal.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish standard (5-minute) from detailed (1-minute) Amazon CloudWatch monitoring, and when the difference actually matters
- Configure a CloudWatch alarm with an appropriate evaluation period and missing-data treatment
- Combine multiple alarms into a single composite alarm to reduce noise
- Convert a recurring log pattern into an alarmable metric using a CloudWatch Logs metric filter
- Choose the right monitoring and alerting approach for a stated operational scenario

---

## CloudWatch Metrics: Standard vs. Detailed Monitoring

Every EC2 instance reports metrics to Amazon CloudWatch automatically, but the frequency depends on what's enabled. **Standard monitoring** reports metrics like CPUUtilization every five minutes, at no additional cost. **Detailed monitoring** reports the same metrics every minute, for an additional charge per instance.

The difference matters when the speed of detection matters. Meridian Loyalty's checkout service, freshly launched and still finding its steady-state load, benefits from detailed monitoring — a five-minute gap between data points can mean a real spike in errors goes unnoticed for most of that window. Café Sol's back-office reporting server, which runs a predictable nightly job, doesn't need that resolution — standard monitoring is enough, and enabling detailed monitoring there would just be an unnecessary cost.

Custom metrics — data an application publishes itself, like a queue depth or a business metric such as orders placed — aren't limited to five-minute or one-minute intervals; they use whatever resolution the application publishes at, down to one second for high-resolution custom metrics.

## Configuring Alarms That Actually Fire Correctly

A CloudWatch alarm watches a metric against a threshold over an **evaluation period** — for example, "CPUUtilization above 80% for 3 out of the last 3 five-minute periods." Getting the evaluation period right matters: too short, and normal, brief spikes trigger false alarms; too long, and a real problem takes too long to surface.

Alarms have three states: **OK** (the metric is within the threshold), **ALARM** (the threshold has been breached for the evaluation period), and **INSUFFICIENT_DATA** (not enough data exists yet to evaluate the alarm — often right after creation, or when a resource stops reporting entirely).

> ⚠️ **Exam trap:** what happens when a metric simply stops reporting data — not too high, not too low, just *absent* — depends entirely on the alarm's **"treat missing data as"** setting: **missing** (the default — evaluated as INSUFFICIENT_DATA, doesn't change the alarm's current state), **notBreaching** (treated as if the threshold wasn't breached, keeping the alarm OK), **breaching** (treated as if the threshold was breached, which can trigger ALARM), or **ignore** (the current state is simply maintained). A stopped or crashed instance that quietly stops reporting metrics needs "breaching" or careful evaluation-period tuning — otherwise the alarm can sit in INSUFFICIENT_DATA or OK while the instance is actually down, and nobody gets paged.

## Composite Alarms: Combining Signals

A single alarm on one metric often isn't enough context to act on — high CPU alone might be a real problem, or it might just be a scheduled batch job. **Composite alarms** combine the states of multiple existing alarms using AND/OR logic (a CloudWatch alarm rule expression), so the composite only enters ALARM when the combination of underlying conditions actually indicates a real problem.

For Meridian Loyalty's checkout service, Priya builds a composite alarm that only fires when **both** high CPU utilization **and** elevated 5xx error rates are true at once — high CPU alone during a legitimate traffic spike doesn't page anyone, but high CPU combined with real errors does. This meaningfully cuts down on alert noise compared to paging on every individual metric alarm.

## Turning Log Patterns into Alarmable Metrics

CloudWatch Alarms watch metrics — but a lot of the signal about what's actually going wrong lives in application log lines, not a pre-existing metric. A **CloudWatch Logs metric filter** solves this: it scans incoming log events in a log group for a pattern (a literal string, or a more structured pattern for JSON logs), and increments a custom metric each time that pattern matches. That metric can then have a normal CloudWatch alarm attached to it, just like any other metric.

Priya sets up a metric filter on Meridian Loyalty's application log group that matches the literal string `"ERROR"`, publishing a custom metric that counts error log lines per minute — then attaches an alarm to that metric so a spike in application-level errors pages the on-call engineer, even though "error count" was never a metric AWS provided out of the box.

> ⚠️ **Exam trap:** a metric filter and **CloudWatch Logs Insights** solve different problems, and the exam expects you to know which. A metric filter is a standing, continuous rule — every matching log event increments a metric, in real time, and that metric can trigger an alarm. Logs Insights is an ad hoc, on-demand query language for searching and analyzing logs that already exist — great for investigating *why* an alarm fired after the fact, but it doesn't continuously watch incoming logs or trigger alarms on its own. If a scenario needs an alert the moment a pattern appears, that's a metric filter with an alarm; if a scenario needs to explore what already happened, that's Logs Insights.

## Putting It Together: Monitoring Meridian Loyalty's Checkout Service

Priya's monitoring setup for the checkout service:

- **Detailed (1-minute) monitoring** on the EC2 instances behind the checkout service, since fast detection matters for a customer-facing, revenue-generating path.
- A CPU utilization alarm with **"treat missing data as breaching"**, so an instance that silently stops reporting is treated as a real problem, not silence.
- A **composite alarm** requiring both high CPU and elevated 5xx errors before paging on-call, cutting down false pages from legitimate traffic spikes.
- A **CloudWatch Logs metric filter** on the application log group matching `"ERROR"`, with its own alarm — catching application-level failures that never show up as an infrastructure metric at all.

## What to skip

You don't need to memorize CloudWatch's full pricing table for detailed monitoring or every composite-alarm rule-expression operator — that's implementation depth beyond this exam. What matters is knowing when detailed monitoring is worth the cost, how missing-data treatment changes alarm behavior, why composite alarms reduce noise, and the difference between a metric filter (continuous, alarmable) and Logs Insights (ad hoc querying).

## Key takeaways

- Detailed (1-minute) monitoring costs more than standard (5-minute) monitoring and is worth it specifically when fast detection matters, not universally.
- An alarm's "treat missing data as" setting decides what happens when a metric stops reporting entirely — getting it wrong can mean a downed resource never pages anyone.
- Composite alarms combine multiple underlying alarms with AND/OR logic, firing only when the actual combination of conditions indicates a real problem.
- A CloudWatch Logs metric filter continuously turns a matching log pattern into an alarmable metric; CloudWatch Logs Insights is for ad hoc querying of logs that already exist, not continuous alerting.
- This is Domain 1's first task — building the raw signal (metrics, alarms, filters) that Module 2's remediation and Module 3's logging both depend on.

## Further reading

- [Amazon CloudWatch User Guide: Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) — alarm states, evaluation periods, missing-data treatment.
- [Composite Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Create_Composite_Alarm.html) — combining alarms with AND/OR logic.
- [CloudWatch Logs Metric Filters](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/MonitoringLogData.html) — turning log patterns into metrics.
- [CloudWatch Logs Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) — ad hoc log querying.
