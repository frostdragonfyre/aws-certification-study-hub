"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/01-implementing-metrics-alarms-and-filters.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-01-deck.py

Paired with instructor-private/01-implementing-metrics-alarms-and-filters-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "01-implementing-metrics-alarms-and-filters.pptx")

d = Deck(1, "Implementing Metrics, Alarms, and Filters",
          "Sofía's team designed, improved, and migrated Meridian's systems. Now Priya's team keeps them running.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 1 · Lecture", ["Implementing Metrics,", "Alarms, and Filters"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 1", "Question of the Day", "Before we start",
    [("An EC2 instance behind Meridian Loyalty's checkout service crashes and stops reporting metrics", "Does the alarm know something's wrong — or does it just go quiet?"),
     ("Recap: SAP-C02 designed, improved, and migrated Meridian's systems", "Sofía's team built it — now Priya's team keeps it running"),
     ("Tonight's task", "Domain 1, Task 1.1 — the first module of the SOA-C02 track: metrics, alarms, and filters")])

# 3 — Objectives
d.numbered_list_slide("Module 1", "Objectives", "Five things by the end of tonight", [
    ("Distinguish standard from detailed CloudWatch monitoring", "and when the difference actually matters"),
    ("Configure an alarm with the right evaluation period and missing-data treatment", "so a real problem doesn't go silent"),
    ("Combine multiple alarms into a composite alarm", "to cut down on false pages"),
    ("Convert a recurring log pattern into an alarmable metric", "using a CloudWatch Logs metric filter"),
    ("Choose the right monitoring approach for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("From Building It to Keeping It Running",
    "Priya Anand is Meridian's Cloud Operations Lead — her job starts where Sofía's design work ends", "Module 1")

# 5 — Section intro: standard vs detailed monitoring
d.content_slide("Same Metrics, Different Resolution",
    "Standard monitoring reports every five minutes. Detailed monitoring reports every one.", "Module 1", dark=True)

# 6 — Applied: standard vs detailed
d.table_slide("Module 1", "Standard vs. Detailed Monitoring, Applied", "Faster detection costs more — apply it where speed matters",
    ["Type", "Resolution"],
    [["Standard monitoring (EC2)", "Every 5 minutes, no additional cost"],
     ["Detailed monitoring (EC2)", "Every 1 minute, additional cost per instance"],
     ["Custom metrics (application-published)", "Whatever resolution is published, down to 1 second"]],
    col_widths=[5.6, 7.0],
    note="Applied where it's worth it, like Meridian Loyalty's checkout service — not everywhere by default.")

# 7 — Exam trap: missing data treatment
d.quad_box_slide("COMMON EXAM TRAP", "What Happens When Data Simply Stops", "Missing data isn't a normal reading — the alarm's setting decides what it means",
    [("missing (the default)", "evaluated as INSUFFICIENT_DATA, doesn't change the alarm's current state."),
     ("notBreaching", "treated as if the threshold wasn't breached — the alarm stays OK."),
     ("breaching", "treated as if the threshold was breached — can trigger ALARM."),
     ("ignore", "the alarm's current state is simply maintained.")],
    note="One line: a crashed resource that stops reporting needs deliberate missing-data treatment, or nobody gets paged.")

# 8 — Applied: missing data treatment
d.table_slide("Module 1", "Missing Data Treatment, Applied", "Same gap, four different outcomes for a crashed instance",
    ["Setting", "What a crashed, silent instance does to the alarm"],
    [["missing (default)", "INSUFFICIENT_DATA — alarm's current state unchanged"],
     ["breaching", "Treated as breached — can trigger ALARM, the safer choice for critical resources"],
     ["notBreaching", "Treated as still OK — a real outage can go unnoticed"]],
    col_widths=[5.0, 7.6],
    note="Priya sets critical checkout instances to breaching, specifically to avoid the notBreaching trap.")

# 9 — Section intro: composite alarms
d.content_slide("Composite Alarms: Combining Signals",
    "One alarm rarely tells the whole story on its own", "Module 1", dark=True)

# 10 — Composite alarm applied
d.numbered_list_slide("Module 1", "Composite Alarm, Applied", "Meridian Loyalty's checkout service", [
    ("High CPU alone often just means a legitimate traffic spike", "paging on that alone creates noise, not signal"),
    ("A composite alarm requires high CPU AND elevated 5xx errors", "only pages when both conditions are true together"),
    ("This meaningfully cuts down on false pages", "compared to alerting on every individual metric alarm"),
    ("The underlying alarms still exist independently", "the composite just adds a layer of combined judgment on top"),
])

# 11 — Exam trap: metric filter vs Logs Insights
d.quad_box_slide("COMMON EXAM TRAP", "Metric Filter vs. Logs Insights", "Continuous alerting and ad hoc searching solve different problems",
    [("Metric filter", "a standing rule — every matching log event increments a metric, in real time."),
     ("That metric can carry a normal alarm", "triggering ALARM the moment the pattern recurs."),
     ("Logs Insights", "an ad hoc query language for logs that already exist — not continuous."),
     ("Great for investigating after the fact", "not for triggering the alert itself.")],
    note="One line: need an alert going forward — that's a metric filter with an alarm. Need to explore what happened — that's Logs Insights.")

# 12 — Applied: metric filter vs Logs Insights
d.table_slide("Module 1", "Metric Filter vs. Logs Insights, Applied", "Same log group, two different jobs",
    ["Need", "Tool"],
    [["Alert the moment an error pattern recurs", "Metric filter + CloudWatch alarm"],
     ["Investigate why an alarm fired three hours ago", "CloudWatch Logs Insights"]],
    col_widths=[7.0, 5.6],
    note="Continuous and alarmable vs. ad hoc and exploratory — not interchangeable.")

# 13 — Putting it together
d.numbered_list_slide("Module 1", "Putting It Together: Monitoring the Checkout Service", "Every piece from tonight, in one design", [
    ("Detailed (1-minute) monitoring on the checkout service's instances", "fast detection matters for a customer-facing, revenue path"),
    ("A CPU alarm set to treat missing data as breaching", "so a silent crash isn't mistaken for OK"),
    ("A composite alarm requiring high CPU and elevated 5xx errors", "before paging on-call, cutting down noise"),
    ("A metric filter on “ERROR” log lines, with its own alarm", "catching application failures no infrastructure metric would show"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 1", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Detailed monitoring should be enabled everywhere”", "Apply it where fast detection is actually worth the added cost."),
    ("“Missing data is the same as a normal reading”", "The missing-data treatment setting decides what a gap actually means."),
    ("“Logs Insights can trigger alerts in real time”", "It's ad hoc querying — a metric filter with an alarm is what alerts."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 2 covers Task 1.2 — turning these alarms into automatic remediation, not just a page", "Module 1")

# 16 — Recap
d.content_slide("Recap",
    "Standard vs. detailed monitoring, missing-data treatment, composite alarms cutting noise, metric filters turning log patterns into alarms", "Module 1", dark=True)

# 17 — Closing
d.closing_slide("Implementing Metrics,", "Alarms, and Filters", "Next up: Module 2 — remediating what these alarms catch")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
