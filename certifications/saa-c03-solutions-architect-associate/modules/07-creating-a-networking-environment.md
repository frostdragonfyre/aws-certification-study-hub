<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](06-adding-a-database-layer.md) · [Next module](08-connecting-networks.md) · [Quiz](../quizzes/07-creating-a-networking-environment-quiz.md) · [Slides](../lectures/07-creating-a-networking-environment.pptx)
<!-- /hub-navigation -->

# Module 7: Creating a Networking Environment

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 45 minutes

## Why this matters

Every module so far has added a *layer* to the café's architecture — S3 for the static site, EC2 for the web application, RDS for the database. Each of those services has been sitting inside a network this whole time, and up to now that network has mostly stayed out of the story. That stops here.

Module 4's version of the café (V3) already split the web tier from the database tier and put the database "on a private subnet" — but that phrase was asserted, not explained. This module explains it. A VPC is the container everything else in this course gets deployed into, and "public" versus "private" isn't a label you attach to a subnet — it's a *consequence* of how that subnet's traffic is routed. Get the network wrong and it doesn't matter how well you configured EC2, RDS, or anything else sitting inside it: the database is either reachable from the internet when it shouldn't be, or the application can't reach anything at all.

This is also the most heavily tested non-security topic on the SAA-C03 exam. Expect scenario questions that never use the word "VPC" directly — they describe a symptom ("instances in this subnet can't reach the internet") and expect you to diagnose which networking component is misconfigured.

## Learning objectives

By the end of this module, you should be able to:

- Explain what a VPC is and why every AWS architecture is built inside one
- Describe how subnets, route tables, and an internet gateway combine to make a subnet "public"
- Explain what a NAT gateway does, and why private subnets need one for outbound-only internet access
- Size a VPC's IP address range using CIDR notation, at the level the exam expects
- Diagnose common networking misconfigurations from a described symptom

---

## The Café's Networking Problem

Recall where the café's architecture stood at the end of Module 6: a web tier running on EC2, and a database tier running on RDS, both "on AWS" — but not yet deliberately placed anywhere. Olivia, the AWS consultant who specializes in networking, raises the obvious question: *where*, exactly?

Right now, nothing stops someone from reaching the database directly from the internet if its security configuration ever slips. Nothing isolates a compromised web server from directly touching the database's network path. And there's no deliberate boundary between "things the public should be able to reach" and "things only the application itself should be able to reach." That boundary is what this module builds.

The business need driving this module is the same one AWS Academy's own café case study names directly: *enhance the security of the web application* by using VPC features to configure and secure public and private subnets. Not a new feature for customers — a foundation the café's existing features now sit on top of, safely.

## Amazon VPC: The Foundation

A **Virtual Private Cloud (VPC)** is a logically isolated section of AWS's network that you define — your own private slice of AWS, with your own IP address range, your own subnets, and full control over how traffic moves in, out, and around inside it. Every EC2 instance, every RDS database, and most other AWS resources with a network presence live inside a VPC. There's no "no VPC" option; the only choice is whether you use the **default VPC** every AWS account gets automatically, or build a **custom VPC** deliberately sized and structured for the workload.

For anything beyond a quick experiment, build a custom VPC. The default VPC exists so a brand-new AWS account can launch an EC2 instance five minutes after signup — it's *not* how AWS Academy or the real exam expects you to design a production network, because it comes with all-public subnets and no thought given to isolation.

### Sizing a VPC: CIDR blocks

A VPC's IP address range is defined using **CIDR (Classless Inter-Domain Routing) notation** — an IP address followed by a slash and a number, like `10.0.0.0/16`. The number after the slash tells you how many of the address's bits are fixed (the network portion) versus how many are free to vary (the host portion, i.e., how many individual addresses that block contains).

The exam-relevant intuition, without turning this into a full networking course:

| CIDR suffix | Addresses available | Typical use |
|---|---|---|
| /16 | 65,536 | A whole VPC — generous room to carve into many subnets later |
| /24 | 256 | A single subnet — a common, comfortable default size |
| /28 | 16 | A small subnet for something like a NAT gateway or a handful of dedicated resources |

