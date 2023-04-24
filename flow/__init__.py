from datetime import datetime


class Message:
    scheduled_at = None
    text = None
    agent_from = None
    agent_to = None

    def __init__(self, scheduled_at, text, agent_from, agent_to):
        self.scheduled_at = scheduled_at
        self.text = text
        self.agent_from = agent_from
        self.agent_to = agent_to

    def is_ready(self):
        return self.scheduled_at <= datetime.now()

    def __str__(self):
        return f"Message from {self.agent_from} to {self.agent_to} at {self.scheduled_at} with text: {self.text}"

