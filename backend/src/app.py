import backend.src.utils.app_config as AppConfig
import backend.src.utils.logger as Logger
from backend.src.cli.cli import display_welcome_message

logger = None

def main() -> None:
    global logger

    try:
        display_welcome_message()
    except Exception as e:
        return    

    try:
        logger = Logger.setup_logging()
    except Exception as e:
        print(f"Error setting up logging: {e}")
        return
    
    logger.debug("Starting application...")

    logger.debug("Stopping application...")

if __name__ == "__main__":
    main()