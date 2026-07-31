# Module 5: Networking and Content Delivery

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 3 — Cloud Technology and Services
**Estimated study time:** 45 minutes

## Why this matters

Every AWS resource lives inside a network, and this module is where "the cloud" stops being an abstract pool of services and becomes something with an actual address, a border, and rules about what's allowed to cross it. Amazon VPC is the foundation almost every other service sits on top of — you'll see it referenced again and again for the rest of this course, and constantly on the Solutions Architect Associate exam that follows this one.

The second half of the module is about getting traffic *to* your resources efficiently: DNS (Route 53), content caching (CloudFront), and dedicated connectivity back to on-premises environments. Together, these two halves answer the same underlying question from opposite directions — "how does traffic get where it needs to go, safely and fast?"

## Learning objectives

By the end of this module, you should be able to:

- Describe a VPC and explain why resources are launched inside one
- Distinguish public and private subnets, and explain what makes a subnet "public"
- Explain the roles of an Internet Gateway, a NAT Gateway, and a route table
- Distinguish Security Groups from Network ACLs
- Describe Amazon Route 53 and what it's used for
- Describe Amazon CloudFront and explain when a CDN helps
- Distinguish AWS Direct Connect from a Site-to-Site VPN
- Describe AWS Global Accelerator at a high level
- Avoid the most common networking traps on the exam

---

## Amazon VPC: Your Own Private Network in AWS

A **Virtual Private Cloud (VPC)** is a logically isolated section of the AWS Cloud where you launch resources — think of it as your own private data center network, carved out of AWS's infrastructure, with a range of IP addresses you define. Nearly everything you launch on AWS — EC2 instances, RDS databases, and more — lives inside a VPC.

A VPC spans an entire **Region** but is subdivided into **subnets**, and each subnet lives in exactly one **Availability Zone** (a direct callback to Module 3 — this is the mechanism that lets an application actually spread across AZs for resilience).

## Public vs. Private Subnets

A subnet's "public" or "private" label isn't a property of the subnet itself — it's determined entirely by its **route table**:

- A **public subnet** has a route table entry sending internet-bound traffic (`0.0.0.0/0`) to an **Internet Gateway**. Resources here can be reached from, and reach out to, the public internet (a web server, for example).
- A **private subnet** has no such route. Resources here — like a backend database — are unreachable directly from the internet, which is exactly the point.

> ⚠️ **Exam trap:** a subnet isn't "public" because someone labeled it that way — it's public because its route table sends internet traffic to an Internet Gateway. If that route is missing, the subnet is private regardless of its name.

## Getting In and Out: Internet Gateway and NAT Gateway

Two different components handle two different directions of traffic:

| Component | Direction | Typical use |
|---|---|---|
| **Internet Gateway (IGW)** | Two-way | Attached to a VPC to allow resources in public subnets to send and receive traffic directly to/from the internet |
| **NAT Gateway** | Outbound only | Placed in a public subnet so resources in a *private* subnet can initiate outbound connections (like downloading a software update) without being directly reachable from the internet |

> ⚠️ **Exam trap:** "a private database instance needs to download a patch from the internet, but must never be directly reachable from it" describes a NAT Gateway, not an Internet Gateway. The giveaway phrase is *outbound only, never inbound*.

## Route Tables

A **route table** is the set of rules that determines where network traffic from a subnet is directed. Every subnet is associated with a route table, and that table's contents are what actually decide whether a subnet behaves as public or private — as covered above.

## Security Groups vs. Network ACLs

Module 4 introduced security groups as "configuring the firewall" in the shared responsibility model. Here's the fuller picture, since the exam frequently tests the difference between the two layers of network filtering inside a VPC:

| | Security Group | Network ACL (NACL) |
|---|---|---|
| Operates at | Instance level | Subnet level |
| Rule types | **Allow only** | Allow and **explicit deny** |
| State | Stateful — return traffic is automatically allowed | Stateless — return traffic must be explicitly allowed |
| Evaluates rules | All rules at once | In numbered order |

> ⚠️ **Exam trap:** "I need to explicitly block traffic from one specific IP address" points to a Network ACL, since security groups can't write deny rules at all — only allow rules. If a scenario needs a deny rule, it isn't a security group question.

## Amazon Route 53: DNS

**Amazon Route 53** is AWS's Domain Name System (DNS) service — it translates human-readable domain names (like `example.com`) into the IP addresses computers actually use to connect. Route 53 also handles domain registration and offers health checks and several routing policies (like routing users to the closest healthy endpoint). The exam cue is simple: anything about translating a domain name to an IP address, or managing DNS records, is Route 53.

## Amazon CloudFront: Content Delivery

