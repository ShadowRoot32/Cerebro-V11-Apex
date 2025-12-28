from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich import box

class TacticalHUD:
    def __init__(self):
        self.console = Console()

    def show_banner(self):
        # Menggunakan raw string untuk menghindari MarkupError
        banner_text = r"""
 ██████╗███████╗██████╗ ███████╗██████╗ ██████╗  ██████╗ 
██╔════╝██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔═══██╗
██║     █████╗  ██████╔╝█████╗  ██████╔╝██████╔╝██║   ██║
██║     ██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██║   ██║
╚██████╗███████╗██║  ██║███████╗██║  ██║██║  ██║╚██████╔╝
 ╚═════╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ 
        -- NEURAL VULNERABILITY INTERCEPTOR V11 --
        """
        self.console.print(Panel(banner_text, style="bold red", box=box.DOUBLE))
        self.console.print("[bold green]       [ STATUS: NEURAL ENGINE ONLINE / PORT 8080 ] [/bold green]\n")

    def show_intercept_notif(self, domain, method):
        self.console.print(f"[bold red]>>>[/bold red] [bold white]LOCK ON:[/bold white] [cyan]{domain}[/cyan] | [yellow]{method}[/yellow] [bold green][NEURAL INTERCEPT][/bold green]")

    def generate_layout(self, target, tech, lvl, status, logs):
        layout = Layout()
        layout.split_column(
            Layout(name="top", size=3),
            Layout(name="mid", ratio=1),
            Layout(name="bot", size=3)
        )
        layout["top"].update(Panel(f"[bold cyan]AI-SCAN:[/bold cyan] {target}", border_style="red"))
        table = Table(expand=True, box=box.SIMPLE, border_style="red")
        table.add_column("NEURAL LOG FEED", style="white")
        for log in logs[-10:]: table.add_row(log)
        layout["mid"].update(table)
        layout["bot"].update(Panel(f"[bold yellow]OTAK:[/bold yellow] {tech} | [bold green]STATUS:[/bold green] {status} | [bold red]MODE:[/bold red] {lvl}", border_style="white"))
        return layout