# dialogues/__init__.py

# Import the main components of the dialogues module so they can be easily accessed
# from other parts of the application.

from .context import DialogueContext
from .manager import DialogueManager
from .responses import generate_response

# Optionally, you can define __all__ to limit what gets imported with "from dialogues import *"
__all__ = ['DialogueContext', 'DialogueManager', 'generate_response']
