import os
from dotenv import load_dotenv

class AppConfig:
    def __init__(self):
        load_dotenv()
        
        self.debug_mode = os.getenv('DEBUG_MODE', 'False').lower() in ('true', '1', 't')
        self.log_level = os.getenv('LOG_LEVEL', 'DEBUG')
        self.GATEWAY_PORT = os.getenv('GATEWAY_PORT', 8585)
        self.UI_PORT = os.getenv('UI_PORT', 80)
        self.DB_STORAGE = os.getenv('DB_STORAGE', 'file')