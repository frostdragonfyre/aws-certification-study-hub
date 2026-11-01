<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](02-transform-data-and-perform-feature-engineering.md) · [Next module](04-choose-a-modeling-approach.md) · [Quiz](../quizzes/03-ensure-data-integrity-and-prepare-data-for-modeling-quiz.md) · [Slides](../lectures/03-ensure-data-integrity-and-prepare-data-for-modeling.pptx)
<!-- /hub-navigation -->

# Module 3: Ensure Data Integrity and Prepare Data for Modeling

**Course:** AWS Academy Machine Learning Engineering — building toward MLA-C01, AWS Certified Machine Learning Engineer – Associate
**Estimated study time:** 45 minutes

## Why this matters

Clean, well-scaled, correctly encoded data can still be unsafe to train on if it's biased, unprotected, or mishandled under compliance rules. This module closes Domain 1 — Data Preparation for Machine Learning — by covering the integrity, bias, security, and compliance work that has to happen before data is genuinely ready for a training job.

## Learning objectives

By the end of this module, you should be able to:

- Distinguish selection bias from measurement bias, and know how each gets identified and mitigated
- Choose the right strategy to address class imbalance in a dataset
- Distinguish encryption at rest from encryption in transit for ML data
- Distinguish anonymization from masking for a stated data-protection requirement
- Design a data integrity and preparation strategy for a stated compliance and bias requirement

---

## Selection Bias vs. Measurement Bias

**SageMaker Clarify** identifies several sources of pre-training bias in a dataset, and two of the most commonly confused are selection bias and measurement bias — because they look similar on the surface but call for different fixes.

**Selection bias** happens when the data collected isn't representative of the population the model will actually see in production — certain groups, regions, or scenarios are systematically over- or under-represented in the training set itself. The fix lives in how the data was **gathered**: broadening data collection, stratified sampling, or actively collecting more data from underrepresented groups.

**Measurement bias** happens when the data collection or labeling *process itself* introduces a systematic error — a sensor that reads consistently high for one group, a labeling rubric that's applied inconsistently, an instrument calibrated differently across sites. The fix lives in how the data was **measured or labeled**: recalibrating instruments, standardizing labeling guidelines, or auditing the collection process itself.

> ⚠️ **Exam trap:** a scenario describing a dataset that's **not representative of the real population** — certain groups systematically missing or underrepresented — is describing **selection bias**, fixed by changing how data is gathered. A scenario describing a **systematic error in how the data was measured or labeled** — even with representative coverage — is describing **measurement bias**, fixed by correcting the measurement or labeling process itself, not by collecting more data.

## Addressing Class Imbalance

A dataset with severe class imbalance — one class vastly outnumbering another, like a fraud dataset that's 99.9% legitimate transactions — biases a model toward the majority class, since predicting the majority class every time already achieves a deceptively high accuracy.

Two AWS-relevant strategies address it: **resampling** — oversampling the minority class, undersampling the majority class, or both — and **synthetic data generation** (such as SMOTE-style techniques), which generates new, plausible minority-class examples rather than simply duplicating existing ones. Both are typically applied during the data preparation stage, before training begins, and often paired with using SageMaker Clarify's class imbalance metric to detect the problem in the first place.

## Encryption at Rest vs. Encryption in Transit

Protecting ML data means protecting it in two different states, and each needs its own mechanism.

**Encryption at rest** protects data while it's stored — in S3, EBS, or a database — typically through **AWS KMS**-managed keys integrated directly into the storage service, so the data is unreadable to anyone without the right key even if the underlying storage is somehow accessed directly.

**Encryption in transit** protects data while it's **moving** — between a client and S3, between a training instance and a data source, between microservices — typically through **TLS**, ensuring the data can't be intercepted and read as it crosses the network.

> ⚠️ **Exam trap:** a scenario asking about data sitting in an S3 bucket or on an EBS volume is asking about **encryption at rest** — the answer involves KMS-integrated storage encryption. A scenario asking about data as it moves **between** systems or across a network is asking about **encryption in transit** — the answer involves TLS. A complete ML data protection strategy needs both, not one or the other.

## Anonymization vs. Masking

Both techniques protect sensitive data, but they trade off differently between protection strength and usability.

**Anonymization** irreversibly removes or transforms identifying information so the original data can never be reconstructed or re-linked to an individual — appropriate when data will be shared broadly, published, or used for research where re-identification must be impossible.

**Masking** obscures sensitive values — replacing digits with asterisks, substituting realistic-looking fake values — while often preserving the data's format and, in some implementations, the ability to reverse it for authorized users. It fits situations like a development or test environment that needs realistic-looking data without exposing real customer information to every engineer who touches it.

> ⚠️ **Exam trap:** a scenario requiring data to be **irreversibly de-identified**, with no path back to the original, safe for broad release, is describing **anonymization**. A scenario requiring data to **look and behave like the real thing** for development, testing, or limited internal use — where format matters and some reversibility may be acceptable — is describing **masking**, not anonymization.

## Putting It Together: Diego's Data Integrity Strategy for Meridian

Diego's data integrity, bias, and compliance strategy, closing out Domain 1:

- **SageMaker Clarify** run against Meridian Loyalty's training data to check for both selection bias (is every customer segment represented?) and measurement bias (was the loyalty-points data collected consistently across all store locations?).
- **Resampling** applied to Café Sol's fraud-detection dataset, where legitimate transactions vastly outnumber fraudulent ones.
- **KMS-encrypted S3 storage** for all training data at rest, with **TLS** enforced for every data transfer into and out of training jobs.
- **Masking** applied to Ridgeline's customer data in the development environment, so engineers can test against realistic-looking records without ever seeing real customer PII.

## What to skip

You don't need to memorize SageMaker Clarify's exact bias metric formulas or the precise cryptographic details behind KMS — that's implementation depth beyond this exam. What matters is recognizing which bias type a scenario describes and where its fix lives, knowing when data needs at-rest versus in-transit protection, and matching anonymization or masking to whether the data needs to be irreversibly de-identified or just realistically obscured.

## Key takeaways

- Selection bias comes from unrepresentative data collection, fixed by changing how data is gathered; measurement bias comes from a flawed measurement or labeling process, fixed by correcting that process.
- Severe class imbalance is addressed through resampling or synthetic data generation, applied during data preparation.
- Encryption at rest (KMS-integrated storage) and encryption in transit (TLS) protect data in different states — a complete strategy needs both.
- Anonymization irreversibly de-identifies data for broad release; masking obscures data, often reversibly, for realistic internal use like development and testing.
- This closes Domain 1 — the largest domain on the exam. Data that's been correctly ingested, transformed, and now verified for integrity and compliance is what Domain 2's model development work builds on next.

## Further reading

- [Amazon SageMaker Clarify](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-configure-processing-jobs.html) — pre-training bias detection.
- [AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) — key management for encryption at rest.
- [Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) — discovering and protecting sensitive data.
