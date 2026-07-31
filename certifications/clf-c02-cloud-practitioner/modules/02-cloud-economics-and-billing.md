# Module 2: Cloud Economics and Billing

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 4 — Billing, Pricing, and Support (touches Domain 1)
**Estimated study time:** 45 minutes

## Why this matters

Module 1 established the shift from CapEx to OpEx and promised it would save money. This module is where that promise gets tested against real numbers. "Pay only for what you use" sounds simple until you're the one reading an invoice that jumped from $200 to $5,000 overnight, or trying to explain to a CFO why a cloud bill should be trusted more than a hardware quote with a single, comforting price tag on it.

Nearly every cost surprise on AWS — and nearly every cost question on this exam — traces back to one of a small number of ideas: how AWS actually charges you, what a fair cost comparison has to include, and which tool answers which billing question. Get those straight and the rest of this module is just detail.

## Learning objectives

By the end of this module, you should be able to:

- Explain AWS's four pricing principles and the three cost drivers behind almost every bill
- Compare the four EC2 purchase options and match a workload to the right one
- Identify what a fair Total Cost of Ownership (TCO) comparison has to include, and what people leave out
- Explain why some AWS services are "free to configure" but not free to run
- State how the AWS Free Tier works for accounts created since mid-2025
- Use AWS Organizations and cost allocation tags to make a multi-account bill manageable and accountable
- Navigate the four billing and cost management tools and know which one answers which question
- Compare the five AWS technical support plans and pick the right one for a scenario

---

## AWS's Pricing Philosophy

Everything about an AWS bill flows from four principles:

| Principle | What it means |
|---|---|
| Pay as you go | No upfront commitment, no long-term contract — turn it on and pay, turn it off and stop paying |
| Save when you reserve | Commit to 1 or 3 years of usage and pay substantially less than on-demand rates |
| Pay less by using more | Volume-based pricing tiers — the more you consume, the lower the per-unit price |
| Pay less as AWS grows | AWS gains efficiency at scale and has cut prices many times over the years |

> ⚠️ **Exam trap:** A question implying you pay *more* per unit as usage grows is testing the opposite of principle three. AWS pricing is built to reward volume, not punish it.

## Three Things Drive Almost Every Bill

If you remember only three words about AWS cost, make them these:

| Cost driver | How it's priced |
|---|---|
| Compute | Pay for the time your compute runs, usually per second or per hour — stop the instance, stop the charge |
| Storage | Pay for the data you keep, typically per GB per month — data sitting still still costs money |
| Data transfer | Pay to move data *out* of AWS; inbound is generally free, outbound is metered per GB |

> ⚠️ **Exam trap:** "Data in is free, data out costs money" is the single most commonly tested — and most commonly experienced — billing surprise. If a scenario describes an unexpectedly high bill tied to serving content to end users, data transfer out is almost always the culprit.

## Paying for Compute: The Four Purchase Options

Same server, four different ways to buy it — with up to roughly a 90% price difference between them. This is a guaranteed exam topic.

| Option | How it works | Best for |
|---|---|---|
| On-Demand | Pay by the second or hour, no commitment | Spiky or unpredictable workloads |
| Reserved Instances / Savings Plans | Commit to 1 or 3 years of usage for a large discount | Steady, predictable baseline workloads |
| Spot Instances | Bid on spare AWS capacity for deep discounts; AWS can reclaim it with little notice | Fault-tolerant, interruptible batch work |
| Dedicated Hosts | A physical server reserved just for you — the most expensive option | Licensing or compliance requirements that demand physical isolation |

> ⚠️ **Exam trap:** the exam telegraphs the answer through workload behavior, not the word "cheap." "Steady, 3-year workload" → Reserved/Savings Plan. "Can tolerate interruption" → Spot. "Unpredictable" → On-Demand. Running a customer-facing database on Spot, or a batch job nobody would notice failing on a 3-year Reserved Instance, are both scenario traps testing whether you matched the option to the workload's actual behavior.

## Storage and Data Transfer, in More Detail

**Storage** isn't a single flat rate:

- Priced per GB per month — you pay for what you store, while you store it.
- Storage *classes* change the price — frequently-accessed data costs more than archival data.
- Requests can cost too — reading or writing objects carries small per-request fees.
- Archival storage often charges a retrieval fee — cheap to store, but you pay to get it back quickly.

**Data transfer** depends on direction:

- Inbound to AWS: generally free — AWS wants your data.
- Outbound to the internet: metered per GB — this is the direction that surprises people.
- Between Regions: costs money — crossing Regions isn't free.
- Between Availability Zones: also generally charged, even inside a single Region.

## Free to Configure, Not Free to Run

Several AWS services cost nothing to use directly — but you still pay for the resources they create or manage underneath. This distinction shows up constantly on the exam and on real bills.

