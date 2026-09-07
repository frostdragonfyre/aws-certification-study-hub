# Module 13: Troubleshooting Network Connectivity Issues

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Modules 11 and 12 built the connections and the routing. Sooner or later, something doesn't connect the way it should, and Priya needs a systematic way to find out why — before customers notice. This is Domain 5's third task, closing out the domain.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish VPC Reachability Analyzer from VPC Flow Logs, and know when each fits
- Use route tables, Network ACLs, and Security Groups, in that order, to localize a connectivity problem
- Recognize when a symptom pattern points to a per-instance versus a per-subnet cause
- Recognize when a connectivity complaint isn't actually a networking problem at all
- Design a troubleshooting approach for a stated connectivity failure

---

## VPC Reachability Analyzer vs. VPC Flow Logs

Both tools help diagnose connectivity problems, but they answer different questions at different times.

**VPC Reachability Analyzer** performs a **point-in-time path analysis** between a source and a destination — without sending any actual traffic. Give it a source and destination, and it traces the theoretical path through route tables, Security Groups, and NACLs, and tells you exactly where the path breaks, if it does: a missing route, a Security Group rule that doesn't allow it, a NACL rule that denies it. It's proactive: useful for testing a path *before* something goes wrong, or for pinpointing a break without needing real traffic to reproduce it.

**VPC Flow Logs** capture **metadata about traffic that actually occurred** — source, destination, port, protocol, and whether it was accepted or rejected — at the ENI, subnet, or VPC level. They're retrospective: useful for auditing what really happened, investigating an incident after the fact, or spotting a pattern over time. Flow Logs need real traffic to have occurred; they don't test a hypothetical path the way Reachability Analyzer does.

> ⚠️ **Exam trap:** a scenario needing to know whether two resources **can** communicate, **before** deploying or without waiting for real traffic, is describing **Reachability Analyzer**. A scenario needing to see what traffic **actually flowed** — and whether it was accepted or rejected — over some period, is describing **Flow Logs**.

## Localizing the Problem: Route Tables, NACLs, and Security Groups

When traffic isn't reaching its destination, the efficient approach checks these in order, because each layer has a different blast radius.

A **route table** problem (a missing or incorrect route) affects **every resource in the subnet** the same way — nothing in that subnet can reach the destination at all. A **NACL** problem also affects **every resource in the subnet**, since NACLs apply at the subnet boundary — but unlike a routing problem, a NACL issue often shows up as asymmetric behavior (inbound allowed, but the response can't get back out, since NACLs are stateless and need explicit rules both directions). A **Security Group** problem is **per-instance** (or per-ENI) — it's the one to suspect when one instance in a subnet can't be reached but a neighboring instance in the very same subnet, with the same route table and NACL, works fine.

> ⚠️ **Exam trap:** a scenario where **one instance** in a subnet can't be reached but another instance **in the same subnet** works normally is pointing at that instance's **Security Group**, not the route table or NACL — a route table or NACL problem would affect the whole subnet equally. A scenario where traffic goes in but a response never comes back is pointing at NACL statelessness — check for a missing outbound rule.

## When It Isn't Really a Networking Problem

Not every "I can't connect" report is actually a VPC configuration issue. A workload's own operating system firewall (Windows Firewall, `iptables`, `firewalld`) can block traffic that every AWS-level control — route table, NACL, Security Group — correctly allows, and none of the AWS-level tools will show anything wrong, because nothing at the AWS level is actually blocking it. Similarly, a DNS resolution failure (an application can't resolve a hostname to an IP at all) can look like a connectivity failure but has nothing to do with routing or firewalling once the IP is known — the fix is in DNS resolution, specifically checking that the VPC's `enableDnsSupport` and `enableDnsHostnames` settings are as expected.

> ⚠️ **Exam trap:** if Reachability Analyzer confirms the path is fully allowed, and Flow Logs show the traffic being accepted end to end, but the application still reports it "can't connect," the cause is very likely **outside AWS's network layer entirely** — the instance's own OS firewall, or the application never resolving a hostname in the first place.

## Putting It Together: Troubleshooting Meridian's Connectivity

Priya's troubleshooting approach, closing out Domain 5:

- **Reachability Analyzer** run against every new cross-VPC or hybrid connection before it goes live, catching a missing route or an overly restrictive Security Group before a real user ever hits it.
- **Flow Logs** enabled on every production VPC, giving Priya a historical record to pull when investigating a specific incident after the fact.
- A standard **troubleshooting order** — route table, then NACL, then Security Group — narrowing from "does the whole subnet have a problem" down to "does this one instance have a problem," in that sequence.
- A standing reminder for the team: if AWS-level tools show a clean, fully allowed path and the application still can't connect, check the instance's own firewall and DNS resolution before assuming AWS is at fault.

## What to skip

You don't need to memorize Reachability Analyzer's exact API response fields or Flow Logs' full record format — that's implementation depth beyond this exam. What matters is knowing when to reach for Reachability Analyzer versus Flow Logs, the route-table-then-NACL-then-Security-Group troubleshooting order and why each layer has a different blast radius, and recognizing when the actual cause is outside AWS's network layer entirely.

## Key takeaways

- Reachability Analyzer proactively tests a theoretical path with no real traffic needed; Flow Logs retrospectively record what traffic actually happened and whether it was accepted or rejected.
- Route table and NACL problems affect an entire subnet; Security Group problems are per-instance — a single misbehaving instance in an otherwise healthy subnet points to its Security Group.
- Not every connectivity complaint is a networking problem — a host-level firewall or a DNS resolution failure can look identical to a blocked network path.
- This closes Domain 5: Module 11 connected the network, Module 12 routed and delivered content over it, and Module 13 gave Priya a systematic way to troubleshoot it when something breaks.

## Further reading

- [VPC Reachability Analyzer](https://docs.aws.amazon.com/vpc/latest/reachability/what-is-reachability-analyzer.html) — point-in-time path analysis between two resources.
- [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) — capturing and reading traffic metadata.
- [Security Groups vs. Network ACLs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-comparison.html) — the blast-radius difference revisited from Module 10.
