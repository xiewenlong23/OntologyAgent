import pytest
import tempfile
import os
from pathlib import Path

from ontology_agent.skills import Skill, SkillLoader


class TestSkillDataclass:
    def test_skill_creation(self):
        skill = Skill(
            name="test_skill",
            description="A test skill",
            skill_type="query",
            triggers=[{"intent": "test intent"}],
            content="# Test Content",
        )
        assert skill.name == "test_skill"
        assert skill.description == "A test skill"
        assert skill.skill_type == "query"
        assert skill.triggers == [{"intent": "test intent"}]
        assert skill.content == "# Test Content"


class TestSkillLoader:
    def test_load_skill_nonexistent_file(self, tmp_path):
        loader = SkillLoader(skills_dir=str(tmp_path))
        result = loader.load_skill("nonexistent.md")
        assert result is None

    def test_load_skill_invalid_markdown(self, tmp_path):
        # Create a markdown file without frontmatter
        invalid_file = tmp_path / "invalid.md"
        invalid_file.write_text("# Just a heading\n\nSome content without frontmatter")

        loader = SkillLoader(skills_dir=str(tmp_path))
        result = loader.load_skill("invalid.md")
        assert result is None

    def test_load_skill_valid(self, tmp_path):
        # Create a valid skill file
        skill_file = tmp_path / "test_skill.md"
        skill_file.write_text(
            """---
name: test_skill
description: Test description
type: query
triggers:
  - intent: "test intent"
---

# Test Skill Content

Some content here.
"""
        )

        loader = SkillLoader(skills_dir=str(tmp_path))
        skill = loader.load_skill("test_skill.md")

        assert skill is not None
        assert skill.name == "test_skill"
        assert skill.description == "Test description"
        assert skill.skill_type == "query"
        assert skill.triggers == [{"intent": "test intent"}]
        assert skill.content == "# Test Skill Content\n\nSome content here."

    def test_load_skill_defaults(self, tmp_path):
        # Create a skill file with minimal frontmatter
        skill_file = tmp_path / "minimal.md"
        skill_file.write_text(
            """---
name: minimal
---

# Minimal Skill
"""
        )

        loader = SkillLoader(skills_dir=str(tmp_path))
        skill = loader.load_skill("minimal.md")

        assert skill is not None
        assert skill.name == "minimal"
        assert skill.description == ""
        assert skill.skill_type == "workflow"  # default
        assert skill.triggers == []  # default
        assert skill.content == "# Minimal Skill"

    def test_load_all_empty_dir(self, tmp_path):
        loader = SkillLoader(skills_dir=str(tmp_path))
        skills = loader.load_all()
        assert skills == []

    def test_load_all_multiple_skills(self, tmp_path):
        # Create multiple skill files
        (tmp_path / "skill1.md").write_text(
            """---
name: skill1
description: First skill
type: query
triggers: []
---

# Skill 1
"""
        )
        (tmp_path / "skill2.md").write_text(
            """---
name: skill2
description: Second skill
type: workflow
triggers: []
---

# Skill 2
"""
        )
        (tmp_path / "notask.md").write_text("Not a skill file content")  # invalid, will be skipped

        loader = SkillLoader(skills_dir=str(tmp_path))
        skills = loader.load_all()

        assert len(skills) == 2
        skill_names = {s.name for s in skills}
        assert skill_names == {"skill1", "skill2"}

    def test_load_all_nonexistent_dir(self):
        loader = SkillLoader(skills_dir="/nonexistent/path")
        skills = loader.load_all()
        assert skills == []

    def test_get_system_prompt_injection(self, tmp_path):
        # Create skill files
        (tmp_path / "skill1.md").write_text(
            """---
name: skill_one
description: First skill
type: query
triggers: []
---

# Skill One Content
Some content for skill one.
"""
        )
        (tmp_path / "skill2.md").write_text(
            """---
name: skill_two
description: Second skill
type: workflow
triggers: []
---

## Skill Two Content
Content for the second skill.
"""
        )

        loader = SkillLoader(skills_dir=str(tmp_path))
        injection = loader.get_system_prompt_injection()

        assert "## Skill: skill_one" in injection
        assert "# Skill One Content" in injection
        assert "## Skill: skill_two" in injection
        assert "## Skill Two Content" in injection

    def test_get_system_prompt_injection_empty(self, tmp_path):
        loader = SkillLoader(skills_dir=str(tmp_path))
        injection = loader.get_system_prompt_injection()
        assert injection == ""
