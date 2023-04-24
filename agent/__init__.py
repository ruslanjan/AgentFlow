import openai

# Chat Gpt Agent
class Agent:
    goals = []
    current_goal = None
    autonomous_mode = False

    def __init__(self, goals, autonomous_mode=False):
        self.goals = goals
        self.current_goal = goals[0]
        self.autonomous_mode = autonomous_mode
        if len(goals) == 0:
            raise Exception("No goals specified")

    # Make next move
    def forward(self, prompt):
        openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"},
                {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
                {"role": "user", "content": "Where was it played?"}
            ]
        )
        return response.choices[0].text

