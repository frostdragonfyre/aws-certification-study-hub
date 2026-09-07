# Module 9: Securing User, Application, and Data Access

**Course:** AWS Academy Cloud Architecting — building toward SAA-C03, AWS Certified Solutions Architect – Associate
**Estimated study time:** 45 minutes

## Why this matters

Module 3 taught IAM as the way *you* — and the café's staff, and the applications running on its behalf — get access to AWS resources: users, groups, roles, policies, least privilege, the explicit-deny-wins evaluation rule. That's the right foundation, and this module assumes you have it solid.

But IAM was never designed to answer a different question the café now has: how does a *customer* — someone placing an online order, who will never have an AWS account and should never be anywhere near the AWS console — log in and check their order history? IAM users are for people and services that need to *manage* AWS resources. Customers need something else entirely. This module covers three things Module 3 didn't: authenticating actual application users (not AWS accounts), safely storing and rotating the credentials applications need to talk to each other, and encrypting the data sitting at rest so a storage-layer breach doesn't automatically mean a data breach.

## Learning objectives

By the end of this module, you should be able to:

- Explain why customer-facing application users need Amazon Cognito instead of IAM users
- Distinguish Cognito user pools from identity pools, and what each actually provides
- Explain what AWS Secrets Manager solves that hardcoding credentials doesn't
- Compare Secrets Manager to Systems Manager Parameter Store, and know when each fits
- Explain the core idea behind AWS KMS and envelope encryption at the level the exam expects

---

## The Café's Access Problem, Expanded

Recall the café's V2 milestone: dynamic content and online ordering, on EC2. The moment customers can place orders, a whole category of access problem shows up that Module 3 never had to deal with. Real customers need accounts, need to log in, need to see their own order history and nobody else's. None of that is an IAM problem — creating an IAM user for every café customer would be unworkable at any real scale, and IAM users were never designed to be handed out to the general public in the first place.

At the same time, the application itself now needs to *store* things that matter: the database credentials the EC2 web tier uses to connect to RDS, and eventually customer data that shouldn't be readable by just anyone who gets at the underlying storage. Those are two more access problems Module 3's IAM material doesn't solve on its own. This module covers the three services that do: Cognito for the customers, Secrets Manager for the credentials, and KMS for the data itself.

## Amazon Cognito: Authentication for Your Application's Users

**Amazon Cognito** provides authentication, authorization, and user management for the actual end users of an application — the café's customers — as opposed to IAM, which manages access for people and services that need to *administer* AWS itself. This is the single most important distinction in this section: **IAM users are for managing AWS. Cognito is for authenticating the people using what you built on AWS.** Confusing the two is a common early mistake, and one AWS Academy's own case studies lean on directly.

Cognito is really two related but distinct pieces:

**User pools** are a managed user directory — they handle sign-up, sign-in, password resets, and can issue tokens after a successful login, optionally supporting multi-factor authentication and federation with external identity providers (like signing in with an existing Google or Facebook account). This is what handles a café customer creating an account and logging back in.

**Identity pools** do something different: they grant temporary, limited AWS credentials to users — including guests who haven't logged in at all — so a client application can talk directly to specific AWS services (like uploading a profile photo straight to S3) without the AWS credentials ever being embedded in the application itself.

| | User pools | Identity pools |
|---|---|---|
| Job | Authentication (who is this person) | Authorization (temporary AWS access) |
| Output | Sign-in tokens (ID, access, refresh) | Temporary AWS credentials |
| Typical use | Customer sign-up and login | Letting a logged-in (or guest) user talk directly to an AWS service |

They're commonly used together: a user pool authenticates the customer, and the resulting token is exchanged through an identity pool for temporary AWS credentials scoped to exactly what that customer should be allowed to touch — never broad, standing access.

> ⚠️ **Exam trap:** a scenario describing "customers need to create accounts and log into a public-facing web or mobile app" is a Cognito question, even if it never uses the word "Cognito." If you see yourself reaching for "create an IAM user for each customer," that's the wrong direction — full stop.

## AWS Secrets Manager: Credentials That Aren't Hardcoded

The café's EC2 web tier needs a database username and password to connect to the RDS instance from Module 6. The tempting shortcut — and a genuine, common real-world mistake — is to hardcode that username and password directly into the application's code or configuration file. That's a liability the moment the code is shared, committed to version control, or read by anyone who shouldn't have database access.

