from models.logger import logger


class DialogueManager:
    def __init__(self):
        self.state = 'welcome'
        self.contract_type = None
        self.context = {}

    def process_input(self, user_input):
        response = ""
        action = None

        try:
            if self.state == 'welcome':
                response, self.state = self.handle_welcome(user_input)
            elif self.state == 'collecting_input':
                response, self.state = self.handle_collecting_input(user_input)
            elif self.state == 'confirming_input':
                response, self.state = self.handle_confirming_input(user_input)
            elif self.state == 'generating_contract':
                response, action = self.handle_generating_contract(user_input)
                self.state = 'goodbye'  # Move to goodbye after generating contract
            elif self.state == 'goodbye':
                response, self.state = self.handle_goodbye(user_input)
            else:
                response = "I'm not sure how to handle that. Can you try again?"
                self.state = 'welcome'
        except Exception as e:
            response = "I'm sorry, something went wrong. Can we start over?"
            self.state = 'welcome'

        return response, action

    def handle_welcome(self, user_input):
        return "Welcome to LegalContractBot! Which type of contract would you like to create?", 'collecting_input'

    def handle_collecting_input(self, user_input):
        if "nda" in user_input.lower():
            self.contract_type = "NDA Agreement"
            return "You've chosen an NDA Agreement. Is this correct?", 'confirming_input'
        elif "lease" in user_input.lower():
            self.contract_type = "Lease Agreement"
            return "You've chosen a Lease Agreement. Is this correct?", 'confirming_input'
        else:
            return "I didn't catch that. Can you specify the type of contract? (NDA or Lease)", 'collecting_input'

    def handle_confirming_input(self, user_input):
        if user_input.lower() in ['yes', 'correct']:
            return f"Confirmed. Generating your {self.contract_type}.", 'generating_contract'
        else:
            return "Let's try again. Which type of contract do you need? (NDA or Lease)", 'collecting_input'

    def handle_generating_contract(self, user_input):
        # This function should ideally call ContractManager to generate the contract
        # Placeholder response for demonstration
        return f"{self.contract_type} has been generated.", 'generate_contract'

    def handle_goodbye(self, user_input):
        return "Thank you for using LegalContractBot. Have a great day!", 'welcome'

if __name__ == "__main__":
    dm = DialogueManager()
    print(dm.process_input("Hi"))
    print(dm.process_input("I need an NDA"))
    print(dm.process_input("yes"))
    print(dm.process_input("bye"))
