[Course index](../README.md) · [Read the paired lesson](../modules/12-caching-content.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 12 Knowledge Check**

Caching Content · 20 questions · Practice — not graded

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

> Amazon CloudFront caches content at edge locations near the requesting user, rather than always serving from the origin.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service is a specialized cache that works only in front of DynamoDB?
>
> **A.** ElastiCache
> **B.** CloudFront
> **C.** DAX
> **D.** Systems Manager

**3. [Fill in the Blank] Easy**

> A cache ____________ occurs when requested content is not yet cached and must be fetched from the origin.

**4. [Multiple Choice] Easy**

> Which ElastiCache engine is simpler, multi-threaded, and built purely for high-throughput caching with no persistence?
>
> **A.** Redis
> **B.** Memcached
> **C.** DAX
> **D.** DynamoDB

**5. [True / False] Easy**

> ElastiCache can be used as a general-purpose cache in front of RDS.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> What controls how long CloudFront holds a cached object before checking the origin again?
>
> **A.** Time to Live (TTL)
> **B.** IAM policy
> **C.** Auto Scaling policy
> **D.** VPC route table

**7. [Fill in the Blank] Moderate**

> On a cache ____________, the requested data is found in the cache and returned immediately, without touching the origin.

**8. [Multiple Choice] Moderate**

> Which of the following is TRUE about DAX and ElastiCache?
>
> **A.** They are fully interchangeable for any database
> **B.** DAX works only in front of DynamoDB; ElastiCache is general-purpose and can front RDS or other data sources
> **C.** ElastiCache works only in front of DynamoDB
> **D.** DAX is simply a rebranded version of ElastiCache

**9. [True / False] Moderate**

> Setting a very long TTL is always the best choice for every type of cached content.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> What is a CloudFront "origin"?
>
> **A.** The edge location closest to the requester
> **B.** The source CloudFront fetches content from on a cache miss, such as an S3 bucket or an ALB
> **C.** A type of TTL setting
> **D.** A DynamoDB table

**11. [Fill in the Blank] Moderate**

> Actively forcing CloudFront to discard a cached object before its TTL expires is called an ____________.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> The café's online ordering site serves the same menu images and CSS to customers across the country after a news segment aired. What's the best fit for reducing latency for these distant users?
>
> **A.** ElastiCache
> **B.** DAX
> **C.** CloudFront
> **D.** A CloudFormation change set

**13. [Scenario / Judgment] Hard**

> The café's web tier repeatedly queries RDS for the same "today's specials" data on every page load. What's the best fit for reducing this repeated database load?
>
> **A.** CloudFront
> **B.** ElastiCache
> **C.** DAX
> **D.** AWS Systems Manager

**14. [Scenario / Judgment] Hard**

> A new DynamoDB table tracks real-time inventory counts, with frequent repeated reads of the same items needing microsecond latency. What's the best fit?
>
> **A.** ElastiCache
> **B.** CloudFront
> **C.** DAX
> **D.** RDS Multi-AZ

**15. [Scenario / Judgment] Hard**

> The café updates a menu price, but CloudFront keeps serving the old price for several more hours. What's happening, and what are two ways to address it?
>
> **A.** This is a bug with no fix
> **B.** The cached object's TTL hasn't expired yet; the fix is either to wait for it to expire naturally or to actively invalidate the cached path
> **C.** CloudFront never caches prices, so this couldn't happen
> **D.** The only fix is to disable CloudFront entirely

**16. [Scenario / Judgment] Hard**

> A team assumes a longer TTL is always better because it means more cache hits. What's the flaw in this reasoning for volatile data like live inventory counts?
>
> **A.** There is no flaw — longer TTLs are always strictly better
> **B.** A longer TTL increases the risk of serving stale data for content that changes frequently — freshness and cache performance are a genuine trade-off, not something to maximize in only one direction
> **C.** TTLs only apply to ElastiCache, not CloudFront
> **D.** Longer TTLs automatically trigger cache invalidation

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "ElastiCache and DAX are basically the same thing, just with different names, so it doesn't matter which one you pick." Correct this using this module's content.
>
> **A.** They're right — the two are interchangeable
> **B.** They're not interchangeable — DAX is purpose-built and API-compatible only with DynamoDB, while ElastiCache is a general-purpose in-memory cache that can sit in front of RDS or other data sources; picking DAX for an RDS workload, or ElastiCache expecting DAX's DynamoDB-specific integration, would not work as described
> **C.** DAX replaced ElastiCache and ElastiCache is deprecated
> **D.** ElastiCache is only for static content, like CloudFront
> 
**18. [Scenario / Judgment] Very Hard**

> A design caches API responses at CloudFront with a 24-hour TTL to maximize performance, but the API returns each user's personal order history. What's the risk in this design?
>
> **A.** There is no risk — longer TTLs are always safe
> **B.** Without cache behavior configured to vary by user (e.g., based on cookies or headers), one user's cached response could be served to a different user, exposing personal order data — a serious risk this module's TTL/cache-behavior discussion is meant to prevent
> **C.** CloudFront cannot cache API responses under any configuration, so this scenario is impossible
> **D.** A 24-hour TTL only affects static assets, never dynamic content
>
**19. [Scenario / Judgment] Very Hard**

> Connect this module to Module 10. Both modules discuss reducing load and improving performance. What's the essential difference between what Auto Scaling does and what caching does?
>
> **A.** They are functionally identical approaches to the same problem
> **B.** Auto Scaling adds more capacity to handle the same amount of repeated work; caching reduces the amount of repeated work that ever reaches the origin (database or backend) in the first place — one scales the response to demand, the other reduces demand on the origin itself
> **C.** Caching is simply a cheaper version of Auto Scaling with no functional difference
> **D.** Auto Scaling only applies to databases, and caching only applies to EC2

**20. [Scenario / Judgment] Very Hard**

> A reviewer says "cache invalidation isn't a real design decision — you just set a short TTL everywhere and you're done." Argue against this using this module's content.
>
> **A.** They're right — a universally short TTL is always correct
> **B.** A universally short TTL defeats much of caching's benefit by forcing frequent origin hits even for content that rarely changes (like a logo or CSS file) — the actual design decision is matching TTL length and invalidation strategy to how costly staleness is for each specific piece of content, not applying one setting everywhere
> **C.** Cache invalidation only matters for DAX, not CloudFront or ElastiCache
> **D.** TTLs cannot be set differently for different content types

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
