<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](11-implementing-networking-features-and-connectivity.md) · [Next module](13-troubleshooting-network-connectivity-issues.md) · [Quiz](../quizzes/12-configuring-domains-dns-and-content-delivery-quiz.md) · [Slides](../lectures/12-configuring-domains-dns-and-content-delivery.pptx)
<!-- /hub-navigation -->

# Module 12: Configuring Domains, DNS, and Content Delivery

**Course:** AWS Academy Cloud Operations — building toward SOA-C02, AWS Certified SysOps Administrator – Associate
**Estimated study time:** 45 minutes

## Why this matters

Module 11 connected Meridian's VPCs and its hybrid network to on-premises. This module is about the layer users actually interact with: how DNS routes them to the right place, how CloudFront delivers content close to them, and how an S3-backed origin stays private while still serving through CloudFront. This is Domain 5's second task.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish a Route 53 failover routing policy from a latency-based routing policy
- Explain how CloudFront's TTL and cache invalidation affect cost and content freshness
- Explain how Origin Access Control (OAC) keeps an S3 origin private behind CloudFront
- Distinguish when a cache-busting object key is preferable to an invalidation
- Design a DNS, caching, and content delivery strategy for a stated requirement

---

## Route 53 Routing Policies: Failover vs. Latency-Based

Route 53 supports several routing policies, and two get confused constantly because both can involve multiple Regions: **failover** and **latency-based**.

A **failover routing policy** is built for an **active-passive** pair: Route 53 sends traffic to the primary resource as long as it's healthy, based on an associated **health check**, and automatically switches to the secondary only when the primary fails that health check. It's not about picking the fastest option — it's about picking the *designated* primary until it breaks.

A **latency-based routing policy** sends each user to whichever Region gives them the **lowest latency**, based on measured network conditions — there's no primary or secondary designation, and no requirement that anything be unhealthy for traffic to shift. It's built for performance across multiple active Regions, not for disaster recovery between a primary and a backup.

> ⚠️ **Exam trap:** a scenario describing an **active-passive** setup, where traffic should stay on one designated resource until a **health check** shows it's down, is describing **failover routing**. A scenario emphasizing sending users to whichever active Region responds **fastest**, with all Regions equally eligible, is describing **latency-based routing** — there's no primary/secondary concept in latency-based routing at all.

## CloudFront: TTL, Cache Invalidation, and Cache-Busting

CloudFront caches content at edge locations close to users, controlled by a **Time to Live (TTL)** — how long an object stays cached before CloudFront checks back with the origin. A longer TTL means a higher cache hit ratio and less load on the origin, but it also means updates take longer to reach users unless something forces CloudFront to fetch a fresh copy.

**Cache invalidation** forces CloudFront to treat cached copies of specified paths as expired immediately — useful for an occasional urgent fix, but it has a per-path cost past a monthly free allotment, and invalidating on every deployment adds up fast. A **cache-busting object key** (giving a new object a new, unique filename or version-numbered path, like `app.v482.js` instead of overwriting `app.js`) sidesteps invalidation entirely: the new file is simply a cache miss the first time any user requests it, and the old cached version can keep expiring naturally.

> ⚠️ **Exam trap:** a scenario needing to force an **immediate, one-off** content update, at low volume, is describing **cache invalidation**. A scenario describing **frequent deployments** needing immediate freshness, where invalidation cost or delay is a concern, is pointing toward **versioned object keys** instead — avoiding the need to invalidate at all by never overwriting a cached filename.

## S3 Origin with Origin Access Control (OAC)

When CloudFront serves content from an S3 bucket, the bucket itself should almost never be publicly accessible — otherwise, anyone can bypass CloudFront entirely and hit S3 directly, skipping caching, any CloudFront-level access controls, and any WAF rules attached to the distribution.

**Origin Access Control (OAC)** solves this: it lets a CloudFront distribution authenticate its requests to an S3 origin, and the bucket policy is scoped to allow access only from that specific distribution. The bucket stays fully private — no public access at all — while CloudFront can still fetch objects from it to serve to users. OAC is the current, recommended mechanism for this, replacing the older Origin Access Identity (OAI) approach.

> ⚠️ **Exam trap:** a scenario requiring content to be served **only** through CloudFront, with the underlying **S3 bucket blocked from direct public access**, is describing **Origin Access Control**. If a scenario's S3 bucket is still reachable by its direct S3 URL despite CloudFront being in front of it, that's a sign OAC (or a bucket policy restricting access to it) hasn't actually been configured.

## Putting It Together: DNS and Delivery for Meridian

Priya's DNS and content delivery design:

- **Latency-based routing** for Meridian Loyalty's API, active in three Regions, so each user reaches whichever Region responds fastest.
- **Failover routing** for Ridgeline's order-status page, with a health check on the primary Region and automatic failover to a static backup if it goes down.
- **CloudFront** in front of Café Sol's marketing site, with versioned asset filenames on every deploy so new content is live immediately without paying for invalidations.
- **Origin Access Control** on the S3 bucket behind that CloudFront distribution, so the bucket stays fully private and all traffic is forced through CloudFront.

## What to skip

You don't need to memorize every Route 53 routing policy (weighted, geolocation, geoproximity, and multi-value answer all exist, but failover-versus-latency is the pairing that shows up as a trap most often) or CloudFront's exact edge cache behavior configuration syntax — that's implementation depth beyond this exam. What matters is knowing failover's active-passive/health-check model versus latency-based routing's performance model, when invalidation versus a cache-busting key is the efficient choice, and why OAC keeps an S3 origin private.

## Key takeaways

- Failover routing is active-passive and health-check driven; latency-based routing sends every user to whichever active Region is fastest, with no primary/secondary concept.
- A longer CloudFront TTL means better cache performance but slower content updates; cache invalidation forces immediate freshness but costs money past the free tier, and versioned object keys avoid the need for invalidation on frequent deploys.
- Origin Access Control keeps an S3 origin private, letting only the specific CloudFront distribution fetch from it — direct public access to the bucket should be blocked entirely.
- Domain 5 continues: Module 11 connected the network, Module 12 routes and delivers content over it, and Module 13 closes the domain with troubleshooting.

## Further reading

- [Route 53 Routing Policies](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html) — failover, latency-based, and the other policy types.
- [Amazon CloudFront Caching](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html) — TTL behavior and cache invalidation.
- [Restricting Access to an Amazon S3 Origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) — Origin Access Control.
