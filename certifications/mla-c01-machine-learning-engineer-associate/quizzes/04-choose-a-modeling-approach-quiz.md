**NET-3100BB2 · AWS MACHINE LEARNING ENGINEER ASSOCIATE · WAKE TECH**

**Module 4 Knowledge Check**

Choose a Modeling Approach · 20 questions · Practice — not graded

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

> A pre-built AWS AI service requires no training data or ML expertise to use.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which AWS service is a pre-built AI service for image and video analysis?

> **A.** SageMaker JumpStart
> **B.** Amazon Rekognition
> **C.** AWS Glue
> **D.** Amazon Bedrock

**3. [Fill in the Blank] Easy**

> Amazon ____________ provides foundation models for building generative AI applications.

**4. [Multiple Choice] Easy**

> Which type of model is easiest for a human to explain the reasoning behind a specific prediction?

> **A.** A deep neural network
> **B.** A complex ensemble method
> **C.** A simple, interpretable model like linear regression or a decision tree
> **D.** A black-box foundation model

**5. [True / False] Easy**

> Foundation models accessed through Bedrock or SageMaker JumpStart come pre-trained on massive general-purpose datasets.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Why might building a custom model to re-solve a problem AWS already offers as a managed AI service be a mistake?

> **A.** It's always technically impossible
> **B.** It usually wastes time and money solving a problem that's already been solved
> **C.** AWS AI services cannot be used for any business problem
> **D.** Custom models are always less accurate than AI services

**7. [Fill in the Blank] Moderate**

> ____________ models sacrifice some raw performance in exchange for a human being able to explain individual predictions.

**8. [Multiple Choice] Moderate**

> A team has limited labeled data and a tight timeline for a task resembling general language understanding. What approach fits best?

> **A.** Training a custom model entirely from scratch
> **B.** Fine-tuning or prompting a foundation model via Bedrock or SageMaker JumpStart
> **C.** Building a brand-new deep learning architecture
> **D.** Ignoring the timeline constraint

**9. [True / False] Moderate**

> A regulated industry requiring an explanation for a denied loan application is a scenario favoring an interpretable model.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which factor should most directly drive the choice between a pre-built AI service and a custom-trained model?

> **A.** Whether the problem is common and well-defined versus specific to your own data
> **B.** The number of AWS regions available
> **C.** The color scheme of the AWS console
> **D.** Whether the company has an AWS support plan

**11. [Fill in the Blank] Moderate**

> Training a model ____________ fits situations with abundant domain-specific labeled data and a requirement a general foundation model doesn't meet.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> Café Sol needs to extract text from receipt images — a common, well-defined problem. What approach fits best?

> **A.** Training a custom OCR model from scratch
> **B.** Amazon Rekognition or a similar pre-built AI service
> **C.** Fine-tuning a foundation model on millions of receipt images
> **D.** Building a new deep learning architecture

**13. [Scenario / Judgment] Hard**

> Ridgeline has limited labeled customer-review data but needs sentiment analysis, a task resembling general language understanding. What approach fits best?

> **A.** Training a custom model entirely from scratch with the limited data
> **B.** Fine-tuning a foundation model via SageMaker JumpStart
> **C.** A pre-built AI service that doesn't exist for this use case
> **D.** Ignoring sentiment analysis entirely

**14. [Scenario / Judgment] Hard**

> Meridian Loyalty has a large, specific purchase-history dataset and needs a recommendation engine tuned to its exact customer behavior. What approach fits best?

> **A.** A generic pre-built AI service
> **B.** A custom-trained SageMaker built-in algorithm, trained from scratch on Meridian's own data
> **C.** A foundation model used with no fine-tuning at all
> **D.** No model at all, since recommendations can't be automated

**15. [Scenario / Judgment] Hard**

> Meridian Loyalty's credit-eligibility scoring is subject to regulations requiring an explainable reason for every decision. What approach fits best?

> **A.** The highest-accuracy black-box model available, regardless of explainability
> **B.** A simpler, interpretable model, even if it sacrifices some raw accuracy
> **C.** A foundation model with no consideration of interpretability
> **D.** Skipping model evaluation entirely

---

## Very Hard Questions

**16. [Scenario / Judgment] Very Hard**

> A student says: "Custom-trained models are always better than pre-built AI services, so you should always build your own." Correct this using this module's content.

> **A.** They're right — custom models are always superior regardless of the problem
> **B.** They're wrong: a common, well-defined problem that a pre-built AI service already solves usually doesn't justify the added cost and complexity of training a custom model — the custom-model approach is worth it specifically when the problem is genuinely specific to your own data or domain
> **C.** Pre-built AI services cannot be used for any real business problem
> **D.** Custom models never require any training data

**17. [Scenario / Judgment] Very Hard**

> A reviewer proposes training every model completely from scratch, arguing "foundation models are just a shortcut for people who don't want to do it properly." Evaluate this using this module's content.

> **A.** Agree — foundation models are always an inferior shortcut
> **B.** Disagree — a foundation model, fine-tuned or prompted via Bedrock or SageMaker JumpStart, is the appropriate choice when labeled data or time is limited and the task resembles the model's existing general capabilities; training from scratch is the right call only when abundant domain-specific data and requirements justify the added investment
> **C.** Disagree, but only because foundation models cannot be fine-tuned
> **D.** Agree, since training from scratch is always faster than fine-tuning

**18. [Scenario / Judgment] Very Hard**

> Explain, using this module's content, why choosing the highest-accuracy model without checking for an interpretability requirement can be a mistake.

> **A.** Higher accuracy is always the only consideration that matters
> **B.** A regulated or high-stakes scenario may require every prediction to be explainable, which a complex, high-performing but black-box model cannot provide — in that case a simpler, interpretable model is the correct choice even at some cost to raw accuracy
> **C.** Interpretable models are always more accurate than complex models
> **D.** Interpretability only matters for image data

**19. [Scenario / Judgment] Very Hard**

> A stakeholder argues that Amazon Rekognition should be used for Meridian Loyalty's recommendation engine, "since it's already available and free to try." Argue against this using this module's content.

> **A.** Agree — Rekognition is the right tool for any ML problem at Meridian
> **B.** Disagree — Rekognition is a pre-built AI service for image and video analysis, not recommendation systems; a recommendation engine tuned to Meridian's own specific purchase-history data calls for a custom-trained model instead, regardless of what's already available
> **C.** Disagree, but only because Rekognition cannot process any images at all
> **D.** Agree, since all AWS AI services are interchangeable

**20. [Scenario / Judgment] Very Hard**

> A student says: "As long as a model gets deployed, the approach used to build it doesn't really matter." Evaluate this claim using this module's content.

> **A.** Agree — all modeling approaches produce identical outcomes once deployed
> **B.** Disagree — choosing a pre-built service versus a custom model, a foundation model versus training from scratch, and an interpretable versus a high-performance model each trade off real costs, data requirements, and explainability needs; getting that choice wrong means paying for the wrong tradeoff for the life of the project
> **C.** Disagree, but only because deployment is always identical regardless of approach
> **D.** Agree, since AWS automatically selects the correct approach

---

*When you finish: count how many you were unsure about. Those are your study list before the exam.*
