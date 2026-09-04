"""
Builds certifications/soa-c02/lectures/12-configuring-domains-dns-and-content-delivery.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-12-deck.py

Paired with instructor-private/12-configuring-domains-dns-and-content-delivery-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "soa-c02", "lectures",
                    "12-configuring-domains-dns-and-content-delivery.pptx")

d = Deck(12, "Configuring Domains, DNS, and Content Delivery",
          "Module 11 connected the network. Tonight routes users to the right place and delivers content close to them.",
          cert_code="SOA-C02")

# 1 — Title
d.title_slide("Module 12 · Lecture", ["Configuring Domains, DNS,", "and Content Delivery"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 12", "Question of the Day", "Before we start",
    [("A CloudFront distribution sits in front of an S3 bucket", "Is that bucket automatically private and secure?"),
     ("Recap: Module 11 connected Meridian's VPCs and its hybrid network", "tonight is the layer users actually interact with — DNS, routing, and content delivery"),
     ("Tonight's task", "Domain 5, Task 5.2 — configuring domains, DNS, and content delivery")])

# 3 — Objectives
d.numbered_list_slide("Module 12", "Objectives", "Five things by the end of tonight", [
    ("Distinguish a Route 53 failover routing policy from a latency-based policy", "and know when each fits"),
    ("Explain how CloudFront's TTL and cache invalidation affect cost and freshness", "the core caching tradeoff"),
    ("Explain how Origin Access Control keeps an S3 origin private behind CloudFront", "and why that matters"),
    ("Distinguish when a cache-busting object key beats an invalidation", "the efficient choice at scale"),
    ("Design a DNS, caching, and content delivery strategy for a stated requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Routing Users, and Delivering Content Close to Them",
    "Module 11 connected the network. Tonight is the layer users actually interact with.", "Module 12")

# 5 — Section intro: Failover vs Latency-based
d.content_slide("Route 53: Failover vs. Latency-Based Routing",
    "Both can span multiple Regions — they solve very different problems", "Module 12", dark=True)

# 6 — Exam trap: Failover vs Latency-based
d.quad_box_slide("COMMON EXAM TRAP", "Designated Primary vs. Fastest Region", "One needs a health check, the other doesn't",
    [("Failover routing", "active-passive — a health check decides when to switch to the secondary."),
     ("Latency-based routing", "sends each user to whichever active Region is fastest for them."),
     ("Designated primary/secondary", "with automatic switchover on failure — failover routing."),
     ("All Regions equally active", "fastest response wins, no primary — latency-based routing.")],
    note="One line: failover needs a designated primary and a health check — latency-based has neither, just the fastest Region.")

# 7 — Applied
d.table_slide("Module 12", "Failover vs. Latency-Based, Applied", "Matching the requirement to the right policy",
    ["Requirement", "Right policy"],
    [["Stay on one designated Region, switch to backup only if it fails", "Failover routing — health-check driven"],
     ["Route each user to whichever active Region is fastest", "Latency-based routing — no primary/secondary"]],
    col_widths=[7.6, 5.0],
    note="A designated primary with a backup is failover; all Regions equally active is latency-based.")

# 8 — Section intro: CloudFront caching
d.content_slide("CloudFront: TTL, Invalidation, and Cache-Busting",
    "A longer cache means less origin load — and slower updates, unless something forces a refresh", "Module 12")

# 9 — Exam trap: Invalidation vs cache-busting
d.quad_box_slide("COMMON EXAM TRAP", "One-Off Fix vs. Every Deployment", "Don't pay to invalidate what a new filename avoids",
    [("Cache invalidation", "forces immediate expiration on specific paths — a per-path cost."),
     ("Versioned object keys", "a new filename is a fresh cache miss — no invalidation needed."),
     ("Occasional, urgent fix", "low volume, one-off — cache invalidation fits."),
     ("Frequent deployments", "immediate freshness at scale — versioned keys avoid the cost.")],
    note="One line: an occasional urgent fix uses invalidation — frequent deploys use versioned keys instead.")

# 10 — Applied
d.table_slide("Module 12", "Invalidation vs. Cache-Busting, Applied", "Matching the release pattern to the right approach",
    ["Requirement", "Right approach"],
    [["A one-time critical fix on a few specific paths, low volume", "Cache invalidation — built for exactly this"],
     ["Frequent deployments, immediate freshness needed every release", "Versioned object keys — avoids repeated invalidation cost"]],
    col_widths=[7.6, 5.0],
    note="Occasional and urgent points to invalidation; frequent and routine points to versioned keys.")

# 11 — Section intro: OAC
d.content_slide("S3 Origin with Origin Access Control",
    "CloudFront in front of a bucket doesn't automatically make it private", "Module 12", dark=True)

# 12 — Exam trap: OAC
d.quad_box_slide("COMMON EXAM TRAP", "Keeping the Origin Private", "The bucket, and only the bucket, should never be reachable on its own",
    [("Public S3 bucket", "reachable directly — bypasses CloudFront's cache, access control, and WAF."),
     ("Origin Access Control", "CloudFront authenticates to a private S3 origin — no public access needed."),
     ("Bucket policy scoped to OAC", "allows access only from the specific CloudFront distribution."),
     ("Replaces legacy OAI", "OAC is the current, recommended mechanism.")],
    note="One line: CloudFront in front of a bucket doesn't make it private on its own — OAC is what actually does.")

# 13 — Applied
d.table_slide("Module 12", "Origin Access Control, Applied", "Matching the requirement to the right control",
    ["Requirement", "Right control"],
    [["Content served only through CloudFront, bucket blocked from direct access", "Origin Access Control on the S3 origin"],
     ["Bucket still reachable by its direct S3 URL despite CloudFront being in front", "A sign OAC hasn't actually been configured"]],
    col_widths=[7.6, 5.0],
    note="If the bucket is still reachable directly, OAC isn't doing its job yet.")

# 14 — Putting it together
d.numbered_list_slide("Module 12", "Putting It Together: DNS and Delivery for Meridian", "Every piece from tonight, in one design", [
    ("Latency-based routing for Meridian Loyalty's API, active in three Regions", "each user reaches whichever Region responds fastest"),
    ("Failover routing for Ridgeline's order-status page, with a health check on the primary", "automatic switchover to a static backup if it goes down"),
    ("CloudFront with versioned asset filenames for Café Sol's site, and Origin Access Control on its S3 origin", "immediate freshness without invalidation cost, and a fully private bucket"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 12", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Failover and latency-based routing are basically the same”", "Failover is health-check-driven active-passive; latency-based has no primary at all."),
    ("“Invalidating on every deploy is always fine”", "It has a real cost — versioned object keys avoid it entirely."),
    ("“CloudFront in front of a bucket makes it private”", "Not without Origin Access Control explicitly configured."),
], dark=True)

# 16 — Recap
d.content_slide("Recap",
    "Failover vs. latency-based routing, CloudFront TTL and invalidation vs. versioned keys, Origin Access Control", "Module 12", dark=True)

# 17 — Closing
d.closing_slide("Configuring Domains, DNS,", "and Content Delivery", "Domain 5 continues — next up: troubleshooting network connectivity")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
