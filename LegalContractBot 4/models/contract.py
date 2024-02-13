# models/contracts.py

class Contract:
    def __init__(self, contract_type, party_one, party_two, details=None):
        """
        Initialize a new Contract object.

        :param contract_type: String indicating the type of contract (e.g., 'NDA', 'Lease Agreement').
        :param party_one: String representing the first party involved in the contract.
        :param party_two: String representing the second party involved in the contract.
        :param details: Dictionary containing other details of the contract.
        """
        self.contract_type = contract_type
        self.party_one = party_one
        self.party_two = party_two
        self.details = details if details is not None else {}

    def fill_details(self, template):
        """
        Fill in the contract's details into a given template.

        :param template: String containing the contract template with placeholders.
        :return: String with placeholders in the template replaced with contract details.
        """
        filled_template = template.format(
            contract_type=self.contract_type,
            party_one=self.party_one,
            party_two=self.party_two,
            **self.details
        )
        return filled_template

    def __str__(self):
        """
        String representation of the Contract object.
        """
        return f"Contract Type: {self.contract_type}, Party One: {self.party_one}, Party Two: {self.party_two}, Details: {self.details}"


# Example usage
if __name__ == "__main__":
    # Example contract details and template
    contract_details = {
        "effective_date": "2024-01-01",
        "termination_date": "2025-01-01",
        "jurisdiction": "New York"
    }
    contract_template = """
    Contract Type: {contract_type}
    This agreement is made between {party_one} and {party_two} effective as of {effective_date}.
    This agreement shall terminate on {termination_date}.
    Governing Law: {jurisdiction}
    """

    # Creating a contract object
    contract = Contract(
        contract_type="NDA Agreement",
        party_one="Company A",
        party_two="Company B",
        details=contract_details
    )

    # Filling the template with contract details
    filled_contract = contract.fill_details(contract_template)
    print(filled_contract)
