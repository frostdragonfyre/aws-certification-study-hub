# Module 9: Determining Security Controls for New Solutions

**Course:** AWS Academy Cloud Architecting — building toward SAP-C02, AWS Certified Solutions Architect – Professional
**Estimated study time:** 45 minutes

## Why this matters

Module 3 built org-wide security guardrails — Service Control Policies, GuardDuty enabled across every account, Security Hub aggregating findings into one place — but, deliberately, none of that decided what specific security controls any one workload actually needs. Meridian Loyalty holds real guest data — names, emails, and transaction history — across three brands, and it's about to have a public-facing guest portal. This module is Task 2.3: the per-workload security decision Module 3's guardrails were built to support, made for Meridian Loyalty specifically.

## Learning objectives

By the end of this module, you should be able to:

- Derive concrete security requirements for a new solution from the data it actually handles
- Choose between AWS Secrets Manager and Systems Manager Parameter Store for a given credential-management need
- Select the right combination of AWS WAF, AWS Shield Standard, and AWS Shield Advanced for a public-facing workload
- Explain how Module 3's organization-wide guardrails (SCPs, GuardDuty, Security Hub) apply automatically to a new workload without new setup
- Design a complete security control set for a stated new-solution scenario

---

## Setting Security Requirements for a New Solution

Before picking any specific service, Meridian Loyalty needs an honest inventory of what it actually handles: guest names, email addresses, and point-earning transaction history, across Café Sol, Haven & Co., and eventually Ridgeline. None of that is payment card data — Meridian Loyalty never touches card numbers, those stay inside each brand's existing point-of-sale systems — but it is personal data, and it's about to be reachable through a public-facing guest portal.

That inventory drives three concrete requirements: guest data needs encryption at rest and in transit, the application's credentials (database passwords, third-party API keys) need to be stored and rotated without ever appearing in code, and the public-facing portal needs protection against common web attacks and denial-of-service traffic before it needs anything more exotic.

> ⚠️ **Exam trap:** the exam expects you to derive security requirements from what the workload actually handles, not from a generic "add all the security services" instinct. Meridian Loyalty needs strong protection for personal data and its public endpoint — it does not need PCI-DSS-scope controls it was never in scope for, because it never touches card data at all.

## Secrets Manager vs. Systems Manager Parameter Store

Meridian Loyalty's application needs its database password and a couple of third-party API keys available at runtime — never hardcoded, never committed to source control. AWS offers two services that look similar here, and the exam expects you to know which one a given requirement actually points to.

- **AWS Secrets Manager** stores secrets and can **automatically rotate them** on a schedule, using a built-in rotation Lambda for supported services like RDS, or a custom rotation function for anything else. It costs more per secret than Parameter Store.
- **AWS Systems Manager Parameter Store** stores configuration values and secrets (as `SecureString` parameters, encrypted with KMS) more cheaply, but has **no built-in automatic rotation** — rotation has to be built and scheduled separately if it's needed at all.

For Meridian Loyalty's database password, which should rotate periodically without anyone touching it by hand, **Secrets Manager** is the fit — automatic rotation is the actual requirement. For static configuration values that don't need rotation — feature flags, non-sensitive environment settings — **Parameter Store** is the cheaper, equally valid choice.

> ⚠️ **Exam trap:** "needs automatic rotation" points to Secrets Manager. "Just needs to be stored encrypted, no rotation required" points to Parameter Store, at lower cost. Reaching for Secrets Manager by default for every stored value is a common mistake — it's the right tool specifically when rotation is the actual requirement.

## Protecting Meridian Loyalty's Guest-Facing Endpoint

Meridian Loyalty's guest portal is about to be reachable from the public internet — every guest, across all three brands, needs to be able to check and redeem their points from a browser or a mobile app. That's a fundamentally different exposure than anything Café Sol's internal systems have had so far.

