# Module 4: Adding a Storage Layer with Amazon S3

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 50 minutes

## Why this matters

This is where the café's architecture stops being theoretical. Module 1 walked through the café's very first ask — a simple website — and landed on Amazon S3 as the right fit, without going deep on why. This module goes deep: what S3 actually is, how it's built to survive failure, and the specific features that make it the right foundation for the café's V1 architecture (and, later, for the media and reporting needs the café's story grows into).

This is also the first module where "adding a layer" stops being a metaphor. From here through Module 8, each module literally adds one architectural layer to the café's design — storage first, because nearly everything else eventually needs somewhere to put data.

## Learning objectives

By the end of this module, you should be able to:

- Explain what Amazon S3 is and how its object storage model differs from a traditional file system
- Describe how S3 achieves durability and availability
- Choose an appropriate S3 storage class for a given access pattern
- Explain how versioning and lifecycle policies manage an object's life over time
- Configure S3 for static website hosting, and secure a bucket appropriately

---

## What Amazon S3 Actually Is

**Amazon Simple Storage Service (S3)** is object storage — a fundamentally different model from the file systems most people are used to. There's no folder hierarchy in the traditional sense and no drive letter. Instead, every piece of data is stored as an **object** inside a **bucket**, and every object is retrieved by a unique **key** — effectively its full path-like name within that bucket.

A few properties fall directly out of this model:

- **Buckets are global-namespace, Region-specific.** A bucket name has to be globally unique across all of AWS, but the bucket itself lives in one specific Region you choose — which means Module 2's placement factors (latency, price, compliance, service availability) apply to bucket placement exactly the way they apply to everything else.
- **Objects can be almost anything.** A single object can range from a few bytes up to 5 terabytes — HTML files, images, video, backups, log files, and structured data all live in S3 the same way, as objects.
- **There's no true "folder."** The console displays keys with slashes (like `menu/breakfast.pdf`) as if they were folders, but S3 doesn't actually have a nested directory structure underneath — it's a flat namespace of keys that happens to display that way for convenience.

> ⚠️ **Trap to know:** Don't confuse S3 with a file system you'd mount and edit in place, and don't confuse it with a block storage volume like Amazon EBS, which attaches to a single EC2 instance. S3 is reached over HTTP(S) APIs, accessible from anywhere with the right permissions, and built for a completely different access pattern than either of those.

## Durability and Availability: What S3 Actually Promises

S3's core promise is durability — the near-certainty that an object you stored won't be lost. AWS designs S3 for what's typically described as "eleven nines" of durability, achieved by automatically storing redundant copies of every object across multiple devices in multiple Availability Zones within the chosen Region, without any extra configuration from you.

It's worth separating two ideas that sound similar but aren't the same:

| Concept | What it means |
|---|---|
| Durability | Whether the data survives at all — will this object still exist and be intact later? |
| Availability | Whether you can access the data *right now* — is the service currently able to serve this request? |

S3 is built for extremely high durability essentially by default. Availability varies somewhat by storage class, and it's one of the trade-offs that makes choosing a storage class an actual decision rather than a formality.

## Choosing a Storage Class

S3 offers multiple storage classes, each trading cost against retrieval speed and availability. The decision comes down to one real question: **how often will this specific object actually get accessed, and how fast do you need it back when it is?**

| Storage class | Best for | Trade-off |
|---|---|---|
| S3 Standard | Frequently accessed data | Highest availability, highest per-GB cost |
| S3 Standard-IA (Infrequent Access) | Data accessed occasionally but needed fast when it is | Lower storage cost, a retrieval fee per access |
| S3 One Zone-IA | Infrequent access, recreatable data | Cheaper than Standard-IA, but stored in only one Availability Zone |
| S3 Glacier (multiple tiers) | Long-term archives, backups, compliance retention | Very low storage cost, retrieval takes minutes to hours depending on tier |
| S3 Intelligent-Tiering | Access patterns you don't know in advance or that change over time | AWS automatically moves objects between tiers based on actual usage |

> ⚠️ **Trap to know:** A scenario describing data with an *unpredictable or changing* access pattern is almost always pointing at Intelligent-Tiering, not a manual choice between Standard and IA — the whole point of that class is removing the guesswork.

## Versioning and Lifecycle Policies: Managing an Object Over Time

**Versioning**, once enabled on a bucket, keeps every version of an object every time it's overwritten or deleted, rather than replacing it in place. This protects against two very different failure modes at once: accidental overwrites (an old version is still there to restore) and accidental deletion (a "delete" just adds a delete marker — the previous version remains recoverable). The cost is exactly what you'd expect — every version is still full storage, so an object that gets rewritten constantly can quietly multiply its own storage footprint if nobody's watching.

**Lifecycle policies** solve the problem that follows directly from that: automatically transitioning objects between storage classes, or expiring them entirely, based on rules you define — for example, moving an object to Standard-IA after 30 days of no access, then to Glacier after 90 days, then deleting it entirely after a year. This turns storage-class selection from a one-time decision into an ongoing, automated policy, which matters enormously once an architecture is generating real volumes of logs, backups, or media over time.

## Static Website Hosting: Where the Café's Story Actually Began

Module 1's scenario — the café's very first website — is S3's most direct architectural fit, and it's worth revisiting now with the real mechanism behind it. S3 can serve static website content (HTML, CSS, JavaScript, images) directly over HTTP, with no web server to patch, scale, or manage. You designate an index document and, optionally, an error document, and S3 handles the rest.

This works because a static site's requirements line up exactly with what S3 is built for: content that doesn't change per-request, read far more often than it's written, and needs no server-side processing. The moment the café needed *dynamic* content and online ordering (Module 1's V2), that fit broke — which is exactly why the café's architecture moves to Amazon EC2 in the next module, not because S3 got worse at its job, but because the job itself changed.

