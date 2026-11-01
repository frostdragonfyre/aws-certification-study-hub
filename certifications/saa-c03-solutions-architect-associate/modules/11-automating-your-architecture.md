<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](10-implementing-monitoring-elasticity-and-high-availability.md) · [Next module](12-caching-content.md) · [Quiz](../quizzes/11-automating-your-architecture-quiz.md) · [Slides](../lectures/11-automating-your-architecture.pptx)
<!-- /hub-navigation -->

# Module 11: Automating Your Architecture

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

Every piece of the café's architecture through Module 10 was built by hand — click through the console, configure the VPC, launch the instances, attach the load balancer. That works once. It does not work the second time, and it definitely doesn't work when Sofía wants an identical environment in a second AWS Region for disaster recovery, or when Frank asks "what exactly is our production setup right now?" and the honest answer is "whatever accumulated from months of console clicks."

This is Module 1's V6 milestone: automate deployments so the café can consistently deploy, manage, and update resources — including deploying the same stack to another Region. This module is about **infrastructure as code**: describing infrastructure in a file instead of building it by hand, so it becomes repeatable, reviewable, and versionable the same way application code already is.

## Learning objectives

By the end of this module, you should be able to:

- Explain what AWS CloudFormation does and why infrastructure as code matters
- Describe a CloudFormation template's core structure and what a stack actually is
- Explain what a change set is and why it matters before updating a live stack
- Describe what AWS Systems Manager adds beyond individual services like EC2 and Secrets Manager
- Compare AWS Elastic Beanstalk to building infrastructure directly, and know when each fits

---

## AWS CloudFormation: Infrastructure as Code

**AWS CloudFormation** lets you describe AWS infrastructure in a text file — a **template** — and have AWS provision, configure, and connect every resource in it automatically, in the right order, based on how you declared they depend on each other. Write the VPC, subnets, route tables, EC2 instances, and RDS database once, in one file, and CloudFormation builds the actual AWS resources to match.

The value isn't just "less clicking." A template is version-controllable — checked into the café's own repository, reviewed like any other change, with a clear history of exactly what changed and why. It's repeatable — the same template deploys an identical environment in a second Region for the café's V6 milestone, instead of an engineer trying to remember and re-click every setting by hand. And it's self-documenting — the template *is* the accurate, current description of what's actually deployed, which directly answers Frank's "what's our production setup?" question.

### Templates and stacks

A CloudFormation **template** is the file you write — JSON or YAML — describing the desired resources and their properties. A **stack** is what you get when CloudFormation actually deploys that template: a single, managed unit representing every resource the template created. Update the template and apply it to the stack, and CloudFormation figures out exactly which underlying resources need to change, be replaced, or be left alone — you don't manually track that yourself.

