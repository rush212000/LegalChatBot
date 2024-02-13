import pytest
from utils.validators import validate_email, validate_date

# Test cases for validate_email function
@pytest.mark.parametrize("email,expected", [
    ("test@example.com", True),
    ("invalid-email.com", False),
    ("user@domain", False),
    ("user.name+tag@domain.com", True)
])
def test_validate_email(email, expected):
    """Test email validation with various inputs."""
    assert validate_email(email) == expected, f"Email validation failed for {email}"

# Test cases for validate_date function
@pytest.mark.parametrize("date_input,expected", [
    ("2023-01-01", True),
    ("01-01-2023", False),  # Assuming the expected format is YYYY-MM-DD
    ("2023/01/01", False),
    ("not-a-date", False),
    ("2023-02-29", False),  # An invalid date, since 2023 is not a leap year
])
def test_validate_date(date_input, expected):
    """Test date validation with various inputs."""
    assert validate_date(date_input) == expected, f"Date validation failed for {date_input}"

