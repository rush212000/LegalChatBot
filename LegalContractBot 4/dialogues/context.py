# dialogues/context.py

class DialogueContext:
    def __init__(self):
        self.reset()

    def reset(self):
        self.state = "initial"
        self.user_data = {}

    def update_state(self, new_state):
        self.state = new_state

    def update_user_data(self, key, value):
        self.user_data[key] = value

    def get_user_data(self, key):
        return self.user_data.get(key, None)

    def get_state(self):
        return self.state
