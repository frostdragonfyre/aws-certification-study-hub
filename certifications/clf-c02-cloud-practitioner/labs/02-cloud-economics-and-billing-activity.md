**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 2**

**Lab Worksheet — Cloud Economics**

Activity 1: AWS Pricing Calculator · Activity 2: Support Plan Hunt

| **Name** | **Date** |
|---|---|
| | |

---

## Activity 1 — Price a Real Workload (40 min)

### Your scenario

A small business wants a web application. Before they commit, they want to know what it will cost per month. Here is everything they told you:

| Requirement | What they said |
|---|---|
| Web servers | Two servers, running 24 hours a day, 7 days a week |
| Storage | About 100 GB |
| Database | A small managed database |
| Data out to users | About 500 GB per month |
| Location | Their customers are in the United States |

*Notice what they did NOT tell you: server size, Region, operating system, database engine, or whether they want to commit long-term. You decide those — and note down why you chose them.*

### Steps

1. Go to calculator.aws — no login or AWS account needed.
2. Click Create estimate. Name it "Small Business Web App."
3. Add Amazon EC2. Choose your Region, set Quantity to 2, and select an instance type. Use "Constant usage" for the 24/7 requirement.
4. Add your storage (EBS) — 100 GB.
5. Add Amazon RDS for the database. Pick the smallest option that seems reasonable.
6. Add Data Transfer — 500 GB per month going OUT to the internet.
7. Record your monthly total below.

### Record your estimate

| Line item | Monthly cost | What you chose |
|---|---|---|
| EC2 (2 web servers) | $ | type: |
| Storage (100 GB) | $ | type: |
| Database | $ | engine/size: |
| Data transfer out (500 GB) | $ | |
| Anything else you added | $ | |
| **MONTHLY TOTAL** | **$** | |

| Region you chose | Purchase model (on-demand or committed?) |
|---|---|
| | |

### Think about it

1. Name two assumptions you made that, if changed, would significantly change your total.
2. Which single line item cost the most? Did that surprise you?
3. The customer said "two web servers." What did they forget to mention that you would also need to pay for?

### Bonus round — commit and save

Go back into your estimate and change the EC2 workload to a 3-year commitment (Savings Plan or Reserved Instance). Re-run it.

| On-demand total | 3-year committed total | You saved |
|---|---|---|
| $ | $ | $ /month |

**If committing saves that much, why doesn't every company just commit to 3 years for everything?**

---

## Activity 2 — Support Plan Scenarios (25 min)

### How this works

Work on your own. For each scenario, write the plan you'd choose — and UNDERLINE the exact phrase in the scenario that decided it. We'll go through the answers together as a class afterward.

*The underline matters as much as the answer. Noticing which phrase is load-bearing is the skill the exam is really testing — and it works on every question type, not just support plans.*

**Don't worry about finishing all ten. Six done carefully beats ten rushed. This is not collected or graded.**

### Your reference — the five plans

| Plan | Best for | Critical response | TAM |
|---|---|---|---|
| Basic (free) | Account & billing help only | No tech support | No |
| Developer | Dev & test, not production | Business hours, email | No |
| Business | Production workloads | Under 1 hour, 24/7 | No |
| Enterprise On-Ramp | Business-critical | Under 30 minutes | Pool of TAMs |
| Enterprise | Mission-critical | Under 15 minutes | Designated TAM |

*Note: Business is also the lowest tier that unlocks the COMPLETE set of Trusted Advisor checks.*

### The scenarios

*Underline the deciding phrase in each scenario as you read it.*

| # | Scenario | Your answer |
|---|---|---|
| 1 | A student learning AWS on a personal account. Wants documentation and help with a billing question. | |
| 2 | A startup's first production app. It cannot be down more than an hour. | |
| 3 | A hospital system, patient-facing, needs sub-30-minute response and architectural guidance from TAMs. | |
| 4 | A global bank running a mission-critical trading platform; requires a designated Technical Account Manager. | |
| 5 | A developer testing an idea nights and weekends; wants occasional email help, no production workload. | |
| 6 | A company wants the COMPLETE set of Trusted Advisor checks. | |
| 7 | A company needs 24/7 phone, chat, and email access to cloud support engineers for a live e-commerce site. | |
| 8 | An enterprise wants proactive guidance and a review before a major launch, plus the fastest possible response if it fails. | |
| 9 | A nonprofit runs a small informational website. They want to keep costs to zero and can wait for forum answers. | |
| 10 | A SaaS company needs a production system-down response in under an hour, but cannot justify TAM costs. | |

### Pick any two and go deeper

For two of the scenarios above, write out why it ISN'T the plan just above or below it. That comparison is where the real learning is.

**Scenario #____ — why not the neighbouring plan:**

**Scenario #____ — why not the neighbouring plan:**

### The shortcut — write this down

**For ANY support plan question on the exam, ask two questions in this order:**

1. How fast does the scenario say they need a response?
2. Do they need a Technical Account Manager — and is it a POOL (On-Ramp) or DESIGNATED (Enterprise)?

*Those two questions resolve nearly every support plan question you will ever see.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Rewrite scenario 2 so the correct answer becomes Enterprise. What did you have to change? |
| 2 | Write your own scenario where the answer is Enterprise On-Ramp — make the deciding phrase obvious. |
| 3 | Which plan would your current or a former employer need, and why? Two sentences. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 2 + knowledge check (aim 80%+ first attempt) |
| | If you have a personal AWS account: set a cost budget with an alert, and screenshot it |
| | Price out an app YOU would want to build, in the Pricing Calculator. Bring the number. |
