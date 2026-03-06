"""CLI entry point for ai-scaffolding."""

import os

import click

from aiscaffold.generator import generate_files
from aiscaffold.prompts import ask_user_choices


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    """AI Scaffolding - Generate AI coding rules for your projects."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.option("--output-dir", default=".", help="Directory to generate files in.")
@click.option("--dry-run", is_flag=True, help="Preview files without creating them.")
def init(output_dir, dry_run):
    """Scaffold AI rule files for your project."""
    choices = ask_user_choices()

    project_name = os.path.basename(os.path.abspath(output_dir))

    click.echo("")
    click.echo("=== Configuracao selecionada ===")
    click.echo(f"  IAs: {', '.join(choices['ais'])}")
    click.echo(f"  Linguagem: {choices['language']}")
    click.echo(f"  Nivel de processo: {choices['process_level']}")
    click.echo(f"  Idioma das regras: {choices['rules_lang']}")
    click.echo("")

    results = generate_files(
        output_dir=output_dir,
        ais=choices["ais"],
        language=choices["language"],
        process_level=choices["process_level"],
        project_name=project_name,
        rules_lang=choices["rules_lang"],
        dry_run=dry_run,
    )

    if dry_run:
        click.echo("Dry run - arquivos que seriam gerados:")
        for r in results:
            if r["status"] == "would_create":
                click.echo(f"  [criar] {r['path']}")
            elif r["status"] == "skipped":
                click.echo(f"  [ja existe] {r['path']}")
    else:
        created = [r for r in results if r["status"] == "created"]
        if created:
            click.echo("Arquivos gerados:")
            for r in created:
                click.echo(f"  {r['path']}")
        else:
            click.echo("Nenhum arquivo novo gerado (arquivos ja existem).")
