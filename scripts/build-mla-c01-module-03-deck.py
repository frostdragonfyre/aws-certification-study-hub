"""
Builds certifications/mla-c01-machine-learning-engineer-associate/lectures/03-ensure-data-integrity-and-prepare-data-for-modeling.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-mla-c01-module-03-deck.py

Paired with instructor-private/03-ensure-data-integrity-and-prepare-data-for-modeling-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "mla-c01-machine-learning-engineer-associate", "lectures",
                    "03-ensure-data-integrity-and-prepare-data-for-modeling.pptx")

d = Deck(3, "Ensure Data Integrity and Prepare Data for Modeling",
          "Clean, scaled, encoded data can still be unsafe to train on. Tonight closes Domain 1 with bias, security, and compliance.",
          cert_code="MLA-C01")

# 1 — Title
d.title_slide("Module 3 · Lecture", ["Ensure Data", "Integrity"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 3", "Question of the Day", "Before we start",
    [("A sensor at one store location consistently reads 10% higher than identical sensors elsewhere", "Is that selection bias or measurement bias?"),
     ("Recap: Modules 1-2 ingested, stored, cleaned, and engineered the data", "tonight checks whether it's safe and compliant to train on"),
     ("Tonight's task", "Domain 1, Task 1.3 — closing out Data Preparation")])

# 3 — Objectives
d.numbered_list_slide("Module 3", "Objectives", "Five things by the end of tonight", [
    ("Distinguish selection bias from measurement bias", "and know how each gets identified and mitigated"),
    ("Choose the right strategy to address class imbalance in a dataset", "resampling vs. synthetic data generation"),
    ("Distinguish encryption at rest from encryption in transit for ML data", "KMS vs. TLS"),
    ("Distinguish anonymization from masking for a stated data-protection need", "irreversible vs. reversible de-identification"),
    ("Design a data integrity strategy for a stated compliance and bias requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Clean Data Can Still Be Unsafe to Train On",
    "Bias, unprotected data, and compliance gaps don't show up in a normal data-quality check.", "Module 3")

# 5 — Section intro: Selection vs Measurement Bias
d.content_slide("Selection Bias vs. Measurement Bias",
    "Both are pre-training bias sources — they look similar, but the fix is different", "Module 3", dark=True)

# 6 — Exam trap: Selection vs Measurement Bias
d.quad_box_slide("COMMON EXAM TRAP", "Who's Missing vs. What Went Wrong Measuring", "The fix lives in a different place for each",
    [("Selection bias", "the data isn't representative — certain groups are under- or over-represented."),
     ("Measurement bias", "the collection or labeling process itself introduces a systematic error."),
     ("Certain groups missing or underrepresented", "selection bias, fixed by changing how data is gathered."),
     ("A systematic measurement or labeling error", "measurement bias, fixed by correcting that process.")],
    note="One line: unrepresentative coverage is selection bias — a flawed measurement or labeling process is measurement bias.")

# 7 — Applied
d.table_slide("Module 3", "Selection vs. Measurement Bias, Applied", "Matching the symptom to the right bias type",
    ["Symptom", "Right bias type"],
    [["A customer segment is almost entirely missing from the training data", "Selection bias — broaden data collection"],
     ["A sensor at one location reads consistently high versus identical sensors elsewhere", "Measurement bias — recalibrate or standardize collection"]],
    col_widths=[7.6, 5.0],
    note="Missing coverage points to selection bias; a flawed measurement process points to measurement bias.")

# 8 — Section intro: Encryption at rest vs in transit
d.content_slide("Encryption at Rest vs. Encryption in Transit",
    "ML data needs protection in two different states, each with its own mechanism", "Module 3")

# 9 — Exam trap: Encryption at rest vs in transit
d.quad_box_slide("COMMON EXAM TRAP", "Sitting Still vs. Moving", "A complete strategy needs both, not one or the other",
    [("Encryption at rest", "protects stored data — S3, EBS — typically via AWS KMS-managed keys."),
     ("Encryption in transit", "protects moving data — between systems, across the network — typically via TLS."),
     ("Data sitting in an S3 bucket or EBS volume", "encryption at rest, KMS."),
     ("Data moving between systems", "encryption in transit, TLS.")],
    note="One line: stored data needs KMS-based encryption at rest — moving data needs TLS-based encryption in transit.")

# 10 — Applied
d.table_slide("Module 3", "Encryption at Rest vs. in Transit, Applied", "Matching the data's state to the right protection",
    ["Data state", "Right protection"],
    [["Training data stored in an S3 bucket", "Encryption at rest — AWS KMS-managed keys"],
     ["Data transferring from S3 into a SageMaker training job", "Encryption in transit — TLS"]],
    col_widths=[7.6, 5.0],
    note="Stored data points to encryption at rest; moving data points to encryption in transit.")

# 11 — Section intro: Anonymization vs Masking
d.content_slide("Anonymization vs. Masking",
    "Both protect sensitive data, but they trade off protection strength against usability", "Module 3", dark=True)

# 12 — Exam trap: Anonymization vs Masking (abbreviated, no applied table)
d.quad_box_slide("COMMON EXAM TRAP", "Irreversible vs. Realistic and Reusable", "How the data needs to be used afterward decides which one fits",
    [("Anonymization", "irreversibly de-identifies data — safe for broad release, no path back."),
     ("Masking", "obscures values while often preserving format — fits realistic internal use."),
     ("Public release, no path back to identity", "anonymization."),
     ("Dev/test data that must look realistic", "masking.")],
    note="One line: irreversible and safe for broad release is anonymization — realistic and reusable for internal work is masking.")

# 13 — Putting it together
d.numbered_list_slide("Module 3", "Putting It Together: Diego's Data Integrity Strategy for Meridian", "Every piece from tonight, in one strategy, closing Domain 1", [
    ("SageMaker Clarify run against Meridian Loyalty's data for both selection and measurement bias", "is every segment represented, was collection consistent across locations"),
    ("Resampling applied to Café Sol's fraud-detection dataset, where legitimate transactions vastly outnumber fraud", "addressing severe class imbalance before training"),
    ("KMS-encrypted S3 storage for all training data at rest, TLS enforced for every transfer into training jobs", "protecting data in both states"),
    ("Masking applied to Ridgeline's customer data in the development environment", "realistic test data without exposing real customer PII"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 3", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Selection bias and measurement bias are fixed the same way”", "One is fixed by gathering different data; the other by fixing the measurement process itself."),
    ("“Encryption at rest is enough on its own”", "Data in motion between systems is a separate exposure point needing TLS."),
    ("“Anonymization and masking are interchangeable”", "Anonymization is irreversible for broad release; masking stays reversible and realistic for internal use."),
], dark=True)

# 15 — Domain 1, Complete
d.table_slide("Module 3", "Domain 1, Complete", "Three modules, data genuinely ready for modeling",
    ["Module", "What it covered"],
    [["Module 1 — Task 1.1", "Ingesting and storing data: S3 vs. EFS vs. FSx, batch vs. streaming, data formats"],
     ["Module 2 — Task 1.2", "Transforming data and feature engineering: scaling, encoding, labeling"],
     ["Module 3 — Task 1.3", "Ensuring data integrity: bias, class imbalance, encryption, anonymization vs. masking"]],
    col_widths=[3.8, 8.8],
    note="Ingested, transformed, and verified — Domain 1 is what makes Domain 2's model development trustworthy.")

# 16 — Recap
d.content_slide("Recap",
    "Selection vs. measurement bias, class imbalance, encryption at rest vs. in transit, anonymization vs. masking", "Module 3", dark=True)

# 17 — Closing
d.closing_slide("Ensure Data", "Integrity", "Domain 1 complete")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
