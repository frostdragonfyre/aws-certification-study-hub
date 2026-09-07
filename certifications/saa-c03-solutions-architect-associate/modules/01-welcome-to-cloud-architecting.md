# Module 1: Welcome to AWS Academy Cloud Architecting

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 20 minutes

## Why this matters

Cloud Foundations answered "what is AWS, and what does it offer?" Cloud Architecting answers a different question: "given a real business, with real people and real constraints, how do you actually design something on AWS?" That shift — from knowing services exist to deciding how and when to use them — is the whole point of the next fifteen modules.

This first module doesn't teach a single AWS service. Instead, it does three things: lays out how the course itself works, introduces the running business case you'll design solutions for throughout the course, and places the "cloud architect" role among the other cloud computing roles you might already know. None of this is exam-scored material — think of it as the map before the trip.

## Learning objectives

By the end of this module, you should be able to:

- Recognize the basic elements of the café business case used throughout this course's challenge labs
- Describe the role of a cloud architect, and how it compares to other common cloud computing roles

---

## How This Course Is Built

Each module in Cloud Architecting pairs a few different kinds of material:

- **Student guides and instructor-led lecture content** — the concept explanation for each module, reinforced with videos.
- **Hands-on labs**, in two flavors:
  - **Guided labs** — step-by-step instructions, built to help you gain hands-on experience creating and configuring real AWS resources.
  - **Challenge labs** — built around the café business case below, these deliberately *don't* give you full click-by-click instructions. Instead, you apply what you learned in the guided labs and lectures to solve a less-scripted problem, the way a real architect would.
- **The AWS Academy Cloud Architecting Capstone** — an additional, longer-lived lab environment where you apply your learning with even less guidance. Unlike the other labs, the capstone environment persists across multiple days, so you can pick up where you left off.
- **Recorded demonstrations and instructor-led activities** — used throughout the course to illustrate specific topics.
- **Knowledge checks** — most modules (starting with Module 2) include a 10-question knowledge check and one sample certification-style exam question for class discussion. A cumulative course assessment pulls questions from across every module.

The point of separating guided labs from challenge labs is deliberate: guided labs build the muscle memory, and challenge labs — grounded in a business you actually understand by that point — test whether you can apply it without a script. That's a much closer simulation of the real job (and the exam's scenario-based questions) than following instructions alone.

## The Café Business Case

The challenge labs in this course are built around a single fictional business case, revisited and evolved module after module. Grounding the labs in one continuous, relatable scenario — rather than a new throwaway example every time — is intentional: it lets you see how *one real architecture* actually grows and changes as a business's needs change, instead of only ever seeing finished, disconnected examples.

### The people

**Frank and Martha** dreamed of opening a café and bakery in retirement — not to stop working, but to do something built around their love of baking that also supplemented their income. Since opening, they've enjoyed becoming part of their neighborhood, supporting community events with baked goods and coffee, and picking up unexpected interest from business travelers and tourists passing through.

| Person | Role | Background |
|---|---|---|
| Frank | Co-owner | Retired from the navy, loves to bake, nontechnical |
| Martha | Co-owner | Retired accountant, comfortable with spreadsheets, otherwise nontechnical |
| Sofía | Frank and Martha's daughter, supply chain manager | Future business administration student; has some programming background |
| Nikhil | Café employee | Visual design skills, interested in learning cloud computing, may take on more responsibility as Sofía starts university |

Sofía recently learned about AWS and started talking to her parents about how cloud services might reduce manual administrative work and improve the customer experience — which is what pulls the café into this course's story in the first place.

Three frequent café visitors happen to be AWS consultants, and they become informal advisors to the café as the story progresses:

| Person | Role | Specialty |
|---|---|---|
| Olivia | AWS Solutions Architect | Databases and network technologies; previously a network engineer |
| Faythe | AWS Developer | Experience with AWS APIs and SDKs; AWS Certified Security – Specialty; interested in big data |
| Mateo | Systems administrator and engineer | Automation, repeatable solutions, backup and disaster recovery; has mentored Faythe since her internship |

In each challenge lab, you take on the role of the café staff — receiving advice from these consultants as you architect solutions for the café's real, growing needs.

### How the café's architecture evolves across the course

The table below previews how the café's AWS architecture grows over the course — not something to memorize now, but useful to glance back at as each new module lands, so you can see where that module's concept actually gets applied.

