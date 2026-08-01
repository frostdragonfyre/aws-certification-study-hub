# Module 2: Introducing Cloud Architecting

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

Module 1 introduced the *role* of a cloud architect. This module introduces the *job itself*: what "cloud architecting" actually means as a practice, where it came from, and the four things every architect works with on every project — a shared framework for evaluating designs, a body of best practices, an understanding of how AWS's own infrastructure is laid out, and the judgment to place resources deliberately instead of by default.

If Module 1 was about mindset, this module is about vocabulary and tools — the shared language you'll use for the rest of this course (and, eventually, the SAA-C03 exam) to talk about *why* an architecture is designed one way instead of another.

## Learning objectives

By the end of this module, you should be able to:

- Define cloud architecture
- Describe how to design and evaluate architectures using the AWS Well-Architected Framework
- Explain best practices for building solutions on AWS
- Describe how to make informed decisions about where to place AWS resources

---

## What Is Cloud Architecting?

**Cloud architecting** is the practice of applying cloud best practices to a solution — using cloud services and features to meet an organization's technical needs and its business use cases at the same time. Notice both halves of that definition: technical needs (will it actually work, scale, and stay secure) and business use cases (does it solve the real problem, at a cost and timeline the business can live with). A design that nails one and ignores the other isn't well-architected — it's just architected.

This is the working perspective for the rest of the course. Every module from here forward asks the same underlying question in a different context: given this need, what should the architecture actually look like, and why?

## Where This Practice Came From: AWS's Own Origin Story

It's worth knowing that AWS didn't start as a cloud provider — it became one by solving its own architecture problem first, and the story is a useful preview of what "cloud architecting" is actually for.

Around 2000, Amazon needed to build an ecommerce service that would let third-party sellers build their own shopping sites on top of Amazon's ecommerce engine. The company struggled to make the new shopping website highly available and scalable, because the underlying tools, applications, and architectures had been built without much upfront planning. Services were tangled together, hard to separate into a centralized development platform, and every project took a long time to ship.

The first fix was creating a set of well-documented APIs to organize the development environment. That helped, but Amazon still struggled to build applications quickly as the company grew and hired more engineers — building just the database, compute, and storage components for a project could take three months on its own, even when the entire project was only expected to take three months total. Teams kept building their own resources from scratch, without planning for scalability or reusability across the company.

The real fix was building internal services that provided highly available, scalable, reliable architecture *as a foundation*, so individual teams didn't have to rebuild it every time. In 2006, Amazon began selling those internal services externally as Amazon Web Services, starting with Amazon Simple Queue Service (Amazon SQS), followed by Amazon Simple Storage Service (Amazon S3) and Amazon Elastic Compute Cloud (Amazon EC2).

The lesson worth carrying forward: AWS itself exists because ad hoc, unplanned architecture doesn't scale — not just technically, but organizationally. Cloud architecting, as a discipline, is the accumulated answer to exactly the problem Amazon ran into building its own ecommerce platform.

## The Cloud Architect's Perspective

Throughout this course, it helps to hold three considerations in mind on every design decision, all from the cloud architect's point of view:

- **Understand the practice itself** — applying cloud best practices to meet both an organization's technical needs and its business use cases, not just one or the other.
- **Evaluate with the Well-Architected Framework** — a consistent way to check whether a design actually holds up, rather than relying on gut feeling.
- **Apply best practices to what you build** — patterns that have already been tested at scale, so you're not re-learning Amazon's 2000-era lessons the hard way.

Keep working backward from the business need to the architecture, the same habit Module 1 introduced with the café's very first website request — that habit doesn't change as the scenarios get more complex; it just gets applied to harder problems.

## The AWS Well-Architected Framework, Revisited

You met the Well-Architected Framework's six pillars back in CLF-C02 Module 9 — Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability. That was the conceptual introduction: know the six names, know roughly what each one protects against.

This course uses the Framework differently. Instead of treating it as a list to recognize, you'll use it as an actual **evaluation tool** — a structured way to review a real (or proposed) architecture and find its gaps, the same way AWS itself uses it internally and the same way Olivia, the café's solutions architect consultant, would when reviewing the café's next architecture update. Concretely, that means:

