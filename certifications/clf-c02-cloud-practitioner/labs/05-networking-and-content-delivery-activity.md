**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 5**

**Lab Worksheet — Networking and Content Delivery**

Activity 1: Build the Network · Activity 2: Networking Service Hunt

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Build the Network (20 min)

### How this works

Below is a simple two-tier web application: public-facing web servers and a private backend database, all inside one VPC. For each blank, write in the component that belongs there. Work on your own first, then we'll build it together on the board.

*This is the single most tested layout in Domain 3's networking questions — a public subnet, a private subnet, and the pieces that connect them to the internet (or deliberately don't).*

### Label the diagram

| # | Description | Component |
|---|---|---|
| 1 | The logically isolated network that contains everything below | |
| 2 | Attached to the VPC so the public subnet can send/receive traffic directly to/from the internet | |
| 3 | Sits in the public subnet so the *private* subnet can reach the internet outbound only (e.g., to download updates) | |
| 4 | Determines whether a subnet counts as "public" or "private" in the first place | |
| 5 | Instance-level firewall — stateful, allow rules only | |
| 6 | Subnet-level firewall — stateless, supports explicit deny rules | |

### Does the line move? (discuss as a class)

Look at #2 and #3 again — both gateways touch the internet, but only one is two-way.

| Question | Your answer |
|---|---|
| Which gateway lets traffic flow in *and* out? | |
| Which gateway is outbound only, and why would you want that for a database? | |
| If a private subnet's database instance can somehow be reached directly from the internet, what's most likely misconfigured — the NAT Gateway, or the route table? | |

### Think about it

1. Why does a route table — not a label someone types in — actually decide whether a subnet is public or private?
2. A security group can't write a "deny" rule. If you need to explicitly block one bad IP address, which tool from the diagram do you reach for instead?
3. Give one real-world example of something that belongs in a private subnet, and explain why it shouldn't be directly reachable from the internet.

---

## Activity 2 — Networking Service Hunt (25 min)

### How this works

Work on your own. For each scenario, write which AWS networking or content-delivery service fits best — and UNDERLINE the exact phrase that gave it away. We'll go through the answers together as a class afterward.

*Same skill as the security tool hunt from Lecture 4: noticing which phrase is load-bearing is what the real exam question is testing.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the toolkit

| Service / Component | What it's for |
|---|---|
| Amazon VPC | A logically isolated network where you launch AWS resources |
| Internet Gateway | Two-way internet access for a public subnet |
| NAT Gateway | Outbound-only internet access for a private subnet |
| Security Group | Instance-level, stateful, allow-only firewall |
| Network ACL | Subnet-level, stateless firewall, supports explicit deny |
| Amazon Route 53 | DNS — translates domain names to IP addresses |
| Amazon CloudFront | CDN — caches content at edge locations close to users |
| AWS Direct Connect | Dedicated private physical connection to AWS |
| Site-to-Site VPN | Encrypted connection to AWS over the public internet |
| AWS Global Accelerator | Routes application traffic over AWS's private backbone |

### The scenarios

*Underline the deciding phrase in each scenario as you read it.*

| # | Scenario | Your answer |
|---|---|---|
| 1 | A company needs its own isolated network in AWS before launching any EC2 instances. | |
| 2 | A backend database must be able to download a security patch from the internet, but must never accept an inbound connection from it. | |
| 3 | A security team needs to explicitly block traffic from one specific malicious IP address at the subnet level. | |
| 4 | A streaming company wants viewers around the world to load video content quickly, from a location near them instead of one origin server. | |
| 5 | A visitor types `example.com` into a browser and it needs to resolve to the correct server's IP address. | |
| 6 | A bank needs a dedicated, private, physically separate network connection to AWS for consistent performance, unaffected by public internet congestion. | |
| 7 | A startup needs a hybrid connection to AWS set up quickly and cheaply, encrypted over the existing internet connection. | |
| 8 | A global mobile game needs faster, more reliable routing for its live traffic using AWS's own private backbone instead of the public internet. | |
| 9 | A web server in a public subnet needs two-way internet access attached at the VPC level. | |
| 10 | An architect needs return traffic for an already-allowed connection to pass automatically, without writing a separate rule. | |

### Pick any two and go deeper

For two of the scenarios above, write out why the service you picked beats the next most tempting wrong answer.

**Scenario #____ — why this beats the tempting wrong answer:**

**Scenario #____ — why this beats the tempting wrong answer:**

### The shortcut — write this down

**For ANY AWS networking scenario on the exam, ask in this order:**

1. Is this about **where resources live** and how the network is carved up? → VPC, subnets.
2. Is this about **letting traffic in and out** of a subnet? → Internet Gateway (two-way) or NAT Gateway (outbound only).
3. Is this about **filtering** traffic? → Security Group (instance, stateful, allow-only) or Network ACL (subnet, stateless, allow + deny).
4. Is this about **resolving a domain name**? → Route 53.
5. Is this about **caching content close to users worldwide**? → CloudFront.
6. Is this about **connecting a physical location to AWS**? → Direct Connect (dedicated, consistent) or VPN (fast, over the internet).
7. Is this about **routing live application traffic over AWS's own network**? → Global Accelerator.

*Notice the pattern: VPC/subnets are about where things live, gateways are about direction of internet access, SG/NACL are about filtering, and Route 53/CloudFront/Direct Connect/VPN/Global Accelerator are each about a different flavor of getting traffic where it needs to go. Ten different jobs — the exam is testing whether you can tell them apart, not just recognize the names.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Redraw Activity 1's diagram from memory, no notes, and check it against the worksheet. |
| 2 | Explain in your own words why Direct Connect and Site-to-Site VPN are often paired together (primary + backup), not treated as either/or. |
| 3 | Explain why CloudFront isn't the right answer for connecting a corporate office to AWS, even though both involve "getting data to AWS faster." |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 5 + knowledge check (aim 80%+ first attempt) |
| | Sketch the two-tier VPC diagram from Activity 1 from memory once, without looking at your notes |
| | Pick one networking service from tonight's toolkit and explain what it does in your own words, no notes |
