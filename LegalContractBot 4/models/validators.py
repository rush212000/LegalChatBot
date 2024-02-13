import re
from datetime import datetime
# Assuming NLPModel is your AI model for name validation
from nlp_model import NLPModel

def validate_name(name: str) -> bool:
    """
    Validates a name to ensure it contains only letters, spaces, and possibly hyphens.
    """
    pattern = r'^[A-Za-z\s\-]+$'
    if not re.match(pattern, name):
        return False
    # Further validation with NLP
    return NLPModel.validate_name(name)

def validate_date(date_str: str, date_format='%Y-%m-%d') -> bool:
    """
    Validates a date string to ensure it matches a given date format.
    """
    try:
        datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False

def validate_email(email: str) -> bool:
    """
    Validates an email address to ensure it follows a basic email pattern.
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def validate_phone_number(phone_number: str) -> bool:
    """
    Validates a phone number to ensure it follows a basic international pattern.
    """
    pattern = r'^\+?[\d\s\-]+$'
    return re.match(pattern, phone_number) is not None

def validate_party_name(name: str) -> bool:
    """
    Validates a party name, ensuring it meets basic length requirements and further NLP validation.
    """
    if len(name) < 2:
        raise ValueError("Name must be at least 2 characters long.")
    return NLPModel.validate_name(name)
