**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 4 Review Quiz**

AWS Cloud Security · 20 questions · Practice — not graded

| **Name** | **Date** |
|---|---|
| | |

*Instructions: Answer every question. Questions get harder as you go — the last several are exam-style judgment questions where more than one answer looks reasonable. For those, pick the BEST answer and be ready to defend it out loud.*

| **Question types** | **What to do** |
|---|---|
| Multiple Choice | Circle one letter. |
| True / False | Circle TRUE or FALSE. |
| Fill in the Blank | Write your answer on the line. |
| Scenario / Judgment | Circle the BEST answer. Note WHY the others fail. |

---

## Easy Questions

**1. [True / False] Easy**

> AWS is responsible for security OF the cloud; the customer is responsible for security IN the cloud.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> Which of the following is the customer's job under the Shared Responsibility Model?
>
> **A.** Physical security of the data center building
> **B.** Patching the underlying hypervisor
> **C.** Configuring security groups and network ACLs
> **D.** Maintaining the global network infrastructure

**3. [Fill in the Blank] Easy**

> Granting only the permissions a user or role actually needs, nothing more, is called the principle of ____________.

**4. [Multiple Choice] Easy**

> Which IAM building block is a set of temporary permissions that can be assumed, with no long-term credentials attached?
>
> **A.** User
> **B.** Group
> **C.** Role
> **D.** Policy

**5. [True / False] Easy**

> The root account should be used for daily work since it has full account access.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which service continuously monitors an account for suspicious or malicious behavior using automated threat intelligence?
>
> **A.** Amazon Inspector
> **B.** Amazon Macie
> **C.** Amazon GuardDuty
> **D.** AWS Config

**7. [Fill in the Blank] Moderate**

> Amazon ____________ uses machine learning to scan Amazon S3 for sensitive data, like personally identifiable information.

**8. [Multiple Choice] Moderate**

> Which pair of services is used to defend public-facing applications from malicious traffic and DDoS attacks?
>
> **A.** KMS and Artifact
> **B.** WAF and Shield
> **C.** CloudTrail and Config
> **D.** IAM and MFA

**9. [True / False] Moderate**

> AWS Config logs WHO called which API; AWS CloudTrail tracks WHAT a resource's configuration looked like over time.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which service creates and manages the encryption keys used to protect data at rest?
>
> **A.** AWS Artifact
> **B.** AWS KMS
> **C.** Amazon Inspector
> **D.** Amazon GuardDuty

**11. [Fill in the Blank] Moderate**

> AWS ____________ provides on-demand access to AWS's own compliance reports and certifications.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A company moves a database from a self-managed EC2 instance to Amazon RDS. Who now patches the database engine and underlying OS?
>
> **A.** Still the customer
> **B.** AWS
> **C.** Split evenly between AWS and the customer
> **D.** Neither — patching stops being necessary

**13. [Scenario / Judgment] Hard**

> A new employee needs access to exactly one S3 bucket and nothing else in the account. What's the best practice?
>
> **A.** Give them admin access "to be safe"
> **B.** Write a least-privilege IAM policy scoped to that one bucket
> **C.** Share the root account credentials temporarily
> **D.** Give them a copy of another employee's credentials

**14. [Scenario / Judgment] Hard**

> An EC2 instance suddenly starts communicating with a known malicious IP address. Which service is built to catch this happening in real time?
>
> **A.** Amazon Inspector
> **B.** Amazon Macie
> **C.** Amazon GuardDuty
> **D.** AWS Artifact

**15. [Scenario / Judgment] Hard**

> A security lead wants a historical record of exactly when a security group's rules changed, and by whom. What's the best answer?
>
> **A.** GuardDuty alone
> **B.** IAM alone
> **C.** AWS Config for the "what changed," AWS CloudTrail for the "who did it"
> **D.** AWS WAF and AWS Shield

**16. [Scenario / Judgment] Hard**

> A healthcare company needs to prove to an external auditor that AWS itself is HIPAA-eligible, without waiting on a support ticket. What's the best answer?
>
> **A.** AWS CloudTrail
> **B.** AWS Artifact
> **C.** AWS Config
> **D.** AWS KMS

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A company moves a self-managed database from EC2 to RDS and announces "security is now entirely AWS's responsibility." What's wrong with that claim?
>
> **A.** Nothing — they're correct
> **B.** AWS absorbs OS and database-engine patching, but IAM, data, and access control always remain the customer's job, no matter how managed the service is
> **C.** They should move back to self-managed EC2
> **D.** RDS has no shared responsibility model at all

**18. [Scenario / Judgment] Very Hard**

> A company has three distinct needs: (1) detect suspicious behavior happening right now, (2) scan its EC2 fleet for known software vulnerabilities before a launch, and (3) scan S3 for social security numbers that may have been stored there by mistake. In order, which services match?
>
> **A.** Macie, GuardDuty, Inspector
> **B.** GuardDuty, Inspector, Macie
> **C.** Inspector, Macie, GuardDuty
> **D.** GuardDuty, Macie, Inspector

**19. [Scenario / Judgment] Very Hard**

> A CFO's root account credentials are used for day-to-day work, including reading email between tasks. What's the actual problem, and the fix?
>
> **A.** Nothing is wrong, as long as MFA is enabled
> **B.** This violates root account best practice — root should be locked away for rare, account-level tasks; daily work should use an IAM user or role scoped with least privilege
> **C.** The real problem is that Macie isn't enabled
> **D.** The fix is to disable MFA on root

**20. [Scenario / Judgment] Very Hard**

> A company relies solely on IAM as its only security control, with no security groups, no WAF/Shield, and no KMS in the picture. What's the risk, and what's the recommended fix?
>
> **A.** There's no real risk — IAM alone is sufficient for any workload
> **B.** One misconfigured or bypassed layer means total exposure; the fix is defense in depth — stacking IAM with security groups, WAF/Shield, KMS, and the audit trail so no single control carries all the risk
> **C.** Replace IAM entirely with GuardDuty
> **D.** Nothing needs fixing — AWS automatically adds additional layers

---

*When you finish: count how many you were unsure about. Those are your study list for the Cloud Practitioner exam.*
