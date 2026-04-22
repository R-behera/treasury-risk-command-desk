# Treasury Risk Command Desk

A production-style derivative project inspired by [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal).

## Real-world problem

Treasury teams need a concise control room for FX exposure, refinancing windows, liquidity pressure, and scenario planning instead of a generic market terminal.

## Why this project exists

This derivative translates a broad financial analytics interface into a treasury-specific decision desk with exposures, hedge coverage, scenario impacts, and recommended actions.

## Upstream source

- Upstream repo: [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal)
- Upstream stars: 12905
- Upstream description: FinceptTerminal is a modern finance application offering advanced market analytics, investment research, and economic data tools, designed for interactive exploration and data-driven decision-making in a user-friendly environment.
- Upstream last updated: 2026-04-22T18:58:24Z

## What I changed in the derivative

- Framed the project around a specific operator and decision workflow.
- Added a unique UI and domain-specific language instead of a generic framework demo.
- Added deployment-ready scaffolding with API endpoints, Docker packaging, docs, and a demo surface.
- Added upstream audit and improvement documents to explain the gap between framework capability and productized usage.

## Repo structure

- `src/app/main.py`: FastAPI service and API endpoints
- `src/app/web/index.html`: unique front-end
- `docs/architecture.md`: system framing
- `docs/upstream_audit.md`: lightweight upstream audit
- `docs/improvement_plan.md`: how the derivative differs and why
- `research/upstream_snapshot.json`: metadata snapshot
- `demo/index.html`: demo surface copy
- `demo/screenshot.svg`: visual asset for sharing

## Audit snapshot

- File count scanned: 2756
- Tests present: True
- Docker packaging present: True
- CI present: True
- TODO/FIXME/HACK markers found: 1

## Quick start

```bash
pip install -r requirements.txt
uvicorn src.app.main:app --reload
```
