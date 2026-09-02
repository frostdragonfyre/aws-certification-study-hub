# Module 12: Caching Content

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 40 minutes

## Why this matters

The news segment from Module 10 did more than spike traffic for a day — it put the café's online ordering site in front of people well outside its own city, some of them placing orders from hundreds of miles away. Every one of those requests has been traveling all the way back to the café's single AWS Region, for content that barely changes between requests: the same menu images, the same static assets, the same handful of "today's specials" database lookups, fetched fresh from RDS every single time.

None of that repeated work is necessary. This module is about **caching**: keeping a copy of something that doesn't change often somewhere faster or closer than its original source, so repeat requests stop paying the full cost — in latency, and in load on the database — every single time.

## Learning objectives

By the end of this module, you should be able to:

- Explain what Amazon CloudFront does and how edge locations reduce latency
- Describe Amazon ElastiCache's role as an in-memory cache in front of a database
- Explain what DAX accelerates, specifically, and why it's not a general-purpose cache
- Compare CloudFront, ElastiCache, and DAX and match each to the layer it actually caches
- Explain cache invalidation and why "when to expire a cache" is often the harder design question

---

## Amazon CloudFront: Caching at the Edge

**Amazon CloudFront** is AWS's content delivery network (CDN) — it caches content at **edge locations** distributed around the world, so a request is served from a location physically near the requester instead of traveling all the way back to the café's origin Region every time. For the café's menu images, CSS, JavaScript, and other static assets, this is a direct, significant latency win for exactly the out-of-town customers the news segment brought in.

CloudFront sits in front of an **origin** — commonly an S3 bucket for static assets, or an Application Load Balancer for dynamic content — and serves cached copies from the nearest edge location whenever possible. The first request for a given piece of content from a given edge location is a **cache miss**: CloudFront fetches it from the origin, serves it, and caches it there. Every subsequent request from nearby is a **cache hit**, served directly from the edge, without touching the origin at all.

### Cache behavior and TTL

How long CloudFront holds onto a cached object before checking the origin again is controlled by a **Time to Live (TTL)** — you can set this per file type or path pattern. A long TTL is right for content that rarely changes (a logo, a CSS file); a short TTL, or none at all, is right for content that changes frequently or must always be current (an inventory count, a per-user order confirmation).

> ⚠️ **Exam trap:** CloudFront isn't limited to static content. It can also accelerate *dynamic* content and API responses by caching intelligently based on headers, cookies, and query strings, or by using techniques that don't cache the response body but still speed up the connection itself. A scenario describing "our API needs to be faster for users far from our Region" isn't automatically ruled out from being a CloudFront answer just because the content is dynamic.

## Amazon ElastiCache: An In-Memory Cache in Front of the Database

CloudFront solves latency for content served to the browser. It does nothing for the café's own backend hitting RDS repeatedly for the same "today's specials" query, over and over, from every web tier instance. **Amazon ElastiCache** is a managed, in-memory caching service — it sits between the application and the database, and holds frequently-requested query results in memory, which is dramatically faster to read from than even a well-tuned database on disk.

The pattern is straightforward: the application checks ElastiCache first. On a **cache hit**, it gets the answer back immediately, without ever touching RDS. On a **cache miss**, it queries RDS as usual, then writes that result into ElastiCache so the *next* request for the same data is a hit. Over time, for read-heavy, repeatedly-requested data — exactly the café's "today's specials" and menu-lookup traffic — this removes a large share of load from the database entirely.

ElastiCache supports two underlying engines, and the exam expects you to know the distinguishing feature, not just the names:

| Engine | Distinguishing feature |
|---|---|
| Redis (via ElastiCache for Redis / Valkey) | Supports complex data structures, replication, and persistence — closer to a lightweight database in its own right |
| Memcached | Simpler, multi-threaded, built purely for high-throughput caching with no persistence or replication |

For most application caching needs, including the café's, Redis's richer feature set (and the option of persistence) makes it the more common default choice — Memcached fits scenarios that genuinely need nothing more than a simple, high-throughput cache and want to keep the operational model as simple as possible.

## Amazon DynamoDB Accelerator (DAX): One Specific Job