Deleting a stack deletes every resource it created, cleanly, in the correct dependency order — which is also why a stack, not a pile of individually-clicked resources, is the right unit for tearing down a temporary environment (like a test replica of the café's stack) without hunting down loose resources afterward.

### Change sets: seeing the blast radius before you pull the trigger

Updating a live, running stack is risky if you can't see what will actually happen first. A **change set** is a preview: CloudFormation calculates exactly what would change — which resources would be modified in place, which would be replaced entirely (meaning downtime or data loss risk), and which would be deleted — *before* anything actually happens. You review the change set, and only then choose to execute it or discard it.

> ⚠️ **Exam trap:** some resource property changes can only be applied by **replacing** the resource entirely (a new resource is created, the old one deleted) rather than updating it in place — for a stateful resource like an RDS database, that's a serious, easy-to-miss risk. A change set is exactly how you catch "this update will actually replace your database" before it happens instead of after.

## AWS Systems Manager: Operating What You've Automated

Provisioning infrastructure with CloudFormation is half the story — Systems Manager is about **operating** it afterward, at scale, without console clicking or manual SSH. You've already met one piece of Systems Manager: Parameter Store, from Module 9. It's part of a larger suite of operational tools:

- **Session Manager** provides secure shell access to an EC2 instance without opening an inbound SSH port at all, and without managing SSH keys — access is controlled entirely through IAM, and every session can be logged for audit purposes. For the café's web tier, this closes off a whole category of exposure that a traditional "open port 22 to the world" setup carries.
- **Automation** runs predefined or custom workflows across your resources — like patching every instance in a fleet on a schedule, without touching each one individually.
- **Patch Manager** automates applying operating system and software patches across a fleet of instances on a defined schedule, instead of an administrator manually patching each one.

The thread connecting all of this back to earlier modules: Systems Manager is what makes an architecture *operable* at the scale Module 10's Auto Scaling group could actually reach — patching, accessing, and automating tasks across a fleet of instances that might not even have fixed, memorized identities anymore.

## AWS Elastic Beanstalk: A Faster On-Ramp

CloudFormation gives you precise, explicit control over every resource — which is powerful, and also real work to write and maintain. **AWS Elastic Beanstalk** trades some of that control for speed: you upload your application code, and Beanstalk automatically handles provisioning the underlying infrastructure — EC2 instances, a load balancer, Auto Scaling — using AWS-managed defaults, while still letting you access and adjust the underlying resources if needed.

The honest comparison: Elastic Beanstalk is faster to get started with and asks less infrastructure knowledge of the person deploying, which matters for a small team like the café's without a dedicated infrastructure engineer. CloudFormation gives precise, versioned control over every resource and its exact configuration, which matters more as the architecture grows more specific and deliberate — like everything built across Modules 7 through 10.

| | Elastic Beanstalk | CloudFormation |
|---|---|---|
| What you provide | Application code | A template describing every resource |
| Control over resources | Managed defaults, still adjustable | Full, explicit control |
| Best for | Getting an app running quickly | Precise, repeatable, complex environments |
| Learning curve | Lower | Higher |

> ⚠️ **Exam trap:** Elastic Beanstalk still uses real underlying AWS resources — EC2, ELB, Auto Scaling — it isn't a separate, magical compute model. The distinction the exam tests is *who manages the provisioning decisions*, not what's actually running underneath.

## Putting It Together: The Café's V6 Architecture

For the café's V6 milestone specifically — a version-controlled template that deploys the network and application layers, then redeploys the same stack to another Region — CloudFormation, not Elastic Beanstalk, is the right tool: the café's architecture by this point (VPC, subnets, route tables, gateways, an ALB, an Auto Scaling group, RDS Multi-AZ) is exactly the kind of precise, multi-resource, already-deliberately-designed environment CloudFormation is built to capture and reproduce exactly. The template becomes the single source of truth Sofía and Nikhil can both read, version, and redeploy — in the primary Region, or, for disaster recovery, in a second one — without re-clicking through months of accumulated console configuration.

## What to skip

You don't need to write CloudFormation templates from scratch in JSON or YAML syntax, memorize every Systems Manager document type, or configure Elastic Beanstalk's platform-specific settings in depth — those are hands-on skills for the guided lab, not exam vocabulary. What matters here is the concept of infrastructure as code, what a stack and a change set are, what Systems Manager adds operationally, and when Elastic Beanstalk is the better trade-off over CloudFormation.

## Key takeaways

- CloudFormation turns infrastructure into a version-controlled, repeatable template — a stack is the deployed, managed result of applying one.
- A change set previews exactly what a stack update will do — including which resources get replaced, not just modified — before you commit to it.
- Systems Manager operates what's already provisioned: Session Manager for keyless, auditable access; Automation for workflows at scale; Patch Manager for fleet-wide patching.
- Elastic Beanstalk trades explicit control for speed — upload code, get managed infrastructure — while CloudFormation trades speed for precise, versioned control.
- For a specific, already-designed multi-resource environment like the café's, CloudFormation is the right tool for the V6 milestone: reproducing it exactly, including in a second Region.

## Further reading

- [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) — templates, stacks, and change sets in full detail.
- [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) — the full capability suite beyond what this module covers.
- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html) — supported platforms and configuration options.

---

**Next:** [Module 12 — Caching Content](12-caching-content.md)
