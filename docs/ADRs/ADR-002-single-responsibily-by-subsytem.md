# ADR-002: Single Responsibility by Subsystem

**Status:** Accepted

## Context
The Queue Service must support job submission, execution, retries, scheduling, and recovery without creating tightly coupled components.

## Decision
The Queue Service will be divided into three logical subsystems:
* **API Layer**
* **Scheduler**
* **Workers**

Each subsystem owns a single responsibility.

## Consequences

### Benefits
* Easier testing.
* Clear ownership.
* Independent evolution.
* Easier reasoning.
* Better scalability.

### Trade-offs
* More moving parts.
* More inter-component communication.
* Requires well-defined contracts.