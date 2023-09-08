import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Your other configuration settings here

    # Define the path to the private keys
    PRIVATE_KEY_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'private_keys')

    # Example function to read a private key from a file
    @staticmethod
    def get_private_key(filename):
        private_key_path = os.path.join(Config.PRIVATE_KEY_DIR, filename)
        with open(private_key_path, 'r') as file:
            private_key = file.read()
        return private_key
    
    @staticmethod
    def firebase_private_key_file(filename):
        private_key_path = os.path.join(Config.PRIVATE_KEY_DIR, filename)
        return (private_key_path)
    
    @staticmethod
    def mySQL_config():
        config = {
            "db_host" : os.getenv('DB_HOST'),
            "db_port" : os.getenv('DB_PORT'),
            "db_name" : os.getenv('DB_NAME'),
            "db_user" : os.getenv('DB_USER'),
            "db_password" : os.getenv('DB_PASSWORD'),
        }
        return config

    @staticmethod
    def mySQL_alchemy_config():
        config = {
        "DATABASE_URI" :  'mysql+pymysql://root:admin@localhost/kneg',
        "TRACK_MODIFICATIONS" :  False
        }
        return config

    @staticmethod
    def openAI_config():
        config = {
            "API_KEY": os.getenv('OPENAI_API_KEY'),
            "password": os.getenv('PASSWORD'),
        }
        return config

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False
    # Other production settings here

# Map configuration names to actual configurations
config_by_name = dict(
    development=DevelopmentConfig,
    production=ProductionConfig
)
