# contracts/manager.py

import os
from .generator import ContractGenerator
from utils.ai_utils import select_best_template, generate_custom_contract

class ContractManager:
    def __init__(self, templates_dir='templates'):
        self.templates_dir = templates_dir
        self.generator = ContractGenerator()

    def generate_contract(self, contract_type, details):
        """
        Generates a contract intelligently based on the contract type and details provided.
        Uses AI to select the best template and generate custom content.
        """
        best_template_name = select_best_template(details, self.list_templates())
        template_content = self.get_template_content(best_template_name)
        filled_contract = generate_custom_contract(template_content, details)
        return filled_contract

    def get_template_content(self, template_name):
        """Retrieves the content of a specific contract template."""
        template_path = os.path.join(self.templates_dir, f"{template_name}.txt")
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Template '{template_name}' not found.")
        with open(template_path, 'r', encoding='utf-8') as file:
            return file.read()

    def list_templates(self):
        """List all available contract templates."""
        return [f.replace('.txt', '') for f in os.listdir(self.templates_dir) if f.endswith('.txt')]
