"""Tharun++ CLI Application"""

import typer
from pathlib import Path
from Tharunpp.core.interpreter import Interpreter, TharunppError

app = typer.Typer()


@app.command("run-file")
def run_file(file_path: str):
    """Run a Tharun++ program from a file"""
    try:
        path = Path(file_path)
        if not path.exists():
            typer.echo(f"Error: File '{file_path}' not found", err=True)
            raise typer.Exit(1)
        
        code = path.read_text()
        interpreter = Interpreter()
        interpreter.run(code)
    except TharunppError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)


@app.command("shell")
def shell():
    """Start an interactive Tharun++ shell"""
    typer.echo("Tharun++ Interactive Shell")
    typer.echo("Type 'exit' to quit")
    typer.echo("")
    
    interpreter = Interpreter()
    
    while True:
        try:
            line = input(">>> ")
            if line.strip().lower() == "exit":
                break
            if line.strip():
                # Wrap in program structure for single line execution
                wrapped = f"VANAKKAM DA MAPLA\n{line}\nNANDRI VANNAKAM"
                interpreter.run(wrapped)
        except EOFError:
            break
        except TharunppError as e:
            typer.echo(f"Error: {e}", err=True)
        except KeyboardInterrupt:
            typer.echo("\nKeyboardInterrupt")
            break


@app.command("tokenize")
def tokenize(file_path: str):
    """Tokenize a Tharun++ program and show the parse tree"""
    try:
        path = Path(file_path)
        if not path.exists():
            typer.echo(f"Error: File '{file_path}' not found", err=True)
            raise typer.Exit(1)
        
        code = path.read_text()
        interpreter = Interpreter()
        parser = interpreter._get_parser()
        tree = parser.parse(code)
        typer.echo(tree.pretty())
    except TharunppError as e:
        typer.echo(f"Error: {e}", err=True)
        raise typer.Exit(1)
    except Exception as e:
        typer.echo(f"Parse Error: {e}", err=True)
        raise typer.Exit(1)


@app.command("version")
def version():
    """Show Tharun++ version"""
    typer.echo("Tharun++ version 1.0.0")


if __name__ == "__main__":
    app()
