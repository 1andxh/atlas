# Engineering Principles

## Principle: Platform Modularity

* **One service, one responsibility.**
* **Every service is independently deployable.**
* **Services communicate through contracts, never databases.**
* **Prefer explicitness over "magic".**
* **The platform is modular.**

## Principle: Separate Decision from Execution

Components that decide *when* work should happen should not also *perform* the work. 

* **The Scheduler** decides.
* **Workers** execute.
* **The API** accepts requests.

> **Rationale:** Clear boundaries reduce complexity and make failures easier to isolate.