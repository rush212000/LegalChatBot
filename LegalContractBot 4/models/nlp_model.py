import spacy

class NLPModel:
    def __init__(self):
        # Load the spaCy model, assuming English for this example
        self.nlp = spacy.load('en_core_web_sm')

    def validate_name(self, name: str) -> bool:
        """
        Validates a name using NLP to check if it is likely to be a proper noun.
        """
        doc = self.nlp(name)
        # Return True if the name is a proper noun
        return any(token.pos_ == 'PROPN' for token in doc)

    def summarize_text(self, text: str) -> str:
        """
        Summarizes the given text to its most important sentences.
        """
        doc = self.nlp(text)
        # For simplicity, we'll return the first sentence as a "summary"
        return next(doc.sents).text

# Example usage
if __name__ == "__main__":
    nlp_model = NLPModel()
    name = "John Doe"
    is_valid_name = nlp_model.validate_name(name)
    print(f"Is '{name}' a valid name? {is_valid_name}")

    text = "Your long text here..."
    summary = nlp_model.summarize_text(text)
    print(f"Summary: {summary}")
