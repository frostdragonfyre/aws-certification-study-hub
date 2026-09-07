# Module 11: Implementing Networking Features and Connectivity

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Domain 4 protected the data itself and the traffic moving through a single VPC. Domain 5 zooms out: how VPCs connect to each other, how Meridian's on-premises systems reach AWS, and how workloads reach AWS services without touching the public internet at all. This is Domain 5's first task, opening the domain.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish VPC peering from Transit Gateway, and know when each fits
- Explain why VPC peering connections are non-transitive
- Distinguish Site-to-Site VPN from Direct Connect
- Distinguish a Gateway endpoint from an Interface endpoint
- Design a connectivity strategy for a stated multi-VPC or hybrid requirement

---

## VPC Peering vs. Transit Gateway

**VPC peering** connects exactly two VPCs directly, with a private, one-to-one networking connection between them. It's simple to set up and free of an hourly charge for the connection itself, but it doesn't scale cleanly: connecting five VPCs to each other with peering alone means ten separate peering connections (a full mesh), and every one of them has to be created, routed, and maintained individually.

**Transit Gateway** is a regional hub that many VPCs (and VPN connections, and Direct Connect connections) attach to once. Instead of a mesh of point-to-point connections, every attachment talks to the hub, and the hub routes between them — connecting ten VPCs takes ten attachments to the Transit Gateway, not forty-five peering connections.

The detail that catches people: **VPC peering connections are non-transitive**. If VPC A is peered with VPC B, and VPC B is peered with VPC C, A cannot reach C through B — that traffic simply isn't routed, no matter how the route tables look. A Transit Gateway, by contrast, supports transitive routing by design — that's the whole point of the hub.

> ⚠️ **Exam trap:** a scenario needing connectivity among **many VPCs** (roughly four or more) is describing a job for **Transit Gateway** — peering's full-mesh scaling problem is the tell. And a scenario where traffic needs to pass **through** one VPC to reach another via peering is describing something peering **cannot do** — non-transitivity is the tell, and the fix is either a direct peering connection or a Transit Gateway.

## Site-to-Site VPN vs. Direct Connect

Both **Site-to-Site VPN** and **Direct Connect** connect an on-premises network to a VPC, and both show up constantly in hybrid scenarios. They differ in what they're built on top of.

**Site-to-Site VPN** runs an encrypted IPsec tunnel over the **public internet**. It can be set up in minutes to hours, has no special hardware requirement beyond a supported customer gateway device, and costs relatively little — but its performance depends on the public internet path between the two endpoints, so latency and throughput can vary.

**Direct Connect** is a **dedicated, private physical network connection** from Meridian's premises to AWS, bypassing the public internet entirely. It delivers consistent, predictable latency and higher sustained bandwidth than a VPN — but provisioning it involves working with an AWS Direct Connect partner and physical cross-connects, so it typically takes weeks to establish, not minutes.

A common real-world pairing: Direct Connect as the primary hybrid connection, with a Site-to-Site VPN configured as an automatic failover path if the dedicated connection goes down — consistent performance most of the time, with a fallback that doesn't depend on the same physical infrastructure.

> ⚠️ **Exam trap:** a scenario needing a connection **quickly**, with **encryption** built in, over the public internet, is describing **Site-to-Site VPN**. A scenario emphasizing **consistent, predictable latency** and **high sustained bandwidth**, where setup time isn't the constraint, is describing **Direct Connect**. And a scenario wanting Direct Connect's performance with a safety net if the dedicated line fails is describing **Direct Connect with a VPN as backup** — not one or the other alone.

## Gateway Endpoints vs. Interface Endpoints

A **VPC endpoint** lets resources in a VPC reach an AWS service privately, without traversing the public internet or needing a NAT gateway or internet gateway. There are two kinds, and they aren't interchangeable.

A **Gateway endpoint** supports only **S3 and DynamoDB**. It works as a route table entry — no hourly charge, no ENI, no data processing fee — traffic to the service just gets routed privately through the endpoint. An **Interface endpoint** (built on AWS PrivateLink) supports most other AWS services, and works differently: it creates an **elastic network interface (ENI)** with a private IP address in the subnet, and comes with an hourly charge plus a per-GB data processing fee.

> ⚠️ **Exam trap:** a scenario needing private access to **S3 or DynamoDB** at the **lowest cost**, with no interest in an ENI, is describing a **Gateway endpoint**. A scenario needing private access to a **different AWS service** (SNS, SQS, Systems Manager, and most others) is describing an **Interface endpoint** — Gateway endpoints simply don't support them, regardless of cost preference.

## Putting It Together: Connecting Meridian's Environment

Priya's connectivity design, opening Domain 5:

- **Transit Gateway** as the hub connecting Meridian Loyalty's, Café Sol's, and Ridgeline's VPCs, rather than a growing mesh of individual peering connections as more workloads get added.
- **Direct Connect** as the primary link from Meridian's headquarters to AWS, with a **Site-to-Site VPN** configured as automatic failover if the dedicated connection has an outage.
- **Gateway endpoints** for the S3 buckets every workload reads from and writes to, keeping that traffic off the public internet at no additional hourly cost.
- **Interface endpoints** for Systems Manager, so EC2 instances in private subnets can be managed through Session Manager without a NAT gateway or a public IP.

## What to skip

You don't need to memorize Transit Gateway's exact route table propagation configuration or Direct Connect's physical cross-connect ordering process — that's implementation depth beyond this exam. What matters is knowing when peering's simplicity is enough versus when its non-transitivity and mesh scaling become a problem, VPN versus Direct Connect's performance and setup-time tradeoff, and which VPC endpoint type a given AWS service actually supports.

## Key takeaways

- VPC peering is simple and free but non-transitive and doesn't scale past a few VPCs; Transit Gateway is a hub that supports transitive routing and scales to many attachments.
- Site-to-Site VPN is fast to set up and encrypted over the public internet; Direct Connect is a dedicated private connection with consistent performance but a much longer lead time — the two are often paired, Direct Connect primary with VPN as failover.
- Gateway endpoints (S3 and DynamoDB only) are free route table entries; Interface endpoints (most other services) are ENI-based with an hourly and per-GB cost.
- This opens Domain 5: Module 11 connects the VPCs and the hybrid network, and the next modules build on that foundation with DNS, content delivery, and troubleshooting.

## Further reading

- [VPC Peering vs. Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) — when a hub-and-spoke model replaces a peering mesh.
- [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) — encrypted connectivity over the public internet.
- [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) — dedicated private connectivity, and pairing it with VPN failover.
- [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints.html) — Gateway endpoints vs. Interface endpoints, and which services each supports.