As the café's online ordering system grows, Sofía's team adds a DynamoDB table to track real-time inventory counts — a fast, key-based lookup that fits DynamoDB's strengths well. **DAX (DynamoDB Accelerator)** is a caching layer built specifically for DynamoDB, and *only* for DynamoDB — it isn't a general-purpose cache you can point at any data source the way ElastiCache can.

DAX sits directly in front of DynamoDB and is API-compatible with it, meaning the application code barely changes to start using it. What it delivers is a dramatic drop in read latency — down to microseconds — for a workload that's read-heavy and repeatedly requests the same items, exactly like checking an item's inventory count moments after it was last checked.

> ⚠️ **Exam trap:** DAX is not a substitute for ElastiCache, and ElastiCache is not a substitute for DAX, even though both are "a cache in front of a database." DAX only works in front of DynamoDB. If the data lives in RDS, or anywhere other than DynamoDB, DAX is not an available option — ElastiCache (or CloudFront, for content ultimately served to a browser) is what applies instead.

### Matching the caching layer to the problem

| Scenario | Right service |
|---|---|
| Static assets (images, CSS, JS) served to users worldwide | CloudFront |
| Dynamic content/API responses needing faster delivery to distant users | CloudFront (with appropriate cache behavior) |
| Frequently-repeated RDS (or other database) query results | ElastiCache |
| Frequently-repeated DynamoDB item reads, needing microsecond latency | DAX |

## Cache Invalidation: The Harder Half of Caching

There's a well-known saying in computer science: there are only two hard problems — cache invalidation, and naming things. Caching content is the easy half of this module; knowing *when to stop trusting a cached copy* is the harder half, and it's exam-relevant.

If the café updates a menu price and CloudFront, or ElastiCache, keeps serving the old cached value for the remainder of its TTL, customers see stale information — sometimes just an inconvenience, sometimes a real business problem (a sold-out item still showing as available). The available strategies:

- **Let the TTL expire naturally** — fine for content where a short window of staleness genuinely doesn't matter.
- **Actively invalidate the cache** — for CloudFront, this means creating an invalidation request for specific paths, forcing the next request back to the origin regardless of TTL; for ElastiCache, this typically means the application explicitly deletes or updates the cached key when the underlying data changes.
- **Set a shorter TTL for volatile data** — accept more frequent origin hits in exchange for less staleness, for data (like live inventory) where staleness is costly.

There's no universally "correct" choice here — it's a genuine trade-off between freshness and the performance/cost benefit caching exists to provide, and the right answer depends on how costly stale data actually is for that specific piece of content.

## Putting It Together: The Café's Caching Strategy

With CloudFront in front of the café's static assets and dynamic API responses, ElastiCache in front of RDS for repeated "today's specials" and menu-lookup queries, and DAX in front of the new DynamoDB inventory table, the café now serves its out-of-town, post-news-segment traffic without repeatedly re-fetching content that hasn't changed, or hammering RDS with the same query hundreds of times a minute. Three different caching layers, for three different sources of repeated work — not one cache trying to do all three jobs.

## What to skip

You don't need to configure CloudFront cache behaviors in JSON, hand-tune Redis cluster topology, or memorize DAX's exact latency figures — those are implementation depth beyond the associate exam. What matters is knowing which caching layer applies to which kind of repeated request, and that cache invalidation is a real design decision, not an afterthought.

## Key takeaways

- CloudFront caches content at edge locations near users, reducing latency for both static assets and, with the right configuration, dynamic content.
- ElastiCache is a general-purpose, in-memory cache that sits in front of a database (commonly RDS), reducing repeated query load using Redis or Memcached.
- DAX is a specialized cache that works *only* in front of DynamoDB — it is not interchangeable with ElastiCache.
- A cache hit skips the origin entirely; a cache miss falls through to it and (usually) populates the cache for next time.
- Cache invalidation — TTL expiration, active invalidation, or shorter TTLs for volatile data — is a genuine design trade-off between freshness and performance, not a solved problem you can ignore.

## Further reading

- [Amazon CloudFront Developer Guide](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) — cache behaviors and invalidation in full detail.
- [Amazon ElastiCache](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/WhatIs.html) — Redis vs. Memcached feature comparison in depth.
- [Amazon DynamoDB Accelerator (DAX)](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.html) — API compatibility and cluster setup.

---

**Next:** [Module 13 — Building Decoupled Architectures](13-building-decoupled-architectures.md)
