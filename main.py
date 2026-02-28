from agent import GoalBasedAgent
from environment import Environment

def run():
    goal = 10
    agent = GoalBasedAgent(goal)
    env = Environment()

    while env.state < goal:
        current_state = agent.perceive(env.state)
        action = agent.decide(current_state)
        new_state = env.apply(action)
        agent.update_memory(action, new_state)

    print("Goal reached!")
    print("Memory:", agent.memory)

if __name__ == "__main__":
    run()