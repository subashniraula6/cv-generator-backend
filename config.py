import os

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
