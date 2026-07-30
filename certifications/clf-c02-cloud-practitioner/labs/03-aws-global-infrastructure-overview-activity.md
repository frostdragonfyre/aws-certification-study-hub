**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 3**

**Lab Worksheet — Global Infrastructure**

Activity 1: Explore the Global Infrastructure Map · Activity 2: Region-Picking Scenarios

| **Name** | **Date** |
|---|---|
| | |

---

## Activity 1 — Explore the AWS Global Infrastructure Map (20 min)

### Steps

1. Go to the AWS Global Infrastructure page (aws.amazon.com/about-aws/global-infrastructure) — no login or AWS account needed.
2. Find the Region closest to Wake Tech. Record its name, code (e.g., `us-east-1`), and how many Availability Zones it has.
3. Pick two more Regions on two different continents. Record the same information for each.
4. Look for a Region with a noticeably different Availability Zone count than the others you recorded. Note which one.
5. Open the regional service availability page and pick one AWS service. Note two Regions where it's available and, if you can find one, a Region where it isn't yet.

### Record your findings

| Region name | Region code | Location | # of Availability Zones |
|---|---|---|---|
| | | | |
| | | | |
| | | | |

| Service you checked | Available in | NOT yet available in (if found) |
|---|---|---|
| | | |

### Think about it

1. Why might one Region have more Availability Zones than another?
2. If you were launching a business serving customers mostly in Australia, which Region from the map would you pick, and why?
3. The Availability Zone counts you just recorded can change — AWS adds AZs over time. What does that tell you about memorizing an exact count for the exam versus understanding the concept?

---

## Activity 2 — Region-Picking Scenarios (25 min)

### How this works

Work on your own. For each scenario, write which of the four Region-selection factors is deciding it — and UNDERLINE the exact phrase in the scenario that gave it away. We'll go through the answers together as a class afterward.

*Same skill as the support-plan hunt from Lecture 2: noticing which phrase is load-bearing. That's what the real exam question is actually testing.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the four factors

| Factor | What it means |
|---|---|
| Latency | Put resources close to your users for a faster experience |
| Price | The same service can cost different amounts in different Regions |
| Compliance | Data-residency laws may require data to physically stay in a specific country |
| Service availability | Not every AWS service launches in every Region on day one |

### The scenarios

*Underline the deciding phrase in each scenario as you read it.*

| # | Scenario | Your answer |
|---|---|---|
| 1 | A law firm in Frankfurt must keep all client records within Germany under local regulation. | |
| 2 | A gaming studio in Seoul wants the lowest possible latency for its almost entirely Korean player base. | |
| 3 | A startup is choosing between two Regions with identical latency and no compliance constraints, and picks the one with lower storage pricing. | |
| 4 | A healthcare startup needs a specific AWS machine-learning service that has only launched in three Regions worldwide so far. | |
| 5 | A nonprofit with a single-country audience and no compliance constraints picks the Region nearest their users because it tested noticeably faster. | |
| 6 | A financial services company must comply with a law requiring customer data never leave the country. | |
| 7 | A mobile analytics company wants a Region that supports every AWS AI service, including ones AWS announced last month. | |
| 8 | An e-commerce company serving both US and EU customers is deciding whether one Region can serve both audiences well. | |

### Pick any two and go deeper

For two of the scenarios above, write out why the deciding factor you picked beats the other three — not just why it's plausible, but why the others don't win.

**Scenario #____ — why this factor over the other three:**

**Scenario #____ — why this factor over the other three:**

### The shortcut — write this down

**For ANY Region-selection question on the exam, ask in this order:**

1. Is there a legal or regulatory requirement mentioned? If yes, that wins immediately — compliance overrides everything else.
2. If no, is a specific service or feature named that might not be everywhere? Check service availability next.
3. If neither applies, weigh latency against price based on what the scenario actually emphasizes.

*Compliance almost never loses when it's actually in play — the trap is picking latency or price when a legal requirement was quietly sitting in the scenario.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Pick a real business idea and defend a Region choice using all four factors, not just the one that decided it. |
| 2 | Using the regional service availability page, find a real AWS service that ISN'T available in a Region you recorded in Activity 1. Would that change your answer? |
| 3 | Explain in your own words the difference between a Local Zone and a full Region — no notes. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 3 + knowledge check (aim 80%+ first attempt) |
| | Bookmark the AWS Global Infrastructure map — you'll use it again this term |
| | Pick one AWS service you're curious about and note which category (Compute, Storage, Database, Networking, Security, Management) it belongs to |
