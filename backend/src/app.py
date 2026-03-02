import backend.src.utils.AppConfig as AppConfig

def print_config() -> None:
    config = AppConfig.AppConfig()

    # Log the environment values
    print("\n########## Application Configuration ##########")
    print(f"1. Debug Mode:       {config.debug_mode}")
    print(f"2. Log Level:        {config.log_level}")
    print(f"3. Gateway Port:     {config.GATEWAY_PORT}")
    print(f"4. UI Port:          {config.UI_PORT}")
    print(f"5. DB Storage:       {config.DB_STORAGE}")
    print("###############################################\n")

def main() -> None:
    print_config()

if __name__ == "__main__":
    main()