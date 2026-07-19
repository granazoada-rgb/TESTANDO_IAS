from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()

# OLA]

class Calc:
    def somar(self, a: float, b: float) -> float:
        return a + b

    def subtrair(self, a: float, b: float) -> float:
        return a - b

    def multiplicar(self, a: float, b: float) -> float:
        return a * b

    def dividir(self, a: float, b: float) -> float:
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


if __name__ == "__main__":
    c = Calc()
    
    # Painel de título
    console.print(Panel.fit(
        "[bold cyan]Calculadora com Rich[/bold cyan]",
        border_style="cyan"
    ))
    
    # Tabela de operações
    table = Table(title="Operações", show_header=True, header_style="bold magenta")
    table.add_column("Operação", style="cyan", justify="center")
    table.add_column("Expressão", style="yellow", justify="center")
    table.add_column("Resultado", style="green", justify="center")
    
    table.add_row("Soma", "2 + 3", str(c.somar(2, 3)))
    table.add_row("Subtração", "5 - 2", str(c.subtrair(5, 2)))
    table.add_row("Multiplicação", "4 × 3", str(c.multiplicar(4, 3)))
    table.add_row("Divisão", "10 ÷ 2", str(c.dividir(10, 2)))
    
    console.print(table)
    
    # Exemplo de erro formatado
    console.print()
    console.print(Panel(
        "[red]Erro ao dividir por zero:[/red]\n"
        "[yellow]ValueError: Divisão por zero não é permitida.[/yellow]",
        title="[bold red]Exceção[/bold red]",
        border_style="red"
    ))



