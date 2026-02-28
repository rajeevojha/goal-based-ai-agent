# Project Roadmap

This repository evolves in structured phases to progressively explore
AI agent architecture — from a minimal goal-based system to applied,
real-world decision agents.

The goal is not rapid feature expansion, but disciplined architectural growth.

---

# Phase 1 — Foundational Agent (Current State)

Status: Completed

Objectives:
- Implement minimal goal-based agent
- Separate agent and environment
- Introduce utility-based action evaluation
- Maintain action memory
- Document architecture and intent

Key Concepts Introduced:
- Perception-action loop
- Goal termination condition
- Utility scoring
- Decision abstraction
- System modularity

---

# Phase 2 — Smarter Utility-Based Agent

Status: Planned (feature branch)

Objectives:
- Introduce action cost
- Expand utility beyond distance-to-goal
- Optimize for multi-factor objectives
- Add optional stochastic environment behavior

Concepts Introduced:
- Tradeoffs
- Multi-objective optimization
- Robust decision-making under uncertainty

Expected Structural Changes:
- Utility scoring refactor
- Cost tracking
- Environment randomness hooks

---

# Phase 3 — Comparative Agents

Status: Planned (feature branch)

Objectives:
- Implement a rule-based (non-utility) agent
- Compare behavior against goal-based agent
- Document behavioral differences

Concepts Introduced:
- Static logic vs dynamic evaluation
- Predictability vs adaptability
- Deterministic vs evaluative decision systems

Deliverable:
- `rule_based_agent.py`
- `docs/agent-comparison.md`

---

# Phase 4 — Domain-Specific Agents

Status: Planned (separate branches per domain)

The agent architecture will be applied to real-world modeled problems.

## 4.1 Portfolio Risk Agent
Goal:
Optimize risk-adjusted return under simulated market conditions.

Concepts:
- Risk modeling
- Allocation decision-making
- Utility under uncertainty
- Rebalancing logic

## 4.2 Mortgage Optimization Agent
Goal:
Balance extra principal payments against investment allocation.

Concepts:
- Long-term projection modeling
- Opportunity cost
- Tradeoff analysis

## 4.3 Local Decision Agent
Goal:
Provide strategy recommendations for user-defined objectives.

Concepts:
- Strategy scoring
- Goal planning abstraction
- Extensible decision modeling

---

# Phase 5 — Engineering Maturity

Status: Planned

Objectives:
- Add unit tests
- Introduce Makefile
- Improve logging and observability
- Optional performance visualization

Concepts:
- Reproducibility
- Test-driven validation
- Production-readiness principles

---

# Long-Term Vision

This repository aims to demonstrate:

- Clear understanding of agent architecture
- Systematic evolution of complexity
- Application of decision systems across domains
- Clean separation of concerns
- Documentation-driven engineering

Each phase builds intentionally on the previous one.

No shortcuts. No hype. Structured growth.