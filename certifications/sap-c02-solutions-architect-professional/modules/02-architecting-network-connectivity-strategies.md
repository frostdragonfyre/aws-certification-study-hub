<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](01-welcome-to-solutions-architect-professional.md) · [Next module](03-prescribing-security-controls-at-the-organization-level.md) · [Quiz](../quizzes/02-architecting-network-connectivity-strategies-quiz.md) · [Slides](../lectures/02-architecting-network-connectivity-strategies.pptx)
<!-- /hub-navigation -->

# Module 2: Architecting Network Connectivity Strategies

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Right now, Meridian Hospitality Group's AWS footprint is three disconnected islands. Café Sol runs in its own account. Haven & Co. Hotels runs in a separate account with its own VPC. Ridgeline Diner Co. doesn't touch AWS at all yet — its point-of-sale and inventory systems run on physical servers at company headquarters. None of these three environments can currently reach any of the others, and there's no shared way for Meridian's central IT team to manage identity, logging, or shared services across all three.

This module is about the first real Domain 1 task: designing how network traffic should actually flow — between AWS accounts, and between AWS and an on-premises data center — as an organization grows past a single account. Get this wrong early, and every VPC added later inherits a tangled, unmanageable mess of ad-hoc connections. Get it right, and adding a fourth brand next year is a straightforward extension of an existing pattern.

## Learning objectives

By the end of this module, you should be able to:

- Compare VPC peering and AWS Transit Gateway for connecting multiple VPCs, and explain why hub-and-spoke scales better than a full mesh
- Compare AWS Direct Connect and Site-to-Site VPN for hybrid connectivity to an on-premises data center
- Explain what AWS PrivateLink does and how it differs from full network-level connectivity
- Describe how Route 53 Resolver supports DNS resolution across VPCs and between AWS and on-premises networks
- Recommend a network connectivity strategy for a stated multi-account, hybrid scenario

---

## Connecting Multiple VPCs: Peering vs. Transit Gateway

The most basic way to connect two VPCs — even across different AWS accounts — is **VPC peering**: a direct, one-to-one network connection between exactly two VPCs, with traffic routed privately without crossing the public internet. It works well for a small, fixed number of connections.

It stops working well the moment the number of VPCs grows. VPC peering connections aren't transitive — if VPC A peers with VPC B, and VPC B peers with VPC C, traffic still can't flow from A to C through B. Connecting every VPC to every other VPC directly requires a full mesh of peering connections, and the number of connections needed grows quadratically: 3 VPCs need 3 peering connections, 6 VPCs need 15, 10 VPCs need 45. Each one needs its own route table entries, on both sides, maintained by hand.

**AWS Transit Gateway** solves this with a hub-and-spoke model: each VPC connects once, to the Transit Gateway, and the Transit Gateway routes traffic between all attached VPCs (and, as covered below, on-premises networks) centrally. Adding a new VPC means one new attachment, not N new peering connections. Transit Gateway also supports route tables of its own, so you can segment traffic — for example, allowing Café Sol's and Haven & Co.'s VPCs to reach a shared services VPC, without necessarily allowing them to reach each other directly.

> ⚠️ **Exam trap:** a scenario describing "a small, fixed number of VPCs that need to talk to each other, with no plans to grow" can reasonably use VPC peering. A scenario describing "multiple accounts, expected to grow, needing centralized control over which networks can reach which" is describing Transit Gateway. The number of VPCs mentioned in the scenario is often the signal — a handful stays peering-friendly; a dozen or more, or an explicit statement about future growth, points to Transit Gateway.

## Connecting to On-Premises: Direct Connect vs. Site-to-Site VPN

Ridgeline's headquarters isn't in AWS at all yet, but Meridian's IT team still needs a way to reach it — for the migration planning covered later in this course, and for day-to-day administrative access in the meantime. Two standard options connect an AWS environment to an on-premises network:

- **AWS Site-to-Site VPN** creates an encrypted IPsec tunnel over the public internet between an on-premises router and a VPC. It's fast to set up — often hours, not weeks — and inexpensive, but its throughput and latency are subject to the public internet's variability, since the tunnel still traverses it.
- **AWS Direct Connect** establishes a dedicated, private physical network connection between an on-premises location and AWS, through a Direct Connect location, bypassing the public internet entirely. It offers more consistent latency and higher throughput than VPN, but takes longer to provision — real physical circuits have to be run — and costs meaningfully more.

A common pattern uses both together: Direct Connect as the primary path, with Site-to-Site VPN configured as an automatic failover if the dedicated connection goes down. This gets Direct Connect's performance most of the time, without a single point of failure.

> ⚠️ **Exam trap:** "we need this working by next week" points to VPN — Direct Connect's physical provisioning timeline usually can't meet that. "We need consistent, predictable, high-throughput connectivity for an ongoing, large-scale data transfer" points to Direct Connect. Don't default to Direct Connect just because it sounds more "enterprise" — read for the actual stated timeline and throughput requirement.

## AWS PrivateLink: Private Access Without Full Network Connectivity

