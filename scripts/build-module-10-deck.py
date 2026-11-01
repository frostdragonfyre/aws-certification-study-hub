"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/10-implementing-monitoring-elasticity-and-high-availability.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-10-deck.py

Paired with instructor-private/10-implementing-monitoring-elasticity-and-high-availability-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "10-implementing-monitoring-elasticity-and-high-availability.pptx")

d = Deck(10, "Implementing Monitoring, Elasticity, and High Availability",
          "One instance is a single point of failure. Tonight we stop having one of anything.")

# 1 — Title
d.title_slide("Module 10 · Lecture", ["Monitoring, Elasticity,", "and High Availability"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 10", "Question of the Day", "Before we start",
    [("The café just got a local news segment airing at an unknown time. Is one EC2 instance ready?",
      "No — and tonight is exactly the toolkit that fixes it."),
     ("Recap: CLF-C02 introduced CloudWatch, ELB, and Auto Scaling", "at a conceptual, one-sentence level"),
     ("Tonight's shift", "From “what is it” to “which policy, which config, for this exact traffic pattern”")])

# 3 — Objectives
d.numbered_list_slide("Module 10", "Objectives", "Five things by the end of tonight", [
    ("Explain what CloudWatch monitors", "metric vs. alarm — and what it does NOT do by itself"),
    ("Describe how an ALB distributes traffic", "target groups and health checks"),
    ("Compare Auto Scaling's policy types", "target tracking, step scaling, scheduled scaling"),
    ("Explain why Multi-AZ is required for real HA", "one AZ, however many instances, is still one point of failure"),
    ("Diagnose an availability/scaling scenario", "match the symptom to the right service"),
])

# 4 — The café's V5 problem
d.content_slide("The Café's V5 Problem",
    "A local news segment, an unknown air time, and one EC2 instance that isn't ready", "Module 10")

# 5 — CloudWatch
d.content_slide("Amazon CloudWatch: Seeing What's Actually Happening",
    "You can't scale, fail over, or fix what you can't see", "Module 10")

# 6 — Metrics, alarms, logs, states
d.four_up_slide("Module 10", "Metrics, Alarms, and Logs", "CloudWatch observes and alerts — it doesn't act by itself", [
    ("1", "Metric", "A numeric data point over time — CPU utilization, request count"),
    ("2", "Alarm", "Watches a metric, triggers an action when a threshold is crossed"),
    ("3", "Logs", "Centralized output from EC2, Lambda, and most AWS services"),
    ("4", "Alarm states", "OK, ALARM, or INSUFFICIENT_DATA — not enough data yet to evaluate"),
])

# 7 — ELB
d.content_slide("Elastic Load Balancing: Distributing the Traffic",
    "A single EC2 instance is a single point of failure, by definition", "Module 10", dark=True)

# 8 — Target groups and health checks
d.numbered_list_slide("Module 10", "How an ALB Decides Where Traffic Goes", "Target groups + health checks", [
    ("Targets register with a target group", "typically EC2 instances, spread across multiple AZs"),
    ("The ALB periodically health-checks each target", "commonly a simple HTTP GET to a defined path"),
    ("A target failing enough consecutive checks is marked unhealthy", "automatically removed from rotation"),
    ("Traffic resumes once it passes health checks again", "no manual intervention needed for this part"),
])

# 9 — Exam trap: ALB job vs Auto Scaling job
d.quad_box_slide("COMMON EXAM TRAP", "Elastic Load Balancing vs. Auto Scaling", "Paired constantly, not the same job",
    [("ELB's job", "Distribute traffic across whichever instances currently exist. Routes around unhealthy targets."),
     ("Auto Scaling's job", "Add or remove instances to match demand. Decides how many targets should exist."),
     ("Health check ≠ replacement", "An ALB removing an unhealthy target does NOT by itself launch a replacement instance."),
     ("Used together", "A new Auto Scaling instance is automatically registered with the ALB's target group.")],
    note="Study cue: ELB decides WHERE traffic goes. Auto Scaling decides HOW MANY targets exist.")

# 10 — Auto Scaling
d.content_slide("EC2 Auto Scaling: Adding and Removing Capacity",
    "Elasticity in practice — capacity sized for right now, not a rare spike", "Module 10")

# 11 — Scaling policy types
d.table_slide("Module 10", "Scaling Policy Types", "Match the policy to the traffic pattern",
    ["Policy type", "How it works", "Best for"],
    [["Target tracking", "Hold a metric at a target value automatically", "Most workloads — simplest, most common"],
     ["Step scaling", "Different scaling actions at different alarm thresholds", "Finer-grained control than one target value"],
     ["Scheduled scaling", "Capacity changes at known times", "Predictable patterns — lunch rush, known events"]],
    col_widths=[2.6, 5.2, 4.4],
    note="The café's news-segment spike: unknown timing rules out scheduled scaling — target tracking fits best.")

# 12 — Multi-AZ
d.content_slide("Multi-AZ: High Availability, Not Just More Capacity",
    "Everything so far can live in ONE Availability Zone — and fail with it", "Module 10")

# 13 — Exam trap: Multi-AZ vs read replica
d.split_card_slide("Module 10", "Multi-AZ vs. Read Replica", "Both are “another copy of the database” — for different reasons",
    "Multi-AZ",
    [("Synchronous standby, second AZ", "automatic failover if the primary fails"),
     ("Solves", "availability — NOT read scaling")],
    "Read replica",
    "Offloads read traffic",
    ["Additional readable copies of the database", "Solves read scaling — NOT failover"])

# 14 — Putting it together
d.numbered_list_slide("Module 10", "Putting It Together: The Café's V5 Architecture", "No single instance, no single AZ", [
    ("An ALB spreads traffic across EC2 instances in two AZs", "no single instance or AZ is a single point of failure"),
    ("Target tracking Auto Scaling reacts to rising CPU", "adds instances during the spike, removes them once it settles"),
    ("RDS Multi-AZ protects the database layer", "a single AZ failure doesn't take the whole application down"),
], note="This is the literal technical requirement behind Module 1's V5 milestone.")

# 15 — Common mix-ups
d.resource_list_slide("Module 10", "Common Mix-Ups", "Worth getting right before Module 11", [
    ("“CloudWatch scales things automatically”", "It observes and alerts — Auto Scaling is what actually acts."),
    ("“A load balancer alone means high availability”", "Only if its targets actually span multiple AZs."),
    ("“Multi-AZ improves read performance”", "It solves failover/availability — read replicas solve read scaling."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Skim the Module 10 guided lab overview — you'll configure an ALB and Auto Scaling group yourself", "Module 10")

# 17 — Closing
d.closing_slide("Monitoring, Elasticity,", "and High Availability", "Next up: automating your architecture")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
