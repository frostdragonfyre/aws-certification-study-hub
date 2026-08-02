# Module 3: Securing Access

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 50 minutes

## Why this matters

Every architecture this course builds — starting with the café's very next update — needs an answer to one question before anything else gets designed: who, and what, is allowed to do which things? Get that answer wrong, and every other decision in the architecture inherits the mistake. Get it right, and it becomes something you barely have to think about again, because it was designed deliberately instead of patched together after the fact.

This module is the first of the course's "architecture layer" modules, and it's deliberately first for a reason: access control isn't a feature you bolt onto a finished design. It's a foundation every other layer — storage, compute, databases, networking — gets built on top of.

## Learning objectives

By the end of this module, you should be able to:

- Describe the security principles in the AWS Cloud
- Explain the purpose of IAM users, groups, and roles
- Explain how IAM policies determine permissions in an AWS account

---

## Security Principles in the AWS Cloud

Before any specific service, a few principles shape every access-control decision you'll make in this course:

**Least privilege.** Grant exactly the access a person or system needs to do its job — nothing more. This sounds obvious and is routinely ignored in practice, usually because it's faster to grant broad access once than to figure out the minimum needed. The cost shows up later: broad access that was never actually necessary is pure risk sitting unused, waiting for a mistake or a compromised credential to matter.

**Defense in depth.** Don't rely on a single control to protect something important. Layer multiple, independent protections — so that if one fails or gets bypassed, others are still standing between an attacker and what they're after.