- **AWS Shield Standard** is enabled automatically, at no additional cost, for every AWS resource — it defends against common, most-frequently-occurring network and transport layer DDoS attacks.
- **AWS WAF** sits in front of the portal and inspects application-layer traffic, blocking specific attack patterns — SQL injection attempts, cross-site scripting, known bad IP ranges — using rules Meridian's team defines or pulls from the AWS Managed Rules groups.
- **AWS Shield Advanced** adds enhanced, near-real-time detection for larger and more sophisticated DDoS attacks, cost protection against scaling charges incurred during an attack, and 24/7 access to the AWS DDoS Response Team (DRT) — for a per-resource cost, on top of Shield Standard.

For Meridian Loyalty at launch, **Shield Standard plus WAF** is the right starting point: Shield Standard's baseline protection is already active for free, and WAF handles the application-layer threats an internet-facing guest portal actually faces day to day. Shield Advanced becomes worth the added cost if Meridian Loyalty later becomes a specific, high-value DDoS target — not by default, on day one, for every public-facing workload.

> ⚠️ **Exam trap:** Shield Standard is not "no DDoS protection" — it's automatic, free, and always on. The decision the exam is actually testing is WAF (application-layer rules) versus Shield Advanced (enhanced DDoS detection and response) — and they solve different problems, so a well-protected internet-facing workload often needs both, not one instead of the other.

## Applying Module 3's Org-Wide Guardrails to This One Workload

Meridian Loyalty's team doesn't have to build any of its organizational security posture from scratch — it inherits Module 3's guardrails automatically, the moment its account is provisioned inside the organization:

- **Service Control Policies** already constrain what Meridian Loyalty's account can do, before anyone on the team writes a single IAM policy — the org-wide policies from Module 3 apply the instant the account exists.
- **Amazon GuardDuty**, enabled organization-wide in Module 3, starts monitoring Meridian Loyalty's account for threats automatically — no separate enablement step for this workload.
- **AWS Security Hub** aggregates Meridian Loyalty's findings into the same organization-wide view Module 3 built, alongside every other account — Sofía doesn't need a second dashboard for this one workload.

This is the same payoff Module 8 found with Resilience Hub and Route 53 ARC: Meridian Loyalty plugs into what Domain 1 already established, rather than needing its own parallel security program built from zero.

## Putting It Together: Meridian Loyalty's Security Controls

Sofía's complete security design for Meridian Loyalty:

- **KMS encryption at rest and TLS in transit** for all guest personal data, driven by an honest inventory of what the platform actually handles.
- **AWS Secrets Manager** for the database password and any credential that needs automatic rotation; **Parameter Store** for static configuration that doesn't.
- **AWS Shield Standard (automatic) plus AWS WAF** protecting the public-facing guest portal, with Shield Advanced held in reserve if the workload later becomes a specific DDoS target.
- **Module 3's Service Control Policies, GuardDuty, and Security Hub**, already in effect the moment Meridian Loyalty's account was provisioned — inherited, not rebuilt.

## What to skip

You don't need to memorize Secrets Manager's exact rotation Lambda internals or WAF's full managed rule group catalog — that's implementation depth beyond this exam. What matters is deriving security requirements from what a workload actually handles, choosing between Secrets Manager and Parameter Store based on whether rotation is the real requirement, layering WAF and Shield correctly for a public-facing endpoint, and recognizing that org-wide guardrails from Module 3 apply to a new workload automatically.

## Key takeaways

- Security requirements for a new solution come from an honest inventory of the data it actually handles — not a reflexive "add every security service" instinct.
- Secrets Manager fits credentials that need automatic rotation; Parameter Store fits static configuration values at lower cost, when rotation isn't the actual requirement.
- Shield Standard is automatic and free for every resource; WAF handles application-layer attacks against a public endpoint; Shield Advanced adds enhanced DDoS detection and response for resources that specifically need it.
- Module 3's Service Control Policies, GuardDuty, and Security Hub apply to a new workload's account automatically, the moment it's provisioned inside the organization.
- This module is the per-workload security decision Module 3's org-wide guardrails were built to support — the two are complementary halves of the same overall security picture, the same relationship Module 4 and Module 8 had for reliability.

## Further reading

- [AWS Secrets Manager User Guide](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) — automatic secret rotation.
- [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) — configuration and secret storage without built-in rotation.
- [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) — application-layer protection.
- [AWS Shield Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/shield-chapter.html) — Shield Standard vs. Shield Advanced.
