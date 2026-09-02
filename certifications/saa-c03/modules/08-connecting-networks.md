# Module 8: Connecting Networks

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

Module 7 built one VPC, carefully — a public and private subnet in each of two Availability Zones, with the internet gateway and NAT gateway doing their separate, well-defined jobs. That's the right foundation for one isolated network. But real businesses rarely stay at "one isolated network" for long, and the café is no exception.

This module is about what happens the moment a *second* network enters the picture — another VPC, or a physical location that isn't in AWS at all. Frank and Martha's original café location has a back-office network with a point-of-sale system and inventory scanner that predates any of this cloud work. Sofía is now looking at opening a second location — a commissary kitchen that bakes for both the original café and a growing catering side of the business — and it needs its own AWS presence. Neither of those is solved by anything in Module 7. Connecting networks *to* each other is its own distinct problem, with its own set of AWS services, and its own set of trade-offs between cost, control, and how much you're willing to depend on the public internet.

## Learning objectives

By the end of this module, you should be able to:

- Explain what VPC peering does, and its core limitation (no transitive routing)
- Describe when a Transit Gateway is the better choice over multiple peering connections
- Distinguish a Site-to-Site VPN from AWS Direct Connect, and know when each is appropriate
- Explain what AWS PrivateLink solves that the other options don't
- Match a described connectivity scenario to the right service, the way the exam does

---

## VPC Peering: Connecting Two VPCs Directly

**VPC peering** is a direct, private network connection between exactly two VPCs, letting resources in each one communicate as if they were on the same network — using private IP addresses, never touching the public internet. It's the simplest way to connect two VPCs, and for the café's first step — letting the new commissary kitchen's VPC talk to the original location's VPC — it's exactly enough.

