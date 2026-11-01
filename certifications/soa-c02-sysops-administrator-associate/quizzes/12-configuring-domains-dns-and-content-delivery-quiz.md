[Course index](../README.md) · [Read the paired lesson](../modules/12-configuring-domains-dns-and-content-delivery.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SYSOPS ADMINISTRATOR ASSOCIATE · WAKE TECH**

**Module 12 Knowledge Check**

Configuring Domains, DNS, and Content Delivery · 20 questions · Practice — not graded

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

> A Route 53 failover routing policy sends traffic to whichever Region currently has the lowest latency.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which Route 53 routing policy requires a health check and an active-passive designation?

> **A.** Latency-based routing
> **B.** Failover routing
> **C.** Simple routing
> **D.** Weighted routing

**3. [Fill in the Blank] Easy**

> CloudFront's ____________ controls how long an object stays cached at an edge location before CloudFront checks back with the origin.

**4. [Multiple Choice] Easy**

> What does Origin Access Control (OAC) allow a CloudFront distribution to do?

> **A.** Cache content indefinitely with no TTL
> **B.** Authenticate its requests to a private S3 origin, without the bucket being publicly accessible
> **C.** Replace Route 53 entirely
> **D.** Automatically invalidate its own cache every hour

**5. [True / False] Easy**

> Cache invalidation in CloudFront has a cost past a monthly free allotment.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does latency-based routing not have a "primary" or "secondary" Region?

> **A.** It always routes to the Region with the lowest resource cost instead
> **B.** It sends each user to whichever active Region gives them the lowest measured latency — no designation is required, unlike failover routing
> **C.** Latency-based routing only supports a single Region
> **D.** It requires manual approval before switching Regions

**7. [Fill in the Blank] Moderate**

> A cache-busting object key, like `app.v482.js` instead of overwriting `app.js`, avoids the need for cache ____________ entirely.

**8. [Multiple Choice] Moderate**

> Why might an S3 bucket serving as a CloudFront origin still be reachable by its direct S3 URL, bypassing CloudFront?

> **A.** CloudFront always blocks direct S3 access automatically
> **B.** Origin Access Control (or an equivalent bucket policy) hasn't actually been configured to restrict access to the specific distribution
> **C.** S3 buckets cannot be used as CloudFront origins at all
> **D.** The bucket's TTL is set too high

**9. [True / False] Moderate**

> Origin Access Control is the current, recommended mechanism for restricting an S3 origin to a specific CloudFront distribution, replacing the older Origin Access Identity approach.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A team deploys frequently and needs every deployment's assets to be immediately fresh, without paying for invalidations on every release. What fits best?

> **A.** Set the TTL to zero for every object
> **B.** Use versioned or hashed object keys so each deployment is a new cache miss, rather than invalidating the same filename repeatedly
> **C.** Disable caching entirely for the whole distribution
> **D.** Invalidate the entire distribution after every deploy

**11. [Fill in the Blank] Moderate**

> A Route 53 ____________ routing policy is built for an active-passive pair, switching to the secondary only when the primary fails its health check.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Ridgeline's order-status page needs to stay on a single designated primary Region, switching to a backup only if the primary goes down. Which Route 53 routing policy fits?

> **A.** Latency-based routing, since it automatically picks the best Region
> **B.** Failover routing, since it's built for exactly this active-passive, health-check-driven pattern
> **C.** Weighted routing, since it can send 100% of traffic to one Region
> **D.** Geolocation routing, since it's based on user location

**13. [Scenario / Judgment] Hard**

> Meridian Loyalty's API runs actively in three Regions, and the goal is to route each user to whichever Region responds fastest, with no designated primary. Which Route 53 routing policy fits?

> **A.** Failover routing, since it supports multiple Regions
> **B.** Latency-based routing, since it sends each user to the lowest-latency active Region with no primary/secondary concept
> **C.** Simple routing, since it requires the least configuration
> **D.** A routing policy isn't needed if there are three Regions

**14. [Scenario / Judgment] Hard**

> A CloudFront distribution serves content from an S3 bucket, but a security review finds the bucket is also reachable by its direct public S3 URL, bypassing all of CloudFront's access controls. What's missing?

> **A.** A longer TTL on the CloudFront distribution
> **B.** Origin Access Control, with the bucket policy restricted to allow access only from that specific CloudFront distribution
> **C.** A Route 53 failover routing policy
> **D.** A weighted routing policy on the S3 bucket

**15. [Scenario / Judgment] Hard**

> A one-off critical bug fix needs to reach users on a handful of specific paths immediately, and this won't happen often. What's the appropriate tool?

> **A.** Cache invalidation on those specific paths — a low-volume, occasional need is exactly what it's for
> **B.** Versioned object keys, even though this is a one-time fix
> **C.** Disabling the CloudFront distribution entirely
> **D.** Lowering the TTL to zero permanently

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Failover routing and latency-based routing both work with multiple Regions, so they're basically the same thing." Correct this using this module's content.

> **A.** They're right — the two are fully interchangeable whenever more than one Region is involved
> **B.** They're different: failover routing is active-passive and health-check driven, switching to a secondary only when the primary fails, while latency-based routing sends every user to whichever active Region is fastest with no primary/secondary concept at all
> **C.** Latency-based routing requires a health check; failover routing does not
> **D.** Failover routing is simply a faster version of latency-based routing

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes invalidating the entire CloudFront distribution on every deployment, arguing "it guarantees freshness, so it's always the right call." Evaluate this using this module's content.

> **A.** Agree — invalidation should always be used regardless of deployment frequency or cost
> **B.** Disagree — invalidation has a cost past a monthly free allotment, and frequent deployments are better served by versioned object keys, which avoid the need to invalidate at all by never overwriting a cached filename
> **C.** Disagree, but only because CloudFront cannot invalidate an entire distribution
> **D.** Agree, since versioned object keys are always more expensive than invalidation

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why an S3 bucket behind CloudFront should almost never be left publicly accessible.

> **A.** Public access improves CloudFront's cache hit ratio
> **B.** A publicly accessible bucket lets anyone bypass CloudFront entirely, skipping caching, any CloudFront-level access controls, and any WAF rules attached to the distribution — Origin Access Control is what keeps the bucket private while still letting CloudFront serve from it
> **C.** S3 buckets cannot be made private under any configuration
> **D.** CloudFront requires public S3 access in order to function at all

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that a longer CloudFront TTL is always the better choice because it reduces origin load. Argue against this using this module's content.

> **A.** Agree — a longer TTL has no downside worth considering
> **B.** Disagree — a longer TTL does reduce origin load and improve cache hit ratio, but it also means updates take longer to reach users unless something forces a fresh fetch, so the right TTL depends on how often content actually changes and how quickly updates need to be visible
> **C.** Disagree, but only because CloudFront does not support configurable TTLs
> **D.** Agree, since cache invalidation is always free regardless of TTL

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as CloudFront is in front of an S3 bucket, the bucket is automatically private and secure — no additional configuration is needed." Evaluate this claim using this module's content.

> **A.** Agree — placing CloudFront in front of a bucket automatically restricts direct access
> **B.** Disagree — CloudFront being in front of a bucket doesn't automatically make the bucket private; without Origin Access Control (or an equivalent restrictive bucket policy) explicitly configured, the bucket can remain reachable by its direct S3 URL, bypassing CloudFront entirely
> **C.** Disagree, but only because CloudFront cannot use S3 as an origin
> **D.** Agree, since Origin Access Control is enabled by default on every S3 bucket

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
