[Course index](../README.md) · [Read the paired lesson](../modules/14-improving-reliability-performance-and-cost.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 14 Knowledge Check**

Improving Reliability, Performance, and Cost for an Existing Solution · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|

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

> A design that scores well in AWS Resilience Hub has automatically been proven to survive a real failure.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which service deliberately injects real faults — like terminating an instance — into a running system to test its actual resilience?
>
> **A.** AWS Resilience Hub
> **B.** AWS Fault Injection Service
> **C.** AWS Config
> **D.** Amazon GuardDuty

**3. [Fill in the Blank] Easy**

> AWS ____________ ____________ analyzes historical CloudWatch utilization data and produces evidence-based right-sizing recommendations.

**4. [Multiple Choice] Easy**

> Which Savings Plans metric measures what percentage of eligible usage is covered by a commitment, versus paying On-Demand rates?

> **A.** Utilization
> **B.** Coverage
> **C.** Elasticity
> **D.** Redundancy

**5. [True / False] Easy**

> Compute Optimizer's recommendations for a brand-new workload with no usage history are exactly as precise as its recommendations for a six-month-old workload.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What does AWS Resilience Hub assess, as distinguished from Fault Injection Service in this module?

> **A.** Real, deliberately injected faults in a live running system
> **B.** An application's architecture against a defined resilience policy, based on the design itself, without anything actually breaking
> **C.** Historical CPU and memory utilization data
> **D.** Savings Plans commitment usage

**7. [Fill in the Blank] Moderate**

> Savings Plans ____________ measures what percentage of a purchased commitment is actually being used, as opposed to sitting idle.

**8. [Multiple Choice] Moderate**

> Why does low Savings Plans utilization point to a different fix than low coverage?

> **A.** They actually point to the same fix
> **B.** Low coverage means real usage isn't being discounted, fixed by buying more commitment; low utilization means existing commitment is already too large for actual usage, the opposite direction
> **C.** Both are fixed by purchasing Spot Instances instead
> **D.** Low utilization can only be fixed by canceling all Savings Plans immediately

**9. [True / False] Moderate**

> AWS Fault Injection Service is the SAP-C02 version of chaos engineering — verifying resilience by actually testing it, not just assessing it on paper.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Why are Compute Optimizer's recommendations for Café Sol more precise than a similar recommendation could be for Meridian Loyalty at launch?

> **A.** Compute Optimizer only works for workloads named Café Sol
> **B.** Café Sol has six real months of historical utilization data to analyze; Meridian Loyalty at launch has no usage history yet
> **C.** Compute Optimizer cannot analyze any workload younger than one year
> **D.** There is no actual difference in precision between the two cases

**11. [Fill in the Blank] Moderate**

> AWS ____________ ____________ assesses a design against a resilience policy without anything actually breaking.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Sofía wants to confirm that a failover Resilience Hub assessed as compliant actually executes correctly when something really goes wrong. What should she use?

> **A.** AWS Resilience Hub alone, run a second time
> **B.** AWS Fault Injection Service, in a controlled game day that deliberately triggers the failure
> **C.** Amazon GuardDuty
> **D.** AWS Trusted Advisor

**13. [Scenario / Judgment] Hard**

> A reviewer says a Resilience Hub assessment score of "fully meets policy" means the design is proven resilient in practice. What's the flaw?

> **A.** There is no flaw — a passing assessment score is proof of real-world resilience
> **B.** Resilience Hub assesses the design on paper, without anything actually breaking; only an actual controlled test, like one run through Fault Injection Service, proves the assessed resilience holds up when something really fails
> **C.** Resilience Hub cannot produce a passing score under any circumstances
> **D.** Fault Injection Service and Resilience Hub always produce identical results

**14. [Scenario / Judgment] Hard**

> Café Sol's Savings Plans coverage is high, but utilization is low. What does this combination suggest?

> **A.** Nothing meaningful — the two metrics are unrelated
> **B.** Most eligible usage is already being discounted (high coverage), but a meaningful portion of the purchased commitment itself isn't being consumed (low utilization) — the commitment may be oversized for actual usage
> **C.** More Savings Plans should be purchased immediately
> **D.** The Savings Plans have expired and need to be repurchased

**15. [Scenario / Judgment] Hard**

> A student argues Compute Optimizer's recommendations are "just guesses like any other sizing advice." What's missing from this claim?

> **A.** Nothing — all sizing recommendations are equally speculative
> **B.** Compute Optimizer's recommendations are built from actual, historical CloudWatch utilization data specific to that workload — evidence-based, not a generic best-practice guess
> **C.** Compute Optimizer only works with Lambda functions, never EC2
> **D.** Compute Optimizer recommendations require no underlying data at all

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Module 8 already used Resilience Hub, so this module's reliability content is redundant." Correct this using this module's content and Module 8's.

> **A.** They're right — the two modules cover identical content
> **B.** Module 8 used Resilience Hub to assess a brand-new design before Meridian Loyalty had ever run; this module adds Fault Injection Service to actually test an existing, six-month-old system's assumed resilience for real — assessment before launch versus proof after months of operation, a different question
> **C.** Module 8 only applies to Meridian Loyalty and can never apply to Café Sol
> **D.** This module replaces everything Module 8 covered

**17. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since both coverage and utilization are Savings Plans metrics, whichever one is lower should always be fixed by buying more commitment." Evaluate this using this module's content.

> **A.** Agree — buying more commitment always fixes whichever metric is lower
> **B.** Disagree — low coverage is fixed by buying more commitment, but low utilization means existing commitment is already underused, so buying more would make utilization worse, not better; the two metrics require opposite responses, not the same one
> **C.** Disagree, but only because Savings Plans cannot be purchased incrementally
> **D.** Agree, since coverage and utilization always move in the same direction together

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Café Sol specifically — rather than Meridian Loyalty at launch — is the natural candidate for a Compute Optimizer review.

> **A.** Compute Optimizer works equally well for both, so the choice is arbitrary
> **B.** Compute Optimizer's value comes from analyzing real historical utilization data; Café Sol has six months of that, while Meridian Loyalty at launch has none yet, making its instance-family decisions in Module 11 necessarily based on expected characteristics rather than observed behavior
> **C.** Compute Optimizer cannot analyze any workload associated with Meridian Loyalty
> **D.** Meridian Loyalty is a better candidate specifically because it lacks usage history

**19. [Scenario / Judgment] Very Hard**

> A stakeholder proposes skipping Fault Injection Service entirely, arguing "Resilience Hub already gave us a passing score, so we're done." Argue against this using this module's content.

> **A.** Agree — a passing Resilience Hub score means no further verification is needed
> **B.** Disagree — Resilience Hub's passing score reflects the design on paper; it hasn't been tested against an actual failure. FIS is what confirms the assessed resilience actually holds when a real fault is deliberately, safely introduced — skipping it leaves the design unproven in practice
> **C.** Disagree, but only because Resilience Hub cannot produce passing scores
> **D.** Agree, since FIS and Resilience Hub always agree with each other by design

**20. [Scenario / Judgment] Very Hard**

> A student says: "Continuous improvement for an existing solution is just repeating the same six Domain 2 tasks over again." Evaluate this using this module's content.

> **A.** Agree — Domain 3 and Domain 2 are identical in method and purpose
> **B.** Disagree — Domain 2's decisions were necessarily forward-looking, based on expected characteristics for a system that didn't exist yet; Domain 3's tools — Resilience Hub paired with FIS, Compute Optimizer, coverage and utilization audits — are specifically built to use real operating history that only an existing system has, verifying and correcting decisions rather than making them from scratch
> **C.** Disagree, but only because Domain 3 uses entirely unrelated AWS services with no conceptual connection to Domain 2
> **D.** Agree, since both domains produce exactly the same deliverables for a workload

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
