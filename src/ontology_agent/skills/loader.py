import re
import yaml
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Skill:
    name: str
    description: str
    skill_type: str  # workflow, query, analysis
    triggers: list[str]
    content: str  # markdown body

class SkillLoader:
    def __init__(self, skills_dir: str = "skills"):
        self.skills_dir = Path(skills_dir)

    def load_skill(self, filename: str) -> Skill | None:
        filepath = self.skills_dir / filename
        if not filepath.exists():
            return None

        content = filepath.read_text()
        parts = content.split("---", 2)
        if len(parts) < 3:
            return None

        frontmatter = yaml.safe_load(parts[1])
        markdown_body = parts[2].strip()

        return Skill(
            name=frontmatter.get("name", ""),
            description=frontmatter.get("description", ""),
            skill_type=frontmatter.get("type", "workflow"),
            triggers=frontmatter.get("triggers", []),
            content=markdown_body,
        )

    def load_all(self) -> list[Skill]:
        skills = []
        if not self.skills_dir.exists():
            return skills
        for filepath in self.skills_dir.glob("*.md"):
            skill = self.load_skill(filepath.name)
            if skill:
                skills.append(skill)
        return skills

    def get_system_prompt_injection(self) -> str:
        skills = self.load_all()
        injections = []
        for skill in skills:
            injections.append(f"## Skill: {skill.name}\n\n{skill.content}")
        return "\n\n".join(injections)
