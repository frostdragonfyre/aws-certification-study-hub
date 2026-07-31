**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 1**

**Lab Worksheet — Cloud Concepts**

Activity 1: Is This Really Cloud? · Activity 2: Bridges and Pillars · Activity 3: Who Owns This?

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Is This Really Cloud? (20 min)

### Part A — Name the characteristic (or the violation)

For each scenario, write which of the five characteristics of cloud computing it demonstrates: **on-demand self-service, broad network access, resource pooling, rapid elasticity, or measured service.** Two of the scenarios are actually violating one of the five — if so, write which one is missing instead.

| # | Scenario | Characteristic (or violation) |
|---|---|---|
| 1 | A developer spins up a new server through a web console in under two minutes — no approval ticket, no waiting on a human. | |
| 2 | An online store automatically adds more servers during a flash sale, then removes them once traffic drops back down. | |
| 3 | A company's monthly AWS bill lists exact charges down to the GB and the hour, for only what was actually used. | |
| 4 | Employees access their company's cloud-hosted email from a laptop, a phone, or a tablet, from anywhere with internet. | |
| 5 | Thousands of unrelated companies' workloads run on the same shared physical hardware, invisibly to each other. | |
| 6 | A startup requests a new server but has to email an internal IT team and wait two business days for it to be provisioned. | |
| 7 | A company pays a flat annual license fee regardless of how much they actually use the software. | |

### Part B — IaaS, PaaS, or SaaS?

For each description, write IaaS, PaaS, or SaaS.

| # | Description | Your answer |
|---|---|---|
| 1 | Amazon EC2 — you get a virtual server and manage the OS and everything above it yourself. | |
| 2 | AWS Elastic Beanstalk — you push your code, AWS handles the infrastructure and OS underneath it. | |
| 3 | A web-based email service you just log into and use — no installation, no server to manage. | |
| 4 | A company rents a set of virtual machines and installs their own OS and software on top. | |
| 5 | A company writes application code and deploys it to a platform that handles scaling and patching automatically. | |
| 6 | A finished CRM tool a sales team uses entirely through a browser. | |

### Think about it

1. Scenarios 6 and 7 in Part A are NOT cloud computing, even though both involve remote servers or software. What's the one thing missing in each?
2. Between IaaS, PaaS, and SaaS, which one gives you the most control? Which one gives you the least operational burden? Are those the same answer?
3. Pick one app or service you use personally. Is it IaaS, PaaS, or SaaS from your perspective as the end user?

---

## Activity 2 — Bridges and Pillars (25 min)

### Part A — Match the hybrid driver to the AWS bridge

A fully on-premises company doesn't move to AWS in one step — different reasons for staying partly on-prem call for different AWS "bridge" services. For each scenario, write the correct bridge service, and underline the phrase that gave it away.

**Your reference:**

| Driver | AWS bridge |
|---|---|
| Needs a private, dedicated line into AWS (not the public internet) | AWS Direct Connect |
| Needs an encrypted tunnel to AWS, set up quickly, over the internet | Site-to-Site VPN |
| On-prem apps need to read/write cloud storage during a gradual migration | AWS Storage Gateway |
| A legacy workload legally or physically cannot leave the building | AWS Outposts |

| # | Scenario | Your answer |
|---|---|---|
| 1 | A hospital's records system needs a private, dedicated network connection into AWS — not exposed to the public internet at all. | |
| 2 | A factory floor needs an encrypted connection to the cloud set up quickly, without ordering special dedicated hardware. | |
| 3 | An on-premises application needs to read and write to cloud storage as if it were local, while the company migrates gradually over the next year. | |
| 4 | A legacy system legally cannot leave a specific building, but the company still wants to run AWS services against it on-site. | |

### Part B — Deployment model: Cloud, Hybrid, or On-Premises?

| # | Scenario | Your answer |
|---|---|---|
| 5 | A brand-new startup with no legacy systems builds its entire product on AWS from day one. | |
| 6 | A bank keeps its core mainframe on-site for compliance reasons but runs its new mobile app entirely on AWS, connected via Direct Connect. | |
| 7 | A government agency runs everything in its own data center, virtualized internally, with no public cloud involved. | |

### Part C — Which Well-Architected pillar is this describing?

The six pillars: **Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, Sustainability.**

| # | Symptom | Pillar |
|---|---|---|
| 8 | A company's AWS bill is far higher than it needs to be because nobody ever right-sized instances after launch. | |
| 9 | A system goes down every time a single server fails, with no automatic recovery. | |
| 10 | Engineers have no automated monitoring or logging, so they only learn about outages from angry customers. | |
| 11 | An application runs on much bigger instances than it needs, "just in case," wasting capacity that's never used. | |
| 12 | A company left an S3 bucket world-readable, exposing customer data. | |
| 13 | A company keeps running old, inefficient hardware instead of newer, more efficient options, increasing its carbon footprint. | |

