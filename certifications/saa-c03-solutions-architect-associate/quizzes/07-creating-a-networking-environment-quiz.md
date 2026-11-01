[Course index](../README.md) · [Read the paired lesson](../modules/07-creating-a-networking-environment.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 7 Knowledge Check**

Creating a Networking Environment · 20 questions · Practice — not graded

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

> Every AWS resource with a network presence must live inside a VPC — there is no "no VPC" option.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS component allows communication between resources in a VPC and the internet, and attaches directly to the VPC itself?
>
> **A.** NAT gateway
> **B.** Internet gateway
> **C.** Route table
> **D.** NAT instance

**3. [Fill in the Blank] Easy**

> A range of IP addresses carved out of a VPC's CIDR block, and tied to exactly one Availability Zone, is called a ____________.

**4. [Multiple Choice] Easy**

> In CIDR notation, which address range contains *more* individual IP addresses?
>
> **A.** 10.0.0.0/16
> **B.** 10.0.0.0/24
> **C.** 10.0.0.0/28
> **D.** They all contain the same number of addresses

**5. [True / False] Easy**

> A NAT gateway allows resources in a private subnet to initiate outbound connections to the internet, while blocking connections initiated from the internet.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What actually determines whether a subnet is "public" or "private"?
>
> **A.** A checkbox set when the subnet is created
> **B.** The subnet's name
> **C.** Whether its associated route table has a route to an internet gateway
> **D.** Whether it contains an EC2 instance with a public IP address

**7. [Fill in the Blank] Moderate**

> A NAT gateway must be deployed into a ____________ subnet, even though the resources it serves live in a private subnet.

**8. [Multiple Choice] Moderate**

> A café's database subnet has no route to an internet gateway, but does have a route to a NAT gateway. What can this subnet do?
>
> **A.** Accept inbound connections from the internet, but not send outbound traffic
> **B.** Initiate outbound connections to the internet, but not accept inbound connections from it
> **C.** Neither send nor receive any internet traffic
> **D.** Both send and receive internet traffic freely

**9. [True / False] Moderate**

> A single subnet can span multiple Availability Zones if it's created with a large enough CIDR block.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Every route table in a VPC starts with which default route?
>
> **A.** A route to the internet gateway
> **B.** A route to the NAT gateway
> **C.** A route that keeps traffic addressed to the VPC's own CIDR block inside the VPC
> **D.** No default routes — every route must be added manually

**11. [Fill in the Blank] Moderate**

> The legacy, self-managed EC2-based alternative to a NAT gateway is called a NAT ____________.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A café architecture has one NAT gateway, placed in the public subnet of Availability Zone A. Private subnets exist in both AZ A and AZ B. What happens if AZ A fails?
>
> **A.** Nothing — NAT gateways automatically fail over across AZs
> **B.** Private subnets in AZ B lose outbound internet access, because they depended on the NAT gateway in AZ A
> **C.** Only inbound traffic is affected; outbound traffic continues normally
> **D.** The internet gateway automatically takes over the NAT gateway's job

**13. [Scenario / Judgment] Hard**

> A route table has a correctly configured route to an internet gateway, but instances in its associated subnet still can't be reached from the internet. What's the most likely explanation, based on this module?
>
> **A.** The route table must be misconfigured, despite appearances
> **B.** The subnet must be in the wrong Availability Zone
> **C.** A security group or network ACL (covered in a later module) is most likely blocking the traffic — routing gets traffic to the door, but doesn't decide whether it's let in
> **D.** VPCs cannot support inbound internet traffic under any configuration

**14. [Scenario / Judgment] Hard**

> Sofía wants to resize the café's VPC to a larger CIDR block after several subnets have already been created inside it. What's true here?
>
> **A.** This is a routine, no-cost operation
> **B.** A VPC's CIDR block can't simply be shrunk or resized once subnets are carved out of it — this is exactly why sizing it generously up front matters
> **C.** AWS automatically resizes VPCs as usage grows
> **D.** Only the account root user can ever change a VPC's size

**15. [Scenario / Judgment] Hard**

> An architect proposes giving the café's database subnet a route directly to the internet gateway, reasoning "it's faster than routing through NAT." What's wrong with this reasoning?
>
> **A.** Nothing — this is a legitimate way to improve database performance
> **B.** It would make the database subnet public, exposing the database directly to the internet, which defeats the entire purpose of separating it in the first place
> **C.** Internet gateways don't support database traffic
> **D.** NAT gateways are always faster than internet gateways, so this wouldn't even achieve the stated goal

**16. [Scenario / Judgment] Hard**

> Why does a NAT gateway charge hourly plus a per-GB data processing fee, while an internet gateway has no hourly charge at all?
>
> **A.** This is arbitrary AWS pricing with no underlying reason
> **B.** An internet gateway is a shared, VPC-wide component AWS scales for you at no dedicated cost; a NAT gateway is a dedicated, AZ-scoped managed resource actively processing and translating your traffic
> **C.** NAT gateways are actually cheaper than internet gateways in most Regions
> **D.** Internet gateways only work with S3, so they're priced differently

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "public and private are properties of a subnet, so once I mark a subnet as private, it's secure." Correct this statement precisely, using this module's concepts.
>
> **A.** The statement is correct as written
> **B.** There's no such thing as marking a subnet private — "private" only describes the *absence* of a route to an internet gateway in that subnet's route table; nothing is ever "marked," and the same subnet becomes public the moment such a route is added
> **C.** Subnets are private by default and public only if an internet gateway is physically attached to them
> **D.** Only NAT gateways can make a subnet private

**18. [Scenario / Judgment] Very Hard**

> For high availability, the café deploys public and private subnets in two Availability Zones, with one NAT gateway per AZ. A teammate suggests removing the second NAT gateway to save the hourly cost, keeping just one for the whole VPC. What's the actual trade-off being proposed?
>
> **A.** No trade-off — NAT gateways are redundant across AZs automatically, so removing one is free savings
> **B.** Reduced cost in exchange for a single point of failure: if the AZ holding the remaining NAT gateway fails, every private subnet in the *other* AZ loses outbound internet access too
> **C.** This would only affect inbound traffic, which private subnets don't accept anyway, so it's a safe change
> **D.** Removing a NAT gateway automatically re-routes its traffic through the internet gateway instead

**19. [Scenario / Judgment] Very Hard**

> A café architecture review flags a NAT *instance* still running from an early prototype, instead of a NAT gateway. What's the strongest, most complete justification for replacing it?
>
> **A.** NAT instances are simply not supported by AWS anymore
> **B.** A NAT instance is a self-managed EC2 instance with no built-in redundancy that you must patch and scale yourself, and it represents a single point of failure unless extra infrastructure is built around it — a NAT gateway is managed, redundant within its AZ, and requires none of that operational overhead
> **C.** NAT instances can only be used in the default VPC
> **D.** There is no real difference; the recommendation is purely about naming conventions

**20. [Scenario / Judgment] Very Hard**

> Connect this module back to Module 1's V4 milestone ("enhance the security of the web application" using VPC features). Which combination of this module's components actually delivers that outcome, and why is no single component sufficient alone?
>
> **A.** The internet gateway alone secures the application, since it controls all internet access
> **B.** The VPC, subnets, route tables, and gateways work together — the VPC provides isolation, subnets and their route tables determine what's reachable from where, and gateways (internet and NAT) control the *direction* traffic is allowed to flow; removing any one piece breaks the design, which is why they're taught as one connected system rather than separate features
> **C.** Security groups alone deliver this outcome; the networking layer is irrelevant to security
> **D.** NAT gateways alone secure the application by hiding all resources from the internet

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
