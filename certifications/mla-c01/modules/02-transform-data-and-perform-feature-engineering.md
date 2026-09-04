# Module 2: Transform Data and Perform Feature Engineering

**Course:** AWS Academy Machine Learning Engineering — building toward MLA-C01, AWS Certified Machine Learning Engineer – Associate
**Estimated study time:** 45 minutes

## Why this matters

Raw ingested data almost never arrives in a shape a model can learn from well. This module covers the transformation and feature engineering work that turns Module 1's ingested data into something a model can actually train against — cleaning it, scaling it, encoding it, and labeling it where needed. This is Domain 1's second task, still inside the largest domain on the exam.

## Learning objectives

By the end of this module, you should be able to:

- Choose between normalization and standardization for a stated scaling requirement
- Choose between one-hot encoding and label encoding for a stated categorical variable
- Choose between SageMaker Ground Truth and Amazon Mechanical Turk for a stated labeling requirement
- Use AWS Glue, AWS Glue DataBrew, and SageMaker Data Wrangler to clean and transform data
- Design a feature engineering strategy for a stated dataset and modeling goal

---

## Normalization vs. Standardization

Both are scaling techniques that put numeric features on a comparable footing — but they solve for different assumptions about the data.

**Normalization** (min-max scaling) rescales values into a fixed range, typically 0 to 1, based on the minimum and maximum values in the data. It doesn't assume anything about the data's distribution, which makes it a good fit for algorithms that expect bounded inputs — neural networks and distance-based algorithms like k-nearest neighbors are common examples.

**Standardization** (z-score scaling) rescales values to have a mean of 0 and a standard deviation of 1, without bounding them to a fixed range. It fits algorithms that assume roughly normally distributed data or that are sensitive to variance across features — linear regression, logistic regression, SVMs, and PCA are common examples.

> ⚠️ **Exam trap:** a scenario describing an algorithm that **needs bounded input values** (neural networks, distance-based methods) is describing a fit for **normalization**. A scenario describing an algorithm that **assumes a roughly normal distribution or is sensitive to feature variance** (linear models, SVMs, PCA) is describing a fit for **standardization** — applying the wrong one doesn't break the pipeline, but it can quietly degrade model performance.

## One-Hot Encoding vs. Label Encoding

Categorical variables need to become numbers before most algorithms can use them — but how you convert them depends on whether the categories have a meaningful order.

**One-hot encoding** creates a new binary column for each category, with a 1 marking which category applies and 0s everywhere else. It fits **nominal** data — categories with no inherent order, like a product's color or a customer's region — because it doesn't introduce a false numeric relationship between categories that shouldn't have one.

**Label encoding** assigns each category a single integer instead. It fits **ordinal** data — categories with a genuine, meaningful order, like a satisfaction rating of Low/Medium/High — because the resulting numbers preserve that order in a way a model can use.

> ⚠️ **Exam trap:** a scenario describing **unordered categories** (colors, regions, product types) is describing a fit for **one-hot encoding** — using label encoding here invents a false numeric order between categories that don't have one, which can mislead a model. A scenario describing **genuinely ordered categories** (ratings, tiers, severity levels) is a fit for **label encoding**, which preserves that order instead of expanding it into extra columns.

## SageMaker Ground Truth vs. Amazon Mechanical Turk

Some datasets need to be labeled by humans before training can begin — and the tool to do that depends on how much labeling workflow you actually need built for you.

**SageMaker Ground Truth** is a fully managed data labeling service purpose-built for ML: it supports active learning that automatically labels the easy cases and only routes harder cases to humans, reducing labeling cost and time, with built-in workflow management, quality control, and a choice of workforce (your own team, a vendor workforce, or Amazon Mechanical Turk).

**Amazon Mechanical Turk** on its own is a general-purpose crowdsourcing marketplace for human intelligence tasks — not ML-specific, with no built-in active learning or ML-oriented workflow management. It's a raw workforce, not a labeling pipeline.

> ⚠️ **Exam trap:** a scenario describing a need for a **managed labeling workflow with automated labeling and quality control at scale** is describing a fit for **SageMaker Ground Truth** — even when the actual labeling work is ultimately done by a Mechanical Turk workforce, since Ground Truth is what supplies the ML-specific pipeline around that workforce. A scenario describing simple, general crowdsourced human tasks with no need for an ML-oriented workflow is a more direct fit for **Mechanical Turk alone**.

## Tools for Cleaning and Transforming Data

Three AWS tools cover most of the actual cleaning and transformation work. **SageMaker Data Wrangler** provides a visual interface for exploring, cleaning, and transforming data directly within the ML workflow — outlier detection, missing-value imputation, deduplication, scaling, and encoding are all available as built-in transforms. **AWS Glue** is a serverless ETL service for larger-scale, code-based or visual transformation jobs, often used to merge and clean data before it reaches Data Wrangler. **AWS Glue DataBrew** sits between the two — a visual data-preparation tool for cleaning and normalizing data without writing code, well suited to analysts who need to prepare data without a full ETL pipeline.

## Putting It Together: Diego's Feature Engineering Strategy for Meridian

Diego's data transformation and feature engineering design, continuing Domain 1:

- **Standardization** applied to the numeric features feeding Meridian Loyalty's recommendation model, since it uses a algorithm sensitive to feature variance.
- **One-hot encoding** for Café Sol's unordered transaction-category field, avoiding a false ordinal relationship between category values.
- **Label encoding** for Ridgeline's genuinely ordered customer-satisfaction survey responses (Low/Medium/High), preserving that order for the model.
- **SageMaker Ground Truth**, backed by a Mechanical Turk workforce, to label a new image dataset for Café Sol at scale, with active learning cutting the manual labeling load.

## What to skip

You don't need to memorize every SageMaker Data Wrangler built-in transform by name or the exact API parameters for Glue DataBrew recipes — that's implementation depth beyond this exam. What matters is knowing when a scaling or encoding choice fits the data's actual shape and the algorithm's actual assumptions, and knowing when a labeling task needs Ground Truth's managed ML workflow versus Mechanical Turk's raw crowdsourcing.

## Key takeaways

- Normalization bounds values into a fixed range for algorithms needing bounded input; standardization centers values around a mean of 0 for algorithms sensitive to variance or assuming normality.
- One-hot encoding fits unordered (nominal) categories; label encoding fits genuinely ordered (ordinal) categories.
- SageMaker Ground Truth provides a managed, ML-specific labeling workflow with active learning and workforce options including Mechanical Turk; Mechanical Turk alone is a general crowdsourcing marketplace without that workflow.
- SageMaker Data Wrangler, AWS Glue, and AWS Glue DataBrew each cover a different point on the spectrum from visual, ML-embedded transforms to large-scale, code-based ETL.
- This continues Domain 1, building directly on Module 1's ingested data — the next module covers ensuring that data's integrity and bias profile before it's ready for training.

## Further reading

- [Amazon SageMaker Data Wrangler](https://docs.aws.amazon.com/sagemaker/latest/dg/data-wrangler.html) — visual data preparation within the ML workflow.
- [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html) — managed data labeling with active learning.
- [AWS Glue DataBrew](https://docs.aws.amazon.com/databrew/latest/dg/what-is.html) — visual, no-code data preparation.
- [Amazon Mechanical Turk](https://www.mturk.com/) — general-purpose human intelligence task marketplace.
