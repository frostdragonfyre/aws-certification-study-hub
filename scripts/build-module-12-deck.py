"""
Builds certifications/saa-c03/lectures/12-caching-content.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-12-deck.py

Paired with instructor-private/12-caching-content-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "saa-c03", "lectures",
                    "12-caching-content.pptx")

d = Deck(12, "Caching Content",
          "Repeat requests shouldn't pay the full cost every single time.")

# 1 — Title
d.title_slide("Module 12 · Lecture", ["Caching", "Content"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 12", "Question of the Day", "Before we start",
    [("The Module 10 news segment brought customers from hundreds of miles away",
      "What happens to every one of their requests right now? It travels all the way back to the café's one AWS Region — even for a menu image that hasn't changed in weeks."),
     ("Recap: Module 11 made the architecture repeatable", "CloudFormation templates, stacks, change sets — infrastructure as code"),
     ("Tonight's shift", "From “fetch it fresh every time” to “keep a copy somewhere faster or closer”")])

# 3 — Objectives
d.numbered_list_slide("Module 12", "Objectives", "Five things by the end of tonight", [
    ("Explain what Amazon CloudFront does", "and how edge locations reduce latency"),
    ("Describe ElastiCache's role", "an in-memory cache in front of a database"),
    ("Explain what DAX accelerates, specifically", "and why it's not a general-purpose cache"),
    ("Compare CloudFront, ElastiCache, and DAX", "and match each to the layer it actually caches"),
    ("Explain cache invalidation", "why “when to expire a cache” is often the harder design question"),
])

# 4 — The café's caching problem
d.content_slide("The Café's Caching Problem",
    "Same menu images. Same “today's specials” query. Fetched fresh, every single request.", "Module 12")

# 5 — CloudFront
d.content_slide("Amazon CloudFront: Caching at the Edge",
    "A CDN that serves content from a location near the requester, not the origin Region", "Module 12", dark=True)

# 6 — Cache hit / miss / TTL
d.numbered_list_slide("Module 12", "Cache Hits, Misses, and TTL", "The vocabulary that runs through this whole module", [
    ("Cache miss", "content isn't cached yet at that edge location — CloudFront fetches it from the origin, serves it, and caches it"),
    ("Cache hit", "the next nearby request is served directly from the edge, without touching the origin at all"),
    ("Time to Live (TTL)", "how long a cached object is trusted before CloudFront checks the origin again — set per file type or path"),
])

# 7 — Exam trap: CloudFront isn't just static
d.quad_box_slide("COMMON EXAM TRAP", "CloudFront Isn't Limited to Static Content", "“Our API needs to be faster for distant users” doesn't rule out CloudFront",
    [("Static assets", "Images, CSS, JavaScript — the obvious, textbook case."),
     ("Dynamic content", "Can be cached intelligently based on headers, cookies, and query strings."),
     ("API responses", "Caching can apply here too, not just to files sitting in S3."),
     ("Connection acceleration", "Some techniques speed up the connection itself without caching the response body.")],
    note="Study cue: “dynamic” doesn't automatically mean “not a CloudFront answer.”")

# 8 — ElastiCache
d.content_slide("Amazon ElastiCache: An In-Memory Cache in Front of the Database",
    "CloudFront fixes the browser's latency. This fixes RDS getting hit with the same query, over and over.", "Module 12")

# 9 — Redis vs Memcached
d.table_slide("Module 12", "Redis vs. Memcached", "Two ElastiCache engines — know the distinguishing feature, not just the names",
    ["", "Redis (/ Valkey)", "Memcached"],
    [["Data structures", "Complex — closer to a lightweight database", "Simple key-value only"],
     ["Persistence", "Supported", "None"],
     ["Replication", "Supported", "None"],
     ["Best for", "Most application caching needs", "Simple, high-throughput caching, minimal ops"]],
    col_widths=[3.0, 4.7, 4.7],
    note="Redis's richer feature set makes it the more common default choice.")

# 10 — DAX
d.content_slide("DAX: DynamoDB Accelerator",
    "One specific job — a caching layer built for DynamoDB, and only DynamoDB", "Module 12", dark=True)

# 11 — Exam trap: DAX vs ElastiCache
d.quad_box_slide("COMMON EXAM TRAP", "DAX Is Not a Substitute for ElastiCache", "Both are “a cache in front of a database” — that's where the similarity ends",
    [("DAX", "Works only in front of DynamoDB. API-compatible — app code barely changes."),
     ("ElastiCache", "General-purpose — can sit in front of RDS or other data sources."),
     ("Data in RDS?", "DAX is not an available option, full stop."),
     ("Data in DynamoDB?", "Read-heavy, needs microsecond latency — DAX is the specific fit.")],
    note="Study cue: match the cache to the database it actually sits in front of.")

# 12 — Matching the layer to the problem
d.table_slide("Module 12", "Matching the Caching Layer to the Problem", "Three caches, three different jobs",
    ["Scenario", "Right service"],
    [["Static assets served to users worldwide", "CloudFront"],
     ["Dynamic content/API responses to distant users", "CloudFront"],
     ["Frequently-repeated RDS query results", "ElastiCache"],
     ["Frequently-repeated DynamoDB reads, microsecond latency", "DAX"]],
    col_widths=[7.2, 5.2])

# 13 — Cache invalidation
d.numbered_list_slide("Module 12", "Cache Invalidation: The Harder Half", "Caching is easy. Knowing when to stop trusting a cached copy isn't.", [
    ("Let the TTL expire naturally", "fine when a short window of staleness genuinely doesn't matter"),
    ("Actively invalidate the cache", "CloudFront: an invalidation request for specific paths; ElastiCache: the app deletes/updates the key"),
    ("Set a shorter TTL for volatile data", "accept more origin hits in exchange for less staleness, where staleness is costly"),
], note="There's no universally “correct” choice — it's freshness vs. performance, decided per piece of content.")

# 14 — Putting it together
d.content_slide("Putting It Together: The Café's Caching Strategy",
    "CloudFront for assets and API responses, ElastiCache in front of RDS, DAX in front of DynamoDB — three layers, three jobs", "Module 12")

# 15 — Common mix-ups
d.resource_list_slide("Module 12", "Common Mix-Ups", "Worth getting right before Module 13", [
    ("“CloudFront is only for static files”", "It can also accelerate dynamic content and API responses with the right cache behavior."),
    ("“DAX and ElastiCache are interchangeable”", "DAX only works in front of DynamoDB — ElastiCache is the general-purpose option."),
    ("“A longer TTL is always better”", "Longer TTLs risk stale data — it's a real trade-off, not a setting to maximize."),
], dark=True)

# 16 — Before next class
d.content_slide("Before Next Class",
    "Think about what happens when the café's services need to talk to each other without waiting on one another", "Module 12")

# 17 — Closing
d.closing_slide("Caching", "Content", "Next up: building decoupled architectures")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
