import backend.src.utils.appConfig as AppConfig
import backend.src.utils.logger as Logger

def printConfig() -> None:
    try:
        config = AppConfig.AppConfig()
        # Log the environment values
        print("\n########## Application Configuration ##########")
        print(f"1. Debug Mode:       {config.debug_mode}")
        print(f"2. Log Level:        {config.log_level}")
        print(f"3. Gateway Port:     {config.GATEWAY_PORT}")
        print(f"4. UI Port:          {config.UI_PORT}")
        print(f"5. DB Storage:       {config.DB_STORAGE}")
        print("###############################################\n")
    except Exception as e:
        print(f"Error loading configuration: {e}")
        return  

logger = None

def main() -> None:
    global logger

    try:
        printConfig()
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