Setting one up is a request-and-accept handshake between the two VPC owners (which might be the same AWS account, or a partner's account entirely), followed by updating each VPC's route tables so traffic addressed to the other VPC's CIDR range routes through the peering connection instead of nowhere.

Two constraints matter more than anything else about peering, and both are exam-tested directly:

- **VPC CIDR ranges can't overlap.** If both VPCs happen to use `10.0.0.0/16`, they can never be peered — this is exactly why planning a VPC's address range thoughtfully in Module 7 matters beyond just that one VPC.
- **Peering is not transitive.** If VPC A is peered with VPC B, and VPC B is peered with VPC C, A and C *cannot* reach each other through B. Each pairing is its own direct, standalone connection — there's no "hop through the middle one."

> ⚠️ **Exam trap:** "Not transitive" is the single most tested fact about VPC peering. A scenario describing three or more VPCs that all need to reach each other, expecting peering alone to connect them all through one central VPC, is describing something that doesn't work — and is usually steering you toward Transit Gateway instead.

## When Peering Stops Scaling: Transit Gateway

The math behind that non-transitive limitation gets ugly fast. Connecting 3 VPCs with peering means 3 individual connections. Connecting 10 VPCs means 45. Every new VPC means a new peering connection to *every existing VPC* it needs to reach — a full mesh, growing far faster than the number of VPCs itself.

**AWS Transit Gateway** solves this by acting as a central hub: each VPC (and, importantly, each on-premises network reachable through a VPN or Direct Connect) connects once, to the Transit Gateway, instead of to every other network individually. Ten VPCs need ten connections to the Transit Gateway, not forty-five connections to each other. It genuinely is a hub-and-spoke network, at the scale a peering mesh can't reach cleanly.

For the café, one commissary kitchen and one original location doesn't yet justify a Transit Gateway — two networks is exactly what peering was built for. But the moment the café franchises, or adds a third location, or needs its VPCs *and* its on-premises office network all reachable from one central point, that's the trigger to migrate off a peering mesh and onto a Transit Gateway.

| | VPC Peering | Transit Gateway |
|---|---|---|
| Topology | Direct, one-to-one | Hub-and-spoke |
| Transitive routing | No | Yes |
| Best for | A small, stable number of VPCs | Many VPCs, or VPCs plus on-premises networks |
| Connections needed for *n* networks | Up to n(n-1)/2 | n |

## Getting Back to On-Premises: Site-to-Site VPN

Peering and Transit Gateway both connect VPCs to other VPCs. Neither one, by itself, reaches Frank and Martha's original back-office network — the point-of-sale system and inventory scanner that were never going to move to AWS. That's a different kind of connection entirely: AWS to a physical, on-premises location.

**AWS Site-to-Site VPN** creates an encrypted connection between a VPC and an on-premises network, running over the public internet. It's fast to set up — often production-ready within minutes to hours — and billed with no large upfront commitment, which matters for a small business like the café that can't justify a big infrastructure investment on a hunch.

The trade-off is right there in how it works: it's still traveling over the public internet, just encrypted. Bandwidth and latency depend on general internet conditions at both ends, not a dedicated, predictable path. For a business just getting its on-premises point-of-sale data flowing into AWS for the first time, that's a completely reasonable trade to make.

## When VPN Isn't Enough: AWS Direct Connect

**AWS Direct Connect** is a dedicated, physical network connection from an on-premises location directly into AWS — bypassing the public internet entirely. Where a Site-to-Site VPN is fast and cheap to stand up, Direct Connect is the opposite trade: significant setup time (often weeks, since it involves physical networking work with a connectivity partner) and real ongoing cost, in exchange for consistent, predictable bandwidth and latency that doesn't fluctuate with general internet traffic.

The decision between the two comes down to one honest question: does this workload actually need consistent, dedicated performance, or is "good enough, most of the time, encrypted" acceptable? For the café's point-of-sale data, a Site-to-Site VPN is almost certainly the right call — modest, non-time-critical data volume, no justification for a dedicated circuit. A business running latency-sensitive, high-volume data transfer between its data center and AWS around the clock is the kind of scenario where Direct Connect actually earns its cost and setup time.

> ⚠️ **Exam trap:** Direct Connect does **not**, by itself, provide encryption — it's a private physical connection, not an encrypted tunnel. A scenario that needs *both* the dedicated performance of Direct Connect *and* encryption in transit is describing Direct Connect combined with a VPN running over it, not Direct Connect alone.

### VPN vs. Direct Connect, side by side

| | Site-to-Site VPN | Direct Connect |
|---|---|---|
| Path | Public internet (encrypted) | Dedicated physical connection |
| Setup time | Minutes to hours | Weeks (physical provisioning) |
| Cost | Low, pay-as-you-go | Higher, ongoing |
| Performance | Variable, internet-dependent | Consistent, predictable |
| Encryption | Built in | Not by default — pair with VPN if needed |

## A Different Problem: AWS PrivateLink

Everything so far has connected entire *networks* to each other. **AWS PrivateLink** solves a narrower, more specific problem: privately accessing a single *service* — whether that's an AWS service or another company's service hosted in its own VPC — without that traffic ever crossing the public internet, and without peering your whole VPC to theirs.

Suppose the café's application needs to call a third-party payment processor's API that happens to run inside AWS, in a completely separate account. Peering would work, but it exposes far more than necessary — the entire network, in both directions, when all that's actually needed is access to one specific service endpoint. PrivateLink creates a private, one-directional connection to just that service, through an interface endpoint in your own VPC. The payment processor's network stays fully isolated from yours; you only ever reach the one service they've deliberately exposed.

That directionality is the detail worth remembering: PrivateLink connections are one-way, to a specific service, not a general two-way network connection like peering. It's the right tool when the requirement is "reach this one service privately," not "connect these two networks."

## Matching the Scenario to the Service

By this point in the course, the exam's networking questions stop asking "what does X do" and start describing a situation, expecting you to pick the right tool:

| Scenario | Right service |
|---|---|
| Two VPCs need to talk directly, and that's likely to stay just two | VPC Peering |
| Many VPCs (or VPCs plus on-premises networks) all need central connectivity | Transit Gateway |
| Connect to on-premises quickly and cheaply, encryption required, some latency variability acceptable | Site-to-Site VPN |
| Connect to on-premises with consistent, dedicated, predictable performance | Direct Connect |
| Privately reach one specific service in another account/VPC, without connecting the whole networks | AWS PrivateLink |

## What to skip

You don't need to configure BGP routing, understand Direct Connect's physical partner ecosystem in depth, or memorize exact VPN throughput numbers — those are deployment details outside the associate exam's scope. What matters is recognizing which category a described need falls into, from the table above.

## Key takeaways

- VPC peering directly connects exactly two VPCs over private IPs, but is **not transitive** — connections don't chain through a shared VPC.
- Transit Gateway replaces a growing peering mesh with a hub-and-spoke model — one connection per network instead of one per pair.
- Site-to-Site VPN is fast, cheap, and encrypted, but travels over the public internet with variable performance.
- Direct Connect is a dedicated physical connection with consistent performance, but takes weeks to provision and isn't encrypted by default.
- AWS PrivateLink privately connects to one specific service, not an entire network — the right tool when peering would expose more than necessary.

## Further reading

- [Amazon VPC Peering Guide](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) — the non-transitive limitation explained in full.
- [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) — the hub-and-spoke model in depth.
- [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) — the connectivity partner process this module simplifies.

---

**Next:** [Module 9 — Securing User, Application, and Data Access](09-securing-user-application-and-data-access.md)
