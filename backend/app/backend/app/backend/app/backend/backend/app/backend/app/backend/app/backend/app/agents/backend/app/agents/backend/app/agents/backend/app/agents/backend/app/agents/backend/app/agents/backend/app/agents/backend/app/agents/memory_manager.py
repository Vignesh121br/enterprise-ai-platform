class MemoryManager:

    def __init__(self):
        self.memory = {}

    def save(self, session_id, role, content):

        if session_id not in self.memory:
            self.memory[session_id] = []

        self.memory[session_id].append(
            {
                "role": role,
                "content": content
            }
        )

    def load(self, session_id):

        return self.memory.get(session_id, [])

    def clear(self, session_id):

        self.memory.pop(session_id, None)


memory_manager = MemoryManager()
