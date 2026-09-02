**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 8 Knowledge Check**

Connecting Networks · 20 questions · Practice — not graded

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

> VPC peering allows two VPCs to communicate using private IP addresses, without traffic crossing the public internet.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service acts as a central hub so many VPCs can connect once instead of connecting to every other VPC individually?
>
> **A.** VPC Peering
> **B.** AWS Transit Gateway
> **C.** AWS PrivateLink
> **D.** Amazon Route 53

**3. [Fill in the Blank] Easy**

> A Site-to-Site VPN creates an ____________ connection between a VPC and an on-premises network, over the public internet.

**4. [Multiple Choice] Easy**

> Which connectivity option is a dedicated, physical connection that bypasses the public internet entirely?
>
> **A.** Site-to-Site VPN
> **B.** VPC Peering
> **C.** AWS Direct Connect
> **D.** AWS PrivateLink

**5. [True / False] Easy**

> AWS Direct Connect is encrypted by default, the same way a Site-to-Site VPN is.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> VPC A is peered with VPC B. VPC B is peered with VPC C. Can VPC A reach VPC C through this setup?
>
> **A.** Yes, peering is transitive
> **B.** No — VPC peering is not transitive; A and C would need their own direct peering connection
> **C.** Only if all three VPCs are in the same AWS account
> **D.** Only if Transit Gateway is also enabled

**7. [Fill in the Blank] Moderate**

> Two VPCs cannot be peered if their CIDR ranges ____________.

**8. [Multiple Choice] Moderate**

> A company needs to privately access one specific third-party API hosted in another company's VPC, without connecting the two full networks together. What's the best fit?
>
> **A.** VPC Peering
> **B.** AWS Transit Gateway
> **C.** AWS PrivateLink
> **D.** Site-to-Site VPN

**9. [True / False] Moderate**

> A Site-to-Site VPN is generally faster and cheaper to set up than AWS Direct Connect, but with less predictable performance.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> How many direct peering connections are needed to fully connect 4 VPCs to each other, with no Transit Gateway?
>
> **A.** 4
> **B.** 5
> **C.** 6
> **D.** 8

**11. [Fill in the Blank] Moderate**

> AWS Direct Connect typically takes ____________ to provision, due to the physical networking work involved.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> The café is opening a third location's VPC and already has two VPCs peered together. A teammate suggests peering all three VPCs to each other individually as the business grows further. What's the concern with this approach?
>
> **A.** There is no concern — peering always scales cleanly
> **B.** The number of required peering connections grows much faster than the number of VPCs, which is exactly the scaling problem Transit Gateway is designed to solve
> **C.** VPC peering can only ever connect two VPCs, total, across an entire AWS account
> **D.** Peering connections expire automatically after three VPCs are involved

**13. [Scenario / Judgment] Hard**

> A business needs a connection to AWS with consistent, predictable bandwidth for a latency-sensitive, high-volume data transfer running around the clock. Setup time of several weeks is acceptable. What should they choose?
>
> **A.** Site-to-Site VPN, because it's faster to set up
> **B.** AWS Direct Connect, because consistent, predictable performance is worth the longer setup time here
> **C.** VPC Peering, since it also avoids the public internet
> **D.** AWS PrivateLink, since it's the most private option

**14. [Scenario / Judgment] Hard**

> A company sets up Direct Connect and assumes their traffic is now automatically encrypted in transit. Is this correct?
>
> **A.** Yes, Direct Connect always encrypts traffic by default
> **B.** No — Direct Connect is a private physical connection, not an encrypted tunnel; if encryption is required, a VPN should run over the Direct Connect connection
> **C.** No, and there is no way to add encryption to a Direct Connect connection
> **D.** Yes, but only for traffic under 1 Gbps

**15. [Scenario / Judgment] Hard**

> A start-up needs to connect its AWS VPC to its small office network quickly, with no large upfront investment, and can tolerate some variability in performance. What fits best?
>
> **A.** AWS Direct Connect
> **B.** Site-to-Site VPN
> **C.** VPC Peering
> **D.** AWS PrivateLink

**16. [Scenario / Judgment] Hard**

> Why does PrivateLink expose only a single service, rather than connecting two entire VPCs the way peering does?
>
> **A.** PrivateLink is simply a more limited, worse version of peering
> **B.** PrivateLink is designed for the narrower case of privately reaching one specific service — exposing only what's needed instead of the entire network in both directions, which is the whole point when the requesting side shouldn't see more than that one endpoint
> **C.** PrivateLink can only be used with AWS's own services, never third-party ones
> **D.** PrivateLink and peering solve the identical problem with no real difference

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Transit Gateway is always the better choice over VPC peering, since it can do more." Evaluate this claim using this module's content.
>
> **A.** True without qualification — always use Transit Gateway
> **B.** Not necessarily — for a small, stable number of VPCs (like the café connecting exactly two locations), direct peering is simpler and sufficient; Transit Gateway earns its complexity once the network count or transitive-routing need grows
> **C.** False — Transit Gateway cannot connect more than two VPCs
> **D.** True, but only because Transit Gateway is always cheaper

**18. [Scenario / Judgment] Very Hard**

> The café's original location needs its point-of-sale data flowing into AWS, and separately, its new commissary kitchen's VPC needs to reach the original location's VPC. Which two services are actually being described, and why aren't they interchangeable?
>
> **A.** Both needs are solved by VPC Peering alone
> **B.** A Site-to-Site VPN (or Direct Connect) connects the on-premises point-of-sale network to AWS; VPC Peering connects the two VPCs to each other — one bridges AWS to a physical location, the other bridges two AWS networks, and neither substitutes for the other
> **C.** AWS PrivateLink solves both needs identically
> **D.** Transit Gateway is required for both, since VPN and peering can't coexist

**19. [Scenario / Judgment] Very Hard**

> A reviewer proposes using VPC peering to let a partner company privately call one internal reporting API, arguing "it's simpler than setting up PrivateLink." What's the strongest argument against this?
>
> **A.** There is no real downside; peering and PrivateLink are functionally identical for this use case
> **B.** Peering would connect the two full networks in both directions, exposing far more than the single API endpoint the partner actually needs — PrivateLink's one-directional, single-service model matches the actual requirement much more precisely
> **C.** Peering is technically incapable of connecting to a partner's AWS account
> **D.** PrivateLink is always cheaper than peering, which is the only relevant factor

**20. [Scenario / Judgment] Very Hard**

> Connect this module back to Module 7. Module 7 secured traffic *within* one VPC using subnets, route tables, and gateways. What's the essential difference in the problem this module solves?
>
> **A.** There is no real difference — this module just repeats Module 7's concepts
> **B.** Module 7 controls how traffic moves inside a single, already-isolated network; this module controls how that isolated network connects to other networks entirely — other VPCs or on-premises locations — which requires a completely different set of components because the traffic is now crossing a network boundary, not just moving between subnets
> **C.** Module 7 was about compute, and this module is about storage
> **D.** This module replaces the need for anything built in Module 7

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