**AWS Secrets Manager** stores credentials, API keys, and other secrets centrally, encrypted, and retrievable by an application at runtime through an API call instead of being embedded anywhere in code. Beyond just storage, its standout feature is **automatic rotation** — Secrets Manager can be configured to periodically change a secret's value (like an RDS password) on a schedule, updating both the secret's stored value and the underlying resource, without a human manually touching either one.

## Secrets Manager vs. Parameter Store

AWS Systems Manager also has a **Parameter Store**, which can store secrets too — and the exam expects you to know when each one is the right call, since they genuinely overlap.

| | Secrets Manager | Parameter Store |
|---|---|---|
| Built-in automatic rotation | Yes | No (requires custom automation) |
| Cost | Charged per secret, per month | Free tier available (standard parameters) |
| Best for | Database credentials, API keys needing rotation | General configuration values, and secrets where rotation isn't required |

The honest rule of thumb: if a value needs to rotate on a schedule without manual work — like the café's RDS credentials — Secrets Manager is worth its cost. If it's a configuration value or a secret where rotation isn't a real requirement, Parameter Store does the job for free.

## AWS KMS: Protecting the Data Itself

Everything so far controls *who can request* something. **AWS Key Management Service (KMS)** protects the data itself, so that even if someone bypasses every access control and reaches the raw storage, what they find is unreadable without the right key.

KMS creates and manages **encryption keys**, and most AWS storage services — S3, EBS, RDS among them — integrate with it directly to encrypt data at rest. You have a choice between an **AWS managed key** (created and managed by AWS on your behalf, the simplest option, used automatically when you enable default encryption) and a **customer managed key** (which you create and control yourself, including who can use it and when it can be disabled or deleted) — the difference is how much control you need over the key's lifecycle and access policy, not whether the encryption itself is any different in strength.

### Envelope encryption, at the level the exam expects

KMS doesn't directly encrypt large amounts of data with your key every time. Instead, it uses **envelope encryption**: KMS generates a unique **data key**, that data key encrypts your actual data locally (fast, and it never has to leave where the data lives), and then KMS encrypts that data key itself using your KMS key before storing it alongside the encrypted data. Decryption reverses the process — KMS decrypts the data key first, then the data key decrypts your data. You don't need to implement this yourself; AWS services that integrate with KMS handle it automatically. What matters for the exam is recognizing the term and knowing, at a conceptual level, that it's *why* KMS remains fast even when encrypting large amounts of data.

> ⚠️ **Exam trap:** encryption **at rest** (KMS, protecting stored data) and encryption **in transit** (like TLS/HTTPS, protecting data moving across a network) are two different protections, and a well-architected design typically needs both. A question describing "data must be protected both while stored and while being transmitted" is asking for both — picking only one is picking half the answer.

## Putting It Together: The Café's V2 Access Model

With Cognito, Secrets Manager, and KMS layered on top of Module 3's IAM foundation, the café's online ordering system now has a complete, deliberate access story: customers authenticate through a Cognito user pool and never touch IAM at all; the web tier retrieves its RDS credentials from Secrets Manager at runtime instead of having them hardcoded, with those credentials rotating automatically; and both the RDS database and any stored customer data are encrypted at rest through KMS, so a storage-layer compromise alone doesn't hand over readable data. Four different problems — administering AWS, authenticating customers, protecting credentials, protecting data — four different, deliberately chosen tools.

## What to skip

You don't need to configure Cognito's federation with specific external identity providers in depth, write custom Secrets Manager rotation Lambda functions, or memorize KMS's cryptographic algorithms — those are implementation details past what the associate exam tests. What matters is recognizing which of the four problems above a scenario is describing, and reaching for the right tool.

## Key takeaways

- IAM manages access **to AWS** for people and services; Amazon Cognito authenticates the actual **end users of an application** — don't create IAM users for customers.
- Cognito user pools handle authentication (sign-up/sign-in); identity pools grant temporary AWS credentials — they're often used together.
- AWS Secrets Manager stores credentials centrally with built-in automatic rotation; hardcoding credentials in application code is a real, common mistake it exists to prevent.
- Parameter Store is a free alternative to Secrets Manager for values that don't need automatic rotation.
- AWS KMS protects data at rest using envelope encryption, with a choice between AWS managed keys (simple) and customer managed keys (full control).
- Encryption at rest (KMS) and encryption in transit (TLS) are different protections — a complete design usually needs both.

## Further reading

- [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) — user pools and identity pools in full detail.
- [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) — rotation configuration beyond what this module covers.
- [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) — envelope encryption and key policies in depth.

---

**Next:** [Module 10 — Implementing Monitoring, Elasticity, and High Availability](10-implementing-monitoring-elasticity-and-high-availability.md)