Not every cross-account or cross-VPC need requires full network-level connectivity. Sometimes one VPC just needs to call a *specific service* running in another VPC or account — without being able to reach anything else in that VPC, and without either side needing to manage overlapping IP address ranges or route tables at all.

**AWS PrivateLink** provides exactly this: it exposes a specific service (running behind a Network Load Balancer, for example) as a private endpoint that consumers in other VPCs can call, without any VPC peering, Transit Gateway attachment, or route table changes required. Traffic never traverses the public internet, and the consumer never gets broader network access to the provider's VPC — just access to that one exposed service.

This matters for Meridian specifically: if a shared service like a central authentication API needs to be callable from Café Sol's, Haven & Co.'s, and eventually Ridgeline's environments, but those environments shouldn't otherwise be able to reach into whichever account hosts that API, PrivateLink is a tighter fit than putting all four environments on the same Transit Gateway route table.

## Route 53 Resolver: DNS Across VPCs and On-Premises

Every one of the connectivity patterns above solves *routing* — getting packets from one network to another. None of them, by itself, solves *name resolution* — letting a resource in one VPC look up a hostname that only makes sense in another VPC, or in the on-premises network.

**Amazon Route 53 Resolver** handles this. Every VPC gets a Resolver automatically for resolving standard AWS-internal DNS names, but for hybrid and multi-VPC scenarios, **Resolver endpoints** — inbound and outbound — let DNS queries cross network boundaries. An **outbound endpoint** forwards DNS queries from inside a VPC to DNS servers elsewhere (like an on-premises DNS server, over the Direct Connect or VPN connection already in place). An **inbound endpoint** allows DNS queries from outside the VPC (like from on-premises) to resolve names hosted inside AWS. Combined with **Resolver rules**, specific domains can be forwarded to specific resolvers — so a query for an on-premises hostname goes to the on-premises DNS server, while everything else resolves normally.

Without this, engineers on Café Sol's team troubleshooting a shared service hosted in a different Meridian account would need to know and hardcode IP addresses instead of using hostnames — exactly the kind of manual, error-prone process a professional-level network design is meant to eliminate.

## Putting It Together: Meridian's Network Connectivity Strategy

Sofía's recommendation for Meridian's network architecture uses every piece covered in this module, matched to what it's actually good at:

- A **Transit Gateway** as the hub, with Café Sol's VPC and Haven & Co.'s VPC each attached as spokes — not a peering mesh, since Meridian expects to add more brands over time, and centralized route control matters for keeping brands appropriately isolated from each other while still reaching shared services.
- A dedicated **shared services VPC**, also attached to the Transit Gateway, hosting things every brand needs — central logging, a shared directory service, and (per the PrivateLink discussion above) authentication, exposed via PrivateLink rather than full network access.
- **Site-to-Site VPN** connecting Ridgeline's headquarters to the Transit Gateway immediately, since Meridian's IT team needs working connectivity now for migration planning; a switch to **Direct Connect** is planned for later, once Ridgeline's actual AWS workloads go live and need the more consistent throughput.
- **Route 53 Resolver** endpoints so that hostnames resolve correctly in both directions — AWS resources can look up Ridgeline's on-premises systems by name during the migration-planning work, and once Ridgeline systems move into AWS, the reverse holds too.

## What to skip

You don't need to memorize Direct Connect's exact port speeds or Transit Gateway's specific attachment limits — that's implementation detail beyond this exam. What matters is choosing correctly between peering and Transit Gateway based on scale and growth, between VPN and Direct Connect based on timeline and throughput, recognizing when PrivateLink fits better than full connectivity, and understanding what Route 53 Resolver actually adds on top of routing.

## Key takeaways

- VPC peering is a direct, non-transitive, one-to-one connection that works for a small number of VPCs; Transit Gateway is a hub-and-spoke model that scales to many VPCs and accounts with centralized route control.
- Site-to-Site VPN is fast to provision and inexpensive but travels the public internet; Direct Connect is a dedicated private connection with more consistent performance but a longer setup timeline and higher cost — the two are often combined, Direct Connect primary with VPN as failover.
- AWS PrivateLink exposes one specific service privately across VPCs or accounts, without granting the broader network access that peering or Transit Gateway would.
- Route 53 Resolver, via inbound and outbound endpoints and Resolver rules, solves DNS resolution across VPC and on-premises boundaries — a separate problem from routing, which the other services in this module solve.
- Meridian's strategy combines all four: Transit Gateway as the hub for Café Sol and Haven & Co., a shared-services VPC exposed via PrivateLink, Site-to-Site VPN to Ridgeline now with Direct Connect planned later, and Route 53 Resolver tying DNS together across all of it.

## Further reading

- [Amazon VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) — peering connections and their non-transitive limitation.
- [AWS Transit Gateway Documentation](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) — hub-and-spoke connectivity and Transit Gateway route tables.
- [AWS Direct Connect User Guide](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) and [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) — the two standard hybrid connectivity options.
- [Amazon Route 53 Resolver Documentation](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html) — inbound/outbound endpoints and Resolver rules for hybrid DNS.
