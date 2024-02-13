from openai import OpenAI

class Responses:
    def __init__(self):
        # Make client an instance attribute so it can be accessed by other methods
        self.client = OpenAI(api_key="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")

    def generate_dynamic_response(self, prompt):
        # Use self.client to access the client instance created in __init__
        res = self.client.chat.completions.create(
            model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}]
        )
        # Assuming the response format, extract the text. Adjust as needed based on actual response structure.
        return res.choices[0].message['content']

    def welcome_message(self):
        prompt = "Generate a welcome message for a legal contract bot."
        return self.generate_dynamic_response(prompt)

    @staticmethod
    def contract_type_options():
        return "I can assist you with creating several types of contracts, including lease agreements, NDAs, and employment contracts. Which one are you interested in?"

    @staticmethod
    def ask_for_detail(detail_name):
        return f"Could you please provide the {detail_name}?"

    @staticmethod
    def confirm_detail(detail_name, detail_value):
        return f"Got it. {detail_name} is set to {detail_value}. Is that correct?"

    @staticmethod
    def error_message():
        return "I'm sorry, I didn't understand that. Could you please provide the information again?"

    @staticmethod
    def final_confirmation():
        return "All set! I have all the information needed. Shall I generate the contract now?"

    @staticmethod
    def contract_generated_successfully():
        return "Your contract has been generated successfully. Would you like to review it or make any changes?"

    @staticmethod
    def goodbye_message():
        return "Thank you for using LegalContractBot. Goodbye!"

# Example usage
if __name__ == "__main__":
    responses = Responses()  # Instantiate the Responses class
    print(responses.welcome_message())  # Call the method on the instance
