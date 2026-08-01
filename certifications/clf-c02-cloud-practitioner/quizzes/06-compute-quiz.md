**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 6 Review Quiz**

Compute · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|
| | |

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

> An EC2 instance type determines its combination of CPU, memory, storage, and networking capacity.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which EC2 purchasing option is best for short-term, unpredictable workloads with no commitment?
>
> **A.** Reserved Instances
> **B.** On-Demand
> **C.** Savings Plans
> **D.** Spot Instances

**3. [Fill in the Blank] Easy**

> A ____________ packages an application with its code, runtime, and libraries so it runs consistently across environments.

**4. [Multiple Choice] Easy**

> Which service runs code in response to events with no server for you to manage?
>
> **A.** Amazon EC2
> **B.** Amazon ECS
> **C.** AWS Lambda
> **D.** AWS Elastic Beanstalk

**5. [True / False] Easy**

> AWS Fargate is a third container orchestrator, competing directly with ECS and EKS.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which EC2 purchasing option offers the steepest discount, but can be interrupted by AWS with short notice?
>
> **A.** On-Demand
> **B.** Reserved Instances
> **C.** Savings Plans
> **D.** Spot Instances

**7. [Fill in the Blank] Moderate**

> Amazon ____________ is AWS's own container orchestration service.

**8. [Multiple Choice] Moderate**

> Which service is a managed service for running Kubernetes on AWS?
>
> **A.** Amazon ECS
> **B.** Amazon EKS
> **C.** AWS Fargate
> **D.** AWS Lambda

**9. [True / False] Moderate**

> Elastic Load Balancing changes how many EC2 instances exist; Auto Scaling distributes traffic across them.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which service lets you upload application code and have AWS automatically handle the deployment infrastructure?
>
> **A.** Amazon EC2
> **B.** AWS Lambda
> **C.** AWS Elastic Beanstalk
> **D.** Amazon ECS

**11. [Fill in the Blank] Moderate**

> Reserved Instances commit to a specific instance type, family, and Region; ____________ commit to a dollar-per-hour spend instead, with more flexibility.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A company needs more RAM for an in-memory database running on EC2. What should they change?
>
> **A.** The purchasing option
> **B.** The instance type or family
> **C.** The container orchestrator
> **D.** A Lambda memory setting

**13. [Scenario / Judgment] Hard**

> A workload can be interrupted with short notice, and cost is the top priority. Which purchasing option fits best?
>
> **A.** On-Demand
> **B.** Reserved Instances
> **C.** Savings Plans
> **D.** Spot Instances

**14. [Scenario / Judgment] Hard**

> A team wants to run containers in production but never wants to provision or manage an EC2 instance. What's the best fix?
>
> **A.** Use EC2 directly, but automate the setup
> **B.** Run ECS or EKS on AWS Fargate
> **C.** Use AWS Lambda instead of containers
> **D.** Use AWS Elastic Beanstalk instead

**15. [Scenario / Judgment] Hard**

> A piece of code needs to run continuously for hours and hold a persistent connection. Is this a good Lambda scenario?
>
> **A.** Yes — Lambda handles any workload equally well
> **B.** No — Lambda is built for short, event-driven tasks; this belongs on EC2 or containers
> **C.** Yes, as long as it's billed by the millisecond
> **D.** No, this specifically requires Reserved Instances

**16. [Scenario / Judgment] Hard**

> A service needs incoming traffic spread evenly across a fleet of EC2 instances. Which service provides this?
>
> **A.** AWS Auto Scaling
> **B.** Elastic Load Balancing
> **C.** AWS Lambda
> **D.** AWS Elastic Beanstalk

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A company buys a Reserved Instance in the wrong instance family for a memory-heavy workload, and blames the purchasing option for poor performance. What's the actual fix?
>
> **A.** Cancel the Reserved Instance and switch to Spot
> **B.** The purchasing option isn't the problem — pick a memory-optimized instance type or family, independent of which payment plan was chosen
> **C.** Migrate the workload to AWS Lambda
> **D.** Use Elastic Beanstalk to automatically fix instance sizing

**18. [Scenario / Judgment] Very Hard**

> A company has three needs: (1) full OS control for a legacy application, (2) containers with zero server management, and (3) a function that fires on file upload and exits quickly. In order, which services match?
>
> **A.** EC2, Fargate, Lambda
> **B.** Lambda, EC2, Fargate
> **C.** Fargate, Lambda, EC2
> **D.** EC2, Lambda, Fargate

**19. [Scenario / Judgment] Very Hard**

> A team already knows Kubernetes and wants to bring that same tooling to AWS while avoiding EC2 management entirely. What's the best combination?
>
> **A.** Amazon ECS alone
> **B.** Amazon EKS running on AWS Fargate
> **C.** AWS Lambda
> **D.** AWS Elastic Beanstalk

**20. [Scenario / Judgment] Very Hard**

> A production application runs on a single EC2 instance, and traffic is growing and unpredictable. What's the risk, and the standard fix?
>
> **A.** No risk — EC2 always scales automatically on its own
> **B.** One instance is a single point of failure and can't absorb traffic spikes; pair Elastic Load Balancing with Auto Scaling
> **C.** Switch immediately to AWS Lambda
> **D.** Nothing needs to change, since EC2 is a managed service

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
