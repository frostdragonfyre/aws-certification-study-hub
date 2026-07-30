**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 3 Review Quiz**

AWS Global Infrastructure Overview · 20 questions · Practice — not graded

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

> A Region is a separate geographic area, and an Availability Zone is an isolated data center within that Region.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS concept caches content close to end users to reduce latency?
>
> **A.** Availability Zone
> **B.** Region
> **C.** Edge Location
> **D.** AWS Outposts

**3. [Fill in the Blank] Easy**

> The four factors that decide which AWS Region to use are latency, price, compliance, and ____________.

**4. [Multiple Choice] Easy**

> What is the minimum number of Availability Zones an application should span for basic resilience?
>
> **A.** One
> **B.** Two
> **C.** Five
> **D.** Ten

**5. [True / False] Easy**

> Amazon CloudFront runs your application code the same way an EC2 instance does.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which AWS infrastructure type is embedded directly inside a telecom provider's 5G network?
>
> **A.** AWS Local Zones
> **B.** AWS Wavelength
> **C.** AWS Outposts
> **D.** Amazon CloudFront

**7. [Fill in the Blank] Moderate**

> AWS ____________ is the service that brings actual AWS hardware into a customer's own building.

**8. [Multiple Choice] Moderate**

> Which AWS service category would Amazon RDS and DynamoDB both belong to?
>
> **A.** Compute
> **B.** Database
> **C.** Networking & Content Delivery
> **D.** Management & Governance

**9. [True / False] Moderate**

> A Local Zone has the same built-in redundancy as an Availability Zone.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A German company must keep customer data within the EU by law. Which Region-selection factor is deciding their choice?
>
> **A.** Latency
> **B.** Price
> **C.** Compliance
> **D.** Service availability

**11. [Fill in the Blank] Moderate**

> A company wants a single, consolidated bill and volume discounts across 12 AWS accounts. The AWS service that provides this is AWS ____________.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A company needs its application to survive the failure of a single data center without noticeable downtime for users. Which AWS concept directly addresses this?
>
> **A.** Multiple Regions
> **B.** Multiple Availability Zones
> **C.** Multiple Edge Locations
> **D.** AWS Organizations

**13. [Scenario / Judgment] Hard**

> A media company wants to reduce load times for video thumbnails served to users all over the world. Which is the best fit?
>
> **A.** Launch EC2 instances in every Region
> **B.** Amazon CloudFront
> **C.** AWS Wavelength
> **D.** A Multi-AZ deployment

**14. [Scenario / Judgment] Hard**

> Which of the following is NOT one of the four factors used to choose an AWS Region?
>
> **A.** Latency
> **B.** Price
> **C.** Compliance
> **D.** Number of Availability Zones in the Region

**15. [Scenario / Judgment] Hard**

> Which of these must physically run inside a company's own building?
>
> **A.** An Availability Zone
> **B.** A Region
> **C.** AWS Outposts
> **D.** An Edge Location

**16. [Scenario / Judgment] Hard**

> A company's application runs across 3 Availability Zones within a single Region. That entire Region goes down in a rare, large-scale outage. What happens?
>
> **A.** Nothing — Multi-AZ protects against Region-level failures too
> **B.** The application goes down — Multi-AZ protects against a data-center-level failure, not a Region-level one
> **C.** AWS automatically reroutes traffic to another Region at no charge
> **D.** The application scales up automatically to compensate

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A company designs an application spanning 3 AZs in a single Region and calls it "fully resilient." A consultant pushes back. What is the strongest basis for that pushback?
>
> **A.** 3 AZs is not enough; the company needs 5
> **B.** Multi-AZ only protects against a data-center-level failure — true resilience against a Region-wide event requires a deliberate, more expensive multi-Region design
> **C.** The company should use Edge Locations instead of AZs
> **D.** "Fully resilient" is meaningless without naming a specific AWS service

**18. [Scenario / Judgment] Very Hard**

> A healthcare startup is choosing a Region. Their users are 90% in Chicago, no data-residency law applies, pricing is similar across candidate Regions, and every service they need is available everywhere they're considering. Which factor should decide their choice?
>
> **A.** Compliance, since healthcare data is always compliance-driven
> **B.** Price, since it's the only factor that's ever truly objective
> **C.** Latency, since it's the only one of the four factors that actually differentiates their options in this scenario
> **D.** Service availability, since healthcare workloads always need the newest features

**19. [Scenario / Judgment] Very Hard**

> A mobile game studio wants sub-10-millisecond latency for players connected via their carrier's 5G network, but also needs a full suite of AWS database and analytics services that only exist in standard Regions. What's the best architecture?
>
> **A.** Run entirely in a Local Zone, since it's closest to users
> **B.** Run entirely on Wavelength, since it's built for 5G
> **C.** Use Wavelength for the latency-critical game-state components, while keeping databases and analytics in the parent Region — Wavelength and Local Zones extend a Region, they don't replace it
> **D.** Use AWS Outposts inside the telecom provider's building

**20. [Scenario / Judgment] Very Hard**

> An organization has infrastructure in a standard Region and a Local Zone for a nearby metro area, and is evaluating Wavelength for a new mobile feature. An executive asks: "Since we already have a Local Zone, why would we ever also need Wavelength?" What's the best answer?
>
> **A.** We wouldn't — Wavelength and Local Zones are interchangeable
> **B.** Local Zones serve a metro area generally; Wavelength is specifically embedded inside a telecom carrier's network for mobile/5G workloads needing the lowest possible latency — they solve different problems and can both be used
> **C.** Wavelength always replaces a Local Zone once traffic grows large enough
> **D.** Local Zones are being deprecated in favor of Wavelength

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
