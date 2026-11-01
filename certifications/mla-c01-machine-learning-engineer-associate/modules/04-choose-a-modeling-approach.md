<!-- hub-navigation -->
[Course index](../README.md) · [Previous module](03-ensure-data-integrity-and-prepare-data-for-modeling.md) · [Quiz](../quizzes/04-choose-a-modeling-approach-quiz.md) · [Slides](../lectures/04-choose-a-modeling-approach.pptx)
<!-- /hub-navigation -->

# Module 4: Choose a Modeling Approach

**Course:** AWS Academy Machine Learning Engineering — building toward MLA-C01, AWS Certified Machine Learning Engineer – Associate
**Estimated study time:** 45 minutes

## Why this matters

Domain 1 made the data ready. This module opens Domain 2 — ML Model Development — with the decision that shapes everything after it: what kind of model, or non-model, actually solves the business problem in front of you. Choosing the wrong approach here means paying the cost of the wrong tradeoff for the rest of the project.

## Learning objectives

By the end of this module, you should be able to:

- Choose between a pre-built AWS AI service and a custom-trained model for a stated business problem
- Choose between a foundation model and training a model from scratch for a stated requirement
- Weigh interpretability against raw predictive performance for a stated use case
- Recognize when SageMaker built-in algorithms, JumpStart, or Bedrock fit a stated scenario
- Design a modeling approach for a stated business problem and constraint set

---

## Pre-Built AI Service vs. Custom-Trained Model

Not every ML problem needs a model trained from your own data. AWS offers pre-built AI services — **Amazon Rekognition** for image and video analysis, **Amazon Comprehend** for text analysis, **Amazon Transcribe** for speech-to-text, **Amazon Translate** for language translation, and others — that solve common, well-defined problems out of the box, with no training data or ML expertise required.

A **custom-trained model**, whether built with a SageMaker built-in algorithm or a fully custom architecture, is worth the added cost and complexity when the problem is specific to your own data or domain in a way a generic pre-built service can't capture — a fraud model tuned to your exact transaction patterns, a recommendation engine built on your specific customer behavior.

> ⚠️ **Exam trap:** a scenario describing a **common, well-defined problem** — extracting text from an image, transcribing a call, translating a document — that a pre-built service already solves is describing a fit for an **AWS AI service**, not a custom model. Building a custom model to re-solve a problem AWS already offers as a managed service usually wastes time and money. A scenario describing a problem genuinely **specific to your own data or domain** is a fit for a **custom-trained model**.

## Foundation Model vs. Training From Scratch

When a problem does call for a model rather than an off-the-shelf AI service, the next question is whether to start from a foundation model or train from nothing.

A **foundation model**, accessed through **Amazon Bedrock** or **SageMaker JumpStart**, comes pre-trained on massive general-purpose datasets and can be used directly, prompt-engineered, or fine-tuned on a smaller, domain-specific dataset. It fits situations with limited labeled data, limited time, or a task that resembles general language or vision capability the foundation model already has.

**Training a model from scratch** — using a SageMaker built-in algorithm or a fully custom architecture — fits situations with a large, domain-specific labeled dataset and a requirement that a general-purpose foundation model can't meet, where the investment in a purpose-built model pays for itself.

> ⚠️ **Exam trap:** a scenario describing **limited labeled data, tight timelines, or a task resembling general capabilities** a foundation model already has is describing a fit for **Bedrock or SageMaker JumpStart** — fine-tuning or prompting rather than training from zero. A scenario describing **abundant domain-specific labeled data** and a requirement a general foundation model doesn't meet is a fit for **training from scratch**, whether with a built-in algorithm or a custom architecture.

## Interpretability vs. Performance

Some algorithms are simple enough that a human can explain exactly why they produced a given output — linear regression, decision trees. Others, like deep neural networks and complex ensemble methods, often produce better raw predictive performance but function largely as a black box.

**Interpretable models** matter when a decision needs to be explained — a regulated industry requiring an explanation for a denied loan application, a scenario where stakeholders need to trust and audit the reasoning, not just the output.

**Higher-performance, less interpretable models** are the right tradeoff when maximizing predictive accuracy is what matters and there's no regulatory or operational requirement to explain individual predictions.

> ⚠️ **Exam trap:** a scenario describing a **regulated or high-stakes decision requiring an explanation** for each prediction is describing a fit for a **simpler, interpretable model**, even if it sacrifices some raw accuracy. A scenario where **maximizing predictive performance** is the goal, with no explainability requirement, is a fit for a more complex model — choosing the highest-accuracy model without checking for an interpretability requirement is the trap.

## Putting It Together: Diego's Modeling Approach for Meridian

Diego's approach-selection strategy, opening Domain 2:

- **Amazon Rekognition**, a pre-built AI service, for Café Sol's basic receipt-image text extraction — a well-defined problem AWS already solves.
- **SageMaker JumpStart**, fine-tuning a foundation model, for Ridgeline's customer-review sentiment analysis, given limited labeled review data and a task resembling general language understanding.
- **A custom-trained SageMaker built-in algorithm**, trained from scratch, for Meridian Loyalty's recommendation engine, built on Meridian's own large, specific purchase-history dataset.
- **An interpretable model** for Meridian Loyalty's credit-eligibility scoring, since regulatory requirements mean every decision needs an explainable reason.

## What to skip

You don't need to memorize every SageMaker built-in algorithm's exact hyperparameters or every AWS AI service's full feature list — that's implementation depth beyond this exam. What matters is recognizing whether a problem is already solved by a pre-built service, whether a foundation model or training from scratch fits the data and time available, and whether interpretability is a real requirement or a nice-to-have.

## Key takeaways

- A well-defined problem AWS already solves fits a pre-built AI service; a problem specific to your own data fits a custom-trained model.
- Limited data and general-capability tasks fit a foundation model via Bedrock or JumpStart; abundant domain-specific data fits training from scratch.
- Regulated or high-stakes decisions requiring explanation fit interpretable models; pure performance goals without that requirement can use more complex models.
- This opens Domain 2 — Domain 1 made the data ready, and this module's choice of approach shapes everything Domain 2 builds next: training, tuning, and evaluating whatever model gets chosen here.

## Further reading

- [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) — foundation models for building generative AI applications.
- [Amazon SageMaker JumpStart](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-jumpstart.html) — pre-trained models and solution templates.
- [AWS AI Services](https://aws.amazon.com/machine-learning/ai-services/) — pre-built services for vision, language, and speech.
