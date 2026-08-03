# Module 5: Adding a Compute Layer Using Amazon EC2

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 55 minutes

## Why this matters

Module 4 gave the café a place to put content. It didn't give the café a place to *run* anything. The moment Module 1's café scenario needed dynamic content and online ordering — code that actually processes an order, checks inventory, and responds differently to different requests — static hosting stopped being enough. This module is where the café's architecture gets somewhere to actually execute that code: Amazon EC2, the service most people picture first when they hear "cloud computing."

This module also introduces a pattern that recurs constantly at the Associate level: EC2 isn't one decision, it's several stacked decisions — which storage, which image, which instance type, which pricing model — and getting each one right independently is what separates "it runs" from "it's actually well-architected."

## Learning objectives

By the end of this module, you should be able to:

- Identify how Amazon EC2 can be used in an architecture
- Explain the value of using Amazon Machine Images (AMIs) to accelerate the creation and repeatability of infrastructure
- Recommend EC2 instance types based on requirements
- Recommend storage solutions for Amazon EC2
- Recognize how to configure EC2 instances with user data
- Describe EC2 pricing options and make recommendations based on cost
- Apply AWS Well-Architected Framework principles when designing a compute layer with Amazon EC2

---

## What Amazon EC2 Actually Is

**Amazon Elastic Compute Cloud (EC2)** provides resizable virtual servers — instances — that you configure, launch, and control much like a physical server, without owning or maintaining the underlying hardware. This is Infrastructure as a Service in its most direct form: you're responsible for the operating system, the runtime, the application, and its configuration; AWS is responsible for the physical hardware underneath, per the shared responsibility model you've now applied to several services in this course.

For the café, EC2 is where the actual online-ordering application runs — the code that receives a request, checks the menu and inventory, and returns a response. It's the layer S3 alone was never built to provide.

## Storage for EC2: Instance Store vs. Amazon EBS

Every EC2 instance needs somewhere to store its operating system and any data the running application needs — and AWS offers two genuinely different options, not two flavors of the same thing.

| Option | What it is | Best for |
|---|---|---|
| Instance store | Physically attached, temporary storage on the same host as the instance | Workloads needing very fast local storage and no persistence — data that's fine to lose if the instance stops |
| Amazon EBS | Network-attached, persistent block storage, independent of the instance's own lifecycle | Workloads needing data to survive an instance stop, reboot, or replacement |

The deciding question is simple: **does this data need to survive the instance itself?** If yes, use EBS. If the workload can tolerate losing that data — often because it's regenerated, cached, or replicated elsewhere — instance store's speed advantage becomes worth considering. The café's online ordering application, which needs its order records to persist no matter what happens to any single instance, is a clear EBS case; a short-lived processing job using purely temporary scratch space is a more plausible instance store case.

## Amazon Machine Images (AMIs): Repeatable Infrastructure

An **Amazon Machine Image (AMI)** is a template that includes everything needed to launch an instance: the operating system, any pre-installed software, and configuration settings. AMIs come in a few flavors:

- **Base AMIs** — provided by AWS, a clean starting operating system with nothing extra configured.
- **Preconfigured AMIs** — provided by AWS, AWS Marketplace vendors, or the community, with specific software already installed and ready to go.
- **Custom AMIs** — built by you, capturing an instance's exact state (OS, software, configuration) at a point in time, so it can be relaunched identically, as many times as needed.

The real value of an AMI is repeatability: instead of manually reconfiguring a fresh instance every single time, you configure it once, save it as a custom AMI, and launch identical instances from that image going forward. This is directly connected to Module 2's "automate wherever possible" best practice — an AMI turns a manual, error-prone setup process into a one-click, consistent launch.

## Choosing an Instance Type

EC2 instance types are grouped into families, each optimized for a different resource profile:

