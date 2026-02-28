# Goal-Based AI Agent

A structured exploration of AI agent architecture, starting from a minimal goal-based agent and evolving toward real-world decision systems.

This repository is not just a coding exercise — it is a documented study of:

- Agent design principles
- Decision loops
- Utility-based reasoning
- Environment interaction
- The difference between automation and true agents
- Applying agent architecture to real-world domains (finance, optimization, decision systems)

---

## 1. What Is an AI Agent?

An AI agent is a system that:

1. **Perceives** its environment  
2. **Evaluates** possible actions  
3. **Selects** an action based on a goal  
4. **Acts**  
5. **Updates memory/state**  
6. **Repeats until the goal is achieved**

Unlike traditional automation, an agent does not follow a fixed script.  
It dynamically chooses what to do next based on the current state.

Core loop:

Perceive → Evaluate → Decide → Act → Update Memory → Repeat

---

## 2. Automation vs AI Agent

| Automation | AI Agent |
|------------|----------|
| Predefined steps | Goal-driven behavior |
| Static logic | Dynamic decision-making |
| No evaluation loop | Iterative feedback loop |
| Executes instructions | Pursues objectives |

Automation answers:  
> “How do I do this task?”

An agent answers:  
> “Given my goal and current state, what should I do next?”

Modern agentic systems developed by organizations such as OpenAI and Anthropic follow variations of this decision-loop architecture.

---

## 3. Current Implementation (Phase 1)

The current version implements a **Goal-Based Agent** interacting with a simple environment.

### Agent Characteristics

- Has a defined goal (e.g., reach a target number)
- Evaluates available actions
- Uses utility scoring (closeness to goal)
- Selects the best action dynamically
- Maintains memory of decisions
- Runs in a loop until the goal is reached

### Architecture Separation

- `agent.py` → decision logic
- `environment.py` → state transitions
- `main.py` → orchestration loop

This separation demonstrates:
- Clean system boundaries
- Decoupling of decision logic from environment mechanics
- Extensibility for future domains

---

## 4. How to Run

### Setup (Linux / WSL / macOS)

```bash
python3 -m venv .venv
source .venv/bin/activate
python main.py
```
The agent will iteratively act until the goal state is reached.

## 5. Design Philosophy
This project emphasizes:
- Clarity over complexity
- Explicit decision modeling
- Iterative system evolution
- Documentation-driven development

Each phase expands the sophistication of the agent while maintaining architectural discipline.

## 6. Roadmap
This repository will evolve in structured phases:
### Phase 1 — Foundation
- Minimal goal-based agent
- Documentation of architecture
- Agent vs automation analysis
### Phase 2 — Smarter Agent
- Add action cost
- Multi-factor utility scoring
- Stochastic environment
### Phase 3 — Comparative Agents
- Implement rule-based agent
- Compare decision behaviors
### Phase 4 — Real-World Agents
- Portfolio risk optimization agent
- Mortgage payoff decision agent
- Local decision-planning agent
### Phase 5 — Engineering Maturity
- Unit tests
- Makefile
- Performance logging
- Optional visualization

## 7. Why This Project Exists
Most tutorials show how to call an API.
This project focuses on:
- Understanding what makes something an agent
- Building agent architecture from first principles
- Demonstrating system thinking rather than API usage

The goal is to explore how simple decision loops evolve into powerful adaptive systems.

## 8. License
MIT License
