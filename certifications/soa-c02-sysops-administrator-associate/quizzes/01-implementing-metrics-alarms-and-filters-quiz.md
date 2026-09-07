**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 1 Knowledge Check**

Implementing Metrics, Alarms, and Filters · 20 questions · Practice — not graded

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

> Standard CloudWatch monitoring for EC2 reports metrics every one minute.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which CloudWatch alarm state means there isn't yet enough data to evaluate the alarm?

> **A.** OK
> **B.** ALARM
> **C.** INSUFFICIENT_DATA
> **D.** PENDING

**3. [Fill in the Blank] Easy**

> A CloudWatch Logs ____________ ____________ scans incoming log events for a pattern and increments a custom metric each time it matches.

**4. [Multiple Choice] Easy**

> What does a composite alarm combine?

> **A.** Multiple AWS accounts
> **B.** The states of multiple existing alarms, using AND/OR logic
> **C.** Multiple CloudWatch dashboards
> **D.** Multiple log groups into one

**5. [True / False] Easy**

> CloudWatch Logs Insights continuously watches incoming logs and can trigger an alarm the moment a pattern appears.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does Priya enable detailed (1-minute) monitoring on Meridian Loyalty's checkout service instances specifically, rather than everywhere by default?

> **A.** Detailed monitoring is free, so there's no reason not to enable it everywhere
> **B.** Fast detection matters for a customer-facing, revenue-generating path, and detailed monitoring costs more, so it's applied where the faster detection is actually worth it
> **C.** Standard monitoring doesn't work for EC2 instances at all
> **D.** Detailed monitoring is required for any instance running a web server

**7. [Fill in the Blank] Moderate**

> An alarm's "treat missing data as" setting called ____________ treats a gap in reporting as if the threshold were breached, which can trigger ALARM.

**8. [Multiple Choice] Moderate**

> Why does Priya's composite alarm require both high CPU utilization AND elevated 5xx errors before paging on-call?

> **A.** Composite alarms can only use AND logic, never OR
> **B.** High CPU alone can just be a legitimate traffic spike; combining it with real errors avoids paging on-call for a spike that isn't actually a problem
> **C.** CloudWatch requires at least two conditions for every alarm
> **D.** 5xx errors alone are never worth paging on-call for

**9. [True / False] Moderate**

> A metric filter that matches the literal string "ERROR" in a log group can have a normal CloudWatch alarm attached to the metric it produces.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> An EC2 instance crashes and stops reporting CloudWatch metrics entirely. With the alarm's missing-data treatment set to "missing" (the default), what happens?

> **A.** The alarm immediately enters ALARM state
> **B.** The alarm is evaluated as INSUFFICIENT_DATA, which doesn't change the alarm's current state
> **C.** CloudWatch automatically restarts the instance
> **D.** The alarm is deleted automatically

**11. [Fill in the Blank] Moderate**

> Custom metrics an application publishes itself, like queue depth or orders placed, can use resolutions as fine as one second, known as ____________-resolution custom metrics.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Café Sol's back-office reporting server runs a predictable nightly batch job and nothing else. Should Priya enable detailed monitoring on it?

> **A.** Yes, detailed monitoring should always be enabled on every resource
> **B.** No — its load is predictable and fast detection isn't critical, so standard monitoring is sufficient and detailed monitoring would just add unnecessary cost
> **C.** No, because detailed monitoring is technically incompatible with batch jobs
> **D.** Yes, because standard monitoring cannot detect batch job failures under any circumstances

**13. [Scenario / Judgment] Hard**

> A reviewer sets an alarm's missing-data treatment to "notBreaching" for an instance that's critical to catch immediately if it goes down. What's the risk?

> **A.** There is no risk — notBreaching is always the safest setting
> **B.** If the instance crashes and stops reporting, the alarm is treated as if the threshold wasn't breached, keeping it OK — so a genuinely down instance may never trigger a page
> **C.** notBreaching causes the alarm to fire immediately on any data gap
> **D.** notBreaching is only a valid setting for composite alarms, not standard ones

