# Module 3: Maintaining and Troubleshooting Logging Solutions

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Modules 1 and 2 gave Priya signal and automatic remediation for the problems she anticipated. But some questions only get answered by going back and looking: who made this change, when did this connection get rejected, how long has this log actually been sitting around costing money. This module is Domain 1's third and final task: keeping the logging layer itself trustworthy, complete, and cost-aware — closing out Domain 1.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish AWS CloudTrail's Event History from a configured trail, and know when each is actually enough
- Explain the difference between CloudTrail management events and data events
- Describe what VPC Flow Logs capture, and where they can be published
- Explain CloudWatch Logs' default retention behavior, and why it's a common cost and compliance trap
- Design a complete logging and troubleshooting strategy for a stated scenario

---

## CloudTrail: Event History vs. a Trail

Every AWS account records API activity automatically, visible in **CloudTrail Event History** — no setup required, showing account-level management events for the **past 90 days**, at no additional cost. For many quick "who did this, when" questions, Event History is genuinely enough.

Event History has real limits, though: it only covers 90 days, it doesn't deliver anywhere durable, and it only covers a single region's management events. A **trail** is a configured, ongoing export of CloudTrail events to an S3 bucket (and optionally CloudWatch Logs), and it removes all three limits — events are retained as long as the bucket keeps them, a **multi-region trail** captures activity across every AWS Region, and an **organization trail** captures activity across every account in an AWS Organization from one place.

> ⚠️ **Exam trap:** a scenario asking to investigate an API call from 90 days ago, or asking for logs retained for a compliance requirement, or asking to see activity across multiple regions or accounts, is describing something Event History cannot do — it needs an actual trail. Event History is the free, always-on 90-day view; a trail is what you configure for retention, multi-region or multi-account coverage, and durable delivery.

CloudTrail also distinguishes **management events** (control-plane operations — creating an EC2 instance, changing an IAM policy) from **data events** (data-plane operations — an S3 object being read, a Lambda function being invoked). A trail logs management events by default; data events are high-volume and cost more, so they have to be explicitly turned on for the specific resources that need that level of detail.

## VPC Flow Logs: Capturing Network Traffic

**VPC Flow Logs** capture metadata about the IP traffic going to and from network interfaces in a VPC — source and destination IP and port, protocol, whether the traffic was **ACCEPT**ed or **REJECT**ed, and byte counts — without capturing the actual packet contents. Flow logs can be enabled at the VPC, subnet, or individual network interface level, and published to CloudWatch Logs, Amazon S3, or Amazon Data Firehose depending on what the team wants to do with them afterward.

Priya uses VPC Flow Logs to troubleshoot a specific connectivity complaint from Café Sol's ops team: a request that should reach the reporting server is being silently dropped somewhere. Filtering the flow log for REJECT records on that network interface shows exactly which security group or network ACL rule is responsible — something neither CloudTrail nor CloudWatch application logs would show, since flow logs work at the network layer, not the application or API layer.

## CloudWatch Logs Retention: The Default Nobody Expects

A CloudWatch Logs log group's retention setting decides how long its log events are kept before CloudWatch automatically deletes them. The setting that surprises almost everyone: a **new log group's default retention is "Never Expire"** — logs are kept indefinitely unless someone explicitly sets a retention period.

That default quietly cuts both ways. For an application that genuinely needs long-term log retention for compliance, "Never Expire" by default might sound safe — but for a high-volume log group nobody thought to configure, indefinite retention means storage costs grow without bound, forever, until someone notices and sets an actual retention period.

> ⚠️ **Exam trap:** a scenario describing unexpectedly high CloudWatch Logs storage costs, or logs that were assumed to have "aged out" but are still present months later, is almost always describing a log group that was never given an explicit retention setting — the fix is setting a retention period (a specific number of days, from 1 day up to effectively indefinite), not assuming CloudWatch handles it automatically.

## Putting It Together: Meridian's Logging Strategy

Priya's logging setup, closing out Domain 1:

- A **multi-region, organization-wide CloudTrail trail**, delivering to a durable S3 bucket — covering every account and region Meridian operates in, well beyond Event History's 90-day, single-account view.
- **Data events enabled** specifically on the S3 buckets holding customer data, since object-level access is exactly the kind of detail a compliance review would ask for.
- **VPC Flow Logs** enabled on the VPCs behind Café Sol and Ridgeline, published to CloudWatch Logs, so a rejected-connection complaint can be diagnosed in minutes instead of guessed at.
- An explicit **retention period** set on every CloudWatch Logs log group, instead of leaving new ones on the default "Never Expire" — balancing genuine compliance needs against runaway storage cost.

## What to skip

You don't need to memorize CloudTrail's exact per-event pricing or the complete list of data event resource types — that's implementation depth beyond this exam. What matters is knowing when Event History is enough versus when a trail is required, the difference between management and data events, what VPC Flow Logs actually capture, and CloudWatch Logs' indefinite default retention.

## Key takeaways

- CloudTrail Event History is free, always-on, and covers 90 days of a single account's management events; a trail is required for longer retention, multi-region or multi-account coverage, and durable delivery to S3.
- CloudTrail logs management events by default; data events (like S3 object reads or Lambda invocations) must be explicitly enabled, since they're higher-volume and cost more.
- VPC Flow Logs capture network-layer metadata — including ACCEPT and REJECT decisions — making them the right tool for diagnosing a connection that's being silently dropped.
- A new CloudWatch Logs log group defaults to "Never Expire" retention — a common source of unexpected storage cost until someone sets an explicit retention period.
- This closes Domain 1: Module 1 built the signal, Module 2 turned it into automatic remediation, and Module 3 made sure the logging layer underneath both of them is complete, durable, and cost-aware.

## Further reading

- [AWS CloudTrail Event History](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/view-cloudtrail-events.html) — the default 90-day view.
- [Creating a Trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-a-trail.html) — multi-region and organization trails, management vs. data events.
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) — capturing and publishing network traffic metadata.
- [Change Log Data Retention in CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) — setting an explicit retention period.
