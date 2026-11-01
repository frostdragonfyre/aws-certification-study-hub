# Repository maintenance

[Hub home](../README.md) · [Contribution guide](../CONTRIBUTING.md) · [Authoring templates](../templates/README.md)

Learners can read the published modules and download the existing slide decks without running these scripts. This directory is for maintaining the public material.

## Check navigation and structure

Run from the repository root with Python 3.9 or newer:

```sh
python scripts/check_hub.py
```

The checker uses the standard library. It verifies local Markdown link targets and headings, paired module/quiz/slide files, balanced code fences, and the output destinations in existing slide-builder scripts. It ignores instructor-private, draft, scratch, and tooling directories. It checks local structure rather than live external websites or the factual accuracy of every lesson.

## Maintain lecture decks

The existing builders require `python-pptx`. Scripts are named by the sequence they build:

| Builder pattern | Destination |
| --- | --- |
| `build-module-*-deck.py` | SAA-C03 slide decks |
| `build-sap-c02-module-*-deck.py` | SAP-C02 slide decks |
| `build-soa-c02-module-*-deck.py` | Legacy SOA-C02 slide decks |
| `build-mla-c01-module-*-deck.py` | The available MLA-C01 slide decks |
| `build-ccp-exam-review-deck.py` | Cloud Practitioner exam-review deck |

For example:

```sh
python scripts/build-module-07-deck.py
```

Builders write directly to their existing `certifications/<full-folder-name>/lectures/` destination. Running a builder replaces that deck, so review the source first and inspect the rendered slides before publishing the regenerated file. Some existing decks have no corresponding builder in this directory; keep their source files rather than assuming every presentation can be rebuilt.

Do not run all builders merely to check navigation. `check_hub.py` validates their destination paths without generating or changing presentations.
