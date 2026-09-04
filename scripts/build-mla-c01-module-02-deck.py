"""
Builds certifications/mla-c01/lectures/02-transform-data-and-perform-feature-engineering.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-mla-c01-module-02-deck.py

Paired with instructor-private/02-transform-data-and-perform-feature-engineering-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "mla-c01", "lectures",
                    "02-transform-data-and-perform-feature-engineering.pptx")

d = Deck(2, "Transform Data and Perform Feature Engineering",
          "Module 1 got the data in the door. Tonight makes it something a model can actually learn from.",
          cert_code="MLA-C01")

# 1 — Title
d.title_slide("Module 2 · Lecture", ["Transform Data and", "Feature Engineering"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 2", "Question of the Day", "Before we start",
    [("A field holds Low, Medium, and High satisfaction ratings — a genuine, meaningful order", "Should that get one-hot encoded or label encoded?"),
     ("Recap: Module 1 ingested and stored the raw data", "tonight cleans it, scales it, encodes it, and labels it"),
     ("Tonight's task", "Domain 1, Task 1.2 — continuing Data Preparation")])

# 3 — Objectives
d.numbered_list_slide("Module 2", "Objectives", "Five things by the end of tonight", [
    ("Choose between normalization and standardization for a stated scaling requirement", "matching the technique to the algorithm's assumptions"),
    ("Choose between one-hot encoding and label encoding for a stated categorical variable", "nominal vs. ordinal"),
    ("Choose between SageMaker Ground Truth and Mechanical Turk for a stated labeling need", "managed workflow vs. raw workforce"),
    ("Use AWS Glue, Glue DataBrew, and SageMaker Data Wrangler to clean and transform data", "three tools, three points on one spectrum"),
    ("Design a feature engineering strategy for a stated dataset and modeling goal", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Raw Data Rarely Arrives Ready to Train On",
    "Module 1 got the data in the door. Tonight makes it something a model can actually learn from.", "Module 2")

# 5 — Section intro: Normalization vs Standardization
d.content_slide("Normalization vs. Standardization",
    "Both scale numeric features — they solve for different assumptions about the data", "Module 2", dark=True)

# 6 — Exam trap: Normalization vs Standardization
d.quad_box_slide("COMMON EXAM TRAP", "Bounded Range vs. Variance Sensitivity", "The algorithm's assumptions decide which scaling fits",
    [("Normalization", "rescales into a fixed range, no distribution assumption — fits bounded-input algorithms."),
     ("Standardization", "centers to mean 0, std 1 — fits variance-sensitive or normal-assuming algorithms."),
     ("Neural networks, distance-based methods", "normalization, bounded input values."),
     ("Linear models, SVMs, PCA", "standardization, sensitive to variance.")],
    note="One line: bounded-input algorithms want normalization — variance-sensitive or normal-assuming algorithms want standardization.")

# 7 — Applied
d.table_slide("Module 2", "Normalization vs. Standardization, Applied", "Matching the algorithm to the right scaling",
    ["Algorithm / requirement", "Right scaling"],
    [["A neural network needing bounded input values, no distribution assumption", "Normalization — fixed range"],
     ["A linear regression model sensitive to feature variance", "Standardization — mean 0, std 1"]],
    col_widths=[7.6, 5.0],
    note="Bounded-input needs point to normalization; variance sensitivity points to standardization.")

# 8 — Section intro: One-hot vs label encoding
d.content_slide("One-Hot Encoding vs. Label Encoding",
    "Categorical data needs to become numbers — how depends on whether order is meaningful", "Module 2")

# 9 — Exam trap: One-hot vs label encoding
d.quad_box_slide("COMMON EXAM TRAP", "Unordered vs. Ordered Categories", "A false order can mislead a model just as much as a missing one",
    [("One-hot encoding", "a binary column per category — fits nominal, unordered data."),
     ("Label encoding", "a single integer per category — fits ordinal, genuinely ordered data."),
     ("Colors, regions, product types", "one-hot encoding, no real order to preserve."),
     ("Ratings, tiers, severity levels", "label encoding, order is meaningful.")],
    note="One line: no real order wants one-hot encoding — genuine order wants label encoding.")

# 10 — Applied
d.table_slide("Module 2", "One-Hot vs. Label Encoding, Applied", "Matching the category type to the right encoding",
    ["Categorical field", "Right encoding"],
    [["Café Sol's transaction category — Beverage, Bakery, Retail, no order", "One-hot encoding"],
     ["Ridgeline's satisfaction rating — Low, Medium, High, genuine order", "Label encoding"]],
    col_widths=[7.6, 5.0],
    note="No real order points to one-hot; genuine order points to label encoding.")

# 11 — Section intro: Ground Truth vs Mechanical Turk
d.content_slide("SageMaker Ground Truth vs. Mechanical Turk",
    "Both involve human labelers — they differ in how much workflow comes built in", "Module 2", dark=True)

# 12 — Exam trap: Ground Truth vs Mechanical Turk
d.quad_box_slide("COMMON EXAM TRAP", "Managed Workflow vs. Raw Workforce", "The workflow around the labeling is the real distinction",
    [("SageMaker Ground Truth", "active learning, auto-labels easy cases, quality control, flexible workforce."),
     ("Mechanical Turk alone", "a general crowdsourcing marketplace — no ML-specific workflow built in."),
     ("Automated labeling, quality control at scale", "Ground Truth, even if using an MTurk workforce."),
     ("Simple human tasks, no ML workflow needed", "Mechanical Turk directly.")],
    note="One line: needing the managed ML labeling workflow means Ground Truth — needing just raw human tasks means Mechanical Turk alone.")

# 13 — Applied
d.table_slide("Module 2", "Ground Truth vs. Mechanical Turk, Applied", "Matching the labeling need to the right tool",
    ["Labeling need", "Right tool"],
    [["A large image dataset needing automated labeling and quality control at scale", "SageMaker Ground Truth"],
     ["A simple, one-off crowdsourced task with no ML-specific workflow needed", "Amazon Mechanical Turk alone"]],
    col_widths=[7.6, 5.0],
    note="Scale and automation needs point to Ground Truth; simple raw tasks point to Mechanical Turk alone.")

# 14 — Putting it together
d.numbered_list_slide("Module 2", "Putting It Together: Diego's Feature Engineering for Meridian", "Every piece from tonight, in one strategy", [
    ("Standardization for Meridian Loyalty's recommendation model, which is sensitive to feature variance", "matching the technique to the algorithm's assumptions"),
    ("One-hot encoding for Café Sol's unordered transaction-category field", "avoiding a false order between categories"),
    ("Label encoding for Ridgeline's genuinely ordered satisfaction ratings", "preserving that real order for the model"),
    ("SageMaker Ground Truth, backed by a Mechanical Turk workforce, labeling a new image dataset at scale", "active learning cuts the manual labeling load"),
])

# 15 — Common mix-ups
d.resource_list_slide("Module 2", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Normalization and standardization are interchangeable”", "They solve for different assumptions — bounded range versus variance sensitivity."),
    ("“Label encoding is simpler, so use it everywhere”", "On unordered categories it invents a false numeric order a model can learn from."),
    ("“Mechanical Turk and Ground Truth are the same thing”", "Ground Truth adds the ML-specific managed workflow around a workforce; Mechanical Turk alone doesn't."),
], dark=True)

# 16 — Recap
d.content_slide("Recap",
    "Normalization vs. standardization, one-hot vs. label encoding, Ground Truth vs. Mechanical Turk", "Module 2", dark=True)

# 17 — Closing
d.closing_slide("Transform Data and", "Feature Engineering", "Domain 1 continues")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
