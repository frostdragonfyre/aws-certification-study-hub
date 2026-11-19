# AWS Certification Study Hub

Written lessons, review quizzes, activities, and lecture slides by [Mycal Brown, PhD](https://mycalbrown.com/).

New to AWS? Start with [Cloud Practitioner Module 1](certifications/clf-c02-cloud-practitioner/modules/01-cloud-concepts-overview.md). If you already know the fundamentals, choose a path below. Each course index puts the lesson, slides, and quiz on the same row.

## Choose a learning path

| Learning path | Written modules | Quizzes | Module slides | Where to begin |
| --- | ---: | ---: | ---: | --- |
| [Cloud Practitioner · CLF-C02](certifications/clf-c02-cloud-practitioner/README.md) | 10 | 10 | 10 | Cloud foundations; includes 10 activities and an exam review |
| [Solutions Architect Associate · SAA-C03](certifications/saa-c03-solutions-architect-associate/README.md) | 16 | 15 | 16 | Architecture after foundations; orientation has no separate quiz |
| [Solutions Architect Professional · SAP-C02](certifications/sap-c02-solutions-architect-professional/README.md) | 16 | 16 | 16 | Complex architecture; SAP-C03 transition noted below |
| [Cloud operations · legacy SOA-C02](certifications/soa-c02-sysops-administrator-associate/README.md) | 15 | 15 | 15 | Earlier SysOps sequence; current exam is SOA-C03 |
| [Machine learning · partial MLA-C01](certifications/mla-c01-machine-learning-engineer-associate/README.md) | 4 | 4 | 4 | Modules 1–4 available; updated exam coverage is not claimed |

**Counts describe files available here, not exam readiness or a technical review of every lesson.** The Cloud Practitioner exam-review deck is additional to the module-slide counts above.

## How to use a lesson

1. Open the learning path and choose a numbered module.
2. Read the written lesson; use the slides as another way to explore it.
3. Attempt the paired quiz. Cloud Practitioner also has a paired activity.
4. Revisit the explanation and describe why an answer fits the requirements.

Public quizzes contain questions only. Instructor answer keys and delivery scripts are intentionally excluded. See the [learning guide](LEARNING-GUIDE.md) for prerequisites, study routes, and how the materials fit together.

## Find a reference

- [Service decision tables](shared/cheat-sheets/service-decision-tables.md): compare options after learning the concepts.
- [Glossary](shared/glossary/terms.md): look up a term or a commonly confused pair.
- [Reading scenario questions](shared/exam-strategy/reading-scenario-questions.md): extract requirements and explain tradeoffs.
- [Browse all reference material](shared/README.md).

## Check the exam version

This repository contains versioned teaching material. SOA-C02 is a legacy sequence; MLA-C01 and SAP-C02 also have exam-version transitions. Read the [dated version notes](EXAM-VERSIONS.md) before planning exam preparation. Existing folder names stay stable so links to lessons and slides keep working.

## Teaching and related subjects

- [FinOps Learning Lab](https://github.com/frostdragonfyre/finops-learning-lab): synthetic allocation and AI unit-economics exercises.
- [My Pluralsight courses](https://www.pluralsight.com/authors/mycal-brown): structured FinOps instruction.
- [Accounting for Managers](https://mycalbrown.com/accounting-for-managers/): the business story behind the numbers.
- [My website](https://mycalbrown.com/): accounting, FinOps, AI, and cloud learning.

## Contributing and maintenance

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding material. The [templates](templates/README.md) support consistent lessons, quizzes, and activities. The [maintenance guide](scripts/README.md) explains the slide builders and repository checks.

Run the navigation and structure checks from the repository root:

```sh
python scripts/check_hub.py
```

The checker does not run cloud commands, build slide decks, inspect instructor-private folders, or require third-party packages.

## License and accuracy

Public material is licensed under [CC BY 4.0](LICENSE). Follow the attribution terms when adapting it. AWS changes services, quotas, pricing, and exams; verify time-sensitive details against the official sources linked from the lessons. This is an independent teaching repository, not an official AWS course or endorsement.