| Family | Optimized for | Typical use case |
|---|---|---|
| General purpose | A balance of compute, memory, and networking | Web servers, small-to-medium databases, general application workloads |
| Compute optimized | High-performance processors | Batch processing, high-performance web servers, scientific modeling |
| Memory optimized | Fast performance for memory-intensive workloads | Large in-memory databases, real-time big data analytics |
| Storage optimized | High, sequential read/write access to large local datasets | Data warehousing, distributed file systems |
| Accelerated computing | Hardware accelerators (GPUs and similar) | Machine learning, graphics processing, high-performance computing |

Within each family, instances also come in a range of **sizes** (like small, large, xlarge, 2xlarge), scaling the same balance of resources up or down. Choosing a type isn't about picking the "best" one in the abstract — it's about matching the family's resource profile to what the actual workload needs, then sizing within that family based on real demand.

> ⚠️ **Trap to know:** A scenario naming a specific workload characteristic — "processes large in-memory datasets," "runs GPU-accelerated model training," "needs high sequential disk throughput" — is telling you the instance family directly. Don't default to general purpose just because it sounds safe; the exam is testing whether you can match the profile.

## Configuring Instances with User Data

**User data** is a script you can attach to an instance at launch time, which runs automatically the first time the instance boots. This is how you turn a generic AMI into a specifically-configured, ready-to-serve instance without manual setup after launch — installing packages, pulling the latest application code, or applying configuration, all automatically, every time a new instance launches from that AMI. Combined with Auto Scaling (a service you'll revisit in more depth in Module 10), user data is what makes it possible for a newly launched instance to be fully functional the moment it comes online, with no human intervention.

## EC2 Pricing Options

EC2's pricing models exist because different workloads have fundamentally different commitment profiles, and matching the right model to the right workload is one of the most consistently tested decisions at this level.

| Pricing option | Commitment | Best for |
|---|---|---|
| On-Demand | None — pay by the second or hour, no upfront commitment | Unpredictable, short-term, or brand-new workloads you haven't sized yet |
| Reserved Instances | 1- or 3-year commitment to a specific instance configuration | Steady-state workloads with a well-understood, unchanging profile |
| Savings Plans | 1- or 3-year commitment to a consistent amount of compute usage (measured in $/hour) | Steady-state workloads where you want savings without locking in the exact instance configuration |
| Spot Instances | No commitment, but AWS can reclaim the instance with short notice | Fault-tolerant, flexible workloads that can handle interruption (batch jobs, some big data processing) |
| Dedicated Instances / Hosts | Physical hardware isolation for compliance or licensing needs | Regulatory requirements mandating dedicated physical hardware |

**Savings Plans deserve a closer look**, because the two flavors are easy to conflate and a favorite exam distinction:

- **Compute Savings Plans** offer the most flexibility — the commitment applies across instance families, sizes, Regions, and even compute services beyond EC2 (like Fargate and Lambda), but that flexibility costs you some savings compared to the more specific option.
- **EC2 Instance Savings Plans** commit to a specific instance family within a specific Region, in exchange for the deepest discount — and critically, you can still change the *instance size* within that family without losing the discount or breaking the commitment.

The decision between them comes down to how much flexibility the workload actually needs. A steady workload that will stay in the same instance family, just scaling up and down in size occasionally, gets the best price from an EC2 Instance Savings Plan — trading away flexibility it was never going to use anyway in exchange for the deepest discount available.

## A Worked Example: Matching Pricing to a Real Workload

Consider a workload that will run continuously for at least a year in the same Region, staying mostly steady except for occasional seasonal spikes — spikes handled by increasing the instance *size*, without ever changing the instance *family*. What's the lowest-cost way to purchase this?

Work through the pricing table above by elimination: Dedicated instances solve a compliance problem this workload doesn't have, at one of the highest price points — ruled out. On-Demand is the right choice for unpredictable or short-term needs, but this is a known, year-long, steady workload — paying On-Demand rates the whole time leaves real savings on the table. A Compute Savings Plan would work, since it covers this usage, but its cross-family flexibility isn't needed here and isn't the cheapest option available. An EC2 Instance Savings Plan fits exactly: the workload stays in the same instance family for the full commitment, size changes within that family don't affect the discount, and this is the pricing option built specifically to reward that kind of stable, predictable, single-family usage with its deepest discount.

The general lesson: when a scenario tells you the instance *family* stays fixed while only the *size* changes, that's a strong signal pointing toward an EC2 Instance Savings Plan over its more flexible (and more expensive) Compute Savings Plan sibling.

## Beyond EC2: Managed Compute Services

EC2 isn't AWS's only compute option, and it's worth knowing that a managed alternative sometimes fits better than configuring EC2 instances directly. **AWS Batch** runs batch computing jobs at any scale without you having to manage the underlying compute infrastructure yourself — you define the job, and AWS handles provisioning and scheduling. **AWS Outposts** extends AWS infrastructure, services, and tools to on-premises locations, for workloads that genuinely need to run on-premises but still want a consistent AWS operating model. Neither replaces EC2 for the café's core needs, but both are worth recognizing as options when a scenario's requirements point toward "less infrastructure management," not more.

## Applying the Well-Architected Framework to Compute

A handful of best practices, specific to the compute layer, recur constantly:

- **Automate compute protection** — don't rely on manual intervention to keep instances healthy.
- **Scale to the best compute option for the workload** — the right instance type and pricing model, not just "the one we already know."
- **Configure and right-size compute resources** — an oversized instance wastes money; an undersized one risks performance.
- **Select the correct resource type, size, and number** based on actual data, not assumption.
- **Select the best pricing model** for the workload's real commitment profile.
- **Use the minimum amount of hardware** needed to meet requirements — Module 2's "stop guessing capacity" principle, applied directly to compute.
- **Use instance types with the least environmental and performance impact** for the job at hand.

Notice how directly these map onto decisions already covered in this module — instance type selection, right-sizing, and pricing model choice aren't separate from the Well-Architected Framework; they *are* the Framework, applied specifically to compute.

---

## What to skip

You don't need to memorize every current instance type's exact vCPU and memory specifications, or current Reserved Instance and Savings Plan discount percentages — these numbers change regularly, and the exam tests the *decision logic* (which family, which pricing model, and why) rather than current specs. The guided lab and hands-on practice will build real familiarity with the console itself.

## Key takeaways

- EC2 provides resizable virtual servers under the Infrastructure as a Service model — you manage the OS and application; AWS manages the physical hardware.
- Instance store is fast but temporary; Amazon EBS is persistent and independent of the instance's own lifecycle — the deciding question is whether the data needs to survive the instance.
- AMIs make infrastructure repeatable — configure once, launch identically as many times as needed, directly supporting the "automate wherever possible" best practice.
- Instance type families (general purpose, compute optimized, memory optimized, storage optimized, accelerated computing) each match a different resource profile — match the family to the workload's actual characteristics.
- User data automatically configures a new instance at launch, removing manual setup after boot.
- EC2 Instance Savings Plans reward workloads that stay within one instance family (even as size changes) with the deepest discount; Compute Savings Plans trade some discount for flexibility across families, Regions, and services.
- Well-Architected best practices for compute — automation, right-sizing, and matching pricing to real commitment — are the Framework applied directly to this layer.

## Further reading

- [Amazon EC2 documentation](https://docs.aws.amazon.com/ec2/) — the official source for current instance types, pricing, and features.
- [Amazon EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/) — AWS's own current comparison across every instance family.
- [Amazon EC2 Pricing](https://aws.amazon.com/ec2/pricing/) — the authoritative, current source for On-Demand, Reserved, Savings Plans, and Spot pricing.

*Instance families, pricing model names, and specifications mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 4 — Adding a Storage Layer with Amazon S3](04-adding-a-storage-layer-with-amazon-s3.md) · **Next:** [Module 6 — Adding a Database Layer](06-adding-a-database-layer.md) · **Quiz:** [Module 5 Quiz](../quizzes/05-adding-a-compute-layer-using-amazon-ec2-quiz.md) · **Activity:** [Module 5 Activity](../labs/05-adding-a-compute-layer-using-amazon-ec2-activity.md)