**Amazon CloudFront** is AWS's **content delivery network (CDN)** — it caches copies of content at **edge locations** around the world (the same edge locations introduced in Module 3), so users retrieve content from a location physically close to them instead of from the origin server every time.

The exam cue is **latency for distributed, often static or semi-static, content**: a media company whose video files need to load quickly for users worldwide is a textbook CloudFront scenario. CloudFront reduces load on the origin server and cuts the round-trip distance data has to travel.

> ⚠️ **Exam trap:** CloudFront speeds up delivery of *content* to *end users* around the world. It's not the answer for connecting a corporate data center to AWS — that's Direct Connect or VPN, below. Don't confuse "fast content delivery to many users" with "dedicated private connectivity to one location."

## Connecting to AWS from On-Premises: Direct Connect vs. VPN

Two different services connect an on-premises environment to AWS, and the exam expects you to tell them apart by looking at *how* the connection is made:

| | AWS Direct Connect | Site-to-Site VPN |
|---|---|---|
| Connection type | Dedicated private physical network connection | Encrypted connection over the public internet |
| Setup time | Longer (physical circuit provisioning) | Fast — can be set up quickly |
| Typical use | Consistent, high-bandwidth, low-latency needs (large data transfers, hybrid workloads) | Quick setup, lower cost, backup connectivity |

> ⚠️ **Exam trap:** "consistent network performance, unaffected by public internet congestion" points to Direct Connect. "Needs to be up and running quickly, encrypted over the internet" points to VPN. The two are also commonly paired together — VPN as a backup path if a Direct Connect circuit goes down.

## AWS Global Accelerator

**AWS Global Accelerator** improves availability and performance for global applications by routing traffic over AWS's own private global network backbone instead of the public internet, using static anycast IP addresses as fixed entry points. It's a narrower, less-tested service than CloudFront — the distinguishing cue is that it accelerates traffic to *application* endpoints (including non-HTTP traffic like gaming or IoT protocols), where CloudFront specifically caches *content*.

## Putting It Together: A Simple Web Application

A common exam scenario sketch: a public-facing web application with a backend database.

1. The **VPC** contains a **public subnet** (web servers, routed to an Internet Gateway) and a **private subnet** (database, no route to the internet).
2. A **NAT Gateway** in the public subnet lets the database pull software updates outbound, without being reachable inbound.
3. **Security groups** control instance-level access; a **Network ACL** on the private subnet adds an explicit-deny layer.
4. **Route 53** resolves the application's domain name to the right endpoint.
5. **CloudFront** caches static assets (images, videos, scripts) at edge locations close to users.

Every piece above showed up individually earlier in this module — the exam often just asks you to recognize which piece a given clue is pointing at.

---

## What to skip

You don't need to configure actual VPC CIDR blocks, write NACL rule numbers, or set up a real Direct Connect circuit — that hands-on depth belongs to the Solutions Architect Associate exam. For Cloud Practitioner, focus on matching a scenario's clue phrase to the right networking concept.

## Key takeaways

- A VPC is a logically isolated network in AWS; subnets live inside a VPC, each pinned to one Availability Zone.
- A subnet is public or private based on its **route table**, not a label — public subnets route internet traffic to an Internet Gateway.
- Internet Gateways allow two-way internet traffic; NAT Gateways allow private-subnet resources outbound-only internet access.
- Security groups are stateful and allow-only, operating at the instance level; Network ACLs are stateless, support explicit deny, and operate at the subnet level.
- Route 53 handles DNS — translating domain names to IP addresses.
- CloudFront is a CDN that caches content at edge locations to cut latency for end users worldwide.
- Direct Connect is a dedicated private physical connection for consistent performance; Site-to-Site VPN is a faster-to-set-up encrypted connection over the public internet — they're often paired as primary/backup.
- Global Accelerator routes traffic over AWS's private backbone to improve performance for application endpoints, distinct from CloudFront's content caching.

## Further reading

- [Amazon VPC](https://aws.amazon.com/vpc/) — official VPC documentation, including subnet and routing concepts.
- [Amazon Route 53](https://aws.amazon.com/route53/) — DNS service overview and routing policies.
- [Amazon CloudFront](https://aws.amazon.com/cloudfront/) — CDN overview and how edge locations work.
- [AWS Direct Connect](https://aws.amazon.com/directconnect/) and [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/) — for comparing the two hybrid-connectivity options directly.

*Service capabilities mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 4 — AWS Cloud Security](04-aws-cloud-security.md) · **Next:** [Module 6 — Compute](06-compute.md) · **Quiz:** [Module 5 Quiz](../quizzes/05-networking-and-content-delivery-quiz.md) · **Activity:** [Module 5 Activity](../labs/05-networking-and-content-delivery-activity.md)
