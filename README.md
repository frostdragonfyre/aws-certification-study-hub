# AWS Certification Study Hub

Original, free study materials for AWS certifications — written by [Dr. Mycal "Mike" Brown](https://github.com/frostdragonfyre), an AWS-certified instructor and adjunct faculty member.

Every module, quiz, and lab here is original writing, built to explain AWS concepts the way I teach them in the classroom: the *why* before the *what*, judgment over memorization, and an honest read on what actually matters for the exam versus what's console trivia.

## Start here

- **New to AWS?** Open the [Cloud Practitioner learning path](certifications/clf-c02-cloud-practitioner/README.md). Begin with its first module, then use the paired quiz and activity.
- **Ready to study architecture?** Open the [Solutions Architect Associate learning path](certifications/saa-c03-solutions-architect-associate/README.md). Its introduction explains prerequisites and where hands-on labs are hosted.
- **Comparing services?** Use the [service decision tables](shared/cheat-sheets/service-decision-tables.md).
- **Working through exam scenarios?** Start with [how to read AWS scenario questions](shared/exam-strategy/reading-scenario-questions.md).

The roadmap below describes material in this repository. Check the current AWS exam guide separately before choosing an exam version; an authored learning path is not a claim that its exam is still available.

For my accounting lessons, FinOps courses, and other teaching, visit [mycalbrown.com](https://mycalbrown.com/) or my [Pluralsight author page](https://www.pluralsight.com/authors/mycal-brown).

For original cost-allocation and AI unit-economics exercises, visit the [FinOps Learning Lab](https://github.com/frostdragonfyre/finops-learning-lab).

## How this is organized

```
certifications/<exam-code>/
  modules/    concept lessons, one file per topic (the primary written content)
  lectures/   source slide decks (.pptx) paired with each module, where available
  quizzes/    practice questions with reasoned explanations
  labs/       hands-on exercises paired with modules

shared/
  exam-strategy/   general test-taking and study approach, not exam-specific
  cheat-sheets/     quick-reference tables (limits, service comparisons, etc.)
  glossary/         term definitions used across all certs

templates/    starting point for every new module, quiz, and lab
```

Each exam gets its own folder under `certifications/`, named by its exam code (e.g. `clf-c02-cloud-practitioner`, `saa-c03`). Content within a cert folder is numbered so modules can be worked through in order, but each one is written to also stand alone as a reference.

## Certification roadmap

This hub is being built out across the full AWS certification path. Status reflects what's actually written, not what's planned.

| Level | Exam | Status |
|---|---|---|
| Foundational | Cloud Practitioner (CLF-C02) | **Complete** — all 10 modules |
| Associate | Solutions Architect (SAA-C03) | **Complete** — all 16 modules |
| Associate | Developer (DVA-C02) | Planned |
| Associate | SysOps Administrator (SOA-C02) | **Complete** — all 15 modules, all 6 domains |
| Associate | Data Engineer (DEA-C01) | Planned |
| Associate | Machine Learning Engineer (MLA-C01) | **In progress** — Modules 1-4 of 12, Domain 1 complete |
| Professional | Solutions Architect (SAP-C02) | **Complete** — all 16 modules |
| Professional | DevOps Engineer (DOP-C02) | Planned |
| Specialty | Security, Networking, ML, Database, etc. | Planned |

## Using this repo

- **Studying for an exam?** Start in `certifications/<exam-code>/modules/01-...` and work through in order. Each module links to its quiz and any paired lab.
- **Need a quick refresher?** [Service decision tables](shared/cheat-sheets/service-decision-tables.md) answer "which service do I pick?" and the [glossary](shared/glossary/terms.md) defines the terms, including the pairs that get confused on exams.
- **Struggling with scenario questions rather than the content?** Read [how to read AWS scenario questions](shared/exam-strategy/reading-scenario-questions.md). Most people who fail knew the services and answered a question the exam wasn't asking.
- **Contributing or adapting this material?** See [CONTRIBUTING.md](CONTRIBUTING.md) — the short version is: original content only, no AWS documentation or courseware text, no real exam questions.

## License

This work is licensed under [CC BY 4.0](LICENSE). You're free to use, adapt, and share it — including commercially — as long as you give appropriate credit. See the [LICENSE](LICENSE) file for full terms.

## A note on accuracy

AWS changes services, pricing, and exam content regularly. Where this repo references prices, quotas, or limits, treat them as illustrative and verify current values at [aws.amazon.com](https://aws.amazon.com). Where the exam itself has shifted (retired services, renamed domains, changed weighting), the relevant module will say so rather than pretend the old version still holds.
