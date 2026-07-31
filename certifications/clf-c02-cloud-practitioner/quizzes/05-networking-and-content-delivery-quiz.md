**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 5 Review Quiz**

Networking and Content Delivery · 20 questions · Practice — not graded

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

> A VPC spans an entire Region but is subdivided into subnets, and each subnet is pinned to exactly one Availability Zone.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What actually determines whether a subnet is public or private?
>
> **A.** Its name
> **B.** Its route table
> **C.** Its size
> **D.** Which Availability Zone it's in

**3. [Fill in the Blank] Easy**

> An Internet ____________ gives a public subnet two-way access to the internet.

**4. [Multiple Choice] Easy**

> Which component gives a private subnet outbound-only internet access?
>
> **A.** Internet Gateway
> **B.** NAT Gateway
> **C.** Virtual Private Gateway
> **D.** Transit Gateway

**5. [True / False] Easy**

> Security groups operate at the subnet level, and Network ACLs operate at the instance level.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which firewall type supports explicit deny rules, in addition to allow rules?
>
> **A.** Security Group
> **B.** Network ACL
> **C.** Both
> **D.** Neither

**7. [Fill in the Blank] Moderate**

> Amazon ____________ is AWS's DNS service — it translates domain names into IP addresses.

**8. [Multiple Choice] Moderate**

> Which service caches content at edge locations to reduce latency for end users around the world?
>
> **A.** Amazon Route 53
> **B.** Amazon CloudFront
> **C.** AWS Direct Connect
> **D.** Site-to-Site VPN

**9. [True / False] Moderate**

> Security groups are stateful — return traffic for an already-allowed connection is automatically permitted.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which connection type is a dedicated, private, physical connection to AWS?
>
> **A.** Site-to-Site VPN
> **B.** AWS Direct Connect
> **C.** Amazon CloudFront
> **D.** AWS Global Accelerator

**11. [Fill in the Blank] Moderate**

> AWS Global ____________ routes application traffic over AWS's private global network backbone using static anycast IP addresses.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A private subnet's database instance needs to download a security patch from the internet, but must never accept an inbound connection from it. What allows this?
>
> **A.** Internet Gateway
> **B.** NAT Gateway
> **C.** Network ACL
> **D.** Amazon Route 53

**13. [Scenario / Judgment] Hard**

> A security team needs to explicitly block one specific malicious IP address at the subnet level. Which tool is built for this?
>
> **A.** Security Group
> **B.** Network ACL
> **C.** IAM
> **D.** AWS KMS

**14. [Scenario / Judgment] Hard**

> A streaming company wants viewers around the world to load video content quickly, from a location physically near them. What's the best fit?
>
> **A.** AWS Global Accelerator
> **B.** Amazon CloudFront
> **C.** Amazon Route 53
> **D.** AWS Direct Connect

**15. [Scenario / Judgment] Hard**

> A bank needs a hybrid connection to AWS with consistent performance, unaffected by public internet congestion. What's the best fit?
>
> **A.** Site-to-Site VPN
> **B.** AWS Direct Connect
> **C.** Amazon CloudFront
> **D.** A NAT Gateway

**16. [Scenario / Judgment] Hard**

> A subnet has no route to an Internet Gateway, but it does have a NAT Gateway attached (in a different, public subnet) so it can reach the internet outbound. Is this subnet public or private?
>
> **A.** Public, because it can reach the internet
> **B.** Private — no route to an Internet Gateway means private, regardless of outbound NAT access
> **C.** It depends on which Availability Zone it's in
> **D.** Public, but only if it's tagged "public"

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> An architect claims: "Since our private subnet has a NAT Gateway attached, it's effectively public now." What's the correct pushback?
>
> **A.** They're right — a NAT Gateway removes the subnet's privacy
> **B.** They're wrong — a NAT Gateway only allows outbound access, never inbound; the subnet is still private because it has no route to an Internet Gateway
> **C.** The subnet should be relabeled "public" now that it has a NAT Gateway
> **D.** NAT Gateways are being phased out, so this won't matter soon

**18. [Scenario / Judgment] Very Hard**

> A public subnet's web server needs two-way internet access, and the company also wants to explicitly deny one known-bad IP address at the subnet level while allowing everything else. Which two components together provide this?
>
> **A.** Just a Security Group
> **B.** An Internet Gateway (for two-way access) plus a Network ACL (for the explicit deny)
> **C.** Just a NAT Gateway
> **D.** Route 53 plus CloudFront

**19. [Scenario / Judgment] Very Hard**

> A global mobile game needs faster, more reliable routing over AWS's own private backbone for live, non-HTTP traffic — distinct from simply caching static content. Which service fits, and why isn't CloudFront the answer?
>
> **A.** CloudFront, because it's the general "make it faster" answer for anything
> **B.** AWS Global Accelerator — it optimizes routing to application endpoints, including non-HTTP traffic, while CloudFront specifically caches content
> **C.** Amazon Route 53, because DNS speeds up all traffic types
> **D.** AWS Direct Connect, because dedicated connections are always the fastest option

**20. [Scenario / Judgment] Very Hard**

> A company wants AWS Direct Connect for consistent hybrid performance, but is worried about a single point of failure if the physical circuit goes down. What's the standard architecture fix?
>
> **A.** Use only Direct Connect and accept the risk
> **B.** Pair Direct Connect as the primary path with a Site-to-Site VPN as an automatic backup
> **C.** Replace Direct Connect entirely with a VPN
> **D.** Add a second NAT Gateway

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
