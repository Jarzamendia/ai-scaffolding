"""Interactive prompts for user choices."""

import questionary

AI_CHOICES = [
    "Claude Code",
    "Cursor",
    "Codex",
]

LANGUAGE_CHOICES = [
    "Python",
    "Node.js",
]

PROCESS_LEVEL_CHOICES = [
    "Pipeline completa (TDD + boas praticas + fronteiras arquiteturais)",
    "Apenas testes (TDD enforcement)",
    "Apenas boas praticas (estilo, convencoes, minimal changes)",
    "Minimo (apenas arquivo base da IA)",
]

RULES_LANG_CHOICES = [
    "Português (Brasil)",
    "English",
]


def _rules_lang_to_code(choice: str) -> str:
    """Map display choice to rules_lang code."""
    return "en-US" if choice == "English" else "pt-BR"


def ask_user_choices() -> dict:
    """Ask the user for AI, language, and process level choices."""
    ais = questionary.checkbox(
        "Quais IAs voce pretende usar?",
        choices=AI_CHOICES,
        validate=lambda x: len(x) > 0 or "Selecione ao menos uma IA.",
    ).ask()

    if ais is None:
        raise KeyboardInterrupt

    language = questionary.select(
        "Qual linguagem do projeto?",
        choices=LANGUAGE_CHOICES,
    ).ask()

    if language is None:
        raise KeyboardInterrupt

    process_level = questionary.select(
        "Qual nivel de processo?",
        choices=PROCESS_LEVEL_CHOICES,
    ).ask()

    if process_level is None:
        raise KeyboardInterrupt

    rules_lang_choice = questionary.select(
        "Em qual idioma devem ser geradas as regras?",
        choices=RULES_LANG_CHOICES,
    ).ask()

    if rules_lang_choice is None:
        raise KeyboardInterrupt

    return {
        "ais": ais,
        "language": language,
        "process_level": process_level,
        "rules_lang": _rules_lang_to_code(rules_lang_choice),
    }
