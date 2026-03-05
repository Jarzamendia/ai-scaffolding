"""CLI entry point for ai-scaffolding."""

import os

import click

from ai_scaffolding.generator import generate_files
from ai_scaffolding.prompts import ask_user_choices


@click.group()
def main():
    """AI Scaffolding - Generate AI coding rules for your projects."""
    pass


@main.command()
@click.option("--output-dir", default=".", help="Directory to generate files in.")
def init(output_dir):
    """Scaffold AI rule files for your project."""
    choices = ask_user_choices()

    project_name = os.path.basename(os.path.abspath(output_dir))

    click.echo("")
    click.echo("=== Configuracao selecionada ===")
    click.echo(f"  IAs: {', '.join(choices['ais'])}")
    click.echo(f"  Linguagem: {choices['language']}")
    click.echo(f"  Nivel de processo: {choices['process_level']}")
    click.echo("")

    created = generate_files(
        output_dir=output_dir,
        ais=choices["ais"],
        language=choices["language"],
        process_level=choices["process_level"],
        project_name=project_name,
    )

    if created:
        click.echo("Arquivos gerados:")
        for f in created:
            click.echo(f"  {f}")
    else:
        click.echo("Nenhum arquivo novo gerado (arquivos ja existem).")
