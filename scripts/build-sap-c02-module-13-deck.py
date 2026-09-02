"""
Builds certifications/sap-c02/lectures/13-continuously-improving-an-existing-solution.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-13-deck.py

Paired with instructor-private/13-continuously-improving-an-existing-solution-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02", "lectures",
                    "13-continuously-improving-an-existing-solution.pptx")

d = Deck(13, "Continuously Improving an Existing Solution",
          "Domain 2 built something new. Domain 3 revisits what's already running.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 13 · Lecture", ["Continuously Improving", "an Existing Solution"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 13", "Question of the Day", "Before we start",
    [("Café Sol's system has run well for six months under Meridian", "Does “runs well” mean it's been reviewed against current best practice?"),
     ("Recap: Domain 2 designed Meridian Loyalty from nothing", "Deployment, continuity, security, scaling, performance, cost — six deliberate decisions"),
     ("Tonight's task", "Domain 3, Tasks 3.1 and 3.2 — reviewing and improving what's already running")])

# 3 — Objectives
d.numbered_list_slide("Module 13", "Objectives", "Five things by the end of tonight", [
    ("Explain what a Well-Architected review actually produces", "and how it differs from Trusted Advisor"),
    ("Identify operational excellence gaps in an existing architecture", "and the tools that address them"),
    ("Use IAM Access Analyzer to find unused permissions", "and unintended external access"),
    ("Distinguish Access Analyzer's purpose from GuardDuty's", "two different security questions"),
    ("Design a continuous improvement plan for a stated scenario", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("From Building New to Improving What Exists",
    "Café Sol's original architecture was never revisited with everything the team has learned since", "Module 13")

# 5 — Well-Architected review intro
d.content_slide("Conducting a Formal Review of Café Sol's Architecture",
    "“Runs well” and “reviewed against current best practice” aren't the same claim", "Module 13", dark=True)

# 6 — Exam trap: Well-Architected Tool vs Trusted Advisor
d.quad_box_slide("COMMON EXAM TRAP", "Structured Review vs. Continuous Checking", "Neither one replaces the other",
    [("Well-Architected Tool", "a deliberate, six-pillar review producing a prioritized list of design gaps."),
     ("Trusted Advisor", "continuous, automated checks — cost, security, fault tolerance, performance, limits."),
     ("The review finds structural gaps", "like a design that never accounted for multi-brand realities."),
     ("Trusted Advisor catches what's smaller and ongoing", "in between formal reviews — not instead of them.")],
    note="One line: Well-Architected is a deliberate structured review. Trusted Advisor is continuous automated checking. Use both.")

# 7 — Well-Architected vs Trusted Advisor table
d.table_slide("Module 13", "Where Each Tool Actually Fits", "Applied to Café Sol's six-month-old architecture",
    ["Need", "Right tool"],
    [["A deliberate, prioritized review of the actual design", "AWS Well-Architected Tool"],
     ["Ongoing, automated checks between reviews", "AWS Trusted Advisor"],
     ["Discovering the design never accounted for multi-brand use", "AWS Well-Architected Tool"],
     ["Catching a smaller issue before the next scheduled review", "AWS Trusted Advisor"]],
    col_widths=[7.6, 5.0],
    note="Neither is a substitute for the other — a well-run program uses both, on different cadences.")

# 8 — Operational excellence intro
d.content_slide("Operational Excellence: Turning Runbooks into Automation",
    "Manual steps that were fine for one café aren't fine six months into multi-brand operation", "Module 13")

# 9 — Ops excellence split card
d.split_card_slide("Module 13", "Systems Manager Automation vs. AWS Config", "Two tools, two different operational excellence jobs",
    "Systems Manager Automation",
    [("Converts a manual runbook into a defined document", "the same steps, executed consistently, every time"),
     ("No longer depends on one person's memory", "restarting a stuck job, rotating a credential, scaling for a rush")],
    "AWS Config",
    "Tracks configuration and evaluates against rules",
    ["Catches drift before it becomes an incident", "A security group opened for a fix, never closed"])

# 10 — Security posture intro
d.content_slide("Improving Security Posture: AWS IAM Access Analyzer",
    "Six months of ordinary operation tends to leave residue", "Module 13", dark=True)

# 11 — Exam trap: Access Analyzer vs GuardDuty
d.quad_box_slide("COMMON EXAM TRAP", "Permission Hygiene vs. Active Threats", "Two different security questions, not one",
    [("“Unused permissions, unintended access”", "points to IAM Access Analyzer."),
     ("“Active malicious behavior underway”", "points to Amazon GuardDuty."),
     ("Access Analyzer asks what's POSSIBLE", "given current permissions and public exposure, whether exploited or not."),
     ("GuardDuty asks what's HAPPENING", "signs that something malicious is actively underway.")],
    note="One line: permission hygiene is Access Analyzer. Active threat detection is GuardDuty. Both matter, for different questions.")

# 12 — Access Analyzer applied
d.numbered_list_slide("Module 13", "IAM Access Analyzer, Applied to Café Sol", "The accumulated residue of six months of real operation", [
    ("A forgotten cross-account role", "from a vendor integration that ended months ago"),
    ("An IAM policy still granting write access", "nobody has actually used in that time"),
    ("Unused access findings surface exactly this", "the accumulated slack in a real, lived-in environment"),
    ("None of it required an incident to be worth fixing", "exposure is a risk on its own, before anything happens"),
])

# 13 — Putting it together
d.numbered_list_slide("Module 13", "Putting It Together: Café Sol's Continuous Improvement Plan", "Every piece from tonight, in one design", [
    ("A Well-Architected review, prioritized against Café Sol's actual design", "supplemented by Trusted Advisor's continuous checks between reviews"),
    ("Systems Manager Automation for the team's manual runbooks", "AWS Config catching configuration drift before it's an incident"),
    ("IAM Access Analyzer clearing accumulated unused permissions", "distinct from GuardDuty's ongoing watch for active threats"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 13", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Trusted Advisor makes a Well-Architected review unnecessary”", "One is continuous and automated; the other is a deliberate design review — not substitutes."),
    ("“Unused permissions aren't a real risk if nothing bad happened”", "Exposure is the risk, independent of whether it's been exploited yet."),
    ("“Access Analyzer and GuardDuty check the same thing”", "One is permission hygiene; the other is active threat detection."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 14 continues Domain 3 with Tasks 3.3–3.5: reliability, performance, and cost for existing solutions", "Module 13")

# 16 — Recap
d.content_slide("Recap",
    "Well-Architected reviews plus Trusted Advisor, runbooks becoming automation, Access Analyzer clearing residue distinct from GuardDuty's threat watch", "Module 13", dark=True)

# 17 — Closing
d.closing_slide("Continuously Improving", "an Existing Solution", "Next up: reliability, performance, and cost for existing solutions")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