## Securing a Bucket

By default, a newly created S3 bucket is private — nothing in it is publicly accessible, which is the same default-deny posture Module 3 introduced for IAM, applied here to storage instead of identity. Making a bucket's content public (like a static website's files) requires deliberately opting in, through two layers working together:

- **Block Public Access settings** — an account- and bucket-level setting that, by default, blocks public access outright, even if a policy below would otherwise allow it. This exists specifically as a safety net against an accidentally permissive bucket policy.
- **Bucket policies** — resource-based policies (the same concept from Module 3), attached directly to the bucket, that explicitly grant or deny specific actions to specific principals.

> ⚠️ **Trap to know:** A famous, recurring category of real-world data breach is a publicly readable S3 bucket that was never supposed to be public. The fix is almost always the same: Block Public Access should stay enabled unless a bucket has a specific, deliberate reason (like static website hosting) to be public — and even then, only the specific objects that need to be public should be, not the whole bucket by default.

---

## What to skip

You don't need to memorize exact storage-class pricing figures or the precise retrieval-time ranges for every Glacier tier — those numbers change, and the exam tests the *decision logic* (access frequency and retrieval-speed need) rather than current pricing. Similarly, don't try to memorize every possible lifecycle-policy configuration option; understand what the feature is for, and the guided lab will build the hands-on muscle memory.

## Key takeaways

- S3 is object storage — buckets, objects, and keys, not a traditional file system, and objects are reached over HTTP(S) rather than mounted like a drive.
- S3 is built for extremely high durability by default; availability and retrieval speed are what actually vary by storage class.
- Choosing a storage class comes down to one question: how often is this object accessed, and how fast do you need it back?
- Versioning protects against accidental overwrite and deletion; lifecycle policies automate moving objects through storage classes (or expiring them) over time.
- Static website hosting is S3's most direct fit for content that's read far more than it's written and needs no server-side processing — exactly the café's V1 need.
- Buckets are private by default; Block Public Access and bucket policies work together, and a bucket should only become public through a specific, deliberate decision.

## Further reading

- [Amazon S3 documentation](https://docs.aws.amazon.com/s3/) — the official source for current storage classes, features, and pricing.
- [Amazon S3 Storage Classes](https://aws.amazon.com/s3/storage-classes/) — AWS's own current comparison of every storage class and its trade-offs.
- [Security Best Practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html) — the authoritative source for keeping a bucket secured deliberately, not accidentally.

*Storage class names, pricing, and durability figures mentioned above are illustrative — verify current details at aws.amazon.com before relying on them.*

---

**Previous:** [Module 3 — Securing Access](03-securing-access.md) · **Next:** [Module 5 — Adding a Compute Layer Using Amazon EC2](05-adding-a-compute-layer-using-amazon-ec2.md) · **Quiz:** [Module 4 Quiz](../quizzes/04-adding-a-storage-layer-with-amazon-s3-quiz.md) · **Activity:** [Module 4 Activity](../labs/04-adding-a-storage-layer-with-amazon-s3-activity.md)
