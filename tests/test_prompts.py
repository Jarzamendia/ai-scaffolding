from aiscaffold.prompts import (
    AI_CHOICES,
    LANGUAGE_CHOICES,
    PROCESS_LEVEL_CHOICES,
    RULES_LANG_CHOICES,
)


class TestChoicesDefinitions:
    def test_ai_choices_contains_claude(self):
        assert "Claude Code" in AI_CHOICES

    def test_ai_choices_contains_cursor(self):
        assert "Cursor" in AI_CHOICES

    def test_ai_choices_contains_codex(self):
        assert "Codex" in AI_CHOICES

    def test_language_choices_contains_python(self):
        assert "Python" in LANGUAGE_CHOICES

    def test_language_choices_contains_node(self):
        assert "Node.js" in LANGUAGE_CHOICES

    def test_process_levels_has_full_pipeline(self):
        assert any("Pipeline completa" in level for level in PROCESS_LEVEL_CHOICES)

    def test_process_levels_has_tests_only(self):
        assert any("Apenas testes" in level for level in PROCESS_LEVEL_CHOICES)

    def test_process_levels_has_best_practices_only(self):
        assert any("Apenas boas praticas" in level for level in PROCESS_LEVEL_CHOICES)

    def test_process_levels_has_minimum(self):
        assert any("Minimo" in level for level in PROCESS_LEVEL_CHOICES)

    def test_rules_lang_choices_contains_english(self):
        assert "English" in RULES_LANG_CHOICES

    def test_rules_lang_choices_contains_portuguese(self):
        assert any("Português" in choice for choice in RULES_LANG_CHOICES)
