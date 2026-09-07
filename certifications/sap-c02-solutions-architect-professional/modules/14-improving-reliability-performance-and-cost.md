# Module 14: Improving Reliability, Performance, and Cost for an Existing Solution

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 13 reviewed Café Sol's operational and security posture. Tonight covers the other three legs of continuous improvement — Domain 3, Tasks 3.3, 3.4, and 3.5: is the system actually as reliable as it's assumed to be, is it sized correctly for how it's really used, and is Meridian actually getting what it's paying for. Three questions, one existing architecture, six months of real usage data to answer them with — data a brand-new workload never has.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish AWS Resilience Hub's assessment role from AWS Fault Injection Service's actual failure testing
- Explain why Compute Optimizer's recommendations are more precise for an existing workload than a new one
- Distinguish Savings Plans coverage from Savings Plans utilization, and explain what each metric actually tells you
- Design a complete reliability, performance, and cost improvement plan for a stated existing-solution scenario

---

## Testing Reliability, Not Just Designing It

Module 8 used **AWS Resilience Hub** to assess whether Meridian Loyalty's design — on paper — met its RTO and RPO targets. That was true before the system had ever actually failed. Café Sol has been running for six months, which raises a different question: does it actually survive a real failure, or does it just look like it should on paper?

**AWS Resilience Hub** answers the first question: it assesses an application's architecture against a defined resilience policy, based on the design itself — configuration, redundancy, backup strategy — without anything actually breaking.

**AWS Fault Injection Service (FIS)** answers the second: it deliberately injects real faults — terminating an instance, throttling an API, cutting off a subset of network traffic — into a running system, in a controlled experiment, to observe whether the design's assumed resilience actually holds up in practice. This is the SAP-C02 version of chaos engineering: verifying resilience by testing it, not just assessing it on paper.

Sofía runs both against Café Sol: **Resilience Hub** confirms the design is assessed as meeting its policy; **FIS** then actually terminates an instance in a controlled game day to confirm the failover Resilience Hub assessed actually executes correctly when something really goes wrong.

> ⚠️ **Exam trap:** the exam expects you to know that Resilience Hub assesses a design's resilience without breaking anything, while Fault Injection Service actually breaks something, deliberately and safely, to test whether that assessed resilience holds. A design that scores well in Resilience Hub hasn't necessarily been proven — only FIS actually proves it, by testing it for real.

## Right-Sizing with Real Usage Data

A brand-new workload, like Meridian Loyalty at launch, has no usage history — Module 11 and Module 12's compute decisions were necessarily based on the workload's expected characteristics, not its actual, observed behavior. Café Sol, six months in, has exactly what a new workload lacks: real, historical utilization data.

**AWS Compute Optimizer** analyzes that historical CloudWatch utilization data — CPU, memory (with the CloudWatch agent installed), network — across EC2 instances, Auto Scaling groups, EBS volumes, and Lambda functions, and produces specific, evidence-based recommendations: this instance is consistently over-provisioned and could move to a smaller size at lower cost; this one is under-provisioned and risks a performance problem under real load. These aren't generic best-practice guesses — they're precise, because they're built from what Café Sol's system has actually done for six real months.

Sofía runs Compute Optimizer against Café Sol's fleet and finds exactly what six months of real, lived-in operation tends to produce: an instance sized for a launch-day traffic guess that turned out too large, and another that's been quietly running hotter than it should.

## Auditing What's Already Being Spent

Module 12 was a forward-looking decision: which purchase option should Meridian Loyalty use, before it launched. Café Sol's Savings Plans, purchased when the system first went live, deserve a backward-looking audit now that six months of real spend exists to check them against.

- **Savings Plans coverage** measures what percentage of Café Sol's actual eligible usage is covered by a Savings Plan commitment, versus paying On-Demand rates. Low coverage means real spend is happening at On-Demand rates that a larger commitment could discount.
- **Savings Plans utilization** measures what percentage of the Savings Plan commitment itself is actually being used. Low utilization means Meridian is paying for commitment capacity that isn't being consumed — money spent on a commitment sitting partially idle.

These aren't the same problem, and they point to opposite fixes: low coverage suggests buying **more** commitment to capture more of real usage at a discount; low utilization suggests the existing commitment is **already too large** for actual usage and needs no more added — or even needs to be right-sized down at the next purchase decision.

> ⚠️ **Exam trap:** "usage that should be covered isn't" points to a coverage problem, fixed by more commitment. "Commitment that's been purchased isn't being used" points to a utilization problem, fixed by not buying more — the opposite direction. Reading which metric a scenario is actually describing is the whole question.

## Putting It Together: Café Sol's Reliability, Performance, and Cost Plan

Sofía's complete improvement plan for Café Sol:

- **Resilience Hub assessing the design, Fault Injection Service testing it for real** in a controlled game day — verified resilience, not just assumed resilience.
- **Compute Optimizer's evidence-based recommendations**, built from six real months of usage data no new workload has access to.
- **Savings Plans coverage and utilization**, reviewed separately, pointing to different fixes depending on which one is actually the gap.

## What to skip

You don't need to memorize FIS's exact supported fault-injection actions or Compute Optimizer's precise recommendation algorithm — that's implementation depth beyond this exam. What matters is telling assessment (Resilience Hub) apart from actual testing (FIS), understanding why historical data makes Compute Optimizer's recommendations more precise for existing workloads, and correctly distinguishing coverage from utilization for Savings Plans.

## Key takeaways

- AWS Resilience Hub assesses a design against a resilience policy without breaking anything; AWS Fault Injection Service actually tests that assessed resilience by deliberately, safely injecting real faults.
- Compute Optimizer's recommendations are precise specifically because they're built from an existing workload's real, historical utilization data — something a brand-new workload doesn't have.
- Savings Plans coverage (how much real usage is discounted) and utilization (how much purchased commitment is actually used) are different metrics pointing to opposite fixes — more commitment versus no more commitment.
- Continuous improvement, across operational excellence, security, reliability, performance, and cost, is what turns "this has run without incident" into "this has actually been verified, right-sized, and audited."
- Domain 3's tasks apply the same underlying rigor Domain 2 used to design Meridian Loyalty — to a system that's already live, using data a new system never has.

## Further reading

- [AWS Resilience Hub User Guide](https://docs.aws.amazon.com/resilience-hub/latest/userguide/introduction.html) — revisit from Module 8, now assessing an existing system.
- [AWS Fault Injection Service User Guide](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) — controlled fault injection experiments.
- [AWS Compute Optimizer User Guide](https://docs.aws.amazon.com/compute-optimizer/latest/ug/what-is-compute-optimizer.html) — evidence-based right-sizing recommendations.
- [AWS Cost Management: Savings Plans Coverage and Utilization](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-savings-plans.html) — the two metrics and what each one means.
