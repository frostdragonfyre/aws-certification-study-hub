<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](13-building-decoupled-architectures.md) · [Next module](15-data-engineering-patterns.md) · [Quiz](../quizzes/14-building-serverless-architectures-and-microservices-quiz.md) · [Slides](../lectures/14-building-serverless-architectures-and-microservices.pptx)
<!-- /hub-navigation -->

# Module 14: Building Serverless Architectures and Microservices

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

The café's new loyalty-points service is small: when an order's SQS message arrives, look up the customer, add points, done. Running a whole EC2 Auto Scaling group — provisioned, patched, and paid for 24/7 — for a service that does a few milliseconds of work each time an order comes in is a lot of standing infrastructure for a genuinely small job. Most of the time, it would sit there doing nothing at all, and Nikhil would still be paying for it and patching it.

This module is about **serverless**: running code without provisioning or managing servers at all, paying only for the compute you actually use, and building a system out of small, independently deployable **microservices** rather than one large application.

## Learning objectives

By the end of this module, you should be able to:

- Explain what AWS Lambda does and what "serverless" actually means
- Describe how Lambda is triggered and what its execution limits are
- Explain what Amazon API Gateway does and how it fronts a serverless API
- Explain what AWS Step Functions does and why orchestration matters for multi-step workflows
- Describe the microservices pattern and how it relates to the decoupling from Module 13

---

## AWS Lambda: Running Code Without Servers

**AWS Lambda** runs your code in response to an event, without you provisioning, patching, or scaling any server yourself. You upload a function — a small piece of code — and Lambda handles everything underneath it: provisioning the execution environment, scaling automatically from zero to thousands of concurrent invocations, and tearing it back down when there's nothing to do.

You pay only for what you use: compute time billed in fine-grained increments for the exact duration of each invocation, and nothing at all while the function isn't running. For the loyalty-points service — small, bursty, event-driven — this is a direct fit: no idle EC2 instances waiting for the next order.

### Triggers

Lambda functions are **event-driven** — something has to invoke them. Common triggers include an SQS queue receiving a message (exactly the loyalty-points case), an S3 upload, an API Gateway request, an SNS notification, or a scheduled EventBridge rule. The function doesn't run on its own schedule by default; it runs *because something happened*.

### Execution limits

Lambda isn't a fit for everything, and the exam tests this directly:

- **Maximum execution time:** 15 minutes per invocation. A long-running batch job or a multi-hour data processing task doesn't fit inside a single Lambda invocation.
- **Cold starts:** the first invocation after a period of inactivity can take noticeably longer, because Lambda has to initialize a new execution environment before your code runs. Subsequent invocations, while that environment stays warm, are fast.
- **Stateless by design:** each invocation should be treated as independent — Lambda doesn't guarantee the same underlying execution environment (or anything cached in memory there) will still be around for the next invocation.

> ⚠️ **Exam trap:** "we need to process a 3-hour video transcoding job" is not a Lambda scenario — the 15-minute hard limit rules it out regardless of how appealing "serverless" sounds otherwise. Look for a compute option built for long-running work instead.

## Amazon API Gateway: The Front Door for an API

Lambda functions don't have a URL of their own by default. **Amazon API Gateway** is a managed service for creating, publishing, and securing APIs — it's commonly placed in front of a set of Lambda functions, giving external clients (the café's mobile app, a partner's system) a real HTTP endpoint to call, while API Gateway routes each request to the right Lambda function behind it.