The smaller the number after the slash, the *larger* the address block — that inverse relationship trips people up more than any other part of CIDR notation. `/16` is a big range; `/28` is a small one.

> ⚠️ **Exam trap:** a VPC's CIDR block should be sized with room to grow, and it can't be resized smaller once subnets are carved out of it. Undersizing a VPC's address range is a real, exam-tested design mistake — not just a theoretical one.

You'll pick a VPC CIDR block once, up front, in the café's Learner Lab challenge lab for this module — after that, every subnet you create has to fit inside it without overlapping any other subnet.

## Subnets: Slicing the VPC

A **subnet** is a range of IP addresses carved out of the VPC's CIDR block, and — this is the detail people skip past — **every subnet lives entirely inside one Availability Zone**. A subnet never spans AZs. That single fact is *why* high availability (Module 10) starts at the subnet layer: to survive an AZ failure, you need resources spread across subnets in at least two different AZs, not just multiple subnets in the same one.

For the café, that means the minimum viable production network isn't one public subnet and one private subnet — it's at least two of each, one pair per AZ, even before Module 10 formally introduces Elastic Load Balancing and Auto Scaling on top of that foundation.

### What actually makes a subnet "public"

Here's the idea this whole module hinges on, and the one most first-time answers get subtly wrong: **a subnet is not public or private because of a setting on the subnet itself.** A subnet is public *only* because its route table sends internet-bound traffic to an internet gateway. Nothing else defines it. Rename a subnet "public-subnet-1" and skip that route table entry, and it behaves as a private subnet regardless of the name.

That means "public" and "private" are really properties of a **route table**, not a subnet — the subnet just happens to be associated with that route table.

## Route Tables: Where Traffic Actually Goes

A **route table** is a set of rules — routes — that determine where network traffic from a subnet is allowed to go. Every VPC starts with a **main route table**, automatically associated with every subnet that isn't explicitly associated with something else. Every route table, by default, contains one route: traffic addressed to somewhere inside the VPC's own CIDR block stays inside the VPC (this is what lets the web tier and the database tier talk to each other at all).

To make a subnet public, you add one more route: send traffic addressed to `0.0.0.0/0` — meaning "anywhere on the internet, not covered by a more specific route" — to an **internet gateway**. Associate that route table with a subnet, and that subnet is now public, by definition, because of that single route.

A private subnet's route table has no such route to an internet gateway. It might still have a route to a NAT gateway for outbound-only access (covered next), but nothing that lets traffic originate *from* the internet and reach it directly.

> ⚠️ **Exam trap:** a scenario question describing "instances in a subnet can't be reached from the internet, even though the subnet is associated with a route table that has a route to an internet gateway" is almost always actually a security group or NACL problem (Module 9), not a routing problem — routing gets traffic to the door; the security layer decides whether it's let in. Don't reach for "the route table is wrong" as your first diagnosis if the question already tells you the route exists.

## Internet Gateway: The Front Door

An **internet gateway** is a horizontally scaled, redundant, highly available VPC component that allows communication between resources in a VPC and the internet. One important structural fact: an internet gateway attaches to the *VPC itself*, not to any individual subnet. A VPC has at most one internet gateway attached at a time, and every public subnet in that VPC shares it — "public" subnets aren't each getting their own gateway; they're all just routed to the one the VPC has.

There's no hourly charge for an internet gateway itself, and no capacity planning required — AWS manages its scaling and availability. From a design standpoint, attaching an internet gateway to a VPC and adding one route to it is genuinely the entire mechanism. The complexity in this module is almost all in getting the surrounding pieces — subnets, route tables, and (for private subnets) NAT — arranged correctly around that one simple gateway.

## NAT Gateway: Outbound Only, On Purpose

The café's database subnet should never be reachable *from* the internet — but it still needs to reach *out*, for things like OS patches and software updates. That's a different problem from the one an internet gateway solves, and it needs a different component: a **NAT (Network Address Translation) gateway**.

