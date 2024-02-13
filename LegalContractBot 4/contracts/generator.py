import os
import logging
import openai
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file
openai.api_key = os.getenv('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')  # Get the OpenAI API key from an environment variable

class ContractGenerator:

    def __init__(self, templates_dir='templates'):
        self.templates_dir = templates_dir
    def fill_template(self, template_content, details):
        """Fills in the template content with the provided details.

        Args:
            template_content (str): The contract template as a string.
            details (dict): A dictionary containing the details to fill into the template.

        Returns:
            str: The filled contract.
        """
        for key, value in details.items():
            placeholder = f"{{{{ {key} }}}}"  # Assuming placeholders in the template look like {{ key }}
            template_content = template_content.replace(placeholder, value)
        return template_content

    def load_template(self, template_name):
        """Load a contract template from the specified directory."""
        try:
            with open(os.path.join(self.templates_dir, template_name), 'r') as file:
                return file.read()
        except FileNotFoundError as e:
            logging.error(f"Template {template_name} not found in {self.templates_dir}. Error: {e}")
            raise

    def generate_contract(self, template_name, context):
        # Load the template content
        try:
            template_content = self.load_template(template_name)
        except FileNotFoundError:
            logging.error(f"Template file {template_name} not found.")
            return None

        # Fill the template using GPT-3
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=template_content.format(**context),
                temperature=0.7,
                max_tokens=2048,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            filled_content = response.choices[0].text.strip()
            return filled_content
        except openai.error.OpenAIError as e:
            logging.error(f"Error in generating contract using OpenAI: {e}")
            return None