# Module 9: Cloud Architecture

**Exam:** CLF-C02 — AWS Certified Cloud Practitioner
**Domain:** Domain 1 — Cloud Concepts (Well-Architected Framework)
**Estimated study time:** 45 minutes

## Why this matters

Every service covered so far in this course is a piece of infrastructure. This module is about how those pieces get assembled into something that actually holds up — the difference between a collection of AWS services and a genuinely well-designed system. Architecture, in the traditional sense, is the art and science of designing and building large structures; cloud architects do the same job for technology, working with decision makers to identify business goals and with delivery teams to make sure a solution's technical features actually serve those goals.

AWS's answer to "what does a good cloud architecture actually look like" is the **AWS Well-Architected Framework** — not a specific product, but a set of questions and best practices developed by reviewing thousands of real customer architectures. This module covers the Framework's six pillars and general design principles, then two services that operationalize good architecture in practice: reliability/high availability patterns and AWS Trusted Advisor.

## Learning objectives

By the end of this module, you should be able to:

- Describe the AWS Well-Architected Framework, including its six pillars
- Identify the Framework's general design principles
- Explain the importance of reliability and high availability
- Identify how AWS Trusted Advisor helps customers
- Interpret AWS Trusted Advisor recommendations
- Avoid the most common cloud architecture traps on the exam

---

## What Is the AWS Well-Architected Framework?

The **AWS Well-Architected Framework** is a guide designed to help you build the most secure, high-performing, resilient, and efficient infrastructure possible for your cloud workloads. It's three things at once:

- A guide for designing infrastructures that are secure, high-performing, resilient, and efficient
- A consistent approach to evaluating and implementing cloud architectures
- A set of best practices developed through lessons learned by reviewing thousands of real customer architectures on AWS

It provides a set of foundational questions you can ask about any workload to evaluate how well it's actually architected — not a checklist of specific services, but a way of thinking about trade-offs.

## The Six Pillars

The Framework organizes its guidance into six pillars, each addressing a different dimension of a well-designed system:

| Pillar | What it's about |
|---|---|
| **Operational Excellence** | Running and monitoring systems, and continuously improving processes |
| **Security** | Protecting information, systems, and assets |
| **Reliability** | The ability to recover from failure and meet demand |
| **Performance Efficiency** | Using resources efficiently, and keeping up as demand and technology evolve |
| **Cost Optimization** | Avoiding unnecessary costs |
| **Sustainability** | Minimizing the environmental impact of running cloud workloads |

> ⚠️ **Exam trap:** the exam expects you to know there are six pillars and roughly what each one covers — not to rank them or pick a "most important" one. Every real architecture makes trade-offs between pillars (more redundancy costs more, tighter security can add friction); the Framework's job is to make those trade-offs deliberate instead of accidental.

## General Design Principles

Separate from the six pillars, the Framework also lists general design principles that apply across all of them — habits of a well-architected system, regardless of which pillar you're focused on:

- **Stop guessing your capacity needs.** Use elasticity (Module 10 territory) instead of over-provisioning for a peak that may never come.
- **Test systems at production scale.** Use the cloud to spin up a full-scale test environment on demand, then tear it down — something impractical with physical hardware.
- **Automate to make architectural experimentation easier.** Automation makes it cheap to create, replicate, and retire environments, which makes experimentation safer.
- **Allow for evolutionary architectures.** Design for change, since business and technical requirements shift over time — a static architecture ages badly.
- **Drive architectures using data.** Collect data on how the architecture actually performs, and let that data inform decisions instead of assumptions.
- **Improve through game days.** Simulate real events, including failures, in production (or production-like) environments to find weaknesses before they cause real incidents.

> ⚠️ **Exam trap:** these are principles about *how to design*, not the six pillars themselves — a question asking for a design principle (like "test at production scale") shouldn't be answered with a pillar name (like "Reliability"), even though the two are related.

## Reliability and High Availability

