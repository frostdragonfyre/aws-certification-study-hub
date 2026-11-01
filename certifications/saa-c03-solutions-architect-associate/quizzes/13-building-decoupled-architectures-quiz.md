[Course index](../README.md) · [Read the paired lesson](../modules/13-building-decoupled-architectures.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 13 Knowledge Check**

Building Decoupled Architectures · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|

*Instructions: Answer every question. Questions get harder as you go — the last several are exam-style judgment questions where more than one answer looks reasonable. For those, pick the BEST answer and be ready to defend it out loud.*

| **Question types** | **What to do** |
|---|---|
| Multiple Choice | Circle one letter. |
| True / False | Circle TRUE or FALSE. |
| Fill in the Blank | Write your answer on the line. |
| Scenario / Judgment | Circle the BEST answer. Note WHY the others fail. |

---

## Easy Questions

**1. [True / False] Easy**

> Amazon SQS decouples a producer from a consumer by letting the producer place a message on a queue instead of calling the consumer directly.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service is built around a publish/subscribe model using topics?
>
> **A.** SQS
> **B.** EventBridge
> **C.** SNS
> **D.** DAX

**3. [Fill in the Blank] Easy**

> A message that keeps failing processing after repeated retries is routed to a ____________ queue instead of looping forever.

**4. [Multiple Choice] Easy**

> Which SQS queue type guarantees strict message ordering and exactly-once processing?
>
> **A.** Standard
> **B.** FIFO
> **C.** Dead-letter
> **D.** Delay queue

**5. [True / False] Easy**

> Every subscriber to an SNS topic must be an SQS queue.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What prevents two different consumers from processing the same SQS message at the same time?
>
> **A.** Visibility timeout
> **B.** Dead-letter queue
> **C.** FIFO ordering
> **D.** Topic subscription

**7. [Fill in the Blank] Moderate**

> The pattern where one SNS topic publishes to several independent SQS queues, one per downstream system, is called ____________.

**8. [Multiple Choice] Moderate**

> Which of the following is TRUE about EventBridge compared to SNS?
>
> **A.** They are functionally identical
> **B.** EventBridge can route events based on their content using rules; SNS delivers to every current topic subscriber
> **C.** SNS supports schema discovery and EventBridge does not
> **D.** EventBridge fully replaced SNS and SNS is deprecated

**9. [True / False] Moderate**

> A standard SQS queue guarantees that every message is delivered exactly once.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> In a queue-based architecture, what does the producer do?
>
> **A.** Reads and deletes messages
> **B.** Places a message onto the queue
> **C.** Subscribes to a topic
> **D.** Defines EventBridge rules

**11. [Fill in the Blank] Moderate**

> The window during which a picked-up SQS message is hidden from other consumers, so it isn't processed twice, is called the ____________ ____________.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A single café order needs to reach the kitchen display, the inventory service, and the email notifier — all independently, all reliably. What's the best fit?
>
> **A.** A single SQS queue shared by all three
> **B.** SNS alone, with each system as an HTTP subscriber
> **C.** Fan-out — SNS publishing to a separate SQS queue per subscriber
> **D.** An EventBridge scheduled rule

**13. [Scenario / Judgment] Hard**

> Kitchen order tickets must come out in the exact order they were placed. What's the best fit?
>
> **A.** Standard SQS queue
> **B.** FIFO SQS queue
> **C.** SNS topic
> **D.** EventBridge with no ordering configuration

**14. [Scenario / Judgment] Hard**

> Orders over $100 need to be routed to a fraud-review workflow, based on the order total inside the event itself, without the ordering service knowing that rule exists. What's the best fit?
>
> **A.** An SNS topic with every subscriber getting every message
> **B.** A standard SQS queue
> **C.** An EventBridge rule matching on the event's content
> **D.** A FIFO queue

**15. [Scenario / Judgment] Hard**

> The kitchen-display consumer is briefly offline for a redeploy. Orders must not be lost while it's down. What property makes this safe?
>
> **A.** SNS delivers instantly no matter what
> **B.** SQS retains messages durably until a consumer is available to process them
> **C.** EventBridge retries every delivery forever, automatically
> **D.** The visibility timeout deletes unprocessed messages

**16. [Scenario / Judgment] Hard**

> A team notices the same order is being processed twice by their SQS consumer. What's the most likely cause and fix?
>
> **A.** The visibility timeout is too short for how long processing actually takes, or the consumer isn't deleting the message in time — lengthen the timeout or fix the delete logic
> **B.** Switch from SQS to SNS to fix duplicate processing
> **C.** Add more subscribers to the topic
> **D.** Enable content-based filtering

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "SNS and SQS are basically the same service with different names." Correct this using this module's content.
>
> **A.** They're right — fully interchangeable
> **B.** They're not the same — SQS is a durable queue typically read by one type of consumer, while SNS is pub/sub, broadcasting one message to every current subscriber; the fan-out pattern combines both to get broadcast and durability together
> **C.** SNS has fully replaced SQS in modern architectures
> **D.** SQS only works with AWS-native event sources

**18. [Scenario / Judgment] Very Hard**

> Connect this module to Module 12. Caching reduces repeated work reaching an origin or database. What's the essential job decoupling does instead?
>
> **A.** It also caches data, just for messages instead of files
> **B.** It breaks a chain of dependent processing steps into independent pieces, so a slowdown or failure in one piece doesn't cascade into failing or blocking the whole request
> **C.** Decoupling and caching solve the exact same problem
> **D.** Decoupling only applies to database queries

**19. [Scenario / Judgment] Very Hard**

> A design publishes order events to an SNS topic with HTTP endpoints as the only subscribers — no SQS queues involved. During a brief outage of one subscriber's server, some notifications are silently lost and never retried. What's missing from this design?
>
> **A.** Nothing — this is expected, normal behavior with no fix needed
> **B.** Durability — a plain HTTP subscriber has no built-in retry/durability the way a queue does; using the fan-out pattern (SNS publishing into an SQS queue for that subscriber) would have held the messages until it recovered
> **C.** SNS never loses messages regardless of subscriber type, so this couldn't happen
> **D.** Only EventBridge can prevent lost notifications, SNS cannot

**20. [Scenario / Judgment] Very Hard**

> A reviewer says "EventBridge is just SNS with a longer name — there's no real difference." Argue against this using this module's content.
>
> **A.** They're right, there's no meaningful difference
> **B.** EventBridge adds content-based rule filtering, schema discovery, and broad native integrations with AWS services and SaaS partners as both sources and targets — letting routing decisions depend on what's actually inside the event, not just who happens to be subscribed to a topic
> **C.** EventBridge cannot integrate with AWS services at all
> **D.** SNS already supports identical content-based filtering, so the two are the same

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
