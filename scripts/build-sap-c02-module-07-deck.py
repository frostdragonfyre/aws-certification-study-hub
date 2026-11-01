"""
Builds certifications/sap-c02-solutions-architect-professional/lectures/07-designing-a-deployment-strategy.pptx

Run from the repo root (needs scripts/deck_lib.py on the path):
    python3 scripts/build-module-07-deck.py

Paired with instructor-private/07-designing-a-deployment-strategy-script.md.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from deck_lib import Deck

OUT = os.path.join(os.path.dirname(__file__), "..",
                    "certifications", "sap-c02-solutions-architect-professional", "lectures",
                    "07-designing-a-deployment-strategy.pptx")

d = Deck(7, "Designing a Deployment Strategy",
          "Domain 1 built the foundation. Domain 2 is where it actually gets used — starting with Meridian Loyalty.",
          cert_code="SAP-C02")

# 1 — Title
d.title_slide("Module 7 · Lecture", ["Designing a", "Deployment Strategy"])

# 2 — QOTD + recap
d.numbered_list_slide("Module 7", "Question of the Day", "Before we start",
    [("Meridian Loyalty is a brand-new guest rewards platform", "It touches real reward balances across three brands — how should a bad release be caught before it affects everyone?"),
     ("Recap: Domain 1 built the organizational foundation", "Connectivity, governance, reliability tooling, accounts, cost — all in place. Now it gets used"),
     ("Tonight's task", "Domain 2, Task 2.1 — designing a deployment strategy, the first Domain 2 module")])

# 3 — Objectives
d.numbered_list_slide("Module 7", "Objectives", "Five things by the end of tonight", [
    ("Compare in-place, rolling, blue/green, and canary deployment", "and the speed/risk/rollback trade-off each makes"),
    ("Explain how CodePipeline, CodeBuild, and CodeDeploy work together", "to automate a deployment end to end"),
    ("Explain why Infrastructure as Code matters", "for consistency across environments and accounts"),
    ("Describe deploying safely across account boundaries", "using the cross-account role pattern from Module 3"),
    ("Recommend a deployment strategy for a stated requirement", "the actual exam skill tonight"),
])

# 4 — Problem framing
d.content_slide("Meridian Loyalty: The First New Solution",
    "Nothing here inherits legacy decisions — every choice is being made fresh, starting with deployment", "Module 7")

# 5 — Four strategies table
d.table_slide("Module 7", "Four Deployment Strategies", "Every one trades deployment speed, risk, and rollback time differently",
    ["Strategy", "Downtime?", "Rollback"],
    [["In-place", "Yes, during the window", "Slow — redeploy the old version from scratch"],
     ["Rolling", "No — batches keep it up", "Moderate — but versions run mixed mid-rollout"],
     ["Blue/green", "No — instant cutover", "Instant — switch back to the untouched blue env"],
     ["Canary", "No — gradual traffic shift", "Fast — limited exposure catches issues early"]],
    col_widths=[2.6, 4.4, 5.6])

# 6 — Exam trap: canary vs blue/green
d.quad_box_slide("COMMON EXAM TRAP", "Canary vs. Blue/Green Isn't the Same Ask", "Instant complete cutover vs. gradual limited exposure",
    [("“Zero downtime, catch a bad release early”", "is canary — gradual traffic shift limits exposure before it's caught."),
     ("“Fastest rollback, two full separate environments”", "is blue/green — an instant, complete cutover."),
     ("Blue/green's cutover", "is typically all-or-nothing once traffic shifts."),
     ("Canary's shift", "is specifically what limits how many users see a bad release first.")],
    note="One line: gradual, limited exposure is canary. Instant, complete cutover is blue/green. Read for which.")

# 7 — CodePipeline/CodeBuild/CodeDeploy
d.content_slide("Automating Deployment: CodePipeline, CodeBuild, CodeDeploy",
    "Manual execution reintroduces exactly the “forgot a step” risk Domain 1 was built to eliminate", "Module 7", dark=True)

# 8 — Three services, three jobs
d.table_slide("Module 7", "Three Services, Three Distinct Jobs", "Working together as one pipeline",
    ["Service", "Responsible for"],
    [["CodePipeline", "Orchestrates the release as stages — source, build, test, deploy — stopping on failure"],
     ["CodeBuild", "Compiles source code, runs tests, produces deployable build artifacts"],
     ["CodeDeploy", "Executes the deployment — natively supports in-place, blue/green, and more"]],
    col_widths=[3.0, 9.6])

# 9 — Infrastructure as Code
d.content_slide("Infrastructure as Code: Consistent, Not Just Repeatable",
    "Manually clicking through the console invites exactly the drift Domain 1 spent five modules preventing", "Module 7")

# 10 — IaC mechanics
d.numbered_list_slide("Module 7", "What CloudFormation or CDK Actually Buys You", "Infrastructure defined once, deployed everywhere it's needed", [
    ("A version-controlled definition", "not a manually reproduced console configuration"),
    ("The same pipeline as application code", "source control, build, deployment — the same audit trail as any other change"),
    ("Consistency across environments and accounts", "dev, staging, and each brand's production stay aligned by construction"),
], note="For Meridian Loyalty: deploying into Ridgeline's account, once it's ready, becomes a parameter change — not a manual rebuild from memory.")

# 11 — Cross-account deployment
d.content_slide("Deploying Across Account Boundaries",
    "The pipeline lives in a tooling account — but has to deploy into Café Sol's, Haven & Co.'s, and eventually Ridgeline's", "Module 7", dark=True)

# 12 — Cross-account deployment mechanics
d.numbered_list_slide("Module 7", "The Same Pattern as Module 3", "Cross-account roles, not shared credentials", [
    ("The pipeline's role in the tooling account", "assumes a role in each target brand account, via sts:AssumeRole"),
    ("Scoped to exactly what deployment requires", "creating and updating Meridian Loyalty's specific resources — nothing more"),
    ("Every cross-account action logged via CloudTrail", "no long-lived credentials stored per brand account, anywhere"),
])

# 13 — Putting it together
d.numbered_list_slide("Module 7", "Putting It Together: Meridian Loyalty's Deployment Strategy", "Every piece from tonight, in one design", [
    ("Canary deployment", "real guest balances at stake — a bad release needs to be caught while affecting few, not all"),
    ("CodePipeline, CodeBuild, and CodeDeploy automate the release", "CodeDeploy's native canary config handles the gradual shift and rollback"),
    ("CloudFormation (or CDK) defines the infrastructure", "deployed through the same pipeline — dev, staging, and each brand stay consistent"),
    ("A cross-account role from the tooling account", "into each brand's account, scoped narrowly to deployment needs"),
])

# 14 — Common mix-ups
d.resource_list_slide("Module 7", "Common Mix-Ups", "Worth getting right before the exam", [
    ("“Blue/green and canary are basically the same”", "Blue/green cuts over all at once; canary gradually limits exposure to a bad release."),
    ("“CodeBuild and CodeDeploy do the same job”", "One compiles and tests; the other executes the actual deployment."),
    ("“Manually built infrastructure is fine if it works once”", "It invites drift over time — IaC keeps every environment consistent by construction."),
], dark=True)

# 15 — Before next class
d.content_slide("Before Next Class",
    "Module 8 continues Domain 2 with Task 2.2: designing Meridian Loyalty's business continuity solution", "Module 7")

# 16 — Recap
d.content_slide("Recap",
    "Four deployment strategies, three CI/CD services, Infrastructure as Code, and cross-account roles — the first new solution, deployed deliberately", "Module 7", dark=True)

# 17 — Closing
d.closing_slide("Designing a", "Deployment Strategy", "Next up: designing Meridian Loyalty's business continuity solution")

n = d.save(OUT)
print(f"Saved {n} slides to {OUT}")