- Asking pillar-specific questions of a design (*"How does this recover from an Availability Zone failure?"* is a Reliability question; *"What happens to this bill if traffic triples?"* is a Cost Optimization question).
- Recognizing that pillars often trade off against each other — more redundancy usually costs more, tighter security can add friction — and a well-architected system makes those trade-offs on purpose, not by accident.
- Using design principles (like the ones from CLF-C02 Module 9 — stop guessing capacity, test at production scale, automate, allow for evolutionary architectures, drive architectures with data, improve through game days) as cross-cutting habits that apply no matter which pillar you're focused on.

You'll return to the Well-Architected Framework repeatedly for the rest of this course — not as a new topic each time, but as the lens every later module gets viewed through.

## Best Practices for Building Solutions on AWS

"Best practice" gets used loosely in tech, so it's worth being precise about what it means in an AWS architecture context: a pattern that has already been tested at scale, by AWS and by its customers, that reliably avoids a known failure mode. A few examples that recur throughout this course:

| Best practice | What it protects against |
|---|---|
| Design for failure — assume any single component can fail | A single point of failure taking down the whole system |
| Decouple components | A failure or slowdown in one part of the system cascading into every other part |
| Implement elasticity | Paying for permanent capacity sized for a rare peak |
| Automate wherever possible | Manual, error-prone, unrepeatable deployment processes |
| Use multiple storage options | Forcing every kind of data into one storage service regardless of fit |

Notice these aren't AWS-specific tricks — they're general distributed-systems wisdom that AWS's own services are built to make easy to apply. Learning the best practice matters more than memorizing which specific service implements it, because the same best practice usually maps to more than one valid service choice depending on the situation.

## Making Informed Decisions About Where to Place AWS Resources

You met Regions, Availability Zones, and edge locations conceptually back in CLF-C02 Module 1. As an architect, "where do I put this?" stops being a background fact and becomes an active design decision, driven by the same four factors — now with real weight behind each one:

| Factor | The architect's question |
|---|---|
| Latency | Which Region keeps this workload physically close to the users who'll actually use it? |
| Price | Does the cost difference between candidate Regions change the decision, especially at scale? |
| Compliance | Does a data-residency law or contractual requirement force this workload into a specific country or jurisdiction? |
| Service availability | Does every AWS service this architecture depends on actually exist in the Region being considered? |

Within a chosen Region, the same "don't put all your eggs in one basket" logic applies one level down: spreading resources across multiple Availability Zones protects against a single data center failure, the same habit introduced in CLF-C02 Module 1 and reinforced constantly since. As the course progresses into networking, high availability, and disaster recovery modules, this placement logic gets one layer more sophisticated each time — first within a Region, later across Regions entirely.

---

## What to skip

You don't need to memorize the exact three-month development-time figure from Amazon's early history, or a specific year-by-year AWS service launch timeline — the point of the origin story is the lesson (unplanned architecture doesn't scale), not the trivia. Similarly, don't try to memorize every AWS best practice as an exhaustive checklist; the goal for this course is recognizing the *category* of problem a best practice solves, so you can apply the right one to a scenario you haven't seen before.

## Key takeaways

- Cloud architecting means applying best practices to meet both technical needs and business use cases at once — a design that only satisfies one of those isn't actually well-architected.
- AWS itself exists because Amazon's own unplanned, siloed architecture didn't scale — the internal fix became AWS's first three services (SQS, S3, EC2) in 2006.
- The Well-Architected Framework's six pillars, introduced conceptually in CLF-C02, now get used as an active evaluation tool for real designs, not just a list to recognize.
- Best practices are tested-at-scale patterns that avoid known failure modes — worth learning by category (design for failure, decouple, elasticity, automate, right storage for the job), not as an exhaustive checklist.
- Placing resources is a deliberate decision built on latency, price, compliance, and service availability at the Region level, and Availability Zone spread within it.

## Further reading

- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — the official, current source for the six pillars and design principles.
- [Overview of Amazon Web Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/) — AWS's own whitepaper covering the platform's breadth, useful background for placement and service-selection decisions.
- [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) — AWS's current, authoritative map of Regions and Availability Zones.

*Historical details, service names, and best-practice examples mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 1 — Welcome to AWS Academy Cloud Architecting](01-welcome-to-cloud-architecting.md) · **Quiz:** [Module 2 Quiz](../quizzes/02-introducing-cloud-architecting-quiz.md) · **Activity:** [Module 2 Activity](../labs/02-introducing-cloud-architecting-activity.md)
