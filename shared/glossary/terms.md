# AWS Glossary

Plain-English definitions of terms that come up across every AWS certification. Written for someone encountering the term for the first time, not as a substitute for the module that teaches it properly.

Where a term is genuinely taught somewhere in this repo, the definition points there. Where a term is commonly confused with another, that confusion is called out directly, because on the exam the confusion is usually the point.

Jump to: [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [G](#g) · [H](#h) · [I](#i) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w)

---

## A

**Availability** — Whether you can reach your data or service right now. Distinct from durability, which is whether the data still exists at all. A system can be highly durable and temporarily unavailable at the same time.

**Availability Zone (AZ)** — One or more discrete data centers within a Region, with independent power, cooling, and networking. Placing resources across multiple AZs is the standard defense against a single facility failing. AZs sit *inside* a Region; they are not an alternative to choosing one.

**AMI (Amazon Machine Image)** — The template an EC2 instance launches from, containing the operating system and any preinstalled software. Base AMIs are clean starting images; custom AMIs capture a state you configured yourself so it can be relaunched identically.

**Amazon Aurora** — A premium database engine option selected *inside* Amazon RDS, offering higher performance, more read replicas, and storage that grows automatically. Not a separate service competing with RDS, which is the most common misreading.

**Auto Scaling** — Automatically adding or removing capacity in response to demand. It performs the action; CloudWatch supplies the metrics and alarms that trigger it. Two different jobs.

## B

**Block storage** — Storage presented to an operating system as a raw disk it can format and mount, such as Amazon EBS. Contrast with object storage (S3) and file storage (EFS).

**Bucket** — The top-level container for objects in Amazon S3. Bucket names are globally unique across all of AWS.

## C

**CapEx / OpEx** — Capital expenditure means buying hardware upfront; operating expenditure means paying for what you consume as you consume it. The shift from the first to the second is the core financial argument for cloud computing.

**CloudFormation** — AWS's infrastructure-as-code service. You describe infrastructure in a template file, and AWS provisions it, making environments repeatable rather than hand-built.

**CloudFront** — AWS's content delivery network. Caches content at edge locations worldwide so requests are served near the user instead of from the origin Region.

**CloudWatch** — The monitoring and observability service. Collects metrics, logs, and alarms. It observes and alerts; it does not itself scale anything.

## D

**Durability** — The likelihood that stored data survives without being lost. In S3, durability stays extremely high across every storage class; what changes between classes is availability, retrieval speed, and cost.

**DynamoDB** — AWS's fully managed non-relational (NoSQL) database, built for fast lookups by a known key at very large scale. Trades away complex joins and enforced relationships in exchange for that scale.

## E

**EBS (Elastic Block Store)** — Network-attached block storage for EC2, with a lifecycle independent of any single instance. Data on EBS survives an instance stopping or being replaced.

**EC2 (Elastic Compute Cloud)** — Resizable virtual servers you configure, launch, and control. The most direct example of Infrastructure as a Service in the AWS catalog.

**Edge location** — A site in AWS's global network used to cache content close to users, primarily for CloudFront. Not the same as a Region or an AZ, and not a place you run general workloads.

**Elastic Load Balancing (ELB)** — Distributes incoming traffic across multiple targets, such as EC2 instances. Frequently paired with Auto Scaling, but a separate function: ELB distributes, Auto Scaling adds and removes.

**Elasticity** — The ability to acquire resources when needed and release them when not. Related to but distinct from scalability, which is about handling growth.

## G

**Glacier** — S3's storage class family for archival data, priced for long-term retention where retrieval speed doesn't matter much.

## H

**High availability** — Designing so a system keeps operating through the failure of a component, usually by removing single points of failure and spreading across AZs.

## I

**IAM (Identity and Access Management)** — Controls who can do what in an AWS account, through users, groups, roles, and policies.

**IAM group** — A collection of users that a policy can be attached to once and applied to everyone in it. The scalable alternative to attaching the same policy to each user individually.

**IAM role** — A set of permissions that can be assumed temporarily, by a user, an application, or an AWS service. Roles are how a service gets permissions without embedding long-lived credentials.

**IaaS / PaaS / SaaS** — Infrastructure, Platform, and Software as a Service. The distinction is how much of the stack you manage versus the provider: most with IaaS, least with SaaS.

**Instance store** — Temporary block storage physically attached to the host running an EC2 instance. Fast, but lost when the instance stops or terminates. The deciding question against EBS is persistence, not price.

## K

**Key (S3)** — The unique identifier used to retrieve an object from a bucket. Keys often contain slashes and look like file paths, but S3's namespace is flat rather than a true directory tree.

**KMS (Key Management Service)** — Creates and controls the encryption keys used to protect data across AWS services.

## L

**Lambda** — Runs code without provisioning or managing servers, billed by execution. The canonical serverless compute service.

**Latency** — The delay before a transfer of data begins. A primary reason to choose a Region near your users, and the reason edge locations exist.

**Lifecycle policy** — Rules that automatically transition S3 objects between storage classes, or expire them, based on age. Replaces manual storage-class management.

**Local Zone** — An extension of a Region placed closer to a specific metropolitan area for latency-sensitive workloads. Extends a parent Region rather than replacing it.

## M

**Multi-AZ** — An RDS deployment maintaining a synchronous standby in a second Availability Zone with automatic failover. Solves availability. Does *not* scale reads, which is what read replicas are for. Confusing these two is one of the most common errors on the exam.

## N

**Neptune** — AWS's purpose-built graph database, for data whose value is in the relationships between entities.

**NoSQL** — Non-relational databases, typically schema-flexible and optimized for scale and fast key-based access rather than complex querying.

## O

**Object storage** — Storage that keeps data as objects with metadata in a flat namespace, retrieved by key. Amazon S3 is the example. Contrast with block and file storage.

**OLTP / OLAP** — Online Transaction Processing means many small fast operations, like placing an order. Online Analytical Processing means fewer, much larger queries across historical data, like a trend report. RDS, Aurora, and DynamoDB serve OLTP; Redshift serves OLAP.

**On-Demand** — Paying for compute by the second or hour with no commitment. The correct default when a workload's pattern is genuinely unknown; the mistake is never revisiting it once the pattern is known.

## P

**Presigned URL** — A time-limited URL granting access to a specific S3 object without requiring the recipient to have an IAM identity.

## R

**RDS (Relational Database Service)** — Managed relational databases across several engines, with AWS handling patching, backups, and failover infrastructure.

**Read replica** — An additional readable copy of a database that absorbs read traffic without consuming the primary's write capacity. Solves read scaling, not failover.

**Redshift** — AWS's data warehouse, purpose-built for analytical queries across large historical datasets. Not simply "RDS for bigger data" — a different workload shape entirely.

**Region** — A separate geographic area containing multiple Availability Zones. The top-level choice determining where data physically resides, which makes it the lever for data residency requirements.

**Reserved Instance** — A commitment to a specific instance configuration for one or three years in exchange for a discount. Less flexible than a Savings Plan, which is the detail that usually separates them on an exam question.

**RTO / RPO** — Recovery Time Objective is how quickly you must be running again. Recovery Point Objective is how much data you can afford to lose. The two numbers together determine which disaster recovery strategy is appropriate.

## S

**S3 (Simple Storage Service)** — Object storage for effectively unlimited data, retrieved over the web by key. The default answer for backups, media, and static website content.

**Savings Plan** — A commitment to a consistent amount of usage for one or three years in exchange for a discount. Compute Savings Plans stay flexible across instance families and Regions; EC2 Instance Savings Plans commit to one family in one Region for a deeper discount while still allowing the size to change.

**Scalability** — The ability to handle growth by adding resources. Vertical scaling means a bigger instance; horizontal scaling means more instances.

**SCP (Service Control Policy)** — An AWS Organizations feature setting the maximum permissions an account can have, capping what even that account's own IAM policies can grant.

**Serverless** — A model where you don't provision or manage servers and pay only for what executes. Servers still exist; you just aren't responsible for them.

**Shared Responsibility Model** — The division of security duties: AWS secures the cloud itself (hardware, facilities, the hypervisor), you secure what you put in it (guest OS, data, access, configuration). The most heavily tested single idea on the CLF-C02 exam.

**Spot Instance** — Deeply discounted spare EC2 capacity that AWS can reclaim with little notice. Appropriate only for fault-tolerant, interruption-tolerant workloads.

**Subnet** — A range of IP addresses within a VPC. Public subnets have a route to an internet gateway; private subnets do not, which is how database tiers are typically isolated.

## T

**TCO (Total Cost of Ownership)** — The full cost of a solution including hardware, facilities, staffing, and maintenance, not just the invoice. The basis for honest cloud-versus-on-premises comparisons.

## U

**User data** — A script attached to an EC2 instance at launch and run automatically on first boot. What turns a generic AMI into a configured, ready-to-serve instance without manual setup.

## V

**Versioning** — An S3 feature retaining every prior version of an object instead of overwriting it. Protects against accidental overwrites and deletes, at the cost of storing every version, which is why it's usually paired with a lifecycle policy.

**VPC (Virtual Private Cloud)** — A logically isolated section of the AWS network where you launch resources, with control over IP ranges, subnets, route tables, and gateways.

## W

**Wavelength** — AWS infrastructure embedded inside a telecom carrier's network for ultra-low-latency mobile and 5G workloads. Extends a parent Region rather than replacing it.

**Well-Architected Framework** — AWS's set of design principles organized into pillars: Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability. Used to evaluate and improve architectures rather than as a checklist applied afterward.

---

*Definitions here are written to be understood, not to be authoritative. Service capabilities and limits change; verify current details at [aws.amazon.com](https://aws.amazon.com) before relying on them for production decisions or exam-day specifics.*