**Reliability** is a system's ability to recover from infrastructure or service disruptions, dynamically acquire resources to meet demand, and mitigate disruptions like misconfigurations or transient network issues. It's one of the six pillars, but it's worth calling out specifically because it ties together concepts from earlier in this course.

**High availability** — minimizing downtime, so a system stays operational as close to 100% of the time as possible — is a practical expression of reliability, and it's built from patterns already covered in this course:

- Spreading resources across multiple **Availability Zones** (Module 3), so a single data-center failure doesn't take down the whole application
- **Multi-AZ database deployments** (Module 8), so a database failure fails over automatically
- **Auto Scaling and Elastic Load Balancing** (Module 6), so capacity matches demand and traffic routes around unhealthy resources

> ⚠️ **Exam trap:** high availability and disaster recovery are related but different scopes. High availability is about minimizing downtime for common, smaller-scale failures (an instance or AZ going down); true disaster recovery (a full Region-level event) is a separate, more deliberate and expensive design decision — the same distinction Module 3 drew between multi-AZ and multi-Region.

## AWS Trusted Advisor

**AWS Trusted Advisor** is an online tool that provides real-time guidance to help you provision resources following AWS best practices. It inspects your account and makes recommendations across five categories:

| Category | What it checks |
|---|---|
| Cost Optimization | Underused or idle resources costing money for no benefit |
| Performance | Configurations that could be limiting performance |
| Security | Gaps like overly permissive security groups or MFA not enabled on root |
| Fault Tolerance | Missing redundancy, like a database without Multi-AZ enabled |
| Service Limits | Resources approaching their account service quota |

Trusted Advisor's core checks are available to every account for free. The full set of checks, across all five categories, requires a **Business or Enterprise support plan** — a direct callback to Module 2's support plan tiers.

> ⚠️ **Exam trap:** "which service tells you if your S3 buckets have overly permissive access, your Service Limits are close to being hit, and you have idle EC2 instances, all in one place" is Trusted Advisor — a single tool spanning cost, performance, security, fault tolerance, and service limits, not five separate services.

## Putting It Together

A useful way to hold this module together: the Well-Architected Framework is the *thinking framework* (six pillars, general design principles), reliability and high availability are a *deep dive into one pillar* using patterns from earlier modules, and Trusted Advisor is a *tool* that automatically checks a real account against several of those same pillars at once.

---

## What to skip

You don't need to memorize every question in the Well-Architected Framework's official whitepapers or run an actual Trusted Advisor scan — that hands-on depth belongs to the Solutions Architect Associate exam and beyond. For Cloud Practitioner, focus on naming the six pillars, recognizing the general design principles as principles (not pillars), and knowing what Trusted Advisor checks.

## Key takeaways

- The AWS Well-Architected Framework is a guide, a consistent evaluation approach, and a set of best practices — not a specific product — built from reviewing real customer architectures.
- The six pillars are Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.
- The general design principles (stop guessing capacity, test at production scale, automate, allow for evolution, drive with data, improve through game days) are separate from the six pillars — habits, not categories.
- Reliability is the ability to recover from disruption and meet demand; high availability is its practical expression, built from Multi-AZ, Auto Scaling, and load balancing patterns already covered in this course.
- AWS Trusted Advisor checks an account across five categories — Cost Optimization, Performance, Security, Fault Tolerance, and Service Limits — with full checks requiring a Business or Enterprise support plan.

## Further reading

- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/) — the official Framework, whitepapers, and the six pillars in full depth.
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) — category details and support-plan requirements.

*Service capabilities mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 8 — Databases](08-databases.md) · **Next:** [Module 10 — Auto Scaling and Monitoring](10-auto-scaling-and-monitoring.md) · **Quiz:** [Module 9 Quiz](../quizzes/09-cloud-architecture-quiz.md) · **Activity:** [Module 9 Activity](../labs/09-cloud-architecture-activity.md)
