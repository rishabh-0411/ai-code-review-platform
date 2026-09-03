from pathlib import Path


class FrameworkDetector:

    @classmethod
    def detect(cls, path: Path):

        frameworks = []

        requirements = path / "requirements.txt"

        if requirements.exists():

            content = requirements.read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "fastapi" in content:
                frameworks.append("FastAPI")

            if "django" in content:
                frameworks.append("Django")

            if "flask" in content:
                frameworks.append("Flask")

        package_json = path / "package.json"

        if package_json.exists():

            content = package_json.read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "\"react\"" in content:
                frameworks.append("React")

            if "\"next\"" in content:
                frameworks.append("Next.js")

        pom = path / "pom.xml"

        if pom.exists():

            content = pom.read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "spring-boot" in content:
                frameworks.append("Spring Boot")

        return frameworks