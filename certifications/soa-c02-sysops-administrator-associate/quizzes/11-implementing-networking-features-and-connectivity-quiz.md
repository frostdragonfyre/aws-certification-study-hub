**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 11 Knowledge Check**

Implementing Networking Features and Connectivity · 20 questions · Practice — not graded

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

> A VPC peering connection between VPC A and VPC B automatically lets VPC A reach any VPC that B is separately peered with.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which connectivity option runs an encrypted IPsec tunnel over the public internet?

> **A.** Direct Connect
> **B.** Site-to-Site VPN
> **C.** VPC peering
> **D.** Transit Gateway

**3. [Fill in the Blank] Easy**

> A ____________ endpoint supports only S3 and DynamoDB, and works as a route table entry with no hourly charge.

**4. [Multiple Choice] Easy**

> Which service acts as a regional hub that many VPCs can attach to, instead of a growing mesh of individual peering connections?

> **A.** VPC peering
> **B.** Transit Gateway
> **C.** Site-to-Site VPN
> **D.** Interface endpoint

**5. [True / False] Easy**

> An Interface endpoint creates an elastic network interface (ENI) and comes with an hourly charge.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does connecting ten VPCs to each other become impractical with VPC peering alone?

> **A.** VPC peering has a hard limit of two VPCs total, account-wide
> **B.** It requires a full mesh of separate peering connections — forty-five of them for ten VPCs — each created, routed, and maintained individually
> **C.** VPC peering cannot be used with more than one Availability Zone
> **D.** Peering connections expire automatically after 90 days

**7. [Fill in the Blank] Moderate**

> Direct Connect delivers ____________ latency and higher sustained bandwidth than a VPN, but takes weeks rather than minutes to provision.

**8. [Multiple Choice] Moderate**

> A team needs private access to Amazon SNS from a VPC, without traversing the public internet. Which endpoint type fits?

> **A.** A Gateway endpoint, since it supports all AWS services
> **B.** An Interface endpoint, since Gateway endpoints only support S3 and DynamoDB
> **C.** Neither — SNS cannot be reached privately from a VPC
> **D.** A Transit Gateway attachment

**9. [True / False] Moderate**

> A common hybrid connectivity pattern is Direct Connect as the primary connection with a Site-to-Site VPN configured as automatic failover.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A workload needs private, no-additional-cost access to an S3 bucket from within a VPC. What fits best?

> **A.** An Interface endpoint, since it's the most feature-complete option
> **B.** A Gateway endpoint — a free route table entry, and S3 is one of the two services it supports
> **C.** Site-to-Site VPN routed through the S3 console
> **D.** Direct Connect configured with an S3-specific virtual interface

**11. [Fill in the Blank] Moderate**

> VPC peering connections are ____________, meaning traffic cannot pass through one VPC to reach another VPC it's separately peered with.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> VPC A is peered with VPC B, and VPC B is separately peered with VPC C. A resource in VPC A tries to reach a resource in VPC C. What happens?

> **A.** The traffic routes automatically through VPC B, since both peering connections are active
> **B.** The traffic fails — VPC peering connections are non-transitive, so A cannot reach C through B without a direct connection or a Transit Gateway
> **C.** The traffic routes automatically, but only if both peering connections were created on the same day
> **D.** The traffic fails only if the VPCs are in different Regions

**13. [Scenario / Judgment] Hard**

> Priya needs consistent, predictable latency and high sustained bandwidth for a data-intensive workload connecting Meridian's data center to AWS, and setup time isn't a constraint. What fits best?

> **A.** Site-to-Site VPN, since it's faster to configure
> **B.** Direct Connect, since it delivers consistent performance over a dedicated private connection, and the longer lead time isn't a blocker here
> **C.** VPC peering, since it has no hourly charge
> **D.** A Gateway endpoint, since it avoids the public internet

**14. [Scenario / Judgment] Hard**

> A growing environment now has six VPCs that all need to communicate with each other, and more are expected to be added over time. What connectivity approach avoids an increasingly unmanageable mesh of connections?

