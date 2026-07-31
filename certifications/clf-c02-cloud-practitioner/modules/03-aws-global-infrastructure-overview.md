# Module 3: AWS Global Infrastructure Overview

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 3 — Cloud Technology and Services (touches Domain 1)
**Estimated study time:** 45 minutes

## Why this matters

Modules 1 and 2 covered what cloud computing is and what it costs. This module answers a more physical question: where does any of it actually run? Every purchase option from Module 2 — On-Demand, Reserved, Spot — still has to launch somewhere, and "somewhere" is not one undifferentiated mass called "the cloud." It's a specific, deliberately engineered map of data centers, cities, and telecom networks, and understanding that map is what turns "the cloud" from a buzzword into something you can actually reason about.

This module also introduces the single habit that underlies nearly everything the exam calls "resilience" — and it's simpler than most people expect.

## Learning objectives

By the end of this module, you should be able to:

- Explain what a Region is and name the four factors that decide which one to use
- Describe Availability Zones and why spreading across them is the core resilience habit
- Distinguish edge locations from Regions and AZs, and explain what Amazon CloudFront does
- Compare Local Zones and Wavelength to a standard Region and know when each applies
- Describe AWS Outposts and recognize when it's the right answer
- Recognize the major categories of AWS services, from compute to networking to security
- Avoid the most common global-infrastructure traps on the exam

---

## The Big Picture: Building Blocks of AWS Infrastructure

Everything about where a workload runs comes down to a small set of building blocks, from largest and most general to smallest and most specialized:

| Building block | What it is |
|---|---|
| Regions | Separate geographic areas around the world. You choose where your workload lives. |
| Availability Zones (AZs) | Isolated data centers inside a Region — each with its own power, cooling, and network. |
| Edge Locations | Sites even closer to users, used to cache content and cut latency. |
| Local Zones & Wavelength | Newer extensions that push AWS infrastructure closer to specific cities or telecom networks. |
| Outposts | Actual AWS hardware installed inside a customer's own building. |

## Regions: Where Your Workload Lives

Every workload you launch lives in a Region you choose — it's the first infrastructure decision you make, before you've picked a single service.

- A Region is a separate, self-contained geographic area — for example, a Region in Ohio, or one in Ireland.
- Regions are fully independent — a problem in one Region doesn't take down another.
- A Region contains multiple Availability Zones.
- Not every AWS service launches in every Region on day one.
- Resources usually stay in the Region you launched them in, unless you configure otherwise.

**Choosing which Region to use comes down to four factors:**

| Factor | What to consider |
|---|---|
| Latency | Put resources close to your users — someone in Dallas is served faster from a US Region than from Frankfurt. |
| Price | The same service can cost different amounts in different Regions. |
| Compliance | Data-residency laws, like GDPR, may require data to physically stay in a specific country. |
| Service availability | Not every AWS service launches in every Region on day one. |

> ⚠️ **Exam trap:** if a scenario mentions a country's data-privacy law, the answer is almost always Region choice — not encryption settings. And when compliance is genuinely in play, it wins before latency or price even get a vote — check compliance first, always.

## Spread Across Availability Zones

One habit separates a fragile architecture from a resilient one, and it's simpler than it sounds.

**Single-AZ risk:** one data center means one point of failure. A power or network outage takes the whole application down, with no automatic way to fail over. This is what happens when "in the cloud" gets mistaken for "automatically resilient" — the cloud makes resilience possible, but doesn't grant it for free.

**The multi-AZ habit:** run copies of your application in 2–3 Availability Zones. Each AZ has its own power, cooling, and network, so if one fails, the others keep serving traffic and users never notice. No single AZ becomes a dependency the whole application relies on.

This single habit — spreading across AZs — is the foundation of nearly everything the exam calls "resilience." It's worth being precise about its limit, too: multi-AZ protects against a data-center-level problem. If an entire Region has a rare, large-scale outage, that's a separate, much bigger conversation (see "Single-Region vs. Multi-Region Design," below).

## Edge Locations vs. Regions and Availability Zones

Regions and Availability Zones **run your application** — compute, storage, and databases actually execute there, you choose which Region, and you spread across multiple AZs for resilience. There are far fewer of these sites worldwide than the next category.

Edge locations **don't run your application at all.** They cache content close to users instead. Amazon CloudFront serves cached copies from the nearest edge site, and because their whole purpose is being near *everyone*, there are far more edge locations worldwide than Regions. The result: edge locations cut latency for the "last mile" to the end user, without running any application logic themselves.

> ⚠️ **Exam trap:** don't confuse edge locations with Availability Zones. If a question asks for the fastest way to reduce latency for users worldwide, the answer is almost never "launch more EC2 instances in more Regions" — it's edge locations, via CloudFront.

## Extending the Edge: Local Zones and Wavelength

Two newer infrastructure types push AWS closer to specific places, for workloads that can't tolerate normal Region latency:

- **AWS Local Zones** place compute and storage in a large metro area outside a full Region — think gaming or media production, where a studio needs low latency without needing a whole Region's worth of infrastructure nearby.
- **AWS Wavelength** embeds AWS infrastructure directly inside a telecom provider's 5G network, for single-digit-millisecond mobile latency.

Neither is a replacement for a standard Region — both *extend* a parent Region rather than replacing the Region/AZ model. Most workloads never need either; the exam tests recognition, not configuration.

