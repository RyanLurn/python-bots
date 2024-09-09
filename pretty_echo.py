from rich.console import Console

console = Console()

while True:
    user_input = console.input("[bold blue]You:[/bold blue] ")
    if user_input == "/exit":
        break
    console.print(f"[bold yellow]Pretty Echo:[/bold yellow] {user_input}")
