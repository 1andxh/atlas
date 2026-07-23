# ADR-001: Monorepo Architecture

## Context
Atlas consists of several related infrastructure services (Queue, Gateway, Feature Flags, Dashboard, SDK) that will evolve together during early development.

## Decision
Atlas will use a monorepo. Each service will have its own module, tests, Docker image, and deployment configuration, but all services will live in a single repository.

## Consequences

### Benefits
* Consistent coding standards and tooling.
* Easier refactoring across services.
* Shared CI/CD pipelines.
* Unified documentation and roadmap.
* Simpler onboarding for contributors.

### Trade-offs
* The repository will become larger over time.
* CI pipelines must avoid rebuilding unaffected services.
* Clear boundaries between services become even more important.