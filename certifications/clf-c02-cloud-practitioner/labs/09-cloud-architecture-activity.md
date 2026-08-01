**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 9**

**Lab Worksheet — Cloud Architecture**

Activity 1: Review an Architecture Against the Design Principles · Activity 2: Interpret Trusted Advisor Recommendations

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Review an Architecture Against the Design Principles (20 min)

### How this works

Below is a description of a real-shaped (fictional) company's current architecture. For each of the six general design principles, decide whether the architecture follows it or violates it, and write one sentence explaining why. Work on your own first, then we'll build the review together on the board.

*This mirrors AWS Academy's own Well-Architected Framework design principles activity for this module — it's about applying the principles to a real-sounding system, not just reciting them.*

### The architecture

> A mid-size retailer runs its e-commerce site on a fixed number of EC2 instances, sized for their busiest historical Black Friday, running year-round even though traffic is a fraction of that most of the year. Any new feature gets tested directly in production because there's no separate environment to test in first. Deployments are done manually by one engineer, following steps in his head — nothing is scripted. The architecture hasn't changed in three years, even though the product has grown significantly. Decisions about what to build next come from the loudest voice in the room, not from usage data. The team has never intentionally caused a failure to see how the system responds.

### Review each design principle

| # | Design principle | Followed or violated? | Why (one sentence) |
|---|---|---|---|
| 1 | Stop guessing your capacity needs | | |
| 2 | Test systems at production scale | | |
| 3 | Automate to make architectural experimentation easier | | |
| 4 | Allow for evolutionary architectures | | |
| 5 | Drive architectures using data | | |
| 6 | Improve through game days | | |

### Does this map to a pillar too? (discuss as a class)

Pick any two rows above where you marked "violated."

| Question | Your answer |
|---|---|
| For your first "violated" principle, which of the six Well-Architected pillars does the underlying problem mostly affect? | |
| For your second "violated" principle, which pillar does it mostly affect? | |
| Is it possible for one violated principle to hurt more than one pillar at once? Give an example from the architecture above. | |

### Think about it

1. Why is "the architecture hasn't changed in three years" a violation of a specific design principle, rather than just neutral stability?
2. The retailer sizes for their busiest historical Black Friday, year-round. Which design principle does this violate, and what would AWS's fix actually look like?
3. Pick one design principle from the list and explain, in your own words, why it's a *habit* rather than a *pillar* — what's the actual difference?

---

## Activity 2 — Interpret Trusted Advisor Recommendations (25 min)

### How this works

Work on your own. Below are sample AWS Trusted Advisor–style recommendations (written out, since we don't have live console access tonight). For each one, identify the category, which Well-Architected pillar it maps to, and what action you'd actually take. We'll go through the answers together as a class afterward.

*Same skill as the database case studies from Lecture 8: noticing which phrase is load-bearing is what the real exam question is testing.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the five categories

| Category | What it checks |
|---|---|
| Cost Optimization | Underused or idle resources costing money for no benefit |
| Performance | Configurations that could be limiting performance |
| Security | Gaps like overly permissive security groups or MFA not enabled on root |
| Fault Tolerance | Missing redundancy, like a database without Multi-AZ enabled |
| Service Limits | Resources approaching their account service quota |

### The recommendations

*Underline the deciding phrase in each recommendation as you read it.*

| # | Trusted Advisor recommendation | Category | Pillar | Action you'd take |
|---|---|---|---|---|
| 1 | "Idle Load Balancer detected — this load balancer has had no active backend instances for 30+ days." | | | |
| 2 | "Security Group allows unrestricted access (0.0.0.0/0) to port 22 (SSH)." | | | |
| 3 | "Amazon RDS DB Instance is not configured for Multi-AZ." | | | |
| 4 | "MFA is not enabled on the root account." | | | |
| 5 | "EC2 instance is using 90% of its available vCPU quota for this Region." | | | |
| 6 | "Underutilized EC2 instance detected — average CPU utilization below 10% over the last 14 days." | | | |
| 7 | "Amazon EBS snapshot count is approaching the account limit." | | | |
| 8 | "CloudFront distribution is not using the latest recommended SSL/TLS protocol version." | | | |

### Pick any two and go deeper

For two of the recommendations above, write out what you'd say to a client or manager explaining why this matters, in plain language (no jargon).

**Recommendation #____ — plain-language explanation:**

**Recommendation #____ — plain-language explanation:**

### The shortcut — write this down

**For ANY Trusted Advisor recommendation on the exam, ask in this order:**

1. Is this about **money being wasted**? → Cost Optimization.
2. Is this about **something running slower than it should**? → Performance.
3. Is this about **who can access what, or a security gap**? → Security.
4. Is this about **missing redundancy or backup**? → Fault Tolerance.
5. Is this about **running out of room to grow**? → Service Limits.

*Notice the pattern: Trusted Advisor's five categories map almost directly onto the Well-Architected pillars — Cost Optimization to Cost Optimization, Performance to Performance Efficiency, Security to Security, Fault Tolerance to Reliability, and Service Limits mostly to Operational Excellence.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Write one new Trusted Advisor–style recommendation of your own for each of the five categories. |
| 2 | Explain in your own words why Trusted Advisor's core checks are free, but full checks require Business or Enterprise support. |
| 3 | Pick one recommendation from the list and explain which design principle (not pillar) it most connects to. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 9 + knowledge check (aim 80%+ first attempt) |
| | Sketch the six pillars from memory once, without looking at your notes |
| | Pick one design principle from tonight's list and explain what it means in your own words, no notes |
