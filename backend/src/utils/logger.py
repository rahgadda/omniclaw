import logging
import sys
from uvicorn.logging import DefaultFormatter
import backend.src.utils.app_config as AppConfig


class ColoredLevelFormatter(DefaultFormatter):
    COLOR_RESET = "\033[0m"
    LEVEL_COLORS = {
        logging.DEBUG: "\033[33m",
        logging.INFO: "\033[32m",
        logging.ERROR: "\033[31m",
        logging.CRITICAL: "\033[31m",
    }

    def format(self, record: logging.LogRecord) -> str:
        levelname = record.levelname
        msg = record.msg
        color = self.LEVEL_COLORS.get(record.levelno)

        if color:
            record.levelname = f"{color}{levelname}{self.COLOR_RESET}"
            record.msg = f"{color}{record.getMessage()}{self.COLOR_RESET}"

        try:
            return super().format(record)
        finally:
            record.levelname = levelname
            record.msg = msg


logger = logging.getLogger(__name__)

def setup_logging() -> logging.Logger:
    """
    Setup the logging configuration for the application. 
    """          

    config = AppConfig.AppConfig()
    debug=config.DEBUG_MODE

    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    logger.propagate = False

    # Remove all existing handlers to prevent accumulation
    for handler in logger.handlers:
        logger.removeHandler(handler)

    handlers = []
           
    # Create a new handler
    try:
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG if debug else logging.INFO)
        formatter = ColoredLevelFormatter("%(levelname)s %(message)s", use_colors=False)
        handler.setFormatter(formatter)
        handlers.append(handler)
    except Exception as e:
        print(f"Failed to create stdout log handler: {e}", file=sys.stderr)

    # Add the handlers to the logger
    for handler in handlers:
        logger.addHandler(handler)
    
    return logger