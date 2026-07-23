# terminologies adopted in the course of development

# Queue System Terminology

### Job
A durable, immutable description of a unit of work to be executed asynchronously. 
> **Note:** We say *description*—not "function," "task," or "message."

### Queue
An ordered collection of jobs awaiting execution. Simple and precise.

### Producer
Any application or service that submits jobs to the Queue Service. Examples include:
* FastAuth
* Notification Service
* CLI
* SDK

### Worker
A process responsible for claiming and executing jobs. 
> **Note:** Workers don't create or schedule jobs. They only execute them.

### Claim
The atomic operation that assigns a pending job to a single worker for execution. 
> **Note:** Claiming isn't execution; it's *ownership*.

### Scheduler
The subsystem responsible for time-based decisions. It never executes business logic. Responsibilities include:
* Delayed jobs
* Retries
* Stale job recovery
* Recurring jobs

### Retry
The act of rescheduling a failed job for another execution attempt according to a retry policy.

### Dead Letter Queue (DLQ)
A collection of jobs that exceeded their retry policy and require manual inspection or intervention.

### Heartbeat
A periodic signal sent by a worker indicating it is still actively processing a claimed job.

### Lease
A temporary assignment of a job to a worker. 
> **Concept:** We use the term *lease* instead of *lock* because a lock sounds permanent, whereas a lease expires (like renting a car). When a worker claims a job, it receives a lease. If the worker stops renewing that lease (through heartbeats), another worker may eventually reclaim the job.