| Version | Business reason for the update | Technical requirement / architecture update |
|---|---|---|
| V1 | Build a static website for a small business | Host the website on Amazon S3 |
| V2 | Support dynamic content and online ordering | Deploy the web application and database on Amazon EC2 |
| V3 | Reduce the effort to maintain the database and secure its data | Separate the web and database layers; migrate the database to Amazon RDS on a private subnet |
| V4 | Enhance the security of the web application | Use Amazon VPC features to configure and secure public and private subnets |
| V5 | Handle an expected traffic increase while staying highly available and resilient to failure | Add a load balancer, implement Auto Scaling on the EC2 instances, and distribute compute and database instances across two Availability Zones |
| V6 | Automate deployments so the café can consistently deploy, manage, and update resources across Regions | Build a version-controlled AWS CloudFormation template to deploy the network and application layers, then deploy the stack to another Region |
| V7 | Add reporting capabilities while reducing operational burden, improving performance, and reducing cost | Deploy AWS Lambda functions that connect to the Amazon RDS database and generate a report on a schedule |

Notice the shape of this progression: it moves from "just get something live" (V1) toward increasingly deliberate trade-offs around security, availability, automation, and cost — which is exactly the arc this course itself follows, module by module.

---

## Roles in Cloud Computing

Whether you're starting a career in cloud computing, transitioning into one, or just want to understand how a team with cloud responsibilities is organized, it helps to know the common job titles involved and what each one actually does day to day.

### IT professional

IT professionals are generalists. They typically manage the infrastructure for an entire application and understand how its components fit together, even without deep expertise in any single service. They're highly technical, sometimes specialize in one area (like security or storage), and often manage a production environment directly.

Common job titles: IT administrator, systems administrator, network administrator.

### IT leader

IT leaders are managers — they lead a team of IT professionals, own day-to-day operational decisions, manage budgets, and decide which technologies a team adopts. They're often hands-on early in a project, then delegate implementation details to their team as the project matures.

Common job titles: IT manager, IT director, IT supervisor.

### Developer

Developers work with code — writing, testing, and fixing it, and thinking about a project at the application level rather than the infrastructure level. They work with APIs and SDKs, often build on sample code, and sometimes specialize in one area (like security or storage), much like IT professionals do.

Common job titles: software developer, systems architect, software development manager.

### Where the cloud architect fits

This course exists to build the fourth role: the **cloud architect**. Where an IT professional keeps a system running and a developer builds what runs on top of it, the cloud architect's job is upstream of both — deciding *how* a solution should be built in the first place, before a single resource gets provisioned. That means working backward from a real business need (like the café's) to a specific, deliberate architecture: which services to use, how to arrange them, and what trade-offs to accept along the way.

Recognize the pattern across the three consultant personas introduced above: Olivia (the solutions architect) thinks about the whole system and its trade-offs; Faythe (the developer) thinks about implementation and security within the code; Mateo (the systems engineer) thinks about keeping it running reliably. A cloud architect needs a working understanding of all three perspectives — which is exactly why this course revisits security, development patterns, and operations repeatedly, from an architect's point of view, rather than teaching any one of them in isolation.

## What to skip

You don't need to memorize the café characters' biographies or the exact wording of the version table above — they're context, not exam content. What's worth carrying forward is the shape of the story: a small, real-sounding business whose needs grow in a specific, recognizable order (static site → dynamic app → separated database → secured network → high availability → automation → serverless reporting), because that same *order of concerns* is how real architectural decisions tend to unfold too.

## Key takeaways

- This course pairs lecture content with two kinds of labs: guided labs (step-by-step) and challenge labs (built around the café case study, with less hand-holding by design).
- The café business case — Frank, Martha, Sofía, and Nikhil, advised by consultants Olivia, Faythe, and Mateo — is the running scenario behind every challenge lab in this course.
- The café's architecture evolves across seven versions, moving from a simple static website to a secure, highly available, automated, serverless-enhanced system — mirroring the order this course itself covers.
- A cloud architect's job is to work backward from a real business need to a deliberate architecture, drawing on the same perspectives an IT professional, an IT leader, and a developer each bring individually.

## Further reading

- [AWS Academy](https://aws.amazon.com/training/awsacademy/) — background on the AWS Academy program this course is part of.
- [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html) — you'll meet this framework properly in Module 2, but it's worth bookmarking now since it recurs throughout the course.

---

**Next:** [Module 2 — Introducing Cloud Architecting](02-introducing-cloud-architecting.md)
