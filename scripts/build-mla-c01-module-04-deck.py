"""
Builds certifications/mla-c01-machine-learning-engineer-associate/lectures/04-choose-a-modeling-approach.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-mla-c01-module-04-deck.py

Paired with instructor-private/04-choose-a-modeling-approach-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "mla-c01-machine-learning-engineer-associate", "lectures",
                    "04-choose-a-modeling-approach.pptx")

d = Deck(4, "Choose a Modeling Approach",
          "Domain 1 made the data ready. Tonight is the decision that shapes everything Domain 2 builds next.",
          cert_code="MLA-C01")

# 1 — Title
d.title_slide("Module 4 · Lecture", ["Choose a Modeling", "Approach"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 4", "Question of the Day", "Before we start",
    [("Café Sol needs to extract text from receipt images — a common, well-defined problem", "Do you train a custom model, or reach for something that already exists?"),
     ("Recap: Domain 1 made the data ready", "tonight decides what actually gets built with it"),
     ("Tonight's task", "Domain 2, Task 2.1 — opening ML Model Development")])

# 3 — Objectives
d.numbered_list_slide("Module 4", "Objectives", "Five things by the end of tonight", [
    ("Choose between a pre-built AI service and a custom-trained model", "for a stated business problem"),
    ("Choose between a foundation model and training from scratch", "for a stated requirement"),
    ("Weigh interpretability against raw predictive performance", "for a stated use case"),
    ("Recognize when built-in algorithms, JumpStart, or Bedrock fit a scenario", "matching the tool to the constraint"),
    ("Design a modeling approach for a stated business problem and constraint set", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Not Every Problem Needs a Model You Train Yourself",
    "Domain 1 made the data ready. Tonight is the decision that shapes everything Domain 2 builds next.", "Module 4")

# 5 — Section intro: AI service vs custom model
d.content_slide("Pre-Built AI Service vs. Custom-Trained Model",
    "Not every ML problem needs a model trained from your own data", "Module 4", dark=True)

# 6 — Exam trap: AI service vs custom model
d.quad_box_slide("COMMON EXAM TRAP", "Already Solved vs. Specific to You", "Re-solving a solved problem usually wastes time and money",
    [("Pre-built AI services", "Rekognition, Comprehend, Transcribe — solve common problems out of the box."),
     ("Custom-trained models", "worth it when the problem is specific to your own data or domain."),
     ("Common, well-defined problem", "an AWS AI service, no training required."),
     ("Problem specific to your own data", "a custom-trained model.")],
    note="One line: a problem AWS already solves points to an AI service — a problem specific to your data points to a custom model.")

# 7 — Applied
d.table_slide("Module 4", "AI Service vs. Custom Model, Applied", "Matching the problem to the right approach",
    ["Problem", "Right approach"],
    [["Extracting text from receipt images", "Amazon Rekognition — a pre-built AI service"],
     ["A recommendation engine tuned to Meridian's own purchase history", "A custom-trained model, built on Meridian's specific data"]],
    col_widths=[7.6, 5.0],
    note="Common and already-solved points to an AI service; specific to your data points to a custom model.")

# 8 — Section intro: Foundation model vs from scratch
d.content_slide("Foundation Model vs. Training From Scratch",
    "When a model is the right call, the next question is where it starts from", "Module 4")

# 9 — Exam trap: Foundation model vs from scratch
d.quad_box_slide("COMMON EXAM TRAP", "Limited Data vs. Abundant Domain Data", "What you have available decides where to start",
    [("Foundation models", "Bedrock or JumpStart — pre-trained, fine-tune or prompt on less data."),
     ("Training from scratch", "built-in algorithms or custom architectures, needs abundant labeled data."),
     ("Limited data, tight timeline, general task", "a foundation model, fine-tuned or prompted."),
     ("Abundant data, an unmet requirement", "training from scratch.")],
    note="One line: limited data and general tasks want a foundation model — abundant domain data wants training from scratch.")

# 10 — Applied
d.table_slide("Module 4", "Foundation Model vs. From Scratch, Applied", "Matching the data and task to the right start",
    ["Situation", "Right approach"],
    [["Limited labeled reviews, a task resembling general sentiment understanding", "Fine-tune a foundation model via SageMaker JumpStart"],
     ["Large, specific purchase-history dataset, behavior-tuned requirement", "Train a custom SageMaker built-in algorithm from scratch"]],
    col_widths=[7.6, 5.0],
    note="Limited data and general tasks point to a foundation model; abundant specific data points to training from scratch.")

# 11 — Section intro: Interpretability vs performance
d.content_slide("Interpretability vs. Performance",
    "Some models explain themselves. Others just perform — and the exam expects you to know which is needed", "Module 4", dark=True)

# 12 — Exam trap: Interpretability vs performance
d.quad_box_slide("COMMON EXAM TRAP", "Explainable vs. Highest-Accuracy", "Checking for an interpretability requirement comes before chasing accuracy",
    [("Interpretable models", "linear regression, decision trees — a human can explain each prediction."),
     ("High-performance models", "deep networks, ensembles — often better accuracy, less explainable."),
     ("Regulated decision needing explanation", "an interpretable model, even at some accuracy cost."),
     ("Pure performance goal, no such requirement", "a more complex model.")],
    note="One line: a required explanation points to an interpretable model — pure accuracy with no such requirement allows a complex one.")

# 13 — Putting it together
d.numbered_list_slide("Module 4", "Putting It Together: Diego's Modeling Approach for Meridian", "Every piece from tonight, in one strategy", [
    ("Amazon Rekognition for Café Sol's basic receipt-image text extraction", "a well-defined problem AWS already solves"),
    ("SageMaker JumpStart, fine-tuning a foundation model, for Ridgeline's review sentiment analysis", "limited labeled data, a task resembling general language understanding"),
    ("A custom-trained SageMaker built-in algorithm for Meridian Loyalty's recommendation engine", "trained on Meridian's own large, specific purchase-history data"),
    ("An interpretable model for Meridian Loyalty's credit-eligibility scoring", "regulatory requirements mean every decision needs an explainable reason"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 4", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Custom models are always better than AI services”", "A well-defined, already-solved problem usually doesn't justify the added cost of building custom."),
    ("“Foundation models are a shortcut for skipping real work”", "They're the right choice specifically when data or time is limited."),
    ("“The highest-accuracy model is always the right pick”", "Not if a regulated or high-stakes scenario requires an explainable prediction."),
], dark=True)

# 15 — Recap
d.content_slide("Recap",
    "AI service vs. custom model, foundation model vs. training from scratch, interpretability vs. performance", "Module 4", dark=True)

# 16 — Bonus: SageMaker built-in algorithms note
d.table_slide("Module 4", "Where SageMaker Built-In Algorithms Fit", "One more option worth knowing",
    ["Situation", "Fit"],
    [["A well-understood problem type — classification, regression, clustering — with your own data", "A SageMaker built-in algorithm, often faster to stand up than a fully custom model"],
     ["A problem far outside standard algorithm types", "A custom architecture, trained on SageMaker's flexible training infrastructure"]],
    col_widths=[6.5, 6.1],
    note="Built-in algorithms sit between a pre-built AI service and a fully custom architecture.")

# 17 — Closing
d.closing_slide("Choose a Modeling", "Approach", "Domain 2 underway")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
