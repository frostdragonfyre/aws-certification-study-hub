[Course index](../README.md) · [Read the paired lesson](../modules/13-troubleshooting-network-connectivity-issues.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 13 Knowledge Check**

Troubleshooting Network Connectivity Issues · 20 questions · Practice — not graded

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

> VPC Reachability Analyzer sends real traffic between the source and destination to test connectivity.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which tool captures metadata about traffic that actually occurred, including whether it was accepted or rejected?

> **A.** VPC Reachability Analyzer
> **B.** VPC Flow Logs
> **C.** AWS Config
> **D.** Security Hub

**3. [Fill in the Blank] Easy**

> A ____________ table problem affects every resource in a subnet the same way, since it applies to the whole subnet.

**4. [Multiple Choice] Easy**

> One instance in a subnet can't be reached, but a neighboring instance in the same subnet works fine. What's the most likely cause?

> **A.** The subnet's route table
> **B.** That instance's Security Group
> **C.** The subnet's NACL
> **D.** The VPC's DHCP options set

**5. [True / False] Easy**

> A connectivity complaint can be caused by something outside AWS's network layer entirely, such as the instance's own OS firewall.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why is VPC Reachability Analyzer useful for testing a path before deploying a workload?

> **A.** It requires production traffic to already be flowing
> **B.** It performs a point-in-time path analysis without sending any real traffic, tracing route tables, Security Groups, and NACLs
> **C.** It automatically fixes any connectivity issue it finds
> **D.** It only works after an incident has already occurred

**7. [Fill in the Blank] Moderate**

> Traffic reaching a subnet but the response never returning suggests a ____________ problem, since that control is stateless and needs explicit rules in both directions.

**8. [Multiple Choice] Moderate**

> Reachability Analyzer confirms a fully allowed path, and Flow Logs show the traffic being accepted end to end, but the application still can't connect. What's the most likely explanation?

> **A.** The Security Group must be misconfigured despite what Reachability Analyzer shows
> **B.** The cause is likely outside AWS's network layer — an OS-level firewall or a DNS resolution failure
> **C.** VPC Flow Logs are unreliable and should be ignored
> **D.** The route table needs to be recreated

**9. [True / False] Moderate**

> A NACL problem typically affects only a single instance, not the whole subnet.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> An application can't resolve a hostname to an IP address at all. Which layer does this point to?

> **A.** The Security Group
> **B.** DNS resolution, not routing or firewalling
> **C.** The NACL
> **D.** The route table

**11. [Fill in the Blank] Moderate**

> The efficient troubleshooting order for a connectivity problem is the route table, then the ____________, then the Security Group.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Priya wants to verify that a new cross-account VPC connection will work correctly before any real workload uses it. What tool fits best?

> **A.** VPC Flow Logs, since they show real traffic
> **B.** VPC Reachability Analyzer, since it tests the theoretical path without needing real traffic
> **C.** AWS Config, since it evaluates compliance
> **D.** CloudTrail, since it logs API calls

**13. [Scenario / Judgment] Hard**

> An entire subnet has suddenly lost the ability to reach a specific destination, and every instance in that subnet is affected equally. What's the most likely first place to check?

> **A.** Each individual instance's Security Group, one at a time
> **B.** The subnet's route table, since a routing problem affects every resource in the subnet the same way
> **C.** The application's own logs exclusively
> **D.** The instance's OS-level firewall

**14. [Scenario / Judgment] Hard**

> Priya needs to investigate what traffic actually reached a specific ENI over the past week, including which connections were rejected. What fits best?

> **A.** VPC Reachability Analyzer, since it tests theoretical paths
> **B.** VPC Flow Logs, since they retrospectively record actual traffic and whether it was accepted or rejected
> **C.** Security Hub, since it aggregates findings
> **D.** AWS Config, since it tracks configuration changes

**15. [Scenario / Judgment] Hard**

> A team spends hours checking Security Group rules for a connectivity issue, finds nothing wrong, and then discovers the real cause is the instance's Windows Firewall blocking the port locally. What lesson does this illustrate?

> **A.** Security Groups should always be checked last, never first
> **B.** Not every connectivity complaint is an AWS networking problem — a clean, fully allowed AWS-level path doesn't rule out an OS-level firewall
> **C.** Windows instances cannot use Security Groups at all
> **D.** VPC Flow Logs should have been disabled

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Reachability Analyzer and Flow Logs both diagnose connectivity issues, so it doesn't matter which one you reach for." Correct this using this module's content.

> **A.** They're right — the two tools are fully interchangeable in every situation
> **B.** They're different: Reachability Analyzer proactively tests a theoretical path with no real traffic needed, while Flow Logs retrospectively record what traffic actually happened — testing a path before deployment calls for Reachability Analyzer, and investigating a past incident calls for Flow Logs
> **C.** Flow Logs require no real traffic; Reachability Analyzer requires real traffic
> **D.** Reachability Analyzer is simply a faster version of Flow Logs

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes always starting connectivity troubleshooting with the Security Group, arguing "it's the most common cause, so it's always the fastest place to start." Evaluate this using this module's content.

> **A.** Agree — Security Groups should always be checked first regardless of the symptom
> **B.** Disagree — the efficient order checks route tables and NACLs first because they have a wider blast radius (affecting the whole subnet); jumping straight to a per-instance Security Group check first can waste time when the actual cause is affecting every instance in the subnet equally
> **C.** Disagree, but only because Security Groups cannot be misconfigured
> **D.** Agree, since NACLs and route tables never cause connectivity issues

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a fully allowed path in both Reachability Analyzer and Flow Logs doesn't guarantee an application will actually connect successfully.

> **A.** Reachability Analyzer and Flow Logs are always wrong and shouldn't be trusted
> **B.** Both tools only cover AWS's network layer — route tables, Security Groups, and NACLs — and can't see problems above that layer, like an OS-level firewall blocking the port locally or a DNS resolution failure preventing the application from ever getting an IP to connect to
> **C.** A fully allowed path always guarantees success, so this scenario is impossible
> **D.** Flow Logs and Reachability Analyzer only work for on-premises connections, not VPC traffic

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that VPC Flow Logs alone are sufficient for all pre-deployment connectivity validation, so Reachability Analyzer is unnecessary. Argue against this using this module's content.

> **A.** Agree — Flow Logs can validate a path before any traffic has ever flowed
> **B.** Disagree — Flow Logs are retrospective and require real traffic to have already occurred; validating a path before deployment, with no real traffic yet, is exactly the proactive, no-traffic-needed job Reachability Analyzer is built for
> **C.** Disagree, but only because Flow Logs cannot be enabled on a VPC
> **D.** Agree, since Reachability Analyzer requires production traffic to run

**20. [Scenario / Judgment] Very Hard**

> A student says: "If two instances are in the same subnet with the same route table and NACL, and one can be reached while the other can't, the route table must be misconfigured." Evaluate this claim using this module's content.

> **A.** Agree — a route table issue is the only possible explanation
> **B.** Disagree — a route table or NACL problem would affect every resource in the subnet equally, since both apply at the subnet level; one instance failing while an identically-situated neighbor succeeds points to that specific instance's Security Group instead
> **C.** Disagree, but only because route tables cannot be shared across instances
> **D.** Agree, since Security Groups always match across instances in the same subnet

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
