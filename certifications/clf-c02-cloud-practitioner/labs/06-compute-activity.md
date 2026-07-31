**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 6**

**Lab Worksheet — Compute**

Activity 1: Match the Workload · Activity 2: Compute Service Hunt

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Match the Workload (20 min)

### How this works

Below is a list of workloads. For each one, place it on the compute spectrum — EC2, Containers (ECS/EKS, optionally on Fargate), Lambda, or Elastic Beanstalk. Work on your own first, then we'll build the spectrum together on the board.

*This is the single most tested skill in Domain 3's compute questions — matching a workload's shape to the right point on the spectrum, not just recognizing service names.*

### Place each workload

| # | Workload | Best fit |
|---|---|---|
| 1 | A backend job that runs continuously, 24/7, and needs full control over the OS | |
| 2 | A function that resizes an image the moment it's uploaded to S3, then stops | |
| 3 | A team wants to deploy a standard web app quickly, without hand-configuring servers or load balancers | |
| 4 | An application already packaged as a container, and the team is already standardized on Kubernetes | |
| 5 | A nightly cleanup script that runs once, does its job in a few seconds, and exits | |
| 6 | A containerized application where the team never wants to manage an EC2 instance | |

### Does the payment change the picture? (discuss as a class)

Look at #1 again — a steady, 24/7 backend job on EC2.

| Question | Your answer |
|---|---|
| Is this workload predictable or unpredictable? | |
| Which EC2 purchasing option rewards predictable, long-term usage with a deep discount? | |
| If this same workload could tolerate being interrupted with short notice, which purchasing option would save the most money instead? | |

### Think about it

1. Why is "runs continuously for hours" the detail that rules Lambda out, even if the task itself sounds simple?
2. ECS and EKS both orchestrate containers. What's the actual difference between them — and what does Fargate change about either one?
3. Give one example (not from the list above) of a workload that belongs on Elastic Beanstalk, and explain what makes it a better fit than raw EC2.

---

## Activity 2 — Compute Service Hunt (25 min)

### How this works

Work on your own. For each scenario, write which AWS compute service or purchasing option fits best — and UNDERLINE the exact phrase that gave it away. We'll go through the answers together as a class afterward.

*Same skill as the networking service hunt from Lecture 5: noticing which phrase is load-bearing is what the real exam question is testing.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the toolkit

| Service / Option | What it's for |
|---|---|
| Amazon EC2 | Configurable virtual servers — full control over the OS |
| On-Demand | Short-term, unpredictable usage, no commitment |
| Reserved Instances | Steady usage, 1–3 year commitment to a specific instance type |
| Savings Plans | Steady usage, 1–3 year commitment to a dollar-per-hour spend |
| Spot Instances | Flexible, interruptible workloads, steepest discount |
| Amazon ECS | AWS-native container orchestration |
| Amazon EKS | Managed Kubernetes on AWS |
| AWS Fargate | Serverless compute engine for ECS or EKS — no EC2 to manage |
| AWS Lambda | Runs code in response to events, no server, billed by the millisecond |
| AWS Elastic Beanstalk | Upload code, AWS handles deployment infrastructure |
| Elastic Load Balancing | Distributes traffic across existing instances |
| AWS Auto Scaling | Changes how many instances exist, based on demand |

### The scenarios

*Underline the deciding phrase in each scenario as you read it.*

| # | Scenario | Your answer |
|---|---|---|
| 1 | A company needs a memory-optimized virtual server to run an in-memory database, fully under their own control. | |
| 2 | A workload can be interrupted at any time with short notice, and cost savings is the top priority. | |
| 3 | An application will run steadily, 24/7, for the next three years, on a known instance type. | |
| 4 | A team wants containers running in production, but never wants to provision or patch an EC2 instance. | |
| 5 | A function needs to run the moment a file lands in an S3 bucket, finish in under a second, and then stop. | |
| 6 | A team wants to upload their application code and have AWS handle the servers, load balancer, and scaling automatically. | |
| 7 | A company needs traffic spread evenly across a fleet of EC2 instances. | |
| 8 | A company needs the number of running instances to grow during a traffic spike and shrink afterward. | |
| 9 | A team is already standardized on Kubernetes and wants to bring that same tooling to AWS. | |
| 10 | A company wants a discount for steady usage but doesn't want to commit to one specific instance type or family. | |

### Pick any two and go deeper

For two of the scenarios above, write out why the service you picked beats the next most tempting wrong answer.

**Scenario #____ — why this beats the tempting wrong answer:**

**Scenario #____ — why this beats the tempting wrong answer:**

### The shortcut — write this down

**For ANY AWS compute scenario on the exam, ask in this order:**

1. Is this about **full control** over the OS? → EC2.
2. Is this about **lighter packaging**, consistent across environments? → Containers — ECS or EKS, optionally on Fargate.
3. Is this about **zero infrastructure**, event-driven? → Lambda.
4. Is this about **deploying fast** without configuring infrastructure? → Elastic Beanstalk.
5. Is this about **spreading traffic**? → Elastic Load Balancing.
6. Is this about **capacity that grows and shrinks**? → AWS Auto Scaling.

*Notice the pattern: control, packaging, infrastructure, deployment, and traffic — five questions that resolve almost every compute scenario. Purchasing options (On-Demand, Reserved, Savings Plans, Spot) are a separate question layered on top, once you've already decided EC2 is the right compute choice.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Rewrite scenario 5 so the correct answer becomes EC2 instead of Lambda. What did you have to change? |
| 2 | Explain in your own words why Fargate isn't a "third orchestrator" alongside ECS and EKS. |
| 3 | Pick one EC2 purchasing option and explain, without notes, the specific trade-off it makes. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 6 + knowledge check (aim 80%+ first attempt) |
| | Sketch the compute spectrum from memory once, without looking at your notes |
| | Pick one compute service from tonight's toolkit and explain what it does in your own words, no notes |