> **A.** Add individual VPC peering connections between every pair as needed
> **B.** Transit Gateway — every VPC attaches to the hub once, instead of a peering mesh that grows combinatorially
> **C.** Site-to-Site VPN between each pair of VPCs
> **D.** A single Gateway endpoint shared by all six VPCs

**15. [Scenario / Judgment] Hard**

> A team wants Direct Connect's consistent performance but also needs a fallback if the dedicated connection has an outage. What design fits?

> **A.** Direct Connect alone — outages are rare enough not to plan for
> **B.** Direct Connect as the primary connection, with a Site-to-Site VPN configured as automatic failover
> **C.** Two separate Direct Connect connections from the same physical location with no other option
> **D.** Site-to-Site VPN as primary, with Direct Connect as backup only

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "VPC peering and Transit Gateway do the same job, so it doesn't matter which one you use for a large multi-VPC environment." Correct this using this module's content.

> **A.** They're right — peering and Transit Gateway are fully interchangeable at any scale
> **B.** They're different: peering is a simple, free, non-transitive one-to-one connection that scales poorly as VPCs grow, while Transit Gateway is a hub supporting transitive routing across many attachments — a large or growing multi-VPC environment is a Transit Gateway job, not a peering-mesh job
> **C.** Transit Gateway is simply a faster version of peering with no other differences
> **D.** Peering supports transitive routing; Transit Gateway does not

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes using Direct Connect for every hybrid connectivity need, arguing "dedicated is always better than a VPN." Evaluate this using this module's content.

> **A.** Agree — Direct Connect should always be used regardless of setup time or requirements
> **B.** Disagree — Direct Connect's weeks-long provisioning lead time makes it a poor fit when a connection is needed quickly, and Site-to-Site VPN's built-in encryption over the public internet is often sufficient; the two are also commonly paired, with VPN as failover for Direct Connect rather than one replacing the other entirely
> **C.** Disagree, but only because Direct Connect cannot be encrypted
> **D.** Agree, since Site-to-Site VPN cannot connect to a VPC at all

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a Gateway endpoint cannot satisfy a requirement for private connectivity to Amazon Systems Manager.

> **A.** Gateway endpoints support every AWS service, so this scenario has no real constraint
> **B.** Gateway endpoints only support S3 and DynamoDB — Systems Manager requires an Interface endpoint, which uses an ENI and AWS PrivateLink to support most other AWS services
> **C.** Systems Manager cannot be reached privately from a VPC under any circumstance
> **D.** Interface endpoints and Gateway endpoints are simply two names for the same underlying mechanism

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that since VPC peering has no hourly charge, it's always the more cost-effective choice over Transit Gateway regardless of the number of VPCs involved. Argue against this using this module's content.

> **A.** Agree — peering is always cheaper and there's no tradeoff to consider
> **B.** Disagree — peering's per-connection scaling means a growing VPC count requires a combinatorially growing number of connections to create and maintain, and its non-transitivity can force even more connections just to reach VPCs indirectly; at scale, Transit Gateway's hub model reduces both operational complexity and the number of connections needed, which is a cost in itself even before hourly charges are compared
> **C.** Disagree, but only because Transit Gateway is always free
> **D.** Agree, since Transit Gateway cannot connect more than two VPCs

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as a Direct Connect connection is provisioned, connectivity to AWS is guaranteed with no need for any backup plan." Evaluate this claim using this module's content.

> **A.** Agree — a dedicated physical connection cannot fail
> **B.** Disagree — a Direct Connect connection is still a single physical path that can experience an outage; the common, resilient pattern is Direct Connect as the primary connection paired with a Site-to-Site VPN as automatic failover, so connectivity doesn't depend entirely on one physical link
> **C.** Disagree, but only because Direct Connect cannot carry production traffic
> **D.** Agree, since Site-to-Site VPN is incapable of serving as a backup for Direct Connect

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
