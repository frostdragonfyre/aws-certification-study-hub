<!-- hub-navigation -->
[Course index](../README.md) · [Next module](02-architecting-network-connectivity-strategies.md) · [Quiz](../quizzes/01-welcome-to-solutions-architect-professional-quiz.md) · [Slides](../lectures/01-welcome-to-solutions-architect-professional.pptx)
<!-- /hub-navigation -->

# Module 1: Welcome to Solutions Architect Professional

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 30 minutes

## Why this matters

SAA-C03 ended with a single, working, well-architected system: one café, one AWS account, one Region with a disaster recovery plan. That's the right scope for an associate-level architect — design and operate one workload well.

Professional-level work starts the moment that workload stops being the only thing you're responsible for. This module introduces the case study for the rest of this course: the café you spent sixteen modules building has been acquired into a larger hospitality group, and the architecture decisions in front of you now span multiple businesses, multiple AWS accounts, and one legacy system that has never touched the cloud at all. None of that changes how EC2 or RDS works. It changes what "the right answer" has to account for.

## Learning objectives

By the end of this module, you should be able to:

- Explain what distinguishes the Professional-level exam from the Associate-level exam, beyond difficulty
- Describe the SAP-C02 exam's four domains and roughly what share of the exam each one represents
- Explain what a multi-account AWS environment is and why organizations adopt one
- Describe the new case study for this course and the organizational complexity it introduces
- Identify which of the four exam domains a given scenario in this course maps to

---

## From Associate to Professional: What Actually Changes

The SAA-C03 exam asks: given a set of requirements, can you design and deploy a correct, reasonably well-architected solution inside a single account? The SAP-C02 exam asks a different question: given a requirement that spans multiple accounts, multiple teams, an existing production system you don't get to rebuild from scratch, and constraints your predecessor already baked in, can you design a solution that actually fits?

Three shifts show up constantly across the professional-level material:

- **Organizational scope.** Associate-level scenarios are usually one workload in one account. Professional-level scenarios routinely span multiple AWS accounts belonging to one organization, with different teams, different compliance requirements, and shared services (like networking and identity) that have to work consistently across all of them.
- **Existing systems, not blank slates.** A large share of the professional exam is about improving, migrating, or integrating with something that already exists and is already in production — not designing a brand-new system where every choice is open. "This already runs this way, for reasons; what's the best next step?" is a very different design problem than "design this from scratch."
- **Trade-offs stated as trade-offs.** Associate-level questions often have one design that's simply correct. Professional-level questions more often present two or three designs that all technically work, and ask which one best fits a specific stated priority — cost, operational overhead, migration timeline, compliance requirement — because in real professional practice, "it depends on what you're optimizing for" is usually the honest answer.

None of this means the underlying services are different. RDS is still RDS. What's different is the scope of what you're asked to reason about, and how many legitimate-but-imperfect options you're expected to weigh against each other.

## The SAP-C02 Exam: Four Domains

The exam is organized into four domains, weighted differently:

| Domain | Weight | What it's asking |
|---|---|---|
| Domain 1: Design Solutions for Organizational Complexity | 26% | Networking, security, multi-account structure, and cost strategy *across* an organization, not inside one workload |
| Domain 2: Design for New Solutions | 29% | Designing new systems — deployment, business continuity, security, reliability, performance, cost — the largest single domain |
| Domain 3: Continuous Improvement for Existing Solutions | 25% | Taking something already running in production and making it operationally better, more secure, faster, more reliable, or cheaper |
| Domain 4: Accelerate Workload Migration and Modernization | 20% | Moving existing on-premises or legacy workloads into AWS, and modernizing them once they're there |

Two things worth noticing about this table. First, "new solutions" (Domain 2) is the biggest single chunk, but the other three domains — organizational complexity, improving what exists, and migration — together make up nearly three-quarters of the exam. This exam is not primarily about greenfield design the way the associate exam was. Second, this course maps directly to these four domains: Modules 2 through 6 cover Domain 1's five tasks one at a time, Modules 7 through 12 cover Domain 2's six tasks, Modules 13 and 14 cover Domain 3, and Modules 15 and 16 cover Domain 4. By the end of Module 16, every task statement in the exam guide will have had a dedicated module.

> ⚠️ **Exam trap:** it's tempting to assume the exam is mostly about knowing more services than the associate exam. It isn't, mainly. It's about applying services you likely already know to multi-account, multi-stakeholder, already-in-production situations — and picking the option that fits the *stated* priority rather than the option that's abstractly "best."

## What a Multi-Account AWS Environment Is

At the associate level, "the AWS account" was mostly invisible — there was one account, and everything the café built lived in it. At the professional level, the account boundary becomes a design decision in its own right.

A **multi-account AWS environment** is exactly what it sounds like: an organization runs its workloads across more than one AWS account, rather than putting everything into a single account. Common reasons include:

