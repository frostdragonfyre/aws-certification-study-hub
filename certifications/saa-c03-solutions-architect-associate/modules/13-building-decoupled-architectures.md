# Module 13: Building Decoupled Architectures

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

Right now, when a customer places an order on the café's site, one request tries to do everything at once: charge the card, write the order to the database, push it to the kitchen display, decrement inventory, and send a confirmation email — all before the customer's browser gets a response. If the email service has a slow moment, the customer waits on it. If the kitchen display system is redeploying, the *entire order fails*, even though the payment already went through.

This module is about **decoupling**: breaking that one fragile chain into independent pieces that don't have to succeed or fail together, and that don't have to talk to each other directly, or even at the same time.

## Learning objectives

By the end of this module, you should be able to:

- Explain what Amazon SQS does and how a queue decouples a producer from a consumer
- Describe the difference between SQS standard and FIFO queues, and what a visibility timeout and a dead-letter queue are for
- Explain what Amazon SNS does and how the fan-out pattern combines SNS with SQS
- Explain what Amazon EventBridge adds beyond SNS, and when to reach for it instead
- Compare SQS, SNS, and EventBridge and match each to the messaging problem it solves

---

## Amazon SQS: Decoupling with a Queue

**Amazon SQS (Simple Queue Service)** is a fully managed message queue. Instead of the order-processing service calling the kitchen-display service directly and waiting for a response, it drops a message onto a queue and moves on immediately. Some other process — a *consumer* — picks that message up whenever it's ready, does its work, and deletes the message when it's done.

This is the core of decoupling: the *producer* (the service placing the message) and the *consumer* (the service reading it) never call each other directly, don't need to be available at the same time, and can scale completely independently. If the kitchen-display consumer is temporarily down, orders queue up safely instead of failing — the moment it comes back, it works through the backlog.

### Standard vs. FIFO queues

| Queue type | Ordering | Delivery | Throughput |
|---|---|---|---|
| Standard | Best-effort ordering (not guaranteed) | At-least-once (a message could be delivered more than once) | Nearly unlimited |
| FIFO (First-In-First-Out) | Strict ordering guaranteed | Exactly-once processing | Limited (though still high) |

For the café, kitchen order tickets are a natural FIFO case — orders should generally come out in the order they were placed. A stream of "menu view" analytics events, where order doesn't matter and volume is high, is a better fit for a standard queue.

### Visibility timeout

When a consumer picks up a message, SQS doesn't delete it immediately — it becomes temporarily invisible to other consumers for a **visibility timeout** window, so two consumers don't process the same message at once. If the consumer finishes and explicitly deletes the message before the timeout expires, it's gone for good. If the consumer crashes or times out without deleting it, the message becomes visible again and another consumer picks it up.

> ⚠️ **Exam trap:** if a scenario describes messages being processed more than once, or a consumer that's clearly too slow for the current setting, the visibility timeout is usually the knob — either it's too short for how long processing actually takes, or the consumer isn't deleting messages when it should.

### Dead-letter queues

Sometimes a message can't be processed successfully no matter how many times it's retried — a malformed order payload, for example. A **dead-letter queue (DLQ)** is a separate queue that SQS routes a message to after it has failed processing some configured number of times, so it stops looping endlessly and can be inspected separately instead of blocking the rest of the queue.

## Amazon SNS: Publish/Subscribe Messaging

SQS decouples one producer from one consumer reading a queue. But when the café's order event actually needs to reach *several* independent systems at once — the kitchen display, the inventory service, and the email notifier, all from the same order — writing to three separate queues by hand, and keeping that list current as systems are added, gets brittle fast.

**Amazon SNS (Simple Notification Service)** is a **pub/sub** (publish/subscribe) service built around **topics**. A producer publishes one message to a topic, and every current **subscriber** to that topic receives a copy — the publisher doesn't know or care who, or how many, subscribers exist.

### The fan-out pattern: SNS + SQS together

