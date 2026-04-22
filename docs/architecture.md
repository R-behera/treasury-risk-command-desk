# Architecture

## Workflow

1. Domain data enters the system as structured records or extracted evidence packs.
2. The service shapes those records into operator-facing views through `FastAPI` endpoints.
3. The browser client renders the decision surface and pulls live preview data from `/api/overview`.
4. Reviewers can reason about the output using the same language they use in business operations.

## Design goals

- Keep the stack lightweight enough to demo quickly.
- Preserve a credible production path with API, docs, Docker, and clear roles.
- Make the value visible in the UI within one screen.
