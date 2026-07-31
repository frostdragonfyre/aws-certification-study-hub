# Module 6: Compute

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 3 — Cloud Technology and Services
**Estimated study time:** 45 minutes

## Why this matters

Compute is where your code actually runs, and it's the service family most people picture first when they hear "cloud." But AWS offers compute along a real spectrum — from "you manage the server" all the way to "there is no server for you to think about at all" — and the exam consistently tests whether you can match a scenario to the right point on that spectrum, not just recognize service names.

This module builds that spectrum piece by piece: Amazon EC2 (you manage the server), containers (a lighter-weight way to package and run applications), AWS Lambda (no server at all), and the services that tie compute together — Elastic Load Balancing and a first look at Auto Scaling. Module 10 comes back to Auto Scaling and monitoring in more depth; this module is about knowing where each compute option sits on the spectrum and why you'd reach for it.

## Learning objectives

By the end of this module, you should be able to:

- Describe Amazon EC2 and explain what "instance type" means
- Distinguish the major EC2 purchasing options and when each fits
- Explain what a container is and how ECS, EKS, and Fargate relate to each other
- Describe AWS Lambda and identify serverless-shaped scenarios
- Describe AWS Elastic Beanstalk and when it's the right level of abstraction
- Explain what Elastic Load Balancing does and why it pairs with Auto Scaling
- Avoid the most common compute traps on the exam

---

## Amazon EC2: Virtual Servers in the Cloud

