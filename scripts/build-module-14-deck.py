"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/14-building-serverless-architectures-and-microservices.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-14-deck.py

Paired with instructor-private/14-building-serverless-architectures-and-microservices-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "14-building-serverless-architectures-and-microservices.pptx")

d = Deck(14, "Building Serverless Architectures and Microservices",
          "Standing infrastructure for a job that runs a few milliseconds at a time.")

# 1 — Title
d.title_slide("Module 14 · Lecture", ["Building Serverless", "Architectures and Microservices"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 14", "Question of the Day", "Before we start",
    [("The new loyalty-points service does a few milliseconds of work each time an order arrives",
      "Does that really justify an EC2 Auto Scaling group running, and being paid for, 24/7?"),
     ("Recap: Module 13 decoupled the order pipeline", "SQS, SNS fan-out, EventBridge — independent pieces, connected by messaging"),
     ("Tonight's shift", "From “provision a server for this” to “run code only when something actually happens”")])

# 3 — Objectives
d.numbered_list_slide("Module 14", "Objectives", "Five things by the end of tonight", [
    ("Explain what AWS Lambda does", "and what “serverless” actually means"),
    ("Describe how Lambda is triggered", "and what its execution limits are"),
    ("Explain what Amazon API Gateway does", "and how it fronts a serverless API"),
    ("Explain what AWS Step Functions does", "and why orchestration matters for multi-step workflows"),
    ("Describe the microservices pattern", "and how it relates to the decoupling from Module 13"),
])

# 4 — The café's loyalty-points problem
d.content_slide("The Café's Loyalty-Points Problem",
    "A few milliseconds of work per order — most of the time, standing infrastructure would just sit idle", "Module 14")

# 5 — Lambda
d.content_slide("AWS Lambda: Running Code Without Servers",
    "Upload a function. Lambda provisions, scales, and tears down the environment underneath it.", "Module 14", dark=True)

# 6 — Triggers
d.four_up_slide("Module 14", "Lambda Triggers", "Event-driven — something has to invoke the function", [
    ("1", "SQS queue", "A message arrives — exactly the loyalty-points case"),
    ("2", "S3 upload", "A new object is written to a bucket"),
    ("3", "API Gateway request", "An external client calls an HTTP endpoint"),
    ("4", "Scheduled EventBridge rule", "Runs on a cron-like schedule, no separate scheduler needed"),
])

# 7 — Exam trap: execution limits
d.quad_box_slide("COMMON EXAM TRAP", "Lambda's Execution Limits", "“Serverless” doesn't mean “fits every workload”",
    [("15-minute hard limit", "Per invocation — a multi-hour job cannot run inside a single Lambda call."),
     ("Cold starts", "The first invocation after inactivity takes noticeably longer to initialize."),
     ("Stateless by design", "The same execution environment isn't guaranteed to persist between invocations."),
     ("Not every workload fits", "A 3-hour transcoding job needs a different compute option entirely.")],
    note="Study cue: if the scenario names a duration over 15 minutes, Lambda is already ruled out.")

# 8 — API Gateway
d.content_slide("Amazon API Gateway: The Front Door for an API",
    "Lambda has no URL of its own — API Gateway gives external clients a real HTTP endpoint", "Module 14")

# 9 — Exam trap: API Gateway vs ALB
d.quad_box_slide("COMMON EXAM TRAP", "API Gateway Is Not an ALB", "Both route requests — that's where the similarity ends",
    [("Application Load Balancer", "Distributes traffic across a fleet of already-running servers."),
     ("API Gateway", "The front door for building and securing an API — commonly in front of Lambda."),
     ("API-specific features", "Throttling, authorization, and request/response transformation."),
     ("Not simply interchangeable", "Removing an ALB in favor of API Gateway can drop functionality a design still needs.")],
    note="Study cue: ALB load-balances servers already running. API Gateway manages and secures an API.")

# 10 — Step Functions
d.content_slide("AWS Step Functions: Orchestrating Multi-Step Workflows",
    "Confirm payment, then apply points, then generate a receipt — in order, with real error handling", "Module 14", dark=True)

# 11 — Why orchestration matters
d.split_card_slide("Module 14", "Chaining by Hand vs. Orchestrating", "Same three steps, two very different designs",
    "Chaining Lambdas Directly",
    [("Each function calls the next", "coupled to each other, with no central view of the process"),
     ("Retry logic duplicated", "or missed, inside each function individually")],
    "Step Functions State Machine",
    "Sequencing owned centrally",
    ["Each Lambda stays small and focused on one job", "Retries, branching, and failure paths are visible and explicit"])

# 12 — Matching the serverless building block to the problem
d.table_slide("Module 14", "Matching the Serverless Building Block to the Problem", "Same broad idea — serverless — three different fits",
    ["Scenario", "Right service"],
    [["Run code in response to one event, no server management", "Lambda"],
     ["Give external clients an HTTP endpoint in front of Lambda", "API Gateway"],
     ["A multi-step process needs sequencing, branching, or retries", "Step Functions"],
     ["A job genuinely needs to run longer than 15 minutes", "Not Lambda — a different compute option"]],
    col_widths=[7.6, 4.8])

# 13 — Microservices
d.content_slide("Microservices: Small, Independent, Deployable on Their Own",
    "The loyalty-points service doesn't know or care how the kitchen display is built, deployed, or scaled", "Module 14")

# 14 — Putting it together
d.numbered_list_slide("Module 14", "Putting It Together: The Café's Serverless Loyalty Service", "No servers provisioned, no idle cost between orders", [
    ("An SQS queue from the Module 13 fan-out triggers a Lambda function", "adds loyalty points, scales automatically, costs nothing when idle"),
    ("A Step Functions workflow orchestrates the broader post-payment sequence", "confirm payment, apply points, generate a receipt — with retries and clear failure handling"),
    ("API Gateway fronts a Lambda function for order-status lookups", "giving the mobile app a real endpoint, without provisioning a single server"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 14", "Common Mix-Ups", "Worth getting right before Module 15", [
    ("“Serverless fits every workload”", "A job over 15 minutes, or needing a persistent process, doesn't fit Lambda."),
    ("“API Gateway and an ALB are interchangeable”", "API Gateway manages and secures an API; an ALB load-balances already-running servers."),
    ("“Chaining Lambdas by hand is the same as Step Functions”", "Step Functions centralizes sequencing and retries instead of coupling functions together."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Think about where all of this order and event data actually goes once it's captured", "Module 14")

# 17 — Closing
d.closing_slide("Building Serverless", "Architectures and Microservices", "Next up: data engineering patterns")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
