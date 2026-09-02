"""
Builds certifications/soa-c02/lectures/03-maintaining-and-troubleshooting-logging-solutions.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-03-deck.py

Paired with instructor-private/03-maintaining-and-troubleshooting-logging-solutions-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02", "lectures",
                    "03-maintaining-and-troubleshooting-logging-solutions.pptx")

d = Deck(3, "Maintaining and Troubleshooting Logging Solutions",
          "Modules 1 and 2 handled what Priya anticipated. Tonight is what she goes back and looks for.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 3 · Lecture", ["Maintaining and", "Troubleshooting Logging"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 3", "Question of the Day", "Before we start",
    [("An auditor asks Priya to show every IAM policy change across all of Meridian's accounts over the past year", "Can CloudTrail's default view actually answer that?"),
     ("Recap: Module 1 built signal, Module 2 turned it into automatic remediation", "tonight covers what's underneath both — the logging layer itself"),
     ("Tonight's task", "Domain 1, Task 1.3 — the final module of Domain 1: maintaining and troubleshooting logging")])

# 3 — Objectives
d.numbered_list_slide("Module 3", "Objectives", "Four things by the end of tonight", [
    ("Distinguish CloudTrail Event History from a configured trail", "and know when each is actually enough"),
    ("Explain management events vs. data events", "and why data events need explicit opt-in"),
    ("Describe what VPC Flow Logs capture, and where they publish", "network-layer troubleshooting, not application logs"),
    ("Explain CloudWatch Logs' default retention behavior", "why it's a common cost and compliance trap"),
])

# 4 — Problem framing
d.content_slide("Some Questions Only Get Answered by Looking Back",
    "Modules 1 and 2 handled what Priya anticipated. Tonight is what she goes back and looks for.", "Module 3")

# 5 — Section intro: CloudTrail
d.content_slide("CloudTrail: Two Very Different Views",
    "One is free and instant. One is what compliance actually needs.", "Module 3", dark=True)

# 6 — Exam trap: Event History vs Trail
d.quad_box_slide("COMMON EXAM TRAP", "Event History vs. a Trail", "One is built in — the other you have to configure",
    [("Event History", "free, automatic, past 90 days, single account, management events only."),
     ("A trail", "delivers continuously to S3, retained as long as you keep it."),
     ("Multi-region trail", "captures activity across every AWS Region."),
     ("Organization trail", "captures activity across every account in the org.")],
    note="One line: 90 days and one account is Event History's ceiling — anything more needs an actual trail.")

# 7 — Applied
d.table_slide("Module 3", "Event History vs. Trail, Applied", "Matching the tool to what's actually being asked for",
    ["Need", "Tool"],
    [["Quick check: who did this yesterday?", "Event History — free, no setup"],
     ["Investigate an API call from 6 months ago", "A trail — Event History doesn't go back that far"],
     ["Activity across every account in the org", "An organization trail"]],
    col_widths=[6.6, 6.0],
    note="The scenario's timeframe and scope decide which one actually applies.")

# 8 — Section intro: VPC Flow Logs
d.content_slide("Seeing the Network Layer",
    "CloudTrail shows API calls. It doesn't show a dropped connection.", "Module 3")

# 9 — VPC Flow Logs applied
d.numbered_list_slide("Module 3", "VPC Flow Logs, Applied", "Diagnosing Café Sol's dropped connection", [
    ("A request that should reach the reporting server is silently dropped", "neither CloudTrail nor application logs show why"),
    ("VPC Flow Logs capture ACCEPT and REJECT decisions", "at the VPC, subnet, or network interface level"),
    ("Filtering for REJECT records on that interface", "shows exactly which security group or NACL rule is responsible"),
    ("This is a network-layer answer", "something no API-layer or application log could provide"),
])

# 10 — Section intro: CloudWatch Logs retention
d.content_slide("The Retention Setting Nobody Sets",
    "A new log group doesn't age out on its own", "Module 3", dark=True)

# 11 — Exam trap: Never Expire default
d.quad_box_slide("COMMON EXAM TRAP", "CloudWatch Logs' Default Is Never Expire", "Indefinite retention, until someone changes it",
    [("New log group default", "“Never Expire” — logs are kept indefinitely."),
     ("Nobody notices", "until storage costs are unexpectedly high months later."),
     ("The fix", "set an explicit retention period, from 1 day up."),
     ("Applies per log group", "not one blanket setting for the whole account.")],
    note="One line: CloudWatch Logs doesn't age data out automatically — an explicit retention period is the only thing that does.")

# 12 — Applied
d.table_slide("Module 3", "Retention, Applied", "Matching the retention period to what the log group actually holds",
    ["Log group", "Right retention"],
    [["High-volume debug logs, no long-term value", "A short explicit period — days to weeks"],
     ["Logs needed for a compliance requirement", "An explicit period matching that requirement, not indefinite by accident"]],
    col_widths=[6.6, 6.0],
    note="Deliberate, per-log-group — never left on the default by omission.")

# 13 — Putting it together
d.numbered_list_slide("Module 3", "Putting It Together: Meridian's Logging Strategy", "Every piece from tonight, in one design", [
    ("A multi-region, organization-wide trail", "delivering to durable S3 — beyond Event History's 90-day, single-account view"),
    ("Data events enabled on customer-data S3 buckets", "object-level access, exactly what compliance would ask for"),
    ("VPC Flow Logs on Café Sol's and Ridgeline's VPCs", "a rejected-connection complaint diagnosed in minutes"),
    ("An explicit retention period on every log group", "instead of the default Never Expire"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 3", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Event History is enough for any audit”", "It's 90 days, one account — a trail is required beyond that."),
    ("“A trail logs everything automatically”", "Data events need explicit, per-resource opt-in."),
    ("“CloudWatch Logs ages out on its own”", "The default is Never Expire — retention must be set explicitly."),
], dark=True)

# 15 — Domain 1, Complete
d.table_slide("Module 3", "Domain 1, Complete", "Three modules, one operational foundation",
    ["Module", "Task"],
    [["Module 1", "Task 1.1 — metrics, alarms, and log-based filters"],
     ["Module 2", "Task 1.2 — remediating issues automatically"],
     ["Module 3", "Task 1.3 — maintaining and troubleshooting logging"]],
    col_widths=[3.6, 9.0],
    note="Signal, action, and the record underneath both — Domain 1's three tasks, closed.")

# 16 — Recap
d.content_slide("Recap",
    "Event History vs. trails, management vs. data events, VPC Flow Logs for network-layer troubleshooting, CloudWatch Logs' Never Expire default", "Module 3", dark=True)

# 17 — Closing
d.closing_slide("Maintaining and", "Troubleshooting Logging", "Domain 1 complete — next up: Domain 2, reliability and business continuity")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
