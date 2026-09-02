**NET-3100BB2 · AWS SOLUTIONS ARCHITECT PROFESSIONAL · WAKE TECH**

**Module 2 Knowledge Check**

Architecting Network Connectivity Strategies · 20 questions · Practice — not graded

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

> VPC peering connections are transitive — if VPC A peers with VPC B, and VPC B peers with VPC C, traffic can flow from A to C through B.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service uses a hub-and-spoke model to connect many VPCs, instead of a full mesh of individual connections?
>
> **A.** VPC Peering
> **B.** AWS Transit Gateway
> **C.** AWS PrivateLink
> **D.** Route 53 Resolver

**3. [Fill in the Blank] Easy**

> ____________ ____________ establishes a dedicated, private physical network connection between an on-premises location and AWS, bypassing the public internet.

**4. [Multiple Choice] Easy**

> Which connectivity option travels over the public internet using an encrypted IPsec tunnel?
>
> **A.** AWS Direct Connect
> **B.** AWS Site-to-Site VPN
> **C.** AWS Transit Gateway
> **D.** AWS PrivateLink

**5. [True / False] Easy**

> AWS PrivateLink grants full network-level access to every resource in the provider's VPC.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Ten VPCs need to be fully interconnected using only VPC peering. Approximately how many peering connections are required?
>
> **A.** 10
> **B.** 20
> **C.** 45
> **D.** 100

**7. [Fill in the Blank] Moderate**

> A Route 53 Resolver ____________ endpoint forwards DNS queries from inside a VPC out to DNS servers elsewhere, such as an on-premises DNS server.

**8. [Multiple Choice] Moderate**

> What is a common pattern for combining Direct Connect and Site-to-Site VPN?
>
> **A.** VPN as the primary path, with Direct Connect as automatic failover
> **B.** Direct Connect as the primary path, with VPN as automatic failover
> **C.** They cannot be used together for the same connection
> **D.** Direct Connect replaces the need for any VPN entirely in all cases

**9. [True / False] Moderate**

> Transit Gateway route tables can be used to segment traffic, allowing some attached VPCs to reach a shared services VPC without necessarily allowing them to reach each other directly.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What does a Route 53 Resolver inbound endpoint allow?
>
> **A.** DNS queries from on-premises to resolve names hosted inside AWS
> **B.** VPC peering connections to become transitive
> **C.** Direct Connect circuits to be provisioned automatically
> **D.** PrivateLink endpoints to bypass IAM permissions

**11. [Fill in the Blank] Moderate**

> AWS ____________ exposes one specific service privately to consumers in other VPCs or accounts, without requiring VPC peering, Transit Gateway attachment, or route table changes.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Meridian expects to acquire several more brands over the next two years, each needing its own AWS account with controlled access to shared services. Which connectivity approach best fits?
>
> **A.** A full mesh of VPC peering connections between every account
> **B.** AWS Transit Gateway as a central hub, with each new brand's VPC attached as a spoke
> **C.** AWS Direct Connect between every pair of accounts
> **D.** No connectivity solution is needed until the acquisitions actually happen

**13. [Scenario / Judgment] Hard**

> Meridian's IT team needs working connectivity to Ridgeline's headquarters within the next few days to begin migration planning. Which option fits?
>
> **A.** AWS Direct Connect, since it offers the best long-term performance
> **B.** AWS Site-to-Site VPN, since it can typically be provisioned in hours rather than the weeks Direct Connect's physical circuits require
> **C.** AWS Transit Gateway alone, without any hybrid connectivity option
> **D.** AWS PrivateLink, since it connects on-premises networks to AWS

**14. [Scenario / Judgment] Hard**

> A central authentication API needs to be callable from three separate Meridian AWS accounts, but none of those accounts should be able to reach anything else inside the account hosting the API. What best fits?
>
> **A.** VPC peering between all four accounts
> **B.** AWS PrivateLink, exposing only the authentication API as a private endpoint
> **C.** A single shared VPC across all four accounts
> **D.** AWS Direct Connect from each account to the API's account