| Service | What's free | What's billed |
|---|---|---|
| Amazon VPC | Building the virtual network | NAT gateways and traffic inside it |
| IAM | Users, groups, roles, and policies | Always free — no exception |
| Auto Scaling | The scaling service itself | The instances it launches |
| CloudFormation | Infrastructure-as-code templates | The stack's underlying resources |
| AWS Organizations | Account structure and consolidated billing | Only what member accounts consume |
| Elastic Beanstalk | The orchestration layer | The EC2 and storage underneath |

> ⚠️ **Exam trap:** the pattern is always the same — the *management layer* is free, the *compute, storage, and traffic underneath* are not. A company setting up a VPC and confused why the bill isn't $0 has misunderstood this line, not been billed in error.

## The AWS Free Tier (Accounts Created Since Mid-2025)

The old "12 months free" description is out of date. Accounts created since mid-2025 use a credit model instead:

- **$100 in credits** applied automatically at signup.
- **Up to $100 more** earned by completing onboarding activities in the console.
- **The Free Plan ends early** — at 6 months, or when credits run out, whichever comes first.
- **30+ always-free services** offer permanent monthly allowances that continue regardless of the credit balance.

> ⚠️ **Exam trap:** on the Free Plan, the account can auto-close once credits are exhausted, and joining an AWS Organization can end a Free Plan's credits entirely. The practical habit that follows: set a budget alert on day one, not after the first surprising bill.

## Total Cost of Ownership (TCO)

Comparing a server's purchase price to an EC2 bill isn't a fair fight — TCO is what makes the comparison fair, by counting *every* cost of running a system over its life, not just what you paid at purchase.

Executives ask for a TCO analysis for three reasons: to justify a migration with evidence rather than a gut feeling, to budget honestly for costs that never appear on a purchase order but hit every year, and to compare on-premises, hybrid, and cloud options on the same scale.

**What people forget to count**, beyond the visible hardware price:

| Hidden cost | Why it's easy to miss |
|---|---|
| Facilities | Rent, build-out, floor space |
| Power and cooling | Runs 24/7, and never stops |
| Network gear | Switches, routers, cabling, bandwidth |
| IT labor | Racking, patching, monitoring, on-call |
| Backup and disaster recovery | A second site you hope you never need |
| Refresh cycles | Replacing hardware every 3–5 years |
| Idle capacity | Servers bought "just in case," running at a fraction of utilization |
| Downtime | Lost revenue when something breaks |

> ⚠️ **Exam trap:** any argument that reduces to "the purchase price is lower than N years of cloud bills" is almost always missing several of the items above. This is the single most common Total Cost of Ownership scenario on the exam, and it cuts both ways — "cloud is always cheaper" is just as much of an overreach as "on-prem is always cheaper." The correct objection is about *scope*, not a blanket claim in either direction.

## The AWS Pricing Calculator

The AWS Pricing Calculator (calculator.aws) is free, requires no AWS account, and is the standard way to estimate a workload's monthly cost before building anything. It lets you model a full architecture service by service, compare configurations and Regions side by side, and export or share the estimate with a link. The number it produces depends heavily on the assumptions you feed it — instance size, Region, commitment level — which is exactly why two people pricing "the same" workload often land on very different totals.

## AWS Organizations: Managing Many Accounts

Real companies rarely run one AWS account — they run dozens, split by team, environment, or business unit. AWS Organizations is how that stays manageable:

- **Consolidated billing** — one payer account, one bill for the whole organization.
- **Volume discounts** — usage is aggregated across all accounts, so the whole group reaches cheaper pricing tiers faster than any single account could alone.
- **Organizational Units (OUs)** — group accounts (Dev, Prod, Finance) and manage them as a unit.
- **Service Control Policies (SCPs)** — guardrails that set the *maximum* permissions an account can ever have, even for its own administrators.
- **Central governance** — apply security and compliance rules once, across every account.
- **Free to use** — Organizations itself costs nothing; you only pay for what member accounts consume.

> ⚠️ **Exam trap:** "restrict what an entire account can do, regardless of its own IAM policies" is a Service Control Policy question, not a plain IAM policy question — a regular IAM policy can't cap permissions above what an account's own administrators could otherwise grant themselves.

## Billing and Cost Management Tools

Four tools, four different questions. The exam tests whether you know which tool answers which one.

| Tool | Question it answers |
|---|---|
| AWS Bills | "What do I owe this month?" — the itemized invoice, broken out by service and account |
| Cost Explorer | "Where is the money going, and what's the trend?" — visualize, filter, and forecast spend |
| AWS Budgets | "Tell me *before* I overspend" — set thresholds and get alerted, or trigger an action, as you approach them |
| Cost and Usage Report (CUR) | "Give me every line item, raw" — the most granular billing data AWS provides |

