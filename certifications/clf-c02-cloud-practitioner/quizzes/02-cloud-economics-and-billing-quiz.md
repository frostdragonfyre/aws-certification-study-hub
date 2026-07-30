**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 2 Review Quiz**

Cloud Economics and Billing · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|
| | |

*Instructions: Answer every question. Questions get harder as you go — the last several are exam-style judgment questions where more than one answer looks reasonable. For those, pick the BEST answer and be ready to defend it out loud.*

| **Question types** | **What to do** |
|---|---|
| Multiple Choice | Circle one letter. |
| True / False | Circle TRUE or FALSE. |
| Fill in the Blank | Write your answer on the line. |
| Scenario / Judgment | Circle the BEST answer. Note WHY the others fail. |

---

## Easy Questions

**1. [True / False] Easy**

> One of AWS's four pricing principles is that you pay MORE per unit as your usage grows.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Of the three cost drivers behind almost every AWS bill — compute, storage, and data transfer — which one most often surprises people?
>
> **A.** Compute
> **B.** Storage
> **C.** Data transfer
> **D.** Support plans

**3. [Fill in the Blank] Easy**

> Data transfer ____________ AWS is generally free; data transfer ____________ AWS is metered and costs money.

**4. [Multiple Choice] Easy**

> Which compute purchase option offers the deepest discount but can be reclaimed by AWS with little notice?
>
> **A.** On-Demand
> **B.** Reserved Instance
> **C.** Spot Instance
> **D.** Dedicated Host

**5. [True / False] Easy**

> AWS Organizations itself costs money to use, on top of whatever the underlying accounts spend.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which purchase option requires no upfront commitment and is billed per second or per hour?
>
> **A.** Reserved Instance
> **B.** On-Demand
> **C.** Spot Instance
> **D.** Savings Plan

**7. [Fill in the Blank] Moderate**

> The AWS ____________ ____________ Report is the most granular billing data available — down to the resource and the hour.

**8. [Multiple Choice] Moderate**

> A company wants to restrict what an entire AWS account can do, regardless of that account's own IAM policies. What should they use?

> **A.** A stricter IAM policy
> **B.** A Service Control Policy in AWS Organizations
> **C.** AWS Budgets
> **D.** Cost allocation tags

**9. [Multiple Choice] Moderate**

> Which tool alerts you BEFORE you overspend, rather than just reporting spend after the fact?
>
> **A.** Cost Explorer
> **B.** AWS Budgets
> **C.** Cost and Usage Report
> **D.** Trusted Advisor

**10. [True / False] Moderate**

> For AWS accounts created since mid-2025, the Free Tier still grants 12 months of free usage on eligible services regardless of activity.
>
> TRUE   FALSE

**11. [Fill in the Blank] Moderate**

> Cost allocation ____________ are key/value labels attached to resources that let a company break a lump-sum bill down by project, team, or environment.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A company's EC2 bill is $40,000 with no way to tell which team or project is responsible. What should they implement to fix this going forward?
>
> **A.** Reserved Instances
> **B.** Cost allocation tags
> **C.** A Service Control Policy
> **D.** AWS Wavelength

**13. [Scenario / Judgment] Hard**

> A startup wants the COMPLETE set of AWS Trusted Advisor checks, not just the limited free-tier subset. What is the minimum support plan that unlocks this?
>
> **A.** Basic
> **B.** Developer
> **C.** Business
> **D.** Enterprise On-Ramp

**14. [Scenario / Judgment] Hard**

> A company sets up a VPC, IAM roles, and Auto Scaling, and is confused why their bill isn't $0 even though "these services are free." What's the best explanation?
>
> **A.** The company was billed in error
> **B.** The management/control-plane layer is free, but the underlying resources it creates or manages — NAT gateways, EC2 instances, traffic — are not
> **C.** Free services always have a 30-day trial that expired
> **D.** IAM never appears on a bill, so this must be an unrelated charge

**15. [Scenario / Judgment] Hard**

> A CFO sees that a 3-year Reserved Instance is significantly cheaper than On-Demand and asks, "why doesn't every workload just commit for 3 years?" What is the strongest reason not to?
>
> **A.** Reserved Instances are not actually cheaper in practice
> **B.** A long commitment risks the workload's size, architecture, or existence changing before the term ends, wasting the unused commitment
> **C.** AWS does not allow more than one Reserved Instance per account
> **D.** Reserved Instances cannot be applied to production workloads

**16. [Scenario / Judgment] Hard**

> A finance team wants one consolidated invoice and volume-discount pricing across 15 separate departmental AWS accounts. Which service accomplishes this?
>
> **A.** AWS Budgets
> **B.** Cost Explorer
> **C.** AWS Organizations with consolidated billing
> **D.** Reserved Instances

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A company's monthly bill unexpectedly doubles. Cost Explorer shows the increase is entirely in the "Data Transfer" line, and the engineering lead says "that's strange, we haven't uploaded any more data than usual." What's the most likely explanation?
>
> **A.** AWS raised data transfer prices without notice
> **B.** Data transfer IN increased, which is unusual since inbound is normally free
> **C.** Data transfer OUT increased — likely more users downloading or streaming content, since outbound is the metered direction
> **D.** The increase must be a billing error, since data transfer is always free

**18. [Scenario / Judgment] Very Hard**

> A gaming company's workload is entirely stateless, tolerant of sudden termination, and only runs during off-peak hours to take advantage of cheap spare capacity. Evaluate the purchase-option reasoning below.
>
> **A.** Spot Instances fit well, since the workload can tolerate interruption
> **B.** Reserved Instances would lock in a 1–3 year commitment for a workload that's intentionally opportunistic and short-lived, wasting the commitment
> **C.** Dedicated Hosts would guarantee capacity but are the most expensive option, with no benefit for an interruption-tolerant workload
> **D.** All of the above are true — this is a textbook Spot use case, and the trap would be reaching for Reserved or Dedicated out of habit

**19. [Scenario / Judgment] Very Hard**

> An executive says: "Our on-premises servers cost $200,000 to purchase, which is less than five years of our current AWS bill — so we should move back on-premises." What is the strongest analytical objection?
>
> **A.** AWS is always cheaper, so the executive is simply wrong
> **B.** The comparison ignores that $200,000 is only the hardware — a fair TCO comparison must also include facilities, power, cooling, IT staff, refresh cycles, and the cost of idle capacity
> **C.** On-premises servers never need to be replaced, so the comparison actually understates AWS's advantage
> **D.** Five years is too short a window to compare

**20. [Scenario / Judgment] Very Hard**

> A nonprofit wants to keep costs at zero and can tolerate waiting for community forum answers. A separate e-commerce company needs 24/7 phone and chat access to support engineers, but doesn't need a dedicated Technical Account Manager. Match each organization to the correct support plan.
>
> **A.** Nonprofit: Basic · E-commerce company: Business
> **B.** Nonprofit: Developer · E-commerce company: Enterprise On-Ramp
> **C.** Nonprofit: Basic · E-commerce company: Enterprise
> **D.** Nonprofit: Developer · E-commerce company: Business

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
