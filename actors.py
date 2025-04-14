class Actor:
    def __init__(self, name, role, tokens):
        self.name = name
        self.role = role
        self.tokens = tokens
        self.voted = False

    def __repr__(self):
        return f"{self.name} ({self.role}) - {self.tokens} tokens"

    def reward(self, amount):
        self.tokens += amount
        print(f"💰 {self.name} earned +{amount} token(s)! Total: {self.tokens}")

def get_sample_actors():
    return [
        Actor("Alice", "Admin", 5),
        Actor("Bob", "Teacher", 3),
        Actor("Charlie", "Teacher", 3),
        Actor("Diana", "Student", 1),
        Actor("Eva", "Student", 1),
        Actor("Frank", "Core Member", 2),
    ]
