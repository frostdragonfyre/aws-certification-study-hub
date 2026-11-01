[Course index](../README.md) · [Read the paired lesson](../modules/14-building-serverless-architectures-and-microservices.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 14 Knowledge Check**

Building Serverless Architectures and Microservices · 20 questions · Practice — not graded

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

> AWS Lambda requires you to provision and patch the underlying servers your code runs on.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service runs your code in response to an event, without you managing any servers?
>
> **A.** EC2
> **B.** Lambda
> **C.** API Gateway
> **D.** Step Functions

**3. [Fill in the Blank] Easy**

> The first invocation after a period of inactivity, which can take noticeably longer while Lambda initializes a new execution environment, is called a ____________ start.

**4. [Multiple Choice] Easy**

> What is the maximum execution time for a single AWS Lambda invocation?
>
> **A.** 5 minutes
> **B.** 15 minutes
> **C.** 1 hour
> **D.** Unlimited

**5. [True / False] Easy**

> Lambda functions should be treated as stateless, since the same underlying execution environment isn't guaranteed to persist between invocations.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which service is commonly placed in front of a set of Lambda functions to give external clients a real HTTP endpoint to call?
>
> **A.** Application Load Balancer
> **B.** API Gateway
> **C.** Step Functions
> **D.** EventBridge

**7. [Fill in the Blank] Moderate**

> Something must ____________ a Lambda function for it to run — it doesn't execute on its own schedule by default.

**8. [Multiple Choice] Moderate**

> What does AWS Step Functions centralize that manually chaining Lambda functions together doesn't handle well?
>
> **A.** Compute pricing
> **B.** Sequencing, branching, and retry logic across multiple steps
> **C.** HTTP request routing
> **D.** Server patching schedules

**9. [True / False] Moderate**

> An Application Load Balancer and Amazon API Gateway provide identical functionality.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What billing model does AWS Lambda use?
>
> **A.** A flat monthly fee regardless of usage
> **B.** Pay only for the actual compute time used during execution
> **C.** Pay per server provisioned
> **D.** Pay per API call, regardless of how long it runs

**11. [Fill in the Blank] Moderate**

> An architectural style where a system is built as a set of small, independent, individually deployable services is called ____________.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> The café's loyalty-points service does a few milliseconds of work whenever an order's SQS message arrives, and sits idle the rest of the time. What's the best fit?
>
> **A.** An EC2 Auto Scaling group running 24/7
> **B.** A Lambda function triggered by the queue
> **C.** Step Functions on its own, with no compute service behind it
> **D.** An Application Load Balancer

**13. [Scenario / Judgment] Hard**

> A team needs to run a 3-hour video transcoding job. What's the best fit?
>
> **A.** AWS Lambda
> **B.** A compute option built for long-running work — not Lambda
> **C.** Amazon API Gateway
> **D.** Step Functions with no compute service behind it

**14. [Scenario / Judgment] Hard**

> The café's mobile app needs a real HTTP endpoint it can call to look up order status, backed by a Lambda function. What's the best fit?
>
> **A.** An Application Load Balancer alone
> **B.** API Gateway in front of the Lambda function
> **C.** Step Functions alone
> **D.** An SQS queue

**15. [Scenario / Judgment] Hard**

> Finalizing an order requires three steps in order — confirm payment, then apply loyalty points, then generate a receipt — with retries, and no receipt should ever be generated if applying loyalty points fails. What's the best fit?
>
> **A.** One large Lambda function doing all three steps with no orchestration or retry logic
> **B.** A Step Functions state machine orchestrating each step, with retries and failure handling built in
> **C.** An SNS fan-out to three unrelated subscribers
> **D.** DAX in front of the order table

**16. [Scenario / Judgment] Hard**

> A team chains Lambda A → Lambda B → Lambda C by having each function directly invoke the next, with retry logic duplicated in each one. What's the design problem, and the fix?
>
> **A.** No problem — this is a recommended best practice
> **B.** The sequencing and retry logic are duplicated and tightly coupled across functions; a Step Functions state machine should own that orchestration instead
> **C.** They should replace this with API Gateway
> **D.** They should merge all three into a single large Lambda function

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Microservices don't need decoupling patterns like queues — that's a separate topic." Correct this using this module's content.
>
> **A.** They're right — the two are unrelated
> **B.** Microservices are exactly what Module 13's decoupling patterns (queues, topics, event buses) operate between — independent services communicating over messaging need those patterns in a way a single monolith running in one process never did
> **C.** Microservices make SQS and SNS unnecessary
> **D.** Microservices only work when EventBridge is involved

**18. [Scenario / Judgment] Very Hard**

> Connect this module to Module 13. A fan-out pattern delivers an order event to independent SQS queues, and each queue now triggers its own Lambda function. What's the combined benefit of using both patterns together?
>
> **A.** There's no added benefit over using either pattern alone
> **B.** Each downstream Lambda function scales and fails independently and costs nothing while idle; decoupling determines how events reach each service, while serverless determines how each service actually runs without managed infrastructure
> **C.** This combination is only useful for the kitchen-display system specifically
> **D.** Adding Lambda removes the need for the SNS topic entirely

**19. [Scenario / Judgment] Very Hard**

> A design places API Gateway directly in front of a fleet of long-running EC2 instances that were already load-balanced by an Application Load Balancer, removing the ALB entirely on the assumption the two are interchangeable. What's the flaw?
>
> **A.** There is no flaw — they are fully interchangeable
> **B.** API Gateway is built for managing and securing APIs — throttling, authorization, request transformation — not for general-purpose load balancing across a fleet of already-running servers; the two solve different problems and aren't simply interchangeable
> **C.** An ALB cannot work with EC2 instances
> **D.** API Gateway cannot integrate with Lambda, so this design is impossible

**20. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since Lambda is serverless, every workload should move to it for the cost savings." Argue against this using this module's content.
>
> **A.** Agree — Lambda is always cheaper regardless of workload
> **B.** Whether Lambda fits depends on execution duration, invocation pattern, and orchestration needs — a workload exceeding the 15-minute limit, or requiring long-running or persistent processes, doesn't fit Lambda no matter how appealing "no servers to manage" sounds in the abstract
> **C.** Lambda has no execution time limits, so this is always true
> **D.** Serverless is purely a cost question and never a fit question

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
