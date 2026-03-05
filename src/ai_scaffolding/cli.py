"""CLI entry point for ai-scaffolding."""

import click

from ai_scaffolding.prompts import ask_user_choices


@click.group()
def main():
    """AI Scaffolding - Generate AI coding rules for your projects."""
    pass


@main.command()
def init():
    """Scaffold AI rule files for your project."""
    choices = ask_user_choices()

    click.echo("")
    click.echo("=== Configuracao selecionada ===")
    click.echo(f"  IAs: {', '.join(choices['ais'])}")
    click.echo(f"  Linguagem: {choices['language']}")
    click.echo(f"  Nivel de processo: {choices['process_level']}")
    click.echo("")