A NAT gateway is a managed AWS service that lets resources in a **private** subnet initiate outbound connections to the internet, while blocking any connection initiated *from* the internet toward them. Traffic can go out; nothing can come in unsolicited. That asymmetry — outbound yes, inbound no — is the entire reason it exists, and the entire reason it's a different component from an internet gateway rather than just "an internet gateway for private subnets."

A few placement and cost details the exam expects you to know cold:

- **A NAT gateway is deployed into a *public* subnet**, not the private subnet it serves — it needs its own route to the internet gateway to forward traffic onward.
- **A NAT gateway lives in one AZ.** If that AZ fails, private subnets in *other* AZs lose outbound internet access unless you deployed a separate NAT gateway per AZ. For a highly available design, that's exactly what you do — one NAT gateway per AZ, each serving the private subnets in its own AZ.
- **NAT gateways are billed hourly, plus a per-GB data processing charge** — unlike an internet gateway, this is a real, ongoing line item worth mentioning to a cost-conscious owner like Martha.

> ⚠️ **Exam trap:** AWS also supports a **NAT instance** — a self-managed EC2 instance configured to perform the same job. It's legacy at this point: no built-in redundancy, you patch and scale it yourself, and it's a single point of failure unless you build extra infrastructure around it. The exam may still ask you to recognize it, almost always as the *wrong* choice compared to a managed NAT gateway. Don't design with one; do recognize what one is.

### Gateway comparison, side by side

| | Internet Gateway | NAT Gateway |
|---|---|---|
| Attaches to | The VPC | A specific (public) subnet |
| Direction | Inbound and outbound | Outbound only |
| Serves | Public subnets | Private subnets |
| AZ scope | VPC-wide | Single AZ (deploy one per AZ for HA) |
| Cost | No hourly charge | Hourly + per-GB data processing |
| Legacy self-managed alternative | *(none — always managed)* | NAT instance (not recommended) |

## Putting It Together: The Café's V4 Network

With those four pieces — VPC, subnets, route tables, and gateways — the café's network for this module's version of the architecture looks like this: one VPC sized generously with a `/16`, two Availability Zones for resilience, and in each AZ, one public subnet (web tier, routed to the internet gateway) and one private subnet (database tier, with outbound-only access through a NAT gateway in that AZ's public subnet). The database is not reachable from the internet by construction, not by promise — there's simply no route that gets traffic there.

That's the actual technical requirement behind Module 1's V4 milestone: *use Amazon VPC features to configure and secure public and private subnets.* Every concept in this module was in service of that one sentence.

## What to skip

You don't need to memorize exact CIDR arithmetic for arbitrary subnet sizes — the guided lab walks you through the AWS console's own subnet calculator, and the exam's CIDR questions stay at the conceptual level shown above ("smaller suffix means a bigger range"). You also don't need VPC peering, Transit Gateway, VPN, or Direct Connect yet — those are Module 8's job, once a single VPC's internal design is solid.

## Key takeaways

- Every AWS resource with a network presence lives inside a VPC — the only real choice is default (fine for experiments) versus a deliberately sized custom VPC (correct for anything real).
- A subnet is public or private because of its **route table**, not because of anything set on the subnet itself. A route to an internet gateway is what makes a subnet public.
- Every subnet lives in exactly one Availability Zone — high availability requires subnets spread across multiple AZs, not just multiple subnets.
- An internet gateway attaches to the VPC and enables two-way internet traffic for public subnets; it's free and requires no capacity planning.
- A NAT gateway lives in a public subnet and gives private subnets outbound-only internet access; it's billed hourly, is scoped to one AZ, and should be deployed once per AZ for high availability.
- A NAT instance is the legacy, self-managed alternative to a NAT gateway — recognize it, don't design with it.

## Further reading

- [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) — the official reference for everything in this module, in far more depth than the exam needs.
- [VPC CIDR blocks](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html) — for when you actually need to plan real address ranges outside of a lab environment.

---

**Next:** [Module 8 — Connecting Networks](08-connecting-networks.md)