**Shared responsibility, applied to access.** You met the shared responsibility model in CLF-C02: AWS secures the cloud itself, you secure what you put in it. Access control is one of the clearest places this plays out — AWS gives you IAM as a powerful, flexible tool, but *how* you configure it (who's in which group, what each policy actually allows) is entirely your responsibility. A misconfigured policy is never AWS's failure.

**Verify explicitly, trust nothing by default.** By default, an IAM identity in AWS can do nothing at all. Every single permission has to be explicitly granted — the opposite of an all-access-until-restricted model. This "default deny" posture is one of IAM's most important design decisions, and it's the reason a newly created IAM user is harmless until you deliberately attach policies to it.

## IAM Users, Groups, and Roles

**AWS Identity and Access Management (IAM)** is the service that implements every principle above. It has three core identity types, each solving a different problem:

**IAM users** represent a single person or application with long-term credentials (a password for console access, access keys for programmatic access). A user is a specific, named identity — think Sofía's own individual IAM user, distinct from Nikhil's.

**IAM groups** are collections of users that share the same access needs. A group has no credentials of its own and can't log in — it exists purely to attach permissions to many users at once. Add a user to a group, and they instantly inherit everything the group is allowed to do; remove them, and that access disappears just as instantly.

**IAM roles** are a different shape of identity entirely — instead of belonging permanently to one person, a role is *assumed* temporarily by whoever or whatever needs it: an EC2 instance that needs to read from an S3 bucket, a Lambda function that needs to write to a database, or even a person who needs temporary elevated access for a specific task. Roles issue short-term credentials that expire automatically, rather than the long-term credentials a user has. This matters enormously for architecture: hardcoding a user's access keys into an application is a well-known bad practice precisely because those credentials are long-lived and easy to leak; a role attached to that same application gets temporary credentials that AWS rotates automatically, with nothing to leak in the first place.

> ⚠️ **Trap to know:** Users are permanent identities for people or applications; roles are temporary identities that get assumed. A scenario describing an EC2 instance that needs S3 access should almost always point you toward an IAM role, not a user with hardcoded credentials — this exact distinction is one of the most frequently tested access-control ideas at the Associate level.

## How IAM Policies Determine Permissions

A **policy** is a JSON document that explicitly states what's allowed (or explicitly denied). Every permission an identity has traces back to a policy attached to it, whether directly to a user, to a group that user belongs to, or to a role that identity assumes.

A few rules govern how AWS evaluates policies, and they matter more than the JSON syntax itself:

- **Default deny.** If no policy explicitly allows an action, it's denied. There's no implicit "allow everything not specifically blocked."
- **Explicit deny always wins.** If any applicable policy explicitly denies an action, that denial overrides any other policy that allows it — no exceptions. This is what makes explicit deny statements a reliable safety net even when permissions get complicated across multiple groups and roles.
- **Policies can attach to identities or to resources.** An identity-based policy attaches to a user, group, or role ("this user can read this bucket"). A resource-based policy attaches directly to a resource like an S3 bucket ("this bucket can be read by this account"). Both get evaluated together for any given request.

**Managed policies vs. inline policies** is a practical distinction worth knowing: an AWS managed policy (or a customer-managed policy you create yourself) is a standalone, reusable document you can attach to many identities at once. Update the policy once, and every identity it's attached to picks up the change immediately — which is powerful, but also means a single policy edit can ripple across every user, group, or role using it. An inline policy is embedded directly in one specific identity and isn't reusable — useful for a genuinely one-off permission, but easy to lose track of at scale since it doesn't show up when you're reviewing shared, reusable policies.

## The Best-Practice Pattern: Groups Over Individual Policies

Here's a scenario worth working through directly, because it captures the single most tested IAM decision at this level: a project needs several team members to have identical access to a set of AWS resources for a fixed period of time, and the team's membership is expected to change before the project ends.

Three ways to solve this look reasonable at first glance, and only one is actually correct:

| Approach | What happens |
|---|---|
| One shared IAM user for the whole team | Everyone uses the same credentials — no individual accountability for who did what, and a shared password is inherently harder to rotate safely |
| A separate IAM user for each team member, with the same policies attached to each one directly | Works, but doesn't scale — adding or removing a team member means manually updating policies on every individual user |
| A separate IAM user for each team member, all placed in one IAM group, with the policy attached to the group | The correct pattern — each person keeps individual accountability, and adding or removing someone from the project means adding or removing them from the group, with permissions updating automatically |

The lesson generalizes well beyond this one scenario: whenever multiple identities need the *same* access, attach the policy to a group (or, for machine identities, a role) rather than repeating it across individuals. It's less error-prone, scales cleanly as team membership changes, and keeps individual accountability intact — no shared credentials, no silent permission drift between "identical" users that quietly stopped being identical.

## Applying This to the Café

Consider what access control actually looks like for the café's own team. Sofía manages day-to-day operations and needs broader access than Nikhil, who works the counter and handles visual design tasks. As the café's architecture grows — a website, eventually a database, eventually automated reporting — each of those pieces needs its own access boundaries too, and not necessarily the same ones a person would have.

A cloud architect advising the café (the kind of guidance Olivia might actually give) would ask the same questions this module just walked through: Does each piece of the architecture get its own identity, scoped to only what it needs? Are Frank and Martha's own credentials protected with MFA, given that as account owners they likely have the broadest access of anyone? Is there a group structure that will still make sense if the café hires more staff next season? These aren't abstract exam questions — they're the actual first design decisions behind every version of the café's evolving architecture from here forward.

---

## What to skip

You don't need to memorize IAM policy JSON syntax character-for-character, or every condition key available for fine-grained policy conditions — that level of hands-on policy-writing depth comes from the guided lab itself, not from this overview. Focus on the *decision logic*: default deny, explicit deny wins, users versus roles, and groups over individual policies.

## Key takeaways

- Security in AWS rests on least privilege, defense in depth, shared responsibility applied to access specifically, and a default-deny posture — nothing is allowed until it's explicitly granted.
- IAM users are permanent identities for people or applications; IAM groups collect users who share the same access needs; IAM roles are temporary identities assumed by people or AWS resources, and are the correct choice whenever hardcoded long-term credentials would otherwise be needed.
- Every permission traces back to a policy — identity-based or resource-based — and AWS evaluates them under two consistent rules: deny by default, and an explicit deny always overrides an allow.
- When multiple identities need identical access, attach the policy to a group or role rather than repeating it across individual users — it scales better, reduces error, and preserves individual accountability.

## Further reading

- [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) — the official user guide, useful once you're ready to go deeper than this overview.
- [IAM policy evaluation logic](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html) — the authoritative source for exactly how AWS resolves multiple, sometimes conflicting, policies.

*Service capabilities and policy behavior mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 2 — Introducing Cloud Architecting](02-introducing-cloud-architecting.md) · **Next:** [Module 4 — Adding a Storage Layer with Amazon S3](04-adding-a-storage-layer-with-amazon-s3.md) · **Quiz:** [Module 3 Quiz](../quizzes/03-securing-access-quiz.md) · **Activity:** [Module 3 Activity](../labs/03-securing-access-activity.md)