> ⚠️ **Exam trap:** Budgets is the only one of the four that's forward-looking. If a question asks which tool alerts you *before* overspending, the answer is Budgets — not Cost Explorer, which only describes what already happened.

## Cost Allocation Tags

A bill that just says "EC2: $40,000" doesn't tell anyone which team or project is responsible. Cost allocation tags — simple key/value labels attached to resources — turn a lump sum into an answerable question:

| Without tags | With tags |
|---|---|
| EC2 ................ $40,000 | Project: Website ....... $18,000 |
| S3 ................... $8,000 | Project: Analytics ..... $26,000 |
| RDS ................ $12,000 | Env: Dev (idle!) ....... $16,000 |
| *"Which team? Which project? Who do I even ask?"* | *"Dev is costing us $16K — shut it down nights and weekends."* |

Tags are a small, deliberate habit — but they're how real FinOps teams turn an opaque bill into an actionable one.

## AWS Technical Support Plans

Five tiers, and the exam gives you a scenario and expects you to match it on two things: required response time, and whether a Technical Account Manager (TAM) is needed.

| Plan | Best for | Critical response | TAM |
|---|---|---|---|
| Basic (free) | Everyone; account and billing help only | No tech support | No |
| Developer | Experimenting, dev and test | Business hours, email | No |
| Business | Production workloads | Under 1 hour, 24/7 | No |
| Enterprise On-Ramp | Business-critical workloads | Under 30 minutes | Pool of TAMs |
| Enterprise | Mission-critical workloads | Under 15 minutes | Designated TAM |

Business is also the lowest tier that unlocks the *complete* set of AWS Trusted Advisor checks (see below).

> ⚠️ **Exam trap:** AWS has been consolidating these five tiers in the real world (Developer, Business, and Enterprise On-Ramp are being phased toward newer offerings), but CLF-C02 still tests the classic five above. Answer exam questions with this table, not with whatever AWS's console currently shows.

## AWS Trusted Advisor

Trusted Advisor scans an account and recommends improvements across five categories:

| Category | What it flags |
|---|---|
| Cost Optimization | Idle and underused resources you're still paying for |
| Performance | Bottlenecks and over-utilized resources |
| Security | Open permissions, missing MFA, exposed access keys |
| Fault Tolerance | Missing backups and single points of failure |
| Service Limits | Approaching an account quota |

The free tier gets a core set of checks; Business and Enterprise support unlock the full check list — the same Business-tier threshold mentioned above.

---

## What to skip

You don't need to memorize exact Free Tier dollar amounts or exact support-plan restructuring timelines — both change over time, and CLF-C02 tests the underlying logic (credit model, response-time tiers) rather than current figures. You also don't need pixel-level familiarity with the Pricing Calculator or Billing Dashboard console — the exam tests which tool answers which question, not button locations.

## Key takeaways

- AWS pricing rests on four principles: pay as you go, save when you reserve, pay less by using more, and pay less as AWS grows.
- Compute, storage, and data transfer drive almost every bill — and data transfer *out* is the direction that costs money.
- The four EC2 purchase options trade flexibility for discount: On-Demand (most flexible), Reserved/Savings Plans (steady workloads), Spot (interruptible), Dedicated Hosts (isolation requirements).
- A fair TCO comparison includes facilities, power, labor, refresh cycles, and idle capacity — not just a purchase price versus a subscription bill.
- Many AWS services are free to configure but bill you for the resources they create or manage underneath.
- AWS Budgets is the only billing tool that warns you *before* you overspend; Cost Explorer and the Cost and Usage Report describe what already happened.
- Cost allocation tags and AWS Organizations turn a lump-sum, multi-account bill into something a business can actually act on.
- Support plan questions resolve to two variables: required response time, and whether a TAM (and which kind) is needed.

## Further reading

- [AWS Pricing Calculator](https://calculator.aws/) — build a real estimate using this module's concepts.
- [AWS Organizations](https://aws.amazon.com/organizations/) — official documentation on consolidated billing, OUs, and SCPs.
- [Compare AWS Support Plans](https://aws.amazon.com/premiumsupport/plans/) — AWS's current, authoritative support tier comparison (verify against this if the tiers described above feel out of date by the time you're reading this).

*Prices, Free Tier terms, and support plan structures mentioned above are illustrative and change over time — verify current values at aws.amazon.com before relying on them.*

---

**Previous:** [Module 1 — Cloud Concepts Overview](01-cloud-concepts-overview.md) · **Next:** [Module 3 — AWS Global Infrastructure Overview](03-aws-global-infrastructure-overview.md) · **Quiz:** [Module 2 Quiz](../quizzes/02-cloud-economics-and-billing-quiz.md) · **Activity:** [Module 2 Activity](../labs/02-cloud-economics-and-billing-activity.md)
