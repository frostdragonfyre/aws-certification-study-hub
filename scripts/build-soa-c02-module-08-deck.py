"""
Builds certifications/soa-c02/lectures/08-automating-manual-and-repeatable-processes.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-08-deck.py

Paired with instructor-private/08-automating-manual-and-repeatable-processes-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02", "lectures",
                    "08-automating-manual-and-repeatable-processes.pptx")

d = Deck(8, "Automating Manual and Repeatable Processes",
          "Module 7 made resource creation consistent. Tonight makes the routine work around that infrastructure hands-off.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 8 · Lecture", ["Automating Manual and", "Repeatable Processes"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 8", "Question of the Day", "Before we start",
    [("Someone on Priya's team manually patches EC2 instances the same way, every single month, by hand", "Should a person really still be doing that?"),
     ("Recap: Module 7 made sure resources get created consistently", "tonight covers the routine operational work around that infrastructure"),
     ("Tonight's task", "Domain 3, Task 3.2 — the final module of Domain 3: automating manual and repeatable processes")])

# 3 — Objectives
d.numbered_list_slide("Module 8", "Objectives", "Five things by the end of tonight", [
    ("Distinguish Systems Manager Automation from Run Command", "and know when each fits"),
    ("Explain how EventBridge scheduled rules trigger recurring automation", "routine work, not just reactive remediation"),
    ("Distinguish a rate expression from a cron expression", "and know when each fits"),
    ("Explain when custom Lambda logic beats a built-in runbook", "and when it's just unnecessary engineering"),
    ("Design an automated maintenance workflow for a repeatable process", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Work That Shouldn't Need a Human Doing It By Hand",
    "Routine, repeatable operational work is exactly what automation is for", "Module 8")

# 5 — Section intro: Automation vs Run Command
d.content_slide("Systems Manager Automation vs. Run Command",
    "Two related tools that answer two different questions", "Module 8", dark=True)

# 6 — Exam trap: Automation vs Run Command
d.quad_box_slide("COMMON EXAM TRAP", "Automation vs. Run Command", "Right now, once, vs. the same way, every time",
    [("Run Command", "immediate, ad hoc action on specified instances, run once."),
     ("SSM Automation", "documented, multi-step runbook — approvals, rollback, repeatable."),
     ("One-off need", "run this command on these servers right now — Run Command."),
     ("Repeatable, standardized need", "a documented workflow that runs the same way every time — Automation.")],
    note="One line: Run Command is for right now — Automation is for the same way, every time.")

# 7 — Applied
d.table_slide("Module 8", "Automation vs. Run Command, Applied", "Matching the scenario to the right tool",
    ["Scenario", "Right tool"],
    [["Restart a service on three servers right now", "Run Command — immediate, ad hoc"],
     ["A documented patching workflow with approval steps", "SSM Automation — repeatable runbook"]],
    col_widths=[7.2, 5.4],
    note="Immediate and one-off points to Run Command; documented and repeatable points to Automation.")

# 8 — Section intro: EventBridge scheduled rules
d.content_slide("EventBridge Scheduled Rules: Automation on a Schedule",
    "Not every trigger is reactive — routine maintenance runs whether or not anything went wrong", "Module 8")

# 9 — Exam trap: rate vs cron
d.quad_box_slide("COMMON EXAM TRAP", "Rate vs. Cron Expressions", "Simple interval, or a specific calendar time",
    [("Rate expression", "fixed, recurring interval — rate(1 day), rate(12 hours)."),
     ("Cron expression", "specific, calendar-based times — cron(0 2 * * ? *)."),
     ("Simple fixed interval", "no calendar requirement — a rate expression fits."),
     ("Calendar-specific timing", "a particular day or hour — a cron expression fits.")],
    note="One line: no calendar requirement means rate; a specific day or hour means cron.")

# 10 — Applied
d.table_slide("Module 8", "Rate vs. Cron, Applied", "Reading the schedule requirement correctly",
    ["Requirement", "Right expression"],
    [["“Every 6 hours”", "Rate expression — rate(6 hours)"],
     ["“Every Sunday at 2 AM”", "Cron expression — a specific calendar time"]],
    col_widths=[7.2, 5.4],
    note="A calendar-specific detail (a day, an hour) is the tell for cron.")

# 11 — Section intro + trap: Lambda vs built-in runbooks
d.content_slide("When Lambda Is the Right Tool",
    "Not every operational process fits a built-in Automation action", "Module 8", dark=True)

# 12 — Exam trap: Lambda vs built-in runbook
d.quad_box_slide("COMMON EXAM TRAP", "Custom Code vs. a Built-In Runbook", "Don't reinvent what AWS already built",
    [("Built-in runbook", "a standard, well-known task — patching, restarting, snapshotting."),
     ("Lambda", "custom logic — an internal API call, a business-specific transformation."),
     ("Standard task", "use the built-in runbook — no custom code needed."),
     ("Business-specific logic", "write the Lambda function — no standard runbook covers it.")],
    note="One line: a standard task already has a runbook — custom logic is what Lambda is actually for.")

# 13 — Putting it together
d.numbered_list_slide("Module 8", "Putting It Together: Automating Meridian's Routine Operations", "Every piece from tonight, in one design", [
    ("SSM Automation runbooks for documented, repeatable workflows", "patching, instance recovery, pre-change snapshots — not Run Command's one-off actions"),
    ("EventBridge scheduled rules triggering runbooks and maintenance Lambdas", "rate expressions for simple intervals, cron expressions for calendar-specific timing"),
    ("Lambda reserved for genuinely custom logic", "Café Sol's monthly archival job, while standard tasks use built-in runbooks"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 8", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Run Command and Automation are the same thing”", "Run Command is immediate and ad hoc; Automation is documented and repeatable."),
    ("“Cron is always the safer choice”", "A rate expression is the simpler fit when there's no calendar-specific requirement."),
    ("“Custom Lambda code is always more reliable”", "A standard task already has a built-in runbook — don't reinvent it."),
], dark=True)

# 15 — Domain 3, Complete
d.table_slide("Module 8", "Domain 3, Complete", "Two modules, one consistent, automated foundation",
    ["Module", "Task"],
    [["Module 7", "Task 3.1 — provisioning and maintaining cloud resources"],
     ["Module 8", "Task 3.2 — automating manual and repeatable processes"]],
    col_widths=[3.6, 9.0],
    note="Consistent creation, and hands-off routine operation — Domain 3's two tasks, closed.")

# 16 — Recap
d.content_slide("Recap",
    "Automation vs. Run Command, rate vs. cron expressions, Lambda vs. built-in runbooks", "Module 8", dark=True)

# 17 — Closing
d.closing_slide("Automating Manual and", "Repeatable Processes", "Domain 3 complete — next up: Domain 4, security and compliance")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
