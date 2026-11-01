"""
Builds certifications/soa-c02-sysops-administrator-associate/lectures/04-implementing-scalability-and-elasticity.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-04-deck.py

Paired with instructor-private/04-implementing-scalability-and-elasticity-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02-sysops-administrator-associate", "lectures",
                    "04-implementing-scalability-and-elasticity.pptx")

d = Deck(4, "Implementing Scalability and Elasticity",
          "Domain 1 kept Priya informed. Domain 2 asks whether Meridian's infrastructure survives its own success.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 4 · Lecture", ["Implementing Scalability", "and Elasticity"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 4", "Question of the Day", "Before we start",
    [("Meridian Loyalty's checkout service sees the same large traffic spike every day at lunch, like clockwork", "Should Auto Scaling wait to react, or already know it's coming?"),
     ("Recap: Domain 1 closed with signal, remediation, and trustworthy logging", "Domain 2 asks a different question — does capacity match demand"),
     ("Tonight's task", "Domain 2, Task 2.1 — the first module of Domain 2: scalability and elasticity")])

# 3 — Objectives
d.numbered_list_slide("Module 4", "Objectives", "Four things by the end of tonight", [
    ("Distinguish target tracking, step, and simple scaling policies", "and match each to the scenario it fits"),
    ("Explain when scheduled scaling fits better than any dynamic policy", "known patterns vs. real-time reactions"),
    ("Describe how Aurora Auto Scaling adds and removes read replicas", "the same target tracking concept, applied to a database"),
    ("Design a complete scaling strategy for a stated demand pattern", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Does Capacity Show Up When It's Actually Needed?",
    "Domain 2 opens with the most basic operational question: does Meridian's infrastructure survive its own success", "Module 4")

# 5 — Section intro: target tracking vs step
d.content_slide("Target Tracking vs. Step Scaling",
    "Two ways to turn “the metric changed” into “add or remove instances”", "Module 4", dark=True)

# 6 — Exam trap 1
d.quad_box_slide("COMMON EXAM TRAP", "Matching the Policy to the Pattern", "One size-fits-all response isn't always the point",
    [("Target tracking", "maintain a target metric value — AWS calculates the adjustments automatically."),
     ("The simplest default", "right for a steady relationship between load and the metric."),
     ("Step scaling", "different-sized adjustments for different-sized threshold breaches."),
     ("Reach for it deliberately", "when breach severity, not just breach existence, should change the response.")],
    note="One line: target tracking is the default — step scaling is for when breach size should change the response.")

# 7 — Applied
d.table_slide("Module 4", "Target Tracking vs. Step Scaling, Applied", "Matching the scenario to the right policy type",
    ["Scenario", "Right policy"],
    [["“Keep CPU near 50%”", "Target tracking — simplest fit, no step sizes to define"],
     ["“Small breach → small change, large breach → large change”", "Step scaling — granular, breach-size-aware"]],
    col_widths=[6.6, 6.0],
    note="Default to target tracking unless the scenario specifically asks for graduated responses.")

# 8 — Section intro: scheduled vs dynamic
d.content_slide("Scheduled vs. Dynamic Scaling",
    "Dynamic reacts. Scheduled is already there.", "Module 4", dark=True)

# 9 — Exam trap 2
d.quad_box_slide("COMMON EXAM TRAP", "Known Pattern? Don't Wait for a Metric", "Dynamic scaling is always a step behind a predictable spike",
    [("Scheduled scaling", "capacity changes for known, specific times — set in advance."),
     ("Dynamic scaling", "reacts to a metric after it actually changes."),
     ("Predictable pattern", "scheduled scaling has capacity in place before demand arrives."),
     ("Not mutually exclusive", "a known baseline and unpredictable variation can both be handled at once.")],
    note="One line: a known pattern gets scheduled scaling — dynamic scaling is always reacting after the fact.")

# 10 — Applied
d.table_slide("Module 4", "Scheduled vs. Dynamic, Applied", "Matching the approach to what's actually predictable",
    ["Demand pattern", "Right approach"],
    [["Known daily lunch and evening spikes", "Scheduled scaling — capacity in place beforehand"],
     ["Unpredictable variation on top of that baseline", "Dynamic scaling (target tracking), layered on top"]],
    col_widths=[6.6, 6.0],
    note="Layering both is often the actual right answer, not choosing one over the other.")

# 11 — Section intro: beyond EC2
d.content_slide("Scaling Beyond EC2",
    "The same concepts, applied to services that aren't EC2 instances at all", "Module 4")

# 12 — Applied
d.numbered_list_slide("Module 4", "Application and Aurora Auto Scaling, Applied", "The same mechanism, different resources", [
    ("Application Auto Scaling extends target tracking and scheduling", "to ECS tasks, DynamoDB capacity, and Aurora read replicas"),
    ("Aurora Auto Scaling adds and removes Aurora Replicas", "based on load, using the same target tracking concept"),
    ("Meridian Loyalty's Aurora cluster scales alongside its EC2 fleet", "same lunch-hour spike, same underlying pattern, different service"),
    ("The mechanism carries over, not just the EC2 use case", "target tracking and scheduling aren't EC2-specific ideas"),
])

# 13 — Putting it together
d.numbered_list_slide("Module 4", "Putting It Together: Scaling the Checkout Service", "Every piece from tonight, in one design", [
    ("Scheduled scaling adding baseline capacity ahead of known spikes", "capacity in place before demand arrives, not reacting after"),
    ("Target tracking layered on top for unpredictable variation", "holding CPU near target for whatever happens beyond the known pattern"),
    ("Aurora Auto Scaling adding read replicas to the backing database", "same pattern applied to database read capacity"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 4", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Step scaling is always more precise, so use it by default”", "Target tracking is the simpler right default for a steady load-to-metric relationship."),
    ("“Dynamic scaling reacts fast enough for a known spike”", "It's always a step behind — scheduled scaling has capacity in place first."),
    ("“Auto Scaling only applies to EC2”", "Application Auto Scaling extends it to ECS, DynamoDB, and Aurora."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 5 covers Task 2.2 — what happens when a piece of that capacity actually fails", "Module 4")

# 16 — Recap
d.content_slide("Recap",
    "Target tracking vs. step scaling, scheduled vs. dynamic scaling, Application and Aurora Auto Scaling extending the same concepts beyond EC2", "Module 4", dark=True)

# 17 — Closing
d.closing_slide("Implementing Scalability", "and Elasticity", "Next up: Module 5 — high availability and resilient environments")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