API Gateway also handles the concerns that come with exposing an API publicly: request throttling to protect the backend from being overwhelmed, authorization (checking who's allowed to call which endpoint), request/response transformation, and detailed logging and monitoring of every call — without any of that needing to be built into the Lambda functions themselves.

> ⚠️ **Exam trap:** don't confuse API Gateway with the Application Load Balancer from Module 10. An ALB distributes traffic across a fleet of servers (EC2 instances, containers) that are already running. API Gateway is the front door specifically for building and managing an API — commonly (though not exclusively) in front of Lambda — with API-specific features like throttling and request transformation that an ALB doesn't provide.

## AWS Step Functions: Orchestrating Multi-Step Workflows

A single Lambda function is great for one small job. But finalizing an order is really several steps that have to happen *in a specific sequence*, with real decisions and error handling along the way: confirm payment, then apply loyalty points, then generate a receipt — and if applying loyalty points fails, don't generate a receipt that claims points that were never actually awarded.

**AWS Step Functions** lets you define that sequence as a **state machine** — a visual, declarative workflow made up of steps (states), each of which can call a Lambda function or another AWS service, branch based on a condition, retry automatically on failure, or run steps in parallel. Instead of writing that sequencing and error-handling logic by hand inside one large Lambda function (or worse, scattered across several with no central view of the process), Step Functions manages the flow explicitly, and you can see exactly which step a given execution is on or where it failed.

### Why orchestration matters here specifically

Without Step Functions, chaining "Lambda A calls Lambda B calls Lambda C" means each function has to know about the next one, and retry/error logic gets duplicated or missed in each one individually. Step Functions centralizes that: each Lambda function stays small and focused on one job, and Step Functions owns the sequencing, retries, and failure paths between them.

### Matching the serverless building block to the problem

| Scenario | Right service |
|---|---|
| Run code in response to one event, no server management | Lambda |
| Give external clients an HTTP endpoint in front of Lambda | API Gateway |
| A multi-step process needs sequencing, branching, or retries across several calls | Step Functions |
| A job genuinely needs to run longer than 15 minutes | Not Lambda — a different compute option |

## Microservices: Small, Independent, Deployable on Their Own

**Microservices** is an architectural style: instead of one large application where every feature is bundled together and deployed as a single unit, the system is built as a set of small, independent services, each responsible for one piece of functionality, each deployable and scalable on its own. The loyalty-points service is a microservice — it doesn't know or care how the kitchen-display or inventory services are built, deployed, or scaled, only that it can read order events from its own queue.

This connects directly back to Module 13's decoupling: microservices are what fan-out, queues, and event buses are decoupling *between*. A monolith deployed as one unit doesn't need SQS or SNS internally, because everything already runs in the same process. Independent microservices, each communicating over messaging rather than direct calls, are exactly the shape of system that needs the patterns from Module 13 to hold together.

## Putting It Together: The Café's Serverless Loyalty Service

The loyalty-points service becomes: an SQS queue (from the Module 13 fan-out) triggers a Lambda function that adds points to the customer's account — no servers to provision or patch, scaling automatically with order volume, and costing nothing when there are no orders to process. A Step Functions workflow orchestrates the broader post-payment sequence — confirm payment, apply loyalty points, generate a receipt — with retries and clear failure handling at each step. And if the café later exposes an "order status" API for its mobile app, API Gateway sits in front of a Lambda function that looks up the order, without provisioning a single server for it.

## What to skip

You don't need to hand-write a Step Functions state machine's full JSON definition, memorize Lambda's exact memory-to-CPU allocation curve, or configure API Gateway's request-transformation mapping templates line by line — that's implementation depth beyond the associate exam. What matters is recognizing when a workload fits serverless at all, and which of Lambda, API Gateway, or Step Functions solves which part of the problem.

## Key takeaways

- Lambda runs code in response to events without server management, billed only for actual execution time — but it's capped at 15 minutes per invocation, which rules out long-running jobs.
- API Gateway is the managed front door for an API, commonly in front of Lambda, handling throttling, authorization, and request/response transformation — distinct from an ALB, which load-balances traffic across already-running servers.
- Step Functions orchestrates multi-step workflows as a state machine, centralizing sequencing, branching, and retry logic instead of chaining Lambda functions together by hand.
- Microservices break a system into small, independently deployable services — exactly the shape of architecture that Module 13's queues and event buses are built to decouple.
- The right question isn't "should this be serverless?" in the abstract — it's whether the specific workload's duration, triggers, and orchestration needs actually fit Lambda, API Gateway, and Step Functions.

## Further reading

- [AWS Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) — triggers, execution limits, and cold starts in full detail.
- [Amazon API Gateway Developer Guide](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) — REST vs. HTTP APIs, throttling, and authorization.
- [AWS Step Functions Developer Guide](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) — state machine concepts and error handling patterns.

---

**Next:** [Module 15 — Data Engineering Patterns](15-data-engineering-patterns.md)
