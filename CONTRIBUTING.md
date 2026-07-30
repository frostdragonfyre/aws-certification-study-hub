# Contributing

Thanks for considering a contribution to the AWS Certification Study Hub. This repo has one non-negotiable rule and a handful of style expectations that keep it consistent and legally shareable. Read this before opening a PR.

## The non-negotiable rule: original content only

Every word in this repo must be original writing. That means:

- **Never paste, quote, or closely paraphrase** AWS documentation, AWS training courseware, AWS whitepapers, or any other copyrighted AWS material.
- **Never reproduce real exam questions** — from AWS itself, from braindump sites, or from any other source. All quiz and practice questions here must be original scenarios written from scratch.
- **To reference AWS material**, link to the official source and explain the concept in your own words. A link plus your own explanation is always fine; copied text is never fine.

This rule exists because the repo is licensed under CC BY 4.0 and distributed publicly — content that isn't genuinely original can't legally be shared this way, full stop.

If you're not sure whether something crosses the line, don't guess — open an issue or flag it in your PR description and ask before merging.

## Student privacy

Never include real student data — names, grades, emails, attendance records, submitted work, or anything else identifiable — in any file in this repo. This is a public resource; treat it as fully public at all times, including in commit messages and PR discussions.

## Quiz answers stay private

Quiz files in `quizzes/` are **questions only** — no answer key, no `<details>` reveal block, nothing that gives away the answer. These quizzes get used live in class, so answers can't be sitting in public GitHub history before students take them.

Every quiz's answer key — quick-answers table, score bands, topic-mapped review, and full explanations — goes in that cert's `instructor-private/` folder instead (e.g. `certifications/clf-c02-cloud-practitioner/instructor-private/module-01-quiz-answer-key.md`). That folder is gitignored (`**/instructor-private/` in `.gitignore`); verify with `git check-ignore -v <path>` before trusting a new file is actually excluded. Use `templates/quiz-answer-key-template.md` to start one.

This same rule covers anything else instructor-only: activity answer keys, speaker scripts, graded-assignment solutions. If it's an answer a student shouldn't see before you hand it out, it belongs in `instructor-private/`, not in a public folder.

## Style guide

Match the existing voice. Concretely, that means:

- **Concept before service.** Explain why a problem exists and why it matters before naming the AWS service that solves it.
- **Exam-focused, not exhaustive.** Say explicitly what matters for the exam and what a reader can skip. Comprehensiveness for its own sake isn't the goal.
- **Judgment over memorization**, especially for associate-level and above. Favor scenario reasoning ("here's how to tell which service fits") over rote fact lists.
- **Plain English.** No unexplained jargon walls — define terms on first use or link to the glossary.
- **Be honest about change.** If AWS or the exam has shifted (renamed domain, retired service, changed weighting), say so directly rather than presenting stale info as current.
- **Date anything volatile.** Prices, quotas, and service limits should carry a note like *"verify at aws.amazon.com"* rather than being stated as permanent fact.
- **Tables for comparisons.** Anything with two or more options being weighed against each other belongs in a table, not a paragraph.
- **Flag exam traps** with a `> ⚠️` blockquote, called out explicitly as a trap.
- **One concept per section.** Don't blend two ideas under one heading.

## Starting new content

Always start from the matching file in `templates/`:

- `templates/module-template.md` for a new module
- `templates/quiz-template.md` for a new quiz (public, questions only) and `templates/quiz-answer-key-template.md` for its private answer key
- `templates/lab-template.md` for a new lab

Use `certifications/clf-c02-cloud-practitioner/modules/01-cloud-concepts-overview.md` as the quality bar for depth, tone, and formatting.

## Adding a new certification

To add a new exam, create `certifications/<exam-code>/` with `modules/`, `quizzes/`, and `labs/` subfolders (matching the existing structure), and add a row to the roadmap table in the root `README.md`.

## Submitting changes

- One module/quiz/lab per PR where practical, so review stays focused.
- In the PR description, note which AWS sources (if any) you consulted, to make the "original content" check easy for reviewers.
- Fixes to existing content (typos, broken links, outdated prices) are welcome as smaller, batched PRs.
