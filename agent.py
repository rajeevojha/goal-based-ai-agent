class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal
        self.memory = []
    
    def perceive(self, state):
        return state
    
    def evaluate_actions(self, state):
        actions = {
            "add_1": state + 1,
            "add_2": state + 2
        }

        # Utility = closeness to goal
        scored = {}
        for action, new_state in actions.items():
            scored[action] = -abs(self.goal - new_state)

        return scored
    
    def decide(self, state):
        scored_actions = self.evaluate_actions(state)
        best_action = max(scored_actions, key=scored_actions.get)
        return best_action
    
    def update_memory(self, action, new_state):
        self.memory.append({
            "action": action,
            "resulting_state": new_state
        })