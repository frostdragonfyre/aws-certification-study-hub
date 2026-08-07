**NET-3100BB2 · AWS SOLUTIONS ARCHITECT · WAKE TECH**

**Module 5 Review Quiz**

Adding a Compute Layer Using Amazon EC2 · 20 questions · Practice — not graded

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

> Amazon EC2 provides resizable virtual servers that you configure, launch, and control yourself.
>
> TRUE   FALSE

**2. [Multiple Choice] Easy**

> What does an Amazon Machine Image (AMI) provide when you launch an instance?
>
> **A.** The physical server hardware
> **B.** The template — operating system and any preinstalled software — the instance starts from
> **C.** The network connection to the internet
> **D.** The billing method for the instance

**3. [Fill in the Blank] Easy**

> Amazon ____________ is network-attached block storage that persists independently of the EC2 instance's own lifecycle.

**4. [Multiple Choice] Easy**

> Which EC2 storage option is physically attached to the same host as the instance and is lost when the instance stops or terminates?
>
> **A.** Amazon EBS
> **B.** Amazon S3
> **C.** Instance store
> **D.** Amazon EFS

**5. [True / False] Easy**

> Under the shared responsibility model, AWS manages the physical hardware underneath an EC2 instance while you manage the guest operating system running on it.
>
> TRUE   FALSE

---

## Moderate Questions

**6. [Multiple Choice] Moderate**

> Which instance type family is designed for workloads that need high-performance processors, such as batch processing and scientific modeling?
>
> **A.** General purpose
> **B.** Compute optimized
> **C.** Memory optimized
> **D.** Storage optimized

**7. [Fill in the Blank] Moderate**

> A script attached to an instance at launch and run automatically on first boot is called ____________ data.

**8. [Multiple Choice] Moderate**

> What is the main advantage of creating a custom AMI rather than starting from a base AMI every time?
>
> **A.** Custom AMIs are always free while base AMIs are not
> **B.** It captures your configured state so identical instances can be relaunched repeatedly without manual setup
> **C.** Custom AMIs run faster than base AMIs on the same hardware
> **D.** Only custom AMIs can be used with Auto Scaling

**9. [True / False] Moderate**

> Memory optimized instances are the right choice for large in-memory databases and real-time analytics workloads.
>
> TRUE   FALSE

**10. [Multiple Choice] Moderate**

> Which EC2 purchasing option offers deeply discounted capacity that AWS can reclaim with little notice, making it suitable only for fault-tolerant workloads?
>
> **A.** On-Demand
> **B.** Reserved Instances
> **C.** Spot Instances
> **D.** Dedicated Hosts

**11. [Fill in the Blank] Moderate**

> ____________ Instances are the right purchasing option when a workload must run on physical servers dedicated to a single customer for compliance reasons.

---

## Hard Questions

**12. [Scenario / Judgment] Hard**

> A workload writes temporary scratch data that is regenerated on every run and never needs to survive a restart. Which storage option is worth considering for the performance benefit?
>
> **A.** Instance store, since the data doesn't need to persist beyond the instance
> **B.** Amazon EBS, since all EC2 storage must be persistent
> **C.** Amazon S3 Glacier, since scratch data is rarely accessed
> **D.** No storage is required for scratch data

**13. [Scenario / Judgment] Hard**

> A team launches instances from a base AMI and then spends 20 minutes manually installing packages and configuration on each one. What's the best way to eliminate that repeated manual work?
>
> **A.** Launch fewer instances
> **B.** Use user data to configure at boot, or build a custom AMI capturing the configured state
> **C.** Switch to a larger instance type so setup finishes faster
> **D.** Move the workload to instance store

**14. [Scenario / Judgment] Hard**

> An application is brand new and nobody knows yet how much traffic it will get or how long it will run. Which purchasing option is the most sensible starting point?
>
> **A.** A three-year Reserved Instance, to lock in the lowest rate immediately
> **B.** On-Demand, since there's no commitment and the usage pattern isn't known yet
> **C.** Spot Instances, since the workload is new
> **D.** Dedicated Hosts, since new applications need isolation

**15. [Scenario / Judgment] Hard**

> A general purpose instance is running a workload that consistently maxes out memory while barely using its CPU. What does this suggest?
>
> **A.** The instance needs a larger EBS volume
> **B.** The instance family should be reevaluated — a memory optimized family matches this workload's actual resource profile better
> **C.** General purpose is always correct, so nothing should change
> **D.** The workload should move to instance store

**16. [Scenario / Judgment] Hard**

> Why does combining user data with EC2 Auto Scaling matter more than using user data on a single manually launched instance?
>
> **A.** User data only functions inside an Auto Scaling group
> **B.** Auto Scaling launches instances automatically with no human present, so a newly launched instance must configure itself to be useful the moment it comes online
> **C.** Auto Scaling requires a custom AMI, which user data replaces
> **D.** User data runs faster on Auto Scaling instances

---

## Very Hard Questions

**17. [Scenario / Judgment] Very Hard**

> A student says: "instance store is just a cheaper version of EBS, so use it whenever you want to save money." What's the correct correction?
>
> **A.** They're right — instance store is simply the budget option
> **B.** They're comparing the wrong attribute. The deciding question is persistence, not price: instance store data disappears when the instance stops or terminates, so it's only appropriate when losing that data is acceptable
> **C.** Instance store is more expensive than EBS in every Region
> **D.** EBS and instance store are the same service under different names

**18. [Scenario / Judgment] Very Hard**

> A retailer's inventory service will run continuously for the next year in a single Region. Demand rises during seasonal peaks, so they expect to move to a larger size within the same instance family, but never to a different family. They want the lowest possible cost. Which option fits best?
>
> **A.** On-Demand, since sizes will change during the year
> **B.** A Compute Savings Plan, since it offers the most flexibility
> **C.** An EC2 Instance Savings Plan, which commits to one instance family in one Region for the deepest discount while still allowing the size to change
> **D.** Dedicated Instances, since the workload runs year-round

**19. [Scenario / Judgment] Very Hard**

> Why is it a mistake to treat "general purpose" as the automatic default for every EC2 workload?
>
> **A.** General purpose instances are being deprecated by AWS
> **B.** General purpose balances resources evenly, which wastes money and performance when a workload has one clearly dominant need such as memory, CPU, or sequential disk throughput
> **C.** General purpose instances cannot be used with Auto Scaling
> **D.** General purpose instances only support instance store

**20. [Scenario / Judgment] Very Hard**

> The café's order records must survive an instance being terminated and replaced during a scaling event. Which combination of decisions actually delivers that, and why?
>
> **A.** Instance store plus a custom AMI, because AMIs back up all attached storage automatically
> **B.** Amazon EBS for the data, because EBS persists independently of any single instance's lifecycle, while the AMI and user data handle recreating the instance itself
> **C.** A larger instance type, because larger instances are terminated less often
> **D.** Reserved Instances, because reserved capacity is never terminated

---

*When you finish: count how many you were unsure about. Those are your study list for the next class.*