A very common, exam-relevant pattern combines the two: publish an order event once to an SNS topic, and give each downstream system — kitchen display, inventory, email — its **own SQS queue** subscribed to that topic. This is called **fan-out**. Each subscriber gets every message reliably and durably (because it's sitting in its own SQS queue, not lost if that consumer is briefly offline), and adding a fourth downstream system later — a loyalty-points service, say — means subscribing one new queue to the topic, touching nothing else.

> ⚠️ **Exam trap:** SNS by itself has no built-in retry/durability story the way a queue does — if a subscriber (like an HTTP endpoint) is down when SNS delivers, that specific delivery can be lost unless that subscriber is an SQS queue. The fan-out pattern (SNS → multiple SQS queues) is specifically what gets you both broadcast *and* durability at once.

## Amazon EventBridge: Event-Driven Routing at Scale

SNS fans a message out to whoever is subscribed. **Amazon EventBridge** goes further: it's an event bus built for routing events — from AWS services, custom applications, and even third-party SaaS partners — based on their *content*, using rules that match on the actual fields inside the event, not just "who's subscribed to this topic."

Where SNS subscribers generally get every message published to a topic, EventBridge **rules** can filter: "route this event only if `order.total > 100`," for example, sending high-value orders to a fraud-review service while routing everything else to the normal fulfillment path — without the publisher needing to know that distinction exists. EventBridge also has built-in **schema discovery** (it can infer and register the structure of events flowing through it) and a rich set of native integrations with AWS services as both event sources and targets, plus **scheduled rules** for running something on a cron-like schedule without a separate scheduler.

### Matching the messaging pattern to the problem

| Scenario | Right service |
|---|---|
| One producer, one type of consumer, need a durable buffer | SQS |
| One event needs to reach several independent subscribers | SNS (fan-out with SQS for durability) |
| Routing needs to depend on the event's actual content, or the source is an AWS service/SaaS partner | EventBridge |
| Kitchen tickets that must process strictly in order | SQS FIFO |

## Putting It Together: The Café's Order Pipeline

The café's order flow becomes: the ordering service writes the order and publishes one event to an SNS topic. That topic fans out to three SQS queues — kitchen display, inventory, and email — each processed independently, each durable if its consumer is briefly unavailable. Separately, EventBridge watches for orders above a value threshold and routes those to a fraud-review workflow, using the same order event but a rule the ordering service never had to know about. One order, one publish — and the pieces that react to it can change, grow, or briefly go offline, without ever taking the customer's checkout down with them.

## What to skip

You don't need to hand-write SQS consumer polling loops, memorize EventBridge's exact JSON rule-pattern syntax, or size SNS delivery retry policies precisely — that's implementation depth beyond the associate exam. What matters is recognizing *why* a scenario calls for decoupling at all, and picking the right one of SQS, SNS, or EventBridge for the shape of that specific messaging problem.

## Key takeaways

- SQS decouples a producer from a consumer with a durable queue — standard queues favor throughput, FIFO queues favor strict ordering and exactly-once processing.
- A visibility timeout keeps two consumers from processing the same message at once; a dead-letter queue catches messages that keep failing instead of looping forever.
- SNS is pub/sub — one publish reaches every current topic subscriber, with no need for the publisher to know who they are.
- Fan-out (SNS publishing to multiple SQS queues) combines SNS's broadcast with SQS's durability — the standard pattern for "one event, several independent downstream systems."
- EventBridge adds content-based routing rules, schema discovery, and native AWS/SaaS integrations on top of pub/sub — reach for it when routing depends on what's *in* the event, not just who's subscribed.

## Further reading

- [Amazon SQS Developer Guide](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) — visibility timeout and dead-letter queues in full detail.
- [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) — fan-out pattern walkthrough.
- [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) — rules, schema registry, and scheduled events.

---

**Next:** [Module 14 — Building Serverless Architectures and Microservices](14-building-serverless-architectures-and-microservices.md)
