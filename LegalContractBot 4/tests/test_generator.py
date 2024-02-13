import pytest
from contracts.generator import ContractGenerator

# Sample data for testing
user_input_sample = {
    "contract_type": "employment_contract",
    "party_one": "Company ABC",
    "party_two": "John Doe",
    "effective_date": "2024-01-01",
    "job_title": "Software Developer",
    "job_description": "Develop and maintain software applications.",
    "salary": "100000"
}

# Expected output for the test sample
expected_output_snippet = "This Employment Agreement is made effective as of 2024-01-01, between Company ABC and John Doe."


@pytest.fixture
def generator():
    # Setup code for contract generator instance
    return ContractGenerator()


def test_contract_generation(generator):
    # Generate the contract based on sample user input
    generated_contract = generator.generate_contract(user_input_sample)

    # Test if the generated contract contains the expected output snippet
    assert expected_output_snippet in generated_contract, "The contract generation did not produce the expected output."


def test_invalid_contract_type(generator):
    # Test handling of invalid contract types
    invalid_input = user_input_sample.copy()
    invalid_input['contract_type'] = 'invalid_type'

    with pytest.raises(ValueError) as excinfo:
        generator.generate_contract(invalid_input)

    assert "Invalid contract type" in str(
        excinfo.value), "The generator did not handle an invalid contract type as expected."

# You can add more tests here to cover different scenarios,
# such as missing required fields, invalid input formats, etc.

