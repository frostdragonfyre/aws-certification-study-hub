[Shared references](../README.md) · [Hub home](../../README.md)

# Service Decision Tables

Quick-reference tables for the "which service do I pick?" moment. These are for review and fast lookup once you already understand the concepts — the module that teaches each area is the place to actually learn it.

Every table is organized around the question the exam is really asking, which is almost never "what is this service?" and almost always "which of these four does this specific situation call for?"

---

## Storage: which one?

| If the requirement is | Choose | Why |
|---|---|---|
| Store objects retrieved over the web, effectively unlimited | Amazon S3 | Object storage, flat namespace, accessed by key |
| A disk attached to one EC2 instance that survives the instance | Amazon EBS | Block storage, lifecycle independent of the instance |
| Fast temporary disk where losing the data is acceptable | Instance store | Physically attached to the host, gone on stop/terminate |
| Shared file storage mounted by many instances at once | Amazon EFS | File storage with a standard filesystem interface |
| Archive retained for years, retrieval speed irrelevant | S3 Glacier classes | Lowest storage cost, retrieval trades time for price |

**The deciding question for EBS vs. instance store is persistence, not price.** Does this data need to survive the instance? Yes means EBS.

## S3 storage classes

| If access is | Choose | Watch for |
|---|---|---|
| Frequent and predictable | S3 Standard | Default; no retrieval fee |
| Infrequent but needs fast access when it happens | S3 Standard-IA | Retrieval fee applies |
| Infrequent, and re-creatable if an AZ is lost | S3 One Zone-IA | Single AZ only |
| Unknown or changing, no way to predict | S3 Intelligent-Tiering | AWS moves objects based on observed access |
| Archival, retrieval measured in minutes to hours | S3 Glacier family | Cheapest storage, slowest retrieval |

**Durability stays extremely high across all classes.** What changes between them is availability, retrieval speed, and cost — not the likelihood of losing data.

## Databases: which one?

| If the data | Choose | Why |
|---|---|---|
| Has enforced relationships and needs complex joins | Amazon RDS | Managed relational, multiple engines |
| Is relational but needs many read replicas and auto-growing storage | Amazon Aurora | Premium RDS engine, higher performance and availability |
| Is looked up fast by a known key, structure varies per item | Amazon DynamoDB | Managed NoSQL at scale |
| Is years of history queried analytically for reports | Amazon Redshift | Data warehouse, built for OLAP |
| Is about relationships between entities (graphs) | Amazon Neptune | Purpose-built graph database |
| Needs microsecond reads in front of a primary database | Amazon ElastiCache | In-memory cache |
| Is document-oriented, MongoDB-compatible | Amazon DocumentDB | Purpose-built document database |

**Aurora is an engine option inside RDS, not a separate competing service.** The phrase pattern pointing specifically at Aurora is: highly available, relational, needs substantially more read replicas, storage keeps growing.

## RDS: Multi-AZ vs. read replicas

| | Multi-AZ | Read replicas |
|---|---|---|
| **Solves** | Availability and failover | Read traffic scaling |
| **Replication** | Synchronous to a standby | Asynchronous to readable copies |
| **Standby serves reads?** | No | Yes, that's the point |
| **Failover** | Automatic | Not its purpose |

**These are not alternatives.** A scenario describing both an outage risk and a read bottleneck needs both features. Treating them as interchangeable is among the most common exam errors.

## EC2 pricing: which purchasing option?

| If the workload | Choose | Why |
|---|---|---|
| Is new, unpredictable, or short-lived | On-Demand | No commitment while the pattern is unknown |
| Runs steadily and may change family, size, or Region | Compute Savings Plan | Most flexible commitment discount |
| Runs steadily in one family and one Region, size may change | EC2 Instance Savings Plan | Deepest discount for the narrower commitment |
| Is a specific instance type for 1 or 3 years | Reserved Instance | Commitment tied to a configuration |
| Tolerates interruption and can restart | Spot Instance | Deepest discount, reclaimable with little notice |
| Requires single-tenant physical hardware for compliance | Dedicated Hosts / Instances | Isolation requirement, not a cost optimization |

**The tell for EC2 Instance Savings Plans:** the instance family stays fixed while only the size changes.

## EC2 instance families

| Family | Optimized for | Typical use |
|---|---|---|
| General purpose | Balanced CPU, memory, network | Web servers, dev environments |
| Compute optimized | High-performance processors | Batch processing, scientific modeling |
| Memory optimized | Large memory footprints | In-memory databases, real-time analytics |
| Storage optimized | High sequential read/write | Data warehousing, distributed file systems |
| Accelerated computing | GPUs and hardware accelerators | Machine learning, graphics rendering |

**General purpose is a reasonable default, not a universal answer.** When a scenario names a dominant resource need, the matching family is the answer.

## Global infrastructure: Region, AZ, or edge?

| Concept | What it is | Chosen for |
|---|---|---|
| Region | Separate geographic area with multiple AZs | Data residency, latency to users, price, service availability |
| Availability Zone | One or more discrete data centers in a Region | Fault isolation within a Region |
| Local Zone | Region extension near a metro area | Single-digit-millisecond latency for that metro |
| Wavelength Zone | Infrastructure inside a telecom carrier network | Ultra-low latency for mobile/5G |
| Edge location | Cache site in the CloudFront network | Serving cached content near users |

**Local Zones and Wavelength extend a parent Region, they don't replace it.** A workload can use one for the latency-critical component while keeping databases and analytics in the Region.

## Four factors for choosing a Region

| Factor | Ask |
|---|---|
| Compliance | Does a law require data to stay in a specific country? |
| Latency | Where are the users? |
| Price | Does cost differ meaningfully between candidates? |
| Service availability | Does every service needed exist in this Region? |

**Scenario questions usually neutralize three of the four on purpose.** Read for which factor is actually doing the deciding rather than reciting all four.

## Networking: connecting to on-premises

| If the requirement is | Choose | Trade-off |
|---|---|---|
| Encrypted connection, fast to set up | AWS Site-to-Site VPN | Runs over the public internet, subject to internet conditions |
| Dedicated, consistent, private bandwidth | AWS Direct Connect | Physical circuit, longer to provision, higher cost |
| Connecting many VPCs and networks centrally | AWS Transit Gateway | Hub-and-spoke instead of a mesh of peerings |
| Connecting two VPCs directly | VPC Peering | Doesn't scale well past a handful of VPCs |

## Disaster recovery strategies

| Strategy | RTO / RPO | Cost | What's running |
|---|---|---|---|
| Backup and restore | Hours | Lowest | Backups only |
| Pilot light | Tens of minutes | Low | Core services minimal, rest off |
| Warm standby | Minutes | Medium | Scaled-down full environment |
| Multi-site active-active | Near zero | Highest | Full environment in both locations |

**These form a spectrum trading cost against recovery speed.** The RTO and RPO the business states determine which one is appropriate.

## Well-Architected Framework pillars

| Pillar | Core question |
|---|---|
| Operational Excellence | Can we run, monitor, and continuously improve this? |
| Security | Is data and access protected at every layer? |
| Reliability | Does it recover from failure and meet demand? |
| Performance Efficiency | Are we using the right resources efficiently? |
| Cost Optimization | Are we avoiding unnecessary spend? |
| Sustainability | Are we minimizing environmental impact? |

---

*Tables summarize decision logic, not current specifications. Limits, storage class details, and pricing structures change; verify at [aws.amazon.com](https://aws.amazon.com) before relying on specifics.*
