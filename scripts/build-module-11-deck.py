"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/11-automating-your-architecture.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-11-deck.py

Paired with instructor-private/11-automating-your-architecture-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "11-automating-your-architecture.pptx")

d = Deck(11, "Automating Your Architecture",
          "Click-built infrastructure works once. Tonight is what works the second time.")

# 1 — Title
d.title_slide("Module 11 · Lecture", ["Automating Your", "Architecture"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 11", "Question of the Day", "Before we start",
    [("Frank asks: “what exactly is our production setup right now?” Can you answer honestly?",
      "If the answer is “whatever accumulated from months of console clicks” — tonight fixes that."),
     ("Recap: Modules 7-10 built a real, deliberate architecture", "VPC, ALB, Auto Scaling, RDS Multi-AZ — all built by hand, in the console"),
     ("Tonight's shift", "From “built once by clicking” to “described in a file, deployed anywhere, reviewed like code”")])

# 3 — Objectives
d.numbered_list_slide("Module 11", "Objectives", "Five things by the end of tonight", [
    ("Explain what CloudFormation does", "and why infrastructure as code matters, not just what it is"),
    ("Describe a template's structure and what a stack is", "the file vs. the deployed result"),
    ("Explain what a change set is", "seeing the blast radius before you pull the trigger"),
    ("Describe what Systems Manager adds", "operating a fleet, not just provisioning it"),
    ("Compare Elastic Beanstalk to CloudFormation", "speed vs. precise control — know when each fits"),
])

# 4 — The café's V6 problem
d.content_slide("The Café's V6 Problem",
    "Everything through Module 10 was built by hand. That doesn't survive a second Region.", "Module 11")

# 5 — CloudFormation
d.content_slide("AWS CloudFormation: Infrastructure as Code",
    "Describe infrastructure in a file. AWS builds it to match — in order, every time.", "Module 11", dark=True)

# 6 — Templates vs stacks
d.split_card_slide("Module 11", "Templates vs. Stacks", "The file you write vs. the thing you get",
    "Template",
    [("The file you write", "JSON or YAML, describing desired resources and properties"),
     ("Version-controlled", "checked in, reviewed, with a real change history")],
    "Stack",
    "What you get when it's deployed",
    ["A single, managed unit of every resource created", "Delete the stack, everything it made is cleanly removed"])

# 7 — Why infrastructure as code
d.numbered_list_slide("Module 11", "Why Infrastructure as Code, Specifically", "Three real benefits, not just “less clicking”", [
    ("Version-controllable", "checked into a repo, reviewed like any other change, with real history"),
    ("Repeatable", "the same template deploys an identical environment — including in a second Region"),
    ("Self-documenting", "the template IS the accurate, current description of what's actually deployed"),
])

# 8 — Change sets
d.content_slide("Change Sets: See the Blast Radius First",
    "Updating a live stack is risky if you can't see what will actually happen", "Module 11")

# 9 — Exam trap: change sets catch replacements
d.quad_box_slide("COMMON EXAM TRAP", "What a Change Set Actually Shows", "Not every update is “just an update”",
    [("Modified in place", "The resource is updated without being destroyed and recreated."),
     ("Replaced", "A NEW resource is created, the old one deleted — for a database, that's real risk."),
     ("Deleted", "A resource that no longer appears in the template gets removed."),
     ("Review before execute", "You see all of this calculated BEFORE anything actually happens.")],
    note="Study cue: a change set is how you catch “this will replace your database” before it happens, not after.")

# 10 — Systems Manager
d.content_slide("AWS Systems Manager: Operating What You've Automated",
    "Provisioning is half the story — this is about running it afterward, at scale", "Module 11")

# 11 — Systems Manager capabilities
d.four_up_slide("Module 11", "Systems Manager Capabilities", "Operating a fleet, not one instance at a time", [
    ("1", "Session Manager", "Shell access with no open SSH port — access controlled via IAM, sessions logged"),
    ("2", "Automation", "Runs predefined or custom workflows across resources, no manual per-instance work"),
    ("3", "Patch Manager", "Applies OS/software patches across a fleet on a schedule"),
    ("4", "Parameter Store", "From Module 9 — config values and secrets, part of this same suite"),
])

# 12 — Elastic Beanstalk
d.content_slide("AWS Elastic Beanstalk: A Faster On-Ramp",
    "Upload application code. Beanstalk handles the infrastructure with managed defaults.", "Module 11", dark=True)

# 13 — Beanstalk vs CloudFormation
d.table_slide("Module 11", "Elastic Beanstalk vs. CloudFormation", "Speed and simplicity vs. precise, explicit control",
    ["", "Elastic Beanstalk", "CloudFormation"],
    [["What you provide", "Application code", "A template describing every resource"],
     ["Control over resources", "Managed defaults, still adjustable", "Full, explicit control"],
     ["Best for", "Getting an app running quickly", "Precise, repeatable, complex environments"],
     ["Learning curve", "Lower", "Higher"]],
    col_widths=[3.0, 4.7, 4.7],
    note="Beanstalk still runs on real EC2, ELB, and Auto Scaling underneath — it's not a separate compute model.")

# 14 — Putting it together
d.numbered_list_slide("Module 11", "Putting It Together: The Café's V6 Architecture", "CloudFormation, not Beanstalk — and here's why", [
    ("The café's architecture is already precise and deliberate", "VPC, subnets, ALB, Auto Scaling, RDS Multi-AZ — Modules 7-10, built exactly on purpose"),
    ("CloudFormation captures that exactly", "a template becomes the single source of truth Sofía and Nikhil can both read and version"),
    ("The same template redeploys to a second Region", "for disaster recovery — without re-clicking months of console configuration"),
], note="This is the literal technical requirement behind Module 1's V6 milestone.")

# 15 — Common mix-ups
d.resource_list_slide("Module 11", "Common Mix-Ups", "Worth getting right before Module 12", [
    ("“A stack is the same thing as the template”", "The template is the file; the stack is the deployed, managed result."),
    ("“All stack updates just update resources in place”", "Some replace them entirely — a change set is how you catch that."),
    ("“Elastic Beanstalk uses some different kind of compute”", "It's still ordinary EC2, ELB, and Auto Scaling underneath."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Skim the Module 11 guided lab overview — you'll deploy a CloudFormation stack yourself", "Module 11")

# 17 — Closing
d.closing_slide("Automating Your", "Architecture", "Next up: caching content")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
