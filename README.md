# AWS Certification Study Hub

Original, free study materials for AWS certifications — written by [Dr. Mycal "Mike" Brown](https://github.com/frostdragonfyre), an AWS-certified instructor and adjunct faculty member.

Every module, quiz, and lab here is original writing, built to explain AWS concepts the way I teach them in the classroom: the *why* before the *what*, judgment over memorization, and an honest read on what actually matters for the exam versus what's console trivia.

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
| Foundational | Cloud Practitioner (CLF-C02) | In progress |
| Associate | Solutions Architect (SAA-C03) | Planned |
| Associate | Developer (DVA-C02) | Planned |
| Associate | SysOps Administrator (SOA-C02) | Planned |
| Associate | Data Engineer (DEA-C01) | Planned |
| Professional | Solutions Architect (SAP-C02) | Planned |
| Professional | DevOps Engineer (DOP-C02) | Planned |
| Specialty | Security, Networking, ML, Database, etc. | Planned |

## Using this repo

- **Studying for an exam?** Start in `certifications/<exam-code>/modules/01-...` and work through in order. Each module links to its quiz and any paired lab.
- **Need a quick refresher?** Check `shared/cheat-sheets/` and `shared/glossary/` before digging into a full module.
- **Contributing or adapting this material?** See [CONTRIBUTING.md](CONTRIBUTING.md) — the short version is: original content only, no AWS documentation or courseware text, no real exam questions.

## License

This work is licensed under [CC BY 4.0](LICENSE). You're free to use, adapt, and share it — including commercially — as long as you give appropriate credit. See the [LICENSE](LICENSE) file for full terms.

## A note on accuracy

AWS changes services, pricing, and exam content regularly. Where this repo references prices, quotas, or limits, treat them as illustrative and verify current values at [aws.amazon.com](https://aws.amazon.com). Where the exam itself has shifted (retired services, renamed domains, changed weighting), the relevant module will say so rather than pretend the old version still holds.
