"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/02-remediating-issues-based-on-monitoring-and-availability-metrics.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-02-deck.py

Paired with instructor-private/02-remediating-issues-based-on-monitoring-and-availability-metrics-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "02-remediating-issues-based-on-monitoring-and-availability-metrics.pptx")

d = Deck(2, "Remediating Issues Based on Monitoring and Availability Metrics",
          "Module 1 built the signal. Tonight, that signal triggers an actual fix, before a human has to.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 2 · Lecture", ["Remediating Monitoring", "and Availability Issues"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 2", "Question of the Day", "Before we start",
    [("A checkout service instance fails its system status check — the underlying hardware, not the instance itself", "Should Priya reboot it, recover it, or replace it?"),
     ("Recap: Module 1 built metrics, alarms, and log-based filters", "reliable signal that something's actually wrong"),
     ("Tonight's task", "Domain 1, Task 1.2 — turning that signal into automatic remediation")])

# 3 — Objectives
d.numbered_list_slide("Module 2", "Objectives", "Four things by the end of tonight", [
    ("Match a status check failure to the correct built-in alarm action", "recover, reboot, or replace"),
    ("Explain what recover actually does, and when it isn't available", "EBS-backed, supported instance types only"),
    ("Distinguish an EC2 alarm action from an Auto Scaling response", "fixing one instance vs. changing capacity"),
    ("Describe how EventBridge and Systems Manager Automation extend remediation", "beyond what a built-in alarm action can do"),
])

# 4 — Problem framing
d.content_slide("From Signal to Action",
    "Module 1 built the alarm. An alarm that only pages a human doesn't scale.", "Module 2")

# 5 — Section intro: matching action to failure
d.content_slide("Recover, Reboot, or Replace?",
    "Which built-in response fits depends on which status check actually failed", "Module 2", dark=True)

# 6 — Applied: status check failures
d.table_slide("Module 2", "Status Check Failures, Applied", "Two checks, two different built-in responses",
    ["Status check failed", "Built-in response"],
    [["System status check (underlying hardware)", "Recover — moves to new hardware, preserves ID, IP, EBS volumes"],
     ["Instance status check (OS or application hung)", "Reboot — restarts the OS in place"]],
    col_widths=[6.6, 6.0],
    note="Matching the action to the check, not defaulting to one action for everything.")

# 7 — Exam trap: recover's requirements
d.quad_box_slide("COMMON EXAM TRAP", "Recover Isn't Available for Every Instance", "Two requirements, easy to miss in a scenario",
    [("Must be EBS-backed", "recovery depends on moving the instance's storage to new hardware."),
     ("Must be a supported instance type", "not every instance family supports the recover action."),
     ("Instance store-backed can't recover", "no persistent storage to move, no supported recovery path."),
     ("No fit? Replace instead", "an Auto Scaling group replacing the instance is often the real answer.")],
    note="One line: check EBS-backed and supported instance type first — recover isn't a universal fix.")

# 8 — Applied: recovery requirements
d.table_slide("Module 2", "Recovery Requirements, Applied", "Two scenarios, two different outcomes",
    ["Instance configuration", "Can it use recover?"],
    [["EBS-backed, supported instance type", "Yes — recovers to new hardware, keeps its identity"],
     ["Instance store-backed, or unsupported type", "No — needs a different path, often replacement via Auto Scaling"]],
    col_widths=[5.6, 7.0],
    note="Checking these two requirements first avoids a remediation plan that can't actually run.")

# 9 — Section intro: alarm action vs Auto Scaling
d.content_slide("EC2 Alarm Action vs. Auto Scaling Response",
    "One fixes an instance. The other changes how many exist.", "Module 2", dark=True)

# 10 — Applied
d.numbered_list_slide("Module 2", "Remediation, Applied to the Checkout Service", "Two different problems, two different fixes", [
    ("One checkout instance fails its status check", "a single unhealthy instance — an alarm action problem, not a capacity one"),
    ("The whole checkout service is under heavier load", "a capacity problem — an Auto Scaling policy adds instances, not a reboot"),
    ("Recover or reboot fixes the one instance", "restores that instance without touching the group's size"),
    ("Auto Scaling changes the group's size", "without needing anything wrong with any specific instance"),
])

# 11 — Exam trap: built-in actions vs automation runbooks
d.quad_box_slide("COMMON EXAM TRAP", "Built-In Actions vs. Automation Runbooks", "Fixed responses only reach so far",
    [("Built-in alarm actions", "recover, reboot, stop, terminate — a fixed set acting on the whole instance."),
     ("EventBridge routes the alarm", "to a target that can take real, specific action."),
     ("Systems Manager Automation", "a scripted runbook — restart one service, run a script, patch a package."),
     ("Beyond fixed actions", "anything more specific than the four built-ins needs a runbook behind it.")],
    note="One line: need a fix more specific than recover, reboot, stop, or terminate — that's EventBridge plus an Automation runbook.")

# 12 — Applied
d.table_slide("Module 2", "Remediation Options, Applied", "Matching the tool to how specific the fix needs to be",
    ["Need", "Tool"],
    [["Fix a hardware-level failure, preserve identity", "Recover (built-in alarm action)"],
     ["Restart one hung service, not the whole OS", "EventBridge + Systems Manager Automation runbook"]],
    col_widths=[6.6, 6.0],
    note="The more specific the fix, the more likely it needs an Automation runbook, not a built-in action.")

# 13 — Putting it together
d.numbered_list_slide("Module 2", "Putting It Together: Remediating the Checkout Service", "Every piece from tonight, in one design", [
    ("A recover alarm action for system status check failures", "EBS-backed, supported instance type — preserves ID and IP, nobody paged"),
    ("An Auto Scaling policy for load-driven capacity changes", "kept separate from any individual instance's health"),
    ("An EventBridge rule triggering Systems Manager Automation", "restarting the application service for the Module 1 error alarm"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 2", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Recover always works on any instance”", "It requires EBS-backed storage and a supported instance type."),
    ("“Alarm actions and Auto Scaling solve the same problem”", "One fixes an instance; the other changes capacity for load."),
    ("“Built-in alarm actions can restart just one service”", "That needs EventBridge plus a Systems Manager Automation runbook."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 3 closes out Domain 1 with logging — CloudWatch Logs, CloudTrail, and troubleshooting what's actually happening", "Module 2")

# 16 — Recap
d.content_slide("Recap",
    "Recover vs. reboot, recovery's EBS-backed and instance-type requirements, alarm actions vs. Auto Scaling, EventBridge plus Automation for specific fixes", "Module 2", dark=True)

# 17 — Closing
d.closing_slide("Remediating Monitoring", "and Availability Issues", "Next up: Module 3 — closing out Domain 1 with logging")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
