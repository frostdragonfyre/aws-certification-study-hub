**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · LECTURE 8**

**Lab Worksheet — Databases**

Activity 1: Sort the Data · Activity 2: Database Case Studies

| **Name** | **Date** |
|---|---|

---

## Activity 1 — Sort the Data (20 min)

### How this works

Below is a list of data needs. For each one, sort it two ways: relational or NoSQL, and transactional (OLTP) or analytical (OLAP). Work on your own first, then we'll build the sort together on the board.

*This is the single most tested skill in this module — sorting a scenario by structure and workload shape before picking a specific service.*

### Sort each need

| # | Data need | Relational or NoSQL | OLTP or OLAP |
|---|---|---|---|
| 1 | Customer orders with strict relationships between customers, orders, and line items | | |
| 2 | A shopping cart that needs simple, fast lookups by user ID, at massive scale | | |
| 3 | Five years of company-wide sales history, queried for quarterly trend reports | | |
| 4 | A login system checking username and password on every request | | |
| 5 | A mobile app's user profiles, where different users might have very different sets of stored attributes | | |
| 6 | A bank's transaction ledger, requiring strict consistency and complex joins across accounts | | |

### Does performance vs. availability change the picture? (discuss as a class)

Look at #6 again — a bank's transaction ledger, relational, OLTP.

| Question | Your answer |
|---|---|
| What AWS service is the natural fit for this data, based on its structure? | |
| The bank says this database can never go down during a failure. What RDS feature directly addresses that? | |
| If read traffic (like account balance checks) started overwhelming the database, what RDS feature would help, and how is it different from the failover feature? | |

### Think about it

1. Why is "needs complex joins across related tables" the detail that rules out DynamoDB, even for a workload that also needs to be fast?
2. RDS and Aurora are both relational. What's the actual difference between choosing one over the other?
3. Give one example (not from the list above) of a workload that belongs on Redshift, and explain what makes it OLAP instead of OLTP.

---

## Activity 2 — Database Case Studies (25 min)

### How this works

Work on your own. For each business case, write which AWS database service fits best — and UNDERLINE the exact phrase that gave it away. We'll go through the answers together as a class afterward.

*Same skill as the storage service hunt from Lecture 7: noticing which phrase is load-bearing is what the real exam question is testing. This mirrors AWS Academy's own "database case studies" activity for this module.*

**Don't worry about finishing all of them. Getting through them carefully beats rushing. This is not collected or graded.**

### Your reference — the toolkit

| Service | What it's for |
|---|---|
| Amazon RDS | Managed relational database — standard engines (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server) |
| Amazon Aurora | AWS's own relational engine, MySQL/PostgreSQL-compatible, higher performance, runs on RDS |
| Amazon DynamoDB | Managed NoSQL — key-value/document, massive scale, millisecond latency |
| Amazon Redshift | Managed data warehouse — OLAP, analytics across large historical datasets |
| Multi-AZ | RDS feature — synchronous standby, automatic failover |
| Read Replicas | RDS feature — offloads read traffic to additional copies |

### The case studies

*Underline the deciding phrase in each case as you read it.*

| # | Business case | Your answer |
|---|---|---|
| 1 | A retailer's order-management system needs strict relationships between customers, orders, and inventory, queried with SQL. | |
| 2 | A gaming company needs a player-profile store that can handle millions of simple lookups per second, with profiles that don't all look alike. | |
| 3 | A retail chain wants to analyze five years of transaction history to find seasonal buying patterns across every store. | |
| 4 | A company wants MySQL compatibility but needs better performance and availability than a standard MySQL instance on RDS. | |
| 5 | An airline's booking database absolutely cannot go down during a single Availability Zone outage. | |
| 6 | A news site's article database is getting hammered with read traffic from a spike in visitors, but writes are still low. | |
| 7 | A healthcare provider needs patient records stored with enforced relationships and strong consistency, following a strict schema. | |
| 8 | A social media app needs to store posts with wildly varying structure — some have images, some have polls, some have neither. | |
| 9 | A finance team wants a single tool to run complex quarterly aggregate reports across the entire company's sales data. | |
| 10 | A startup wants a fully managed relational database without picking a specific AWS-built engine, just standard PostgreSQL. | |

### Pick any two and go deeper

For two of the case studies above, write out why the service you picked beats the next most tempting wrong answer.

**Case #____ — why this beats the tempting wrong answer:**

**Case #____ — why this beats the tempting wrong answer:**

### The shortcut — write this down

**For ANY AWS database scenario on the exam, ask in this order:**

1. Is the data **structured with enforced relationships**? → Relational — Amazon RDS.
2. Same, but wants **higher performance and availability**? → Amazon Aurora.
3. Does it need **massive scale with simple key lookups**, flexible schema? → Amazon DynamoDB.
4. Is it **analytical queries across large historical datasets**? → Amazon Redshift.
5. Worried about **a single instance failing**? → Multi-AZ deployment.
6. Is **read traffic** bottlenecking one instance? → Read replicas.

*Notice the pattern: structure first (relational vs. NoSQL), then workload shape (transactional vs. analytical), then availability/scaling features layered on top once you've picked the base service.*

### Finished early?

| # | Try one of these |
|---|---|
| 1 | Rewrite case study 2 so the correct answer becomes RDS instead of DynamoDB. What did you have to change? |
| 2 | Explain in your own words why Aurora isn't a "different kind" of database from RDS. |
| 3 | Pick one AWS database service and explain, without notes, the specific workload shape it's built for. |

### Before you leave

| ✓ | Homework due next class |
|---|---|
| | Finish AWS Academy Module 8 + knowledge check, including Lab 5 (aim 80%+ first attempt) |
| | Sketch the four database services from memory once, without looking at your notes |
| | Pick one database service from tonight's toolkit and explain what it does in your own words, no notes |
