class SimpleMemory:
    def __init__(self):
        self.history = []

    def add(self, question, answer):
        self.history.append(f"Q: {question}\nA: {answer}")

    def get_recent(self, limit=3):
        return self.history[-limit:]