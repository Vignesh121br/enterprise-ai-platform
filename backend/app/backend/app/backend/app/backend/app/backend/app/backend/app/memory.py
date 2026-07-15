class ConversationMemory:

    def __init__(self):
        self.sessions = {}

    def add(self, session_id, role, content):

        if session_id not in self.sessions:
            self.sessions[session_id] = []

        self.sessions[session_id].append(
            {
                "role": role,
                "content": content
            }
        )

    def history(self, session_id):
        return self.sessions.get(session_id, [])


memory = ConversationMemory()
