from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich import box

from pyfiglet import Figlet
from colorama import init

import backend.src.utils.app_config as AppConfig

init()
console = Console()

ORANGE = "\033[38;5;166m"
RESET = "\033[0m"


def display_welcome_message() -> None:
    console.clear()

    banner = Figlet(font="standard").renderText("OmniClawPA")
    print(ORANGE + banner + RESET)

    config = AppConfig.AppConfig()

    table = Table(
        show_header=True,
        header_style="bold white",   # Header bold white
        border_style="white",
        box=box.SIMPLE_HEAVY,
        expand=True
    )

    table.add_column("Setting", style="white", justify="left")
    table.add_column("Value", style="white", justify="right")

    table.add_row("OmniClawPA Home", str(config.OMNICLAW_HOME))
    table.add_row("Debug Mode", str(config.DEBUG_MODE))
    table.add_row("Gateway Port", str(config.GATEWAY_PORT))
    table.add_row("UI Port", str(config.UI_PORT))
    table.add_row("DB Storage", str(config.DB_STORAGE))
    table.add_row("Chrome Profile Dir", str(config.CHROME_PROFILE_DIR))

    panel = Panel(
        table,
        title="[bold dark_orange3]App Configuration[/bold dark_orange3]",
        border_style="dark_orange3",
        box=box.ROUNDED,
        padding=(1, 2),
    )

    console.print(panel)