- **Isolation.** A security incident, a runaway cost, or a broken deployment in one account doesn't automatically threaten workloads in another account.
- **Billing clarity.** Costs for one team, one brand, or one environment (production versus development) are visible on their own, instead of blended into one bill.
- **Blast radius.** Permissions granted in one account don't automatically extend into another — someone with broad access to a development account doesn't get that same access to production by default.
- **Compliance boundaries.** A workload that has to meet a specific regulatory requirement can live in an account scoped and governed specifically for that requirement, without constraining every other workload in the organization to the same rules.

**AWS Organizations** is the AWS service that ties multiple accounts together into one manageable structure — consolidated billing, account creation, and policy-based guardrails applied consistently across accounts. You'll go deeper on AWS Organizations, service control policies, and multi-account design specifically in Module 5. For now, the point is narrower: once an organization has more than one AWS account, "which account should this live in, and what needs to be consistent across all of them" becomes a real design question — and it's a question the associate exam never asked, because the café only ever had one account.

## Putting It Together: Meridian Hospitality Group

Here's where this course's case study picks up.

The café Frank and Martha opened — the one you spent all sixteen SAA-C03 modules building, with Sofía and Nikhil handling the architecture and engineering — did well. Well enough that a regional hospitality investment group took notice, and six months ago, the café was acquired and became the founding brand of a new holding company: **Meridian Hospitality Group**.

The café itself now operates as a formally branded business unit called **Café Sol** — a name it never needed as an independent single-location business, but one it acquired the moment it became part of something larger with its own legal structure, its own board, and its own naming conventions for subsidiaries. Frank and Martha still run day-to-day operations. Sofía, who built Café Sol's original AWS architecture, has been promoted to **Lead Solutions Architect for Meridian Hospitality Group** — she's no longer responsible for one workload, she's responsible for architecture decisions across everything Meridian owns. Nikhil has moved into a platform engineering role supporting all of Meridian's brands. Reporting to Meridian's VP of Engineering, **Priya Anand**, Sofía's mandate for this course is explicit: "You built one great system. Now build the strategy that lets us run several, correctly, across accounts that don't currently talk to each other."

Meridian currently owns three brands, each at a very different point in its AWS journey:

- **Café Sol** — the original café, already running well-architected, production infrastructure in a single AWS account, built across SAA-C03's sixteen modules.
- **Haven & Co. Hotels** — a small boutique hotel chain Meridian acquired around the same time as Café Sol, running its own, separately-managed AWS account with its own reservation and property-management systems.
- **Ridgeline Diner Co.** — a 40-year-old regional diner chain, acquired just last quarter, that has never used AWS, or any public cloud, at all. Ridgeline's point-of-sale systems, inventory tracking, and back-office reporting all run on physical servers in a back room at company headquarters, maintained by a two-person IT team that's now part of Meridian.

Three brands, three different starting points, one Lead Solutions Architect responsible for making them work together sensibly — without breaking what already works at Café Sol, without disrupting Haven & Co.'s guest-facing systems, and with a clear plan for bringing Ridgeline out of that back room. That's the shape of professional-level work, and it's the throughline for the rest of this course: Domain 1's organizational-complexity modules establish how Meridian's accounts, network, security, and cost strategy should work *across* all three brands; Domain 2's modules design new solutions Meridian needs going forward; Domain 3 improves what Café Sol and Haven & Co. already have running; and Domain 4 gets Ridgeline out of that back room and into AWS.

## What to skip

You don't need to memorize the exact percentage weight of each domain — knowing their relative size (Domain 2 largest, then Domain 1, then Domain 3, then Domain 4) is enough. You also don't need AWS Organizations implementation detail yet; that's Module 5's job. This module is orientation — the goal is understanding the shape of the exam and the case study, not depth on any one topic.

## Key takeaways

- SAP-C02 tests reasoning across multiple accounts, existing production systems, and stated trade-offs — not primarily a longer list of services than the associate exam.
- The exam has four domains: Design Solutions for Organizational Complexity (26%), Design for New Solutions (29%, the largest), Continuous Improvement for Existing Solutions (25%), and Accelerate Workload Migration and Modernization (20%).
- A multi-account AWS environment splits workloads across separate AWS accounts for isolation, billing clarity, blast-radius containment, and compliance boundaries; AWS Organizations ties multiple accounts together into one manageable structure.
- This course's case study now follows Meridian Hospitality Group, the holding company that acquired the SAA-C03 café (now branded Café Sol) along with Haven & Co. Hotels and Ridgeline Diner Co. — three brands at three different points in their AWS journey.
- The rest of this course maps directly to the exam's four domains, in order: Modules 2–6 (Domain 1), Modules 7–12 (Domain 2), Modules 13–14 (Domain 3), Modules 15–16 (Domain 4).

## Further reading

- [AWS Certified Solutions Architect – Professional Exam Guide](https://d1.awsstatic.com/training-and-certification/docs-sa-pro/AWS-Certified-Solutions-Architect-Professional_Exam-Guide.pdf) — the official domain breakdown and task statements this course is built around.
- [Organizing Your AWS Environment Using Multiple Accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) — AWS's own guidance on why and how organizations split workloads across accounts.
- [AWS Organizations User Guide](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) — a preview of the service Module 5 covers in depth.
