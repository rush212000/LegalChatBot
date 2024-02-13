from .generator import ContractGenerator
from .manager import ContractManager
import os

# Get the absolute path to the directory where this __init__.py file is
current_dir = os.path.dirname(os.path.abspath(__file__))
TEMPLATES_DIR = os.path.join(current_dir, 'templates/')

# Example (uncomment if needed):
# Assuming that ContractManager and ContractGenerator can be initialized without additional parameters,
# or that they are okay to be initialized with just the path to the templates.
# contract_manager = ContractManager(TEMPLATES_DIR)
# contract_generator = ContractGenerator(TEMPLATES_DIR)

# Note: The above is just an example. Adjust the initialization based on your actual application needs.
