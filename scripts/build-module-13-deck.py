"""
Builds certifications/saa-c03-solutions-architect-associate/lectures/13-building-decoupled-architectures.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-13-deck.py

Paired with instructor-private/13-building-decoupled-architectures-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03-solutions-architect-associate", "lectures",
                    "13-building-decoupled-architectures.pptx")

d = Deck(13, "Building Decoupled Architectures",
          "One slow piece shouldn't be able to take down the whole request.")

# 1 — Title
d.title_slide("Module 13 · Lecture", ["Building Decoupled", "Architectures"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 13", "Question of the Day", "Before we start",
    [("Right now, one order tries to charge, save, notify the kitchen, and email a receipt — all in one request",
      "If the email service has a slow moment, does the customer's checkout really need to wait on it?"),
     ("Recap: Module 12 reduced repeated work reaching the origin", "CloudFront, ElastiCache, DAX — caching, not decoupling"),
     ("Tonight's shift", "From one fragile chain to independent pieces that don't succeed or fail together")])

# 3 — Objectives
d.numbered_list_slide("Module 13", "Objectives", "Five things by the end of tonight", [
    ("Explain what Amazon SQS does", "and how a queue decouples a producer from a consumer"),
    ("Describe standard vs. FIFO queues", "and what a visibility timeout and a dead-letter queue are for"),
    ("Explain what Amazon SNS does", "and how fan-out combines SNS with SQS"),
    ("Explain what EventBridge adds beyond SNS", "and when to reach for it instead"),
    ("Compare SQS, SNS, and EventBridge", "and match each to the messaging problem it solves"),
])

# 4 — The café's fragile order chain
d.content_slide("The Café's Fragile Order Chain",
    "Charge the card, save it, notify the kitchen, update inventory, email a receipt — all in one request", "Module 13")

# 5 — SQS
d.content_slide("Amazon SQS: Decoupling with a Queue",
    "The producer drops a message and moves on. A consumer picks it up whenever it's ready.", "Module 13", dark=True)

# 6 — Standard vs FIFO
d.table_slide("Module 13", "Standard vs. FIFO Queues", "Two SQS queue types — know the trade-off, not just the names",
    ["", "Standard", "FIFO"],
    [["Ordering", "Best-effort (not guaranteed)", "Strict, guaranteed"],
     ["Delivery", "At-least-once — a message could repeat", "Exactly-once processing"],
     ["Throughput", "Nearly unlimited", "Limited (still high)"],
     ["Café example", "Menu-view analytics events", "Kitchen order tickets"]],
    col_widths=[3.0, 4.7, 4.7])

# 7 — Visibility timeout and dead-letter queues
d.numbered_list_slide("Module 13", "Visibility Timeout and Dead-Letter Queues", "Two safety mechanisms baked into SQS", [
    ("Visibility timeout", "a picked-up message is hidden from other consumers for a window, so two consumers don't process it at once"),
    ("Dead-letter queue (DLQ)", "a message that keeps failing after repeated retries gets routed here instead of looping forever"),
])

# 8 — Exam trap: what causes duplicate processing
d.quad_box_slide("COMMON EXAM TRAP", "What Actually Causes Duplicate Processing", "Two culprits, same symptom",
    [("Timeout too short", "The visibility timeout is shorter than how long processing actually takes."),
     ("Consumer doesn't delete", "The consumer finishes but never explicitly deletes the message."),
     ("Message becomes visible again", "Either way, another consumer picks it up and processes it a second time."),
     ("Fix: adjust the timeout or the delete logic", "Not a queue-type problem — check these two things first.")],
    note="Study cue: “processed twice” almost always points back to the visibility timeout, not the queue itself.")

# 9 — SNS
d.content_slide("Amazon SNS: Publish/Subscribe Messaging",
    "One publish to a topic. Every current subscriber gets a copy — the publisher doesn't know who they are.", "Module 13", dark=True)

# 10 — Fan-out pattern
d.split_card_slide("Module 13", "The Fan-Out Pattern", "One event, several independent downstream systems",
    "SNS Topic",
    [("One publish", "the order-processing service publishes the event exactly once"),
     ("Broadcasts to every subscriber", "the publisher never needs to know who, or how many, exist")],
    "Each Subscriber's SQS Queue",
    "Durability, per subscriber",
    ["Kitchen display, inventory, and email each get their own queue", "A brief outage on one subscriber doesn't lose its messages"])

# 11 — Exam trap: SNS alone isn't durable
d.quad_box_slide("COMMON EXAM TRAP", "SNS Alone Isn't Durable", "Broadcast and durability are two different guarantees",
    [("SNS delivers to subscribers", "When published, SNS attempts delivery to every current subscriber."),
     ("An HTTP subscriber that's down", "can miss that specific delivery — SNS alone has no built-in retry/durability for it."),
     ("An SQS queue as the subscriber", "holds the message durably until that consumer is available."),
     ("Fan-out = broadcast + durability", "SNS for the broadcast, SQS queues underneath for the durability.")],
    note="Study cue: if a scenario needs both “reach everyone” and “never lose a message,” it's fan-out, not SNS alone.")

# 12 — EventBridge
d.content_slide("Amazon EventBridge: Event-Driven Routing at Scale",
    "Routes on what's actually inside the event, from AWS services, apps, and SaaS partners", "Module 13")

# 13 — Matching the messaging pattern to the problem
d.table_slide("Module 13", "Matching the Messaging Pattern to the Problem", "Same broad idea — decoupling — three different fits",
    ["Scenario", "Right service"],
    [["One producer, one consumer type, need a durable buffer", "SQS"],
     ["One event needs to reach several independent subscribers", "SNS (fan-out with SQS)"],
     ["Routing must depend on the event's actual content", "EventBridge"],
     ["Kitchen tickets that must process strictly in order", "SQS FIFO"]],
    col_widths=[7.6, 4.8],
    note="EventBridge adds rule-based filtering, schema discovery, and native AWS/SaaS integrations SNS doesn't have.")

# 14 — Putting it together
d.numbered_list_slide("Module 13", "Putting It Together: The Café's Order Pipeline", "One publish — the pieces that react to it can change without touching checkout", [
    ("The ordering service publishes one order event to an SNS topic", "it never needs to know who's listening"),
    ("The topic fans out to three SQS queues", "kitchen display, inventory, and email — each independent, each durable"),
    ("EventBridge separately watches for high-value orders", "routing those to a fraud-review workflow, using a rule the ordering service never had to know about"),
], note="This is the literal technical fix for the fragile, all-in-one-request order chain from the top of the lecture.")

# 15 — Common mix-ups
d.resource_list_slide("Module 13", "Common Mix-Ups", "Worth getting right before Module 14", [
    ("“SNS and SQS are the same thing”", "SQS is a durable queue; SNS is pub/sub broadcast — fan-out combines both."),
    ("“SNS alone is durable”", "An HTTP subscriber can miss a delivery — durability comes from SQS underneath it."),
    ("“EventBridge is just SNS with a longer name”", "EventBridge adds content-based rules, schema discovery, and native integrations SNS doesn't have."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Think about what happens when none of these consumers are servers you manage at all", "Module 13")

# 17 — Closing
d.closing_slide("Building Decoupled", "Architectures", "Next up: serverless architectures and microservices")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