**14. [Scenario / Judgment] Hard**

> An engineer wants to know exactly why an alarm fired three hours ago, searching through the application's log lines from that time window. Which tool fits?

> **A.** A CloudWatch Logs metric filter, since it's built for retroactive investigation
> **B.** CloudWatch Logs Insights, since it's an ad hoc query tool for exploring logs that already exist
> **C.** A composite alarm, since it stores historical log data
> **D.** Detailed monitoring, since it retains logs for longer

**15. [Scenario / Judgment] Hard**

> Priya wants an alert the instant a specific error pattern appears in the application logs going forward, not just the ability to search for it after the fact. What should she set up?

> **A.** A CloudWatch Logs Insights saved query, since queries run continuously by default
> **B.** A CloudWatch Logs metric filter matching that pattern, with a CloudWatch alarm attached to the resulting metric
> **C.** Detailed monitoring, since it automatically alerts on log content
> **D.** A composite alarm with no underlying alarms configured

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Standard monitoring, detailed monitoring, and custom metrics are really just three names for the same thing." Correct this using this module's content.

> **A.** They're right — all three report at the same fixed interval
> **B.** They're different: standard monitoring is EC2's free 5-minute reporting, detailed monitoring is EC2's paid 1-minute reporting, and custom metrics are data an application publishes itself at whatever resolution it chooses, down to one second — three genuinely different mechanisms, not one renamed three times
> **C.** Custom metrics replace the need for both standard and detailed monitoring
> **D.** Detailed monitoring is only available for custom metrics, never for EC2

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since composite alarms reduce noise, every alarm in the account should be folded into one giant composite alarm." Evaluate this using this module's content.

> **A.** Agree — a single giant composite alarm is always the correct design
> **B.** Disagree — composite alarms are useful for combining conditions that together indicate one real problem, like CPU and errors on the same service; folding unrelated alarms into one composite would obscure which specific condition is actually wrong, the opposite of the noise reduction composite alarms are meant to provide
> **C.** Disagree, but only because CloudWatch technically limits accounts to one composite alarm total
> **D.** Agree, since individual alarms serve no purpose once a composite alarm exists

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a metric filter matching "ERROR" in Meridian Loyalty's application logs can catch a problem that no built-in EC2 or ELB metric would ever surface.

> **A.** Built-in metrics already cover every possible application-level failure, so this scenario can't happen
> **B.** Application-level errors — like a caught exception that doesn't crash the process or trigger an HTTP error code — may never appear in infrastructure metrics like CPU or request count at all; a metric filter turns the actual log line recording that error into a metric that can be alarmed on, which infrastructure metrics alone can't provide
> **C.** Metric filters only work on infrastructure metrics, not log content
> **D.** ELB metrics automatically include every application log line

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes setting every alarm's missing-data treatment to "ignore" across the board, arguing "it's simpler to have one consistent setting everywhere." Argue against this using this module's content.

> **A.** Agree — one consistent setting is always safer than tuning each alarm individually
> **B.** Disagree — the right missing-data treatment depends on what a data gap actually means for that specific resource; "ignore" simply maintains whatever state the alarm was already in, which can leave a genuinely down critical resource stuck in a stale OK state instead of surfacing the problem, exactly what happened with "notBreaching" in an earlier scenario
> **C.** Disagree, but only because "ignore" is not a real CloudWatch setting
> **D.** Agree, since missing data never actually indicates a real problem

**20. [Scenario / Judgment] Very Hard**

> A student says: "Metrics, alarms, and log-based filters are three separate tools that don't really connect to each other." Evaluate this using this module's content.

> **A.** Agree — each tool operates in complete isolation from the others
> **B.** Disagree — a metric filter turns a log pattern into a metric, that metric can carry a normal CloudWatch alarm just like any built-in metric, and multiple such alarms can combine into a composite alarm; the three form one connected pipeline from raw signal to actionable alert, not three unrelated tools
> **C.** Disagree, but only because alarms cannot be attached to metrics produced by filters
> **D.** Agree, since composite alarms cannot include alarms based on metric filters

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*