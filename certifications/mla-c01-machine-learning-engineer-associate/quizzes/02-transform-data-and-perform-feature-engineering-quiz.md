[Course index](../README.md) · [Read the paired lesson](../modules/02-transform-data-and-perform-feature-engineering.md) · [All quizzes](README.md)

**NET-3100BB2 · AWS MACHINE LEARNING ENGINEER ASSOCIATE · WAKE TECH**

**Module 2 Knowledge Check**

Transform Data and Perform Feature Engineering · 20 questions · Practice — not graded

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

> Normalization rescales values into a fixed range, typically 0 to 1.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which encoding technique creates a new binary column for each category?

> **A.** Label encoding
> **B.** One-hot encoding
> **C.** Standardization
> **D.** Normalization

**3. [Fill in the Blank] Easy**

> Amazon SageMaker ____________ is a fully managed data labeling service with built-in active learning.

**4. [Multiple Choice] Easy**

> Which AWS service is a general-purpose crowdsourcing marketplace for human intelligence tasks, not specific to ML?

> **A.** SageMaker Ground Truth
> **B.** Amazon Mechanical Turk
> **C.** AWS Glue DataBrew
> **D.** SageMaker Data Wrangler

**5. [True / False] Easy**

> Standardization rescales values to have a mean of 0 and a standard deviation of 1.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why does label encoding fit ordinal categorical data better than one-hot encoding does?

> **A.** Label encoding always uses fewer categories
> **B.** Label encoding preserves the categories' meaningful order as a single number
> **C.** One-hot encoding cannot represent more than two categories
> **D.** Label encoding is only used for numeric data

**7. [Fill in the Blank] Moderate**

> AWS Glue ____________ is a visual, no-code data preparation tool that sits between SageMaker Data Wrangler and full AWS Glue ETL jobs.

**8. [Multiple Choice] Moderate**

> A model uses an algorithm sensitive to feature variance and assumes roughly normally distributed input. What scaling technique fits best?

> **A.** Normalization
> **B.** Standardization
> **C.** One-hot encoding
> **D.** Label encoding

**9. [True / False] Moderate**

> SageMaker Ground Truth can use Amazon Mechanical Turk as one of its workforce options.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which AWS tool provides a visual interface for exploring, cleaning, and transforming data directly within the ML workflow, with built-in transforms like outlier detection and imputation?

> **A.** Amazon Mechanical Turk
> **B.** SageMaker Data Wrangler
> **C.** Amazon Redshift
> **D.** AWS Budgets

**11. [Fill in the Blank] Moderate**

> One-hot encoding fits ____________ categorical data — categories with no inherent order.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Café Sol's transaction-category field has values like "Beverage," "Bakery," and "Retail," with no inherent order between them. What encoding fits best?

> **A.** Label encoding, since it's simpler
> **B.** One-hot encoding, avoiding a false ordinal relationship between categories
> **C.** Standardization
> **D.** Normalization

**13. [Scenario / Judgment] Hard**

> Ridgeline's customer satisfaction survey uses Low, Medium, and High as responses, with a genuine, meaningful order. What encoding fits best?

> **A.** One-hot encoding, to avoid any implied order
> **B.** Label encoding, preserving the genuine order in the resulting numbers
> **C.** Normalization
> **D.** Standardization

**14. [Scenario / Judgment] Hard**

> A neural network needs bounded numeric input values, and the data's distribution shape isn't a concern. What scaling technique fits best?

> **A.** Standardization, since it's always the default
> **B.** Normalization, rescaling into a fixed, bounded range
> **C.** One-hot encoding
> **D.** Label encoding

**15. [Scenario / Judgment] Hard**

> Diego needs to label a large new image dataset for Café Sol at scale, and wants to minimize manual labeling effort using automated labeling on the easy cases. What fits best?

> **A.** Amazon Mechanical Turk alone, with no additional workflow
> **B.** SageMaker Ground Truth, using active learning to automatically label easy cases and route harder ones to humans
> **C.** AWS Glue DataBrew
> **D.** SageMaker Data Wrangler alone

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Normalization and standardization are interchangeable, so it doesn't matter which one you use." Correct this using this module's content.

> **A.** They're right — the two are always interchangeable regardless of algorithm
> **B.** They're different: normalization bounds values to a fixed range for algorithms needing bounded input, while standardization centers values around a mean of 0 for algorithms sensitive to variance or assuming normal distribution — using the wrong one can quietly degrade model performance
> **C.** Normalization is only used for categorical data
> **D.** Standardization always produces values between 0 and 1

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes using label encoding for Café Sol's unordered transaction-category field, arguing "it's simpler than creating multiple columns." Evaluate this using this module's content.

> **A.** Agree — label encoding is always simpler and should always be preferred
> **B.** Disagree — label encoding would assign arbitrary numbers to categories with no real order, inventing a false numeric relationship a model could mistakenly learn from; one-hot encoding avoids that by not implying any order
> **C.** Disagree, but only because one-hot encoding cannot handle more than three categories
> **D.** Agree, since transaction categories always have a natural order

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why a task could call for SageMaker Ground Truth even when the actual labeling work ends up being performed by a Mechanical Turk workforce.

> **A.** Ground Truth and Mechanical Turk are always mutually exclusive
> **B.** Ground Truth supplies the ML-specific managed workflow — active learning, automated labeling of easy cases, and quality control — around whichever workforce does the labeling; Mechanical Turk alone provides only the raw workforce, with none of that workflow built in
> **C.** Mechanical Turk cannot be used for any ML-related task
> **D.** Ground Truth requires abandoning any use of Mechanical Turk entirely

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that AWS Glue DataBrew and SageMaker Data Wrangler are redundant, since "they both clean data visually." Argue against treating them as interchangeable, using this module's content.

> **A.** Agree — the two tools are functionally identical in every scenario
> **B.** Disagree — Data Wrangler's transforms live directly inside the ML workflow, built for feeding a training job, while DataBrew is a more general visual data-preparation tool well suited to analysts preparing data outside a dedicated ML pipeline; the right choice depends on where the work sits relative to model training
> **C.** Disagree, but only because DataBrew cannot deduplicate records
> **D.** Agree, since both tools require writing custom code

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as categorical data gets converted to numbers somehow, the encoding method chosen doesn't really matter to the model." Evaluate this claim using this module's content.

> **A.** Agree — one-hot encoding and label encoding always produce identical model behavior
> **B.** Disagree — label encoding on unordered categories invents a false numeric order a model can mistakenly learn from, while one-hot encoding on genuinely ordered categories discards real order information the model could have used; matching the encoding to whether the categories are ordered is what actually matters
> **C.** Disagree, but only because label encoding cannot be reversed
> **D.** Agree, since models cannot process encoded categorical data at all

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
