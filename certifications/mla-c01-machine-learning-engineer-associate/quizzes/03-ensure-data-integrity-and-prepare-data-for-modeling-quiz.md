[Course index](../README.md) · [Read the paired lesson](../modules/03-ensure-data-integrity-and-prepare-data-for-modeling.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS MACHINE LEARNING ENGINEER ASSOCIATE · WAKE TECH**

**Module 3 Knowledge Check**

Ensure Data Integrity and Prepare Data for Modeling · 20 questions · Practice — not graded

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

> Selection bias happens when the collected data isn't representative of the real population.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service identifies pre-training bias metrics in a dataset?

> **A.** AWS KMS
> **B.** SageMaker Clarify
> **C.** Amazon Macie
> **D.** AWS Budgets

**3. [Fill in the Blank] Easy**

> ____________ bias happens when the data collection or labeling process itself introduces a systematic error.

**4. [Multiple Choice] Easy**

> Which mechanism typically protects data while it's stored in S3 or on an EBS volume?

> **A.** TLS
> **B.** AWS KMS-managed encryption at rest
> **C.** One-hot encoding
> **D.** SageMaker Ground Truth

**5. [True / False] Easy**

> Anonymization irreversibly removes or transforms identifying information so the original data can never be reconstructed.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why is measurement bias fixed by correcting the measurement or labeling process, rather than by collecting more data?

> **A.** Because more data always fixes any kind of bias
> **B.** Because the bias comes from how the data was measured or labeled, not from which population was sampled
> **C.** Because measurement bias only affects text data
> **D.** Because measurement bias cannot be detected by SageMaker Clarify

**7. [Fill in the Blank] Moderate**

> Encryption in ____________ typically uses TLS to protect data as it moves between systems.

**8. [Multiple Choice] Moderate**

> Which two AWS-relevant strategies address severe class imbalance in a dataset?

> **A.** Normalization and standardization
> **B.** Resampling and synthetic data generation
> **C.** One-hot encoding and label encoding
> **D.** Encryption at rest and encryption in transit

**9. [True / False] Moderate**

> Masking often preserves a dataset's format and, in some implementations, can be reversed for authorized users.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> A fraud-detection dataset is 99.9% legitimate transactions and 0.1% fraud. What problem does this describe?

> **A.** Measurement bias
> **B.** Severe class imbalance
> **C.** Encryption in transit
> **D.** Selection bias

**11. [Fill in the Blank] Moderate**

> ____________ bias is fixed by changing how data is gathered — broadening collection or stratified sampling.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A loyalty-points sensor at one Meridian store location consistently records values 10% higher than identical sensors at other locations, even though customer behavior is similar across all locations. What does this describe?

> **A.** Selection bias, fix by collecting more data
> **B.** Measurement bias, fix by recalibrating the sensor or standardizing collection across locations
> **C.** Class imbalance, fix by resampling
> **D.** Encryption in transit, fix with TLS

**13. [Scenario / Judgment] Hard**

> Ridgeline needs a development environment where engineers can test against realistic-looking customer records without ever seeing real customer PII, and the data's format needs to stay intact. What fits best?

> **A.** Anonymization, since it's the strongest protection
> **B.** Masking, preserving format for realistic internal testing
> **C.** Encryption in transit alone
> **D.** Label encoding

**14. [Scenario / Judgment] Hard**

> A dataset needs to be published for public research, with a hard requirement that no individual can ever be re-identified from it. What fits best?

> **A.** Masking, since it's reversible
> **B.** Anonymization, irreversibly de-identifying the data
> **C.** Encryption at rest alone
> **D.** One-hot encoding

**15. [Scenario / Judgment] Hard**

> Training data needs protection both while sitting in an S3 bucket and while being transferred into a SageMaker training job. What's the complete strategy?

> **A.** Encryption at rest only, since the data starts in S3
> **B.** Encryption at rest (KMS) for the S3 data and encryption in transit (TLS) for the transfer — both are needed
> **C.** Encryption in transit only, since transfer is the riskier moment
> **D.** Neither is necessary if the VPC is private

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Selection bias and measurement bias are the same thing, so they're fixed the same way." Correct this using this module's content.

> **A.** They're right — both are always fixed by collecting more data
> **B.** They're different: selection bias comes from unrepresentative data collection and is fixed by changing how data is gathered, while measurement bias comes from a flawed measurement or labeling process and is fixed by correcting that process — collecting more of the same flawed measurements wouldn't fix measurement bias
> **C.** Measurement bias doesn't exist in AWS's bias framework
> **D.** Selection bias can only occur in image data

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes anonymizing Ridgeline's development-environment test data instead of masking it, arguing "stronger protection is always better." Evaluate this using this module's content.

> **A.** Agree — anonymization should always be used regardless of the use case
> **B.** Disagree — anonymization's irreversibility and loss of realistic structure would undermine the development environment's need for realistic-looking, format-preserving test data; masking fits that specific requirement better without sacrificing more protection than the use case needs
> **C.** Disagree, but only because anonymization cannot be applied to customer data
> **D.** Agree, since masking provides no protection at all

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why encrypting only data at rest would leave a gap in Meridian's ML data protection strategy.

> **A.** Encryption at rest already covers data in every state
> **B.** Data moving between systems — a client uploading to S3, a training instance pulling data — is a separate exposure point that encryption at rest doesn't address; encryption in transit (TLS) is needed to protect data while it's actually moving across the network
> **C.** Encryption in transit is only relevant for streaming data
> **D.** KMS automatically encrypts all network traffic as a side effect

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that resampling alone always fully solves class imbalance, "so synthetic data generation is unnecessary." Argue against treating them as fully interchangeable, using this module's content.

> **A.** Agree — resampling and synthetic data generation always produce identical results
> **B.** Disagree — resampling reuses or removes existing examples, which can lead to overfitting on duplicated minority-class data or losing information from discarded majority-class data, while synthetic data generation creates new, plausible examples instead; which approach fits best depends on the dataset and how severe the imbalance is
> **C.** Disagree, but only because resampling cannot be performed in AWS
> **D.** Agree, since synthetic data generation is banned under AWS's shared responsibility model

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as a dataset passes a bias check once, it's guaranteed to be bias-free for the life of the model." Evaluate this claim using this module's content.

> **A.** Agree — a single bias check guarantees permanent freedom from bias
> **B.** Disagree — bias metrics reflect the data and process at the time they were measured; new data sources, changed collection processes, or shifting real-world populations can reintroduce selection or measurement bias later, so integrity checks are part of ongoing data preparation, not a one-time gate
> **C.** Disagree, but only because SageMaker Clarify cannot be run more than once
> **D.** Agree, since bias only ever originates at model training time, never in the data

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