### The shortcut — write this down

**For hybrid-bridge questions, ask: what's actually driving the need?**

1. Must it be **private and dedicated**, off the public internet? → Direct Connect.
2. Just need it **encrypted and fast to set up**? → Site-to-Site VPN.
3. Is this about **storage** specifically, during a migration? → Storage Gateway.
4. Can the workload **not leave the building at all**? → Outposts.

*Notice this is the same shape as the security-tool shortcut from Lecture 4 and the Region-selection shortcut from Lecture 3 — AWS scenario questions almost always resolve to "what's the one constraint actually doing the work here?"*

---

## Activity 3 — Who Owns This? A CAF Perspective Hunt (20 min)

### How this works

Migrating to the cloud isn't just a technology project — the AWS Cloud Adoption Framework (CAF) covers the organizational readiness side too. Below is a mix of people and situations. For each one, write which of the six CAF perspectives owns it, and UNDERLINE the phrase that gave it away.

*Same skill as every other hunt tonight: the exam rarely names the perspective directly — it describes a stakeholder or a symptom and expects you to place it.*

### Your reference — the six perspectives

| Group | Perspective | Stakeholders | Owns |
|---|---|---|---|
| Is the org ready? | Business | CFO, business/strategy owners | IT strategy vs. business strategy, business risk, benefits realization |
| Is the org ready? | People | HR, staffing, people managers | Training, careers, incentives, organizational change |
| Is the org ready? | Governance | CIO, program/portfolio managers | Aligning IT goals with business goals, licenses, portfolio management |
| Is the tech ready? | Platform | CTO, IT managers, solutions architects | Target-state architecture — compute, network, storage, database |
| Is the tech ready? | Security | CISO, security managers/analysts | IAM, detective control, data protection, incident response |
| Is the tech ready? | Operations | IT operations/support managers | Monitoring, resource inventory, change management, BC/DR |

### The scenarios

| # | Scenario | Your answer |
|---|---|---|
| 1 | An HR director is trying to figure out what training budget to request before the migration team starts moving workloads. | |
| 2 | A CISO wants a formal incident response plan in place before any workload goes live in AWS. | |
| 3 | A solutions architect is sketching out the target-state network and compute layout for the new environment. | |
| 4 | A CFO wants to understand how the migration's costs compare to the business value it will unlock. | |
| 5 | A portfolio manager discovers the company is still paying for software licenses nobody uses anymore. | |
| 6 | An IT operations manager sets up automated monitoring and an on-call rotation before go-live. | |
| 7 | A CIO presents to the board on how the cloud program's strategy supports the company's overall goals. | |
| 8 | A people manager designs a program to reward staff who earn new cloud certifications. | |
| 9 | An IT security analyst configures detective controls to flag unusual account activity. | |
| 10 | A program manager tracks the migration's active initiatives and reports on their status. | |

### Pick any two and go deeper

For two of the scenarios above, write out why the perspective you picked beats the next most tempting wrong answer — Governance and Security both get confused with each other whenever the word "risk" shows up, and Governance and Business both get confused whenever the word "strategy" shows up.

**Scenario #____ — why this beats the tempting wrong answer:**

**Scenario #____ — why this beats the tempting wrong answer:**

### The shortcut — write this down

**For ANY CAF scenario, ask two questions in this order:**

1. Is this about the **organization** (budget, people, oversight) or the **technology** (architecture, protection, running it day to day)?
2. Within that half, which of the three jobs is it — strategy/value, people, or oversight (organizational side); or architecture, protection, or daily operation (technology side)?

*If "risk" appears: business risk (missed value, poor alignment) is Governance; security risk (breaches, unauthorized access) is Security — same word, different owner.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Rewrite scenario 6 (Part B, Activity 2) so the correct answer becomes "Cloud" instead of "Hybrid." What has to change? |
| 2 | Pick one Well-Architected pillar and describe a real (or made-up) company failure that violates it, in your own words. |
| 3 | Explain the CapEx-to-OpEx shift to a partner without using either acronym. |
| 4 | Pick one CAF perspective and describe, in your own words, a real gap a company might have in it. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 1 + knowledge check (aim 80%+ first attempt) |
| | Write, in your own words, the difference between IaaS, PaaS, and SaaS — one sentence each |
| | Name one AWS service that acts as a "bridge" for hybrid cloud, and what specific problem it solves |
| | Name one CAF perspective and one stakeholder who owns it, in your own words |