> ⚠️ **Exam trap:** don't confuse a Local Zone with an Availability Zone. A Local Zone is a single site with no AZ-style redundancy of its own — very different from an AZ, which is one of several redundant sites inside a Region.

## Extending Even Further: AWS Outposts

Sometimes the workload can't come to AWS, so AWS goes to it. AWS Outposts is actual AWS hardware, installed in a customer's own data center or facility, but still managed by AWS and running the same APIs and services as a Region, connected back over a network link.

Outposts fits ultra-low on-site latency needs, local data-processing requirements, or workloads that legally cannot leave the building.

> ⚠️ **Exam trap:** whenever a scenario says data or processing *legally or physically cannot leave a specific building*, Outposts is almost always the answer. Local Zones, Wavelength, and standard Regions all assume it's fine for the workload to live somewhere else — Outposts is the only one of the four that's physically installed on the customer's own premises.

## Global Infrastructure by the Numbers

Rough orders of magnitude, not numbers to memorize: 30+ Regions worldwide and still growing; typically 3 or more Availability Zones per Region, roughly 90+ AZs worldwide; hundreds of edge locations; dozens of Local Zones and growing; Outposts and Wavelength deployed based on customer demand rather than a fixed footprint.

AWS adds Regions, AZs, and Local Zones regularly, so treat any specific count — including the ones above — as a snapshot, not a fact to memorize. Check [aws.amazon.com/about-aws/global-infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) for the current figures rather than trusting a number from any lecture or study guide, including this one.

## Single-Region vs. Multi-Region Design

Multi-AZ protects against a data-center problem. It doesn't protect against a whole Region having a bad day.

**Single-Region:** application and database spread across 3 AZs, all inside one Region. One Region, one blast radius. Simpler to build, cheaper to run — with the open question of what happens if the whole Region has a problem.

**Multi-Region:** a primary Region plus a standby Region, with data replicated across both and failover ready if the primary Region goes down.

Multi-Region is rare, expensive, and reserved for workloads that truly can't tolerate downtime — it's a deliberate design choice, not a default. Most workloads are well served by solid multi-AZ alone; reaching for multi-Region without a workload that genuinely requires it is a common exam trap in the other direction.

## A First Look at AWS Service Categories

You don't need to know individual services yet — that starts in later modules. For now, just recognize which family a service belongs to:

| Category | What it does | Example services |
|---|---|---|
| Compute | Runs your code and applications | Amazon EC2, AWS Lambda |
| Storage | Holds your data, from object storage to file systems | Amazon S3 |
| Database | Purpose-built stores for structured and unstructured data | Amazon RDS, DynamoDB |
| Networking & Content Delivery | Connects everything and gets content to users | Amazon VPC, CloudFront |
| Security, Identity & Compliance | Controls who can do what, and protects your data | IAM |
| Management & Governance | Monitors, automates, and keeps accounts organized | CloudWatch, Organizations |

Almost everything you'll learn for the rest of this course sorts into one of these six families. Regions, AZs, and the rest of this module are just *where* all six families physically run.

---

## What to skip

You don't need an exact, current count of Regions or Availability Zones — that number changes as AWS builds more, and the exam tests the concept (Regions contain multiple AZs) rather than a specific figure. You also don't need deep configuration knowledge of Local Zones, Wavelength, or Outposts — for Cloud Practitioner, recognizing what each one is *for* is enough; the hands-on setup detail belongs to the Solutions Architect Associate exam.

## Key takeaways

- A Region is a separate geographic area; an Availability Zone is an isolated data center inside it. Regions and AZs run your application.
- Choosing a Region comes down to four factors: latency, price, compliance, and service availability — and compliance wins whenever it's genuinely in play.
- Spreading an application across 2–3 Availability Zones is the core resilience habit the exam calls "multi-AZ" — but it only protects against a data-center-level failure, not a Region-wide one.
- Edge locations don't run applications — they cache content via Amazon CloudFront to cut latency for users worldwide.
- Local Zones and Wavelength extend a parent Region for latency-sensitive workloads; they don't replace the standard Region/AZ model.
- AWS Outposts is the only infrastructure type physically installed inside a customer's own building — the answer whenever data legally or physically cannot leave the premises.
- Multi-Region design is a deliberate, expensive step up from multi-AZ, reserved for workloads that truly can't tolerate a Region-level event — not a default.

## Further reading

- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) — AWS's current, authoritative map of Regions and Availability Zones.
- [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/) and [AWS Wavelength](https://aws.amazon.com/wavelength/) — official pages for the two edge-extension services covered above.
- [AWS Outposts](https://aws.amazon.com/outposts/) — official documentation on bringing AWS hardware on-premises.

*Region/AZ counts and service availability mentioned above are illustrative — verify current values at aws.amazon.com before relying on them.*

---

**Previous:** [Module 2 — Cloud Economics and Billing](02-cloud-economics-and-billing.md) · **Next:** [Module 4 — AWS Cloud Security](04-aws-cloud-security.md) · **Quiz:** [Module 3 Quiz](../quizzes/03-aws-global-infrastructure-overview-quiz.md) · **Activity:** [Module 3 Activity](../labs/03-aws-global-infrastructure-overview-activity.md)