**Amazon EC2 (Elastic Compute Cloud)** provides resizable virtual servers, called **instances**, that you configure and manage — the most flexible, most hands-on point on the compute spectrum. You choose the operating system, install your own software, and are responsible for patching and securing the guest OS (the customer's side of the Shared Responsibility Model from Module 4).

Every EC2 instance has an **instance type**, which determines its combination of CPU, memory, storage, and networking capacity. Instance types are grouped into families optimized for different workloads:

| Family | Optimized for | Example use case |
|---|---|---|
| General purpose | Balanced compute, memory, networking | Web servers, small databases |
| Compute optimized | High-performance processors | Batch processing, gaming servers, scientific modeling |
| Memory optimized | Fast performance for large datasets in memory | In-memory databases, real-time big data analytics |
| Storage optimized | High, sequential read/write access to large datasets | Data warehousing, distributed file systems |

> ⚠️ **Exam trap:** a scenario naming a specific bottleneck — "needs more RAM," "needs faster processors" — is pointing at an instance family, not a purchasing option. Keep "what kind of instance" and "how do I pay for it" as two separate questions.

## EC2 Purchasing Options

How you pay for EC2 is a separate decision from which instance type you pick, and this table was previewed in Module 2 — here it is in full:

| Option | Best for | Trade-off |
|---|---|---|
| On-Demand | Short-term, unpredictable workloads | Highest price per hour, zero commitment |
| Reserved Instances | Steady-state, predictable usage (1 or 3 years) | Deep discount, tied to a specific instance type/family/Region |
| Savings Plans | Steady-state usage, more flexibility | Deep discount, commits to a $/hour spend rather than a specific instance type |
| Spot Instances | Flexible, interruptible workloads | Steepest discount, AWS can reclaim the instance with short notice |

> ⚠️ **Exam trap:** "can be interrupted, cost is the top priority" is Spot. "Steady, predictable, and running 24/7 for a year or more" is Reserved or Savings Plans. On-Demand is the default when a scenario doesn't describe a steady, long-term pattern.

## Containers: A Lighter Way to Package Applications

A **container** packages an application with everything it needs to run — code, runtime, libraries — so it behaves consistently across environments. Containers are lighter weight than running a full virtual machine for each application, since multiple containers can share the same underlying OS kernel.

AWS offers three related container services, and the exam expects you to know how they relate:

| Service | What it is |
|---|---|
| **Amazon ECS** (Elastic Container Service) | AWS's own container orchestration service — manages where and how containers run |
| **Amazon EKS** (Elastic Kubernetes Service) | A managed service for running Kubernetes, the popular open-source container orchestration standard, on AWS |
| **AWS Fargate** | A serverless compute *engine* for containers — runs ECS or EKS containers without you provisioning or managing any underlying EC2 instances |

> ⚠️ **Exam trap:** ECS and EKS are orchestrators — they decide *how* containers are scheduled and run. Fargate is not a third orchestrator competing with them; it's a way to *run* ECS or EKS workloads without managing servers. "Containers, but I don't want to manage any EC2 instances" is Fargate layered on top of ECS or EKS, not a replacement for either.

## AWS Lambda: No Server to Think About

**AWS Lambda** runs your code in response to events — an uploaded file, an API call, a scheduled time — without you provisioning or managing any server at all. This is true **serverless** compute: there's no instance to patch, no capacity to plan, and you're billed only for the compute time your code actually uses, down to the millisecond.

The exam cue for Lambda is short-lived, event-driven, unpredictable-but-bursty workloads: a function that resizes an image the moment it's uploaded to S3, or one that runs a scheduled cleanup job once a night.

> ⚠️ **Exam trap:** Lambda is for short-duration tasks, not long-running applications. A workload that needs to run continuously for hours, or needs a persistent connection, is an EC2 or container scenario — not Lambda. "Runs in response to an event, finishes quickly" is the Lambda shape.

## AWS Elastic Beanstalk: A Middle Ground

**AWS Elastic Beanstalk** is a platform-as-a-service (PaaS) offering: you upload your application code, and Elastic Beanstalk automatically handles the deployment — provisioning EC2 instances, load balancing, and Auto Scaling — while still giving you access to the underlying resources if you need them.

Think of Elastic Beanstalk as sitting between EC2 (full control, full responsibility) and Lambda (no infrastructure at all, but a specific event-driven shape). It's the answer for "I want to deploy a traditional web application quickly, without hand-configuring every piece of infrastructure myself."

## Elastic Load Balancing and a First Look at Auto Scaling

Two services almost always get mentioned together with EC2 fleets:

- **Elastic Load Balancing (ELB)** automatically distributes incoming application traffic across multiple targets — EC2 instances, containers, or Lambda functions — in one or more Availability Zones, improving both fault tolerance and availability.
- **AWS Auto Scaling** automatically adjusts compute capacity — adding instances when demand rises, removing them when it falls — to maintain performance while controlling cost. Module 10 covers this in depth, including how it works with Amazon CloudWatch metrics.

These two typically work as a pair: Auto Scaling changes *how many* instances exist, and the load balancer keeps traffic spread evenly across *however many* there currently are.

> ⚠️ **Exam trap:** "distributes traffic across instances" is ELB. "Changes the number of instances" is Auto Scaling. They're frequently named together in the same scenario because they solve complementary problems, not because they're the same service.

## Putting the Compute Spectrum Together

A useful way to hold all of this: compute options run from full control to zero infrastructure.

1. **EC2** — you manage the OS, patches, and configuration; maximum control.
2. **Containers (ECS/EKS, optionally on Fargate)** — lighter-weight packaging; Fargate removes server management entirely for containers.
3. **Elastic Beanstalk** — upload code, AWS handles the deployment infrastructure, but it's still built on EC2 underneath.
4. **Lambda** — no server at all, event-driven, billed by the millisecond.

Every exam scenario in this domain is really asking: given this workload's shape, where on that spectrum does it belong?

---

## What to skip

You don't need to write a Dockerfile, configure a Kubernetes deployment YAML, or memorize exact instance-type specs — that hands-on depth belongs to the Solutions Architect Associate exam. For Cloud Practitioner, focus on matching a workload's shape (steady vs. bursty, long-running vs. event-driven, needs control vs. wants simplicity) to the right compute option.

## Key takeaways

- EC2 instance *type* (the hardware profile) and EC2 purchasing *option* (how you pay) are two separate decisions — don't conflate them.
- On-Demand is flexible and default; Reserved Instances and Savings Plans reward steady, predictable usage; Spot Instances trade interruptibility for the deepest discount.
- ECS and EKS are container orchestrators; Fargate is a serverless way to *run* either one without managing EC2 instances underneath.
- Lambda is true serverless compute — no infrastructure, billed by the millisecond, best suited to short, event-driven tasks.
- Elastic Beanstalk sits between EC2 and Lambda — upload code, AWS handles the deployment infrastructure automatically.
- Elastic Load Balancing distributes traffic across existing capacity; Auto Scaling changes how much capacity exists — complementary jobs, not the same service.

## Further reading

- [Amazon EC2](https://aws.amazon.com/ec2/) — instance types, pricing options, and getting-started guides.
- [Amazon ECS](https://aws.amazon.com/ecs/), [Amazon EKS](https://aws.amazon.com/eks/), and [AWS Fargate](https://aws.amazon.com/fargate/) — for comparing the three container services directly.
- [AWS Lambda](https://aws.amazon.com/lambda/) — serverless compute overview and common use cases.
- [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/) — PaaS deployment overview.

*Service capabilities mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 5 — Networking and Content Delivery](05-networking-and-content-delivery.md) · **Next:** [Module 7 — Storage](07-storage.md) · **Quiz:** [Module 6 Quiz](../quizzes/06-compute-quiz.md) · **Activity:** [Module 6 Activity](../labs/06-compute-activity.md)
