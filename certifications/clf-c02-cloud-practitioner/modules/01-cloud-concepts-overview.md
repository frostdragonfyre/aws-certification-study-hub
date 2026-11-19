<!-- hub-navigation -->
[Course index](../README.md) · [Next module](02-cloud-economics-and-billing.md) · [Quiz](../quizzes/01-cloud-concepts-overview-quiz.md) · [Slides](../lectures/01-cloud-concepts-overview.pptx)
<!-- /hub-navigation -->

# Module 1 · Cloud Concepts Overview

**AWS Certified Cloud Practitioner (CLF-C02)** · 35–45 minutes · No AWS account required

## The registration rush

Juniper Community Center runs weekend workshops. Registration opens at noon on the first Monday of each month. The site usually handles about 40 requests per minute, then jumps to 800 per minute for a short window. Assume the current web tier handles its usual traffic comfortably. The team also keeps some member records in an office system that must stay on-site.

Should Juniper buy enough equipment for noon on registration day, or use infrastructure it can adjust as demand changes? Keep that question in mind as you work through the module.

## Learning objectives

- Recognize the characteristics and benefits of cloud computing in a scenario.
- Distinguish deployment models from service models and assign operational responsibilities.
- Explain how usage, reliability, and location affect a cloud decision.
- Use the AWS Cloud Adoption Framework and AWS Well-Architected Framework to address different kinds of decisions.

## What changes when infrastructure is on demand?

Cloud computing lets teams provision computing resources over a network, adjust capacity as needs change, and track consumption. A cloud provider operates the physical infrastructure. The customer chooses which resources to use and how to configure their workload.

| Characteristic | What you could observe at Juniper |
| --- | --- |
| On-demand self-service | An authorized developer creates a test environment through a console or API. |
| Broad network access | Learners reach the registration service from phones or laptops over a network. |
| Resource pooling | The provider allocates capacity from shared infrastructure with isolation between customers. |
| Rapid elasticity | The web tier can add capacity near launch and release it when demand falls. |
| Measured service | The platform records usage, such as instance hours or storage consumed. |

Juniper can test a change sooner, add short-term capacity, and redirect staff time previously spent maintaining servers. Provider purchasing scale can lower unit costs, and a provider's geographic footprint can make expansion easier. Each benefit depends on how the team builds and operates the workload. Read the [AWS overview of cloud advantages](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/six-advantages-of-cloud-computing.html).

> ⚠️ **Exam trap:** Elasticity concerns adjusting to changing load. High availability concerns keeping the service accessible through failures. Juniper needs a capacity plan for the noon rush and a failure plan in case an instance becomes unavailable.

## The money shift

Buying servers typically requires capital expenditure (CapEx) up front. Running rented infrastructure typically produces operating expenses (OpEx) over time. Juniper can pay for additional compute around the event and release it afterward. It still needs to track baseline compute, retained storage, and applicable data transfer. Usage meters can coexist with flat fees, minimum charges, and commitments. The cost comparison depends on the workload and the pricing terms.

**Try it.** Assume Juniper runs two units of capacity for 22 hours and eight units total for the two-hour peak window. How many unit-hours does it use in a day? Compare that with running eight units for 24 hours. Explain one cost the calculation leaves out. Use your result when you get to [Module 2](02-cloud-economics-and-billing.md).

## Where the workload runs

| Deployment | Juniper example |
| --- | --- |
| Cloud | Juniper hosts the complete registration workload in AWS. |
| On-premises | Juniper keeps the whole workload on equipment it operates at its own site. |
| Hybrid | The registration site runs on AWS and exchanges approved data with the on-site member-records system. |

For hybrid decisions, name the requirement before choosing a service. A dedicated network connection points toward [AWS Direct Connect](https://aws.amazon.com/directconnect/). An encrypted network tunnel over the internet points toward [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/site-to-site-vpn/). [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) connects supported on-premises storage workflows to AWS. [AWS Outposts](https://aws.amazon.com/outposts/) extends selected AWS infrastructure and services to a customer location.

## How much the provider operates

| Service model | What the customer works with | Example |
| --- | --- | --- |
| Infrastructure as a service (IaaS) | A virtual machine and the operating system and applications it runs | Amazon EC2 |
| Platform as a service (PaaS) | An application deployment environment that handles more infrastructure operations | AWS Elastic Beanstalk |
| Software as a service (SaaS) | A finished application and the users, permissions, and data within it | A hosted registration application |

Deployment model describes where systems run. Service model describes the level at which the team works. A hybrid design can include an IaaS component. With Amazon EC2, AWS operates the underlying physical infrastructure and Juniper patches the guest operating system. With a finished SaaS application, the vendor operates the application and Juniper still controls who it grants access to. Check the [AWS shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) for how obligations vary by service.

## Regions, Availability Zones, and edge locations

A **Region** is a geographic area. An **Availability Zone** is an isolated infrastructure location within a Region. An **edge location** can bring services such as content delivery closer to users. Juniper can distribute the web tier across Availability Zones and design it to continue operating if one fails. It can use a content delivery network to cache suitable assets near visitors. [Module 3](03-aws-global-infrastructure-overview.md) works through location and reliability decisions in detail.

## Two frameworks for different decisions

The **AWS Cloud Adoption Framework (CAF)** helps an organization identify what it needs to change to adopt cloud services effectively. Match the work to the perspective.

| CAF perspective | Question for Juniper |
| --- | --- |
| Business | How will we know registration improved? |
| People | Who needs training before launch? |
| Governance | How will we oversee the migration and track its risks? |
| Platform | What cloud environment will support the site? |
| Security | How will we protect the records and respond to incidents? |
| Operations | Who monitors registration day and handles disruptions? |

The **AWS Well-Architected Framework** helps a team review a workload. The six pillars are operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability. For Juniper, a recovery drill exercises reliability, while a consistent procedure for reviewing incidents supports operational excellence. Use [AWS CAF](https://docs.aws.amazon.com/whitepapers/latest/overview-aws-cloud-adoption-framework/foundational-capabilities.html) and the [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) as references.

## Apply what you learned

Decide what Juniper should move, what should stay on-site, and who would patch the web servers if the team chooses EC2. Name one risk your recommendation still leaves open. Then do the [practice activity](../labs/01-cloud-concepts-overview-activity.md) and take the [quiz](../quizzes/01-cloud-concepts-overview-quiz.md). For the exam objectives behind this module, see [CLF-C02 Domain 1](https://docs.aws.amazon.com/aws-certification/latest/cloud-practitioner-02/cloud-practitioner-02-domain1.html).
