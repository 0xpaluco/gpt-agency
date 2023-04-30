class Agent:
    def __init__(self, role: str, name: str):
        self.role = role
        self.name = name
        self.context = []

    def start_agent(self, handler: str):
        self.context.append({ "role": "system", "content": self.role, "name": handler })

