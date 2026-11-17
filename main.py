from scraper import extract_article
from rich.console import Console
from rich.panel import Panel

console = Console()


def main():
    console.print(
        Panel("Distraction-Free News Reader\nType 'exit' to quit", style="bold blue")
    )

    while True:
        url = console.input("\n[bold green]Masukkan URL artikel[/bold green]: ").strip()

        # Check exit command
        if url.lower() in ["exit", "quit"]:
            console.print(
                "\n[bold yellow]Program dihentikan. Terima kasih![/bold yellow]"
            )
            break

        if not url:
            console.print("[bold red]URL tidak boleh kosong![/bold red]")
            continue

        try:
            console.print("\n[bold yellow]Mengambil artikel...[/bold yellow]")

            title, article = extract_article(url)

            # Display article title and content
            console.print(
                Panel(
                    f"[bold]{title}[/bold]\n\n{article}",
                    title="Article Content",
                    border_style="green",
                )
            )

        except Exception as error:
            console.print(f"[bold red]Error:[/bold red] {error}")


if __name__ == "__main__":
    main()
