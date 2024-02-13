import os


class Config:
    # Basic settings
    BOT_NAME = "LegalContractBot"
    VERSION = "1.0"
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    TEMPLATE_DIR = os.path.join(BASE_DIR, 'contracts', 'templates')

    # Logging settings
    LOGGING_LEVEL = "INFO"
    LOG_FILE = os.path.join(BASE_DIR, 'logs', 'bot.log')


    # Database settings
    DATABASE_URI = os.path.join(BASE_DIR, 'database', 'legalcontracts.db')

    # Security settings
    SECRET_KEY = os.getenv("SECRET_KEY")  # No default value to enforce setting via environment
    AI_API_KEY = os.getenv("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")  # No default value for security
    AI_ENDPOINT = "https://api.openai.com"

    # Resource allocation
    MAX_MEMORY_USAGE = "4GB"  # This is illustrative; actual enforcement needs to be implemented
    CPU_LIMIT = 2  # This is illustrative; actual enforcement needs to be implemented


class DevelopmentConfig(Config):
    DEBUG = True
    LOGGING_LEVEL = "DEBUG"


class ProductionConfig(Config):
    DEBUG = False
    LOGGING_LEVEL = "WARNING"


# Dynamic configuration selection
env = os.getenv('ENVIRONMENT', 'development').lower()
config = DevelopmentConfig() if env == 'development' else ProductionConfig()