**15. [Scenario / Judgment] Hard**

> An engineer on Café Sol's team needs to reach a shared service in Haven & Co.'s account by hostname, not by hardcoded IP address, once both are attached to a shared Transit Gateway. What additional piece is required to make this work?
>
> **A.** Nothing further — Transit Gateway automatically resolves hostnames across attached VPCs
> **B.** Route 53 Resolver, since Transit Gateway solves routing but not DNS name resolution
> **C.** AWS PrivateLink, since only PrivateLink supports hostname resolution
> **D.** A second Transit Gateway dedicated to DNS

**16. [Scenario / Judgment] Hard**

> A reviewer proposes connecting Café Sol's and Haven & Co.'s VPCs with a single VPC peering connection, since there are currently only two brands. Is this a reasonable choice today?
>
> **A.** No — VPC peering should never be used regardless of scale
> **B.** Yes, for exactly two VPCs with no near-term growth plans — but Meridian's stated plan to add more brands over time makes Transit Gateway the better long-term fit even now
> **C.** Yes, and it will continue to be the best choice no matter how many brands Meridian adds later
> **D.** No — Transit Gateway is required by AWS for any organization with more than one AWS account

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "Direct Connect is always the better choice over VPN, since it performs better." Correct this using this module's content.
>
> **A.** They're right without qualification — Direct Connect should always be chosen
> **B.** Direct Connect generally offers more consistent latency and higher throughput, but it costs more and takes longer to provision — a scenario with a tight timeline or lower throughput needs may be better served by VPN, and the two are often combined rather than treated as mutually exclusive
> **C.** VPN always outperforms Direct Connect
> **D.** Cost and provisioning time are irrelevant to this choice

**18. [Scenario / Judgment] Very Hard**

> A reviewer argues: "Since Transit Gateway can connect to on-premises networks directly, there's no reason Meridian would ever need Site-to-Site VPN or Direct Connect separately." Evaluate this using this module's content.
>
> **A.** Agree — Transit Gateway makes VPN and Direct Connect entirely obsolete
> **B.** Disagree — Transit Gateway is the hub that VPCs and on-premises connections attach to, but the actual hybrid connection into that hub still has to be established using Site-to-Site VPN or Direct Connect; Transit Gateway doesn't replace either, it centralizes what they connect to
> **C.** Disagree, but only because Transit Gateway cannot attach to on-premises networks under any circumstances
> **D.** Agree, as long as the on-premises location has a Direct Connect location nearby

**19. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why Meridian's shared-services VPC is exposed to the other brands' accounts via PrivateLink rather than simply being another spoke on the same Transit Gateway route table as Café Sol and Haven & Co.
>
> **A.** PrivateLink and Transit Gateway route tables are functionally identical, so the choice makes no difference
> **B.** Putting the shared-services VPC on the same route table would give each brand's account broader network reach into that VPC than necessary; PrivateLink exposes only the specific service (like authentication) each brand actually needs to call, without granting wider network access
> **C.** Transit Gateway cannot attach to a shared-services VPC under any circumstances
> **D.** PrivateLink is required before any VPC can join a Transit Gateway

**20. [Scenario / Judgment] Very Hard**

> A stakeholder asks why Meridian doesn't just use Direct Connect for Ridgeline's headquarters from day one, since it's the "better" option. Argue against doing so immediately, using this module's content.
>
> **A.** Direct Connect should always be used immediately regardless of timeline, since performance is the only relevant factor
> **B.** Direct Connect's physical circuit provisioning takes longer than Meridian's IT team can wait to begin migration planning; Site-to-Site VPN gets working connectivity now, with a switch to Direct Connect planned once Ridgeline's actual AWS workloads go live and need the more consistent throughput
> **C.** Direct Connect cannot be used for any location that currently lacks AWS workloads
> **D.** There is no reason not to use Direct Connect immediately — the module recommends it as the day-one choice

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
