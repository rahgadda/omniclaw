import os
from dotenv import load_dotenv

class AppConfig:
    def __init__(self):
        load_dotenv()
        
        self.DEBUG_MODE = os.getenv('DEBUG_MODE', 'False').lower() in ('true', '1', 't')
        self.LOG_LEVEL = 'DEBUG' if self.DEBUG_MODE else 'INFO'
        self.GATEWAY_PORT = os.getenv('GATEWAY_PORT', 8585)
        self.UI_PORT = os.getenv('UI_PORT', 80)
        self.DB_STORAGE = os.getenv('DB_STORAGE', 'file')
        self.OMNICLAW_HOME = os.getenv('OMNICLAW_HOME')
        self.CHROME_PROFILE_DIR = os.getenv('CHROME_PROFILE_DIR')