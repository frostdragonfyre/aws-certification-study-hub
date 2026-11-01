[Course index](../README.md) · [Read the paired lesson](../modules/03-maintaining-and-troubleshooting-logging-solutions.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 3 Knowledge Check**

Maintaining and Troubleshooting Logging Solutions · 20 questions · Practice — not graded

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

> CloudTrail Event History requires creating a trail before it shows any activity.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> How far back does CloudTrail Event History show account activity, by default?

> **A.** 7 days
> **B.** 30 days
> **C.** 90 days
> **D.** Indefinitely

**3. [Fill in the Blank] Easy**

> A new CloudWatch Logs log group's default retention setting is ____________ ____________ — logs are kept indefinitely unless someone sets a retention period.

**4. [Multiple Choice] Easy**

> Which VPC Flow Logs value indicates traffic that was blocked by a security group or network ACL?

> **A.** ACCEPT
> **B.** REJECT
> **C.** DENY
> **D.** DROP

**5. [True / False] Easy**

> CloudTrail data events are logged by default on every trail, with no additional configuration.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What does a multi-region CloudTrail trail provide that Event History alone does not?

> **A.** Faster API response times
> **B.** Coverage of activity across every AWS Region, with durable delivery to S3, instead of a single account's 90-day view
> **C.** Automatic encryption of EC2 instances
> **D.** Free data event logging with no configuration

**7. [Fill in the Blank] Moderate**

> CloudTrail ____________ events are control-plane operations, like creating an EC2 instance or changing an IAM policy, and are logged by a trail by default.

**8. [Multiple Choice] Moderate**

> Priya needs to see which security group rule is silently dropping traffic to Café Sol's reporting server. Which tool fits?

> **A.** CloudTrail Event History, since it logs all network traffic
> **B.** VPC Flow Logs, filtered for REJECT records on the relevant network interface
> **C.** CloudWatch Logs metric filters, since they capture network-layer data
> **D.** AWS Config, since it tracks real-time traffic flow

**9. [True / False] Moderate**

> VPC Flow Logs capture the actual contents (payload) of network packets, not just metadata about them.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Why might a team be surprised by unexpectedly high CloudWatch Logs storage costs months after a log group was created?

> **A.** CloudWatch Logs always deletes data after 30 days regardless of settings
> **B.** The log group was likely left on its default "Never Expire" retention setting, so logs have been accumulating indefinitely
> **C.** CloudWatch Logs charges a flat fee regardless of log volume
> **D.** Log groups cannot be assigned a retention period at all

**11. [Fill in the Blank] Moderate**

> CloudTrail ____________ events are data-plane operations, like an S3 object being read or a Lambda function being invoked, and must be explicitly enabled.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> An auditor asks Priya to show every IAM policy change made across all of Meridian's AWS accounts over the past year. What's needed?

> **A.** CloudTrail Event History, since it retains data indefinitely
> **B.** An organization trail delivering to a durable S3 bucket, since Event History only covers 90 days and a single account
> **C.** VPC Flow Logs, since they capture IAM activity
> **D.** Nothing — CloudTrail cannot show activity across multiple accounts

**13. [Scenario / Judgment] Hard**

> A compliance review asks for a record of every read access to objects in a specific S3 bucket holding customer data. What does Priya need to enable?

> **A.** Nothing — management events already include S3 object-level access by default
> **B.** Data events on that specific S3 bucket, since object-level access is a data-plane operation not covered by default management event logging
> **C.** VPC Flow Logs, since they capture S3 object reads
> **D.** CloudWatch Logs retention, since that determines what CloudTrail captures

**14. [Scenario / Judgment] Hard**

> A team assumed their CloudWatch Logs log groups would automatically stop accumulating data after a reasonable period, and discovers a year of unused, expensive log data instead. What actually happened?

> **A.** CloudWatch Logs silently ignored their retention settings
> **B.** The log groups were left on the default "Never Expire" retention setting, since CloudWatch Logs doesn't apply a default expiration automatically — retention has to be set explicitly
> **C.** CloudWatch Logs only supports a single global retention setting for an entire account
> **D.** This behavior is impossible; CloudWatch Logs always expires data after 90 days

**15. [Scenario / Judgment] Hard**

> A student argues that VPC Flow Logs and CloudTrail cover the same kind of activity, just at different layers. What's the more accurate distinction?

> **A.** They're identical — both capture the same events
> **B.** VPC Flow Logs capture network-layer traffic metadata (accepted or rejected connections); CloudTrail captures API-layer activity (who called which AWS API) — genuinely different layers, not redundant views of the same thing
> **C.** VPC Flow Logs only work within CloudTrail trails
> **D.** CloudTrail captures network traffic, while VPC Flow Logs capture API calls

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Domain 1 was really just three modules about CloudWatch." Correct this using this module's content and the earlier modules'.

> **A.** They're right — every Domain 1 module centers entirely on CloudWatch
> **B.** Module 1 built CloudWatch metrics, alarms, and log-based filters; Module 2 connected those alarms to EC2 actions, Auto Scaling, and Systems Manager Automation; Module 3 covers CloudTrail and VPC Flow Logs alongside CloudWatch Logs retention — three related but genuinely different tools, not one tool repeated three times
> **C.** Module 3 has nothing to do with the earlier two modules
> **D.** CloudTrail and VPC Flow Logs are simply other names for CloudWatch

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes relying on CloudTrail Event History alone for all of Meridian's audit and compliance needs, arguing "it's free and already on." Evaluate this using this module's content.

> **A.** Agree — Event History meets every audit and compliance need with no configuration required
> **B.** Disagree — Event History only covers 90 days of a single account's management events with no durable delivery; a compliance need for longer retention, multi-account coverage, or data event detail requires an actual configured trail
> **C.** Disagree, but only because Event History is a paid feature
> **D.** Agree, since trails cannot capture anything Event History doesn't already show

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why enabling data events on every S3 bucket and Lambda function by default would be a poor default for CloudTrail to ship with.

> **A.** Data events are free, so there's no reason not to enable them everywhere
> **B.** Data events are high-volume, data-plane operations — logging every S3 object read or Lambda invocation account-wide by default would generate far more log volume and cost than most accounts need, which is why they require deliberate, per-resource opt-in instead
> **C.** Data events cannot technically be enabled for more than one resource at a time
> **D.** Management events and data events are actually the same thing under two names

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes setting every CloudWatch Logs log group to the longest possible retention period "just to be safe," without considering what each log group actually contains. Argue against this using this module's content.

> **A.** Agree — maximum retention everywhere is always the correct choice with no tradeoff
> **B.** Disagree — retention should match what a log group actually needs; a high-volume log group with no genuine long-term value accumulates unnecessary storage cost under maximum retention, the same failure mode as leaving it on the "Never Expire" default — the fix is a deliberate retention period per log group, not one blanket setting
> **C.** Disagree, but only because CloudWatch Logs technically caps retention at 90 days
> **D.** Agree, since storage cost is identical regardless of retention period

**20. [Scenario / Judgment] Very Hard**

> A student says: "Now that Domain 1 is done, monitoring, remediation, and logging are three separate concerns that don't really depend on each other." Evaluate this using this module's content and the earlier modules'.

> **A.** Agree — each module's tools operate in complete isolation
> **B.** Disagree — Module 1's metric filters depend on the log groups Module 3 covers, Module 2's Systems Manager Automation remediation can be triggered by exactly the kind of alarm Module 1 built, and Module 3's CloudTrail and VPC Flow Logs are often what confirms a Module 2 remediation actually worked — the three tasks form one connected operational picture, not three unrelated ones
> **C.** Disagree, but only because Module 2 and Module 3 cover identical content
> **D.** Agree, since CloudWatch, CloudTrail, and VPC Flow Logs cannot be used together

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
