class Environment:
    def __init__(self):
        self.state = 1
    
    def apply(self, action):
        if action == "add_1":
            self.state += 1
        elif action == "add_2":
            self.state += 2
        
        return self.state