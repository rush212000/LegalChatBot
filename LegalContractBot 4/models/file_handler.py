import os
from models.logger import logger
# Assuming AIContentGenerator and AIDocumentSummarizer are classes you've developed or integrated for AI tasks
from ai_utils import AIContentGenerator, AIDocumentSummarizer

class FileHandler:
    @staticmethod
    def read_file(file_path):
        content = ''
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        # Example of integrating document summarization on read
        summary = AIDocumentSummarizer.summarize(content)
        return summary

    @staticmethod
    def write_file(file_path, content):
        # Example of refining content before write
        refined_content = AIContentGenerator.refine_content(content)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(refined_content)

    @staticmethod
    def write_contract(contract_name, content):
        directory = '/path/to/generated_contracts'
        # AI to suggest a file name based on content
        suggested_name = AIContentGenerator.suggest_file_name(content)
        file_path = f'{directory}/{suggested_name}.txt'
        try:
            os.makedirs(directory, exist_ok=True)
            FileHandler.write_file(file_path, content)  # Using the updated write_file method
            logger.info(f"Contract successfully saved to {file_path}")
        except Exception as e:
            logger.error(f"An error occurred while writing the contract: {e}")
            raise
