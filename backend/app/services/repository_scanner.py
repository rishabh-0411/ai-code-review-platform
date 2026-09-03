from pathlib import Path
from app.services.detectors.language_detector import LanguageDetector
from app.services.detectors.framework_detector import FrameworkDetector


class RepositoryScanner:

    LANGUAGE_EXTENSIONS = {
        ".py": "Python",
        ".js": "JavaScript",
        ".ts": "TypeScript",
        ".java": "Java",
        ".cpp": "C++",
        ".c": "C",
        ".cs": "C#",
        ".go": "Go",
        ".rs": "Rust",
        ".php": "PHP",
        ".rb": "Ruby",
        ".swift": "Swift",
        ".kt": "Kotlin",
    }

    @classmethod
    def scan(cls, repository_path: str):

        path = Path(repository_path)

        return {
            "files": cls.count_files(path),
            "directories": cls.count_directories(path),
            "languages": LanguageDetector.detect(path),
            "frameworks": FrameworkDetector.detect(path),
        }

    @classmethod
    def count_files(cls, path: Path):

        return sum(
            1
            for item in path.rglob("*")
            if item.is_file()
        )

    @classmethod
    def count_directories(cls, path: Path):

        return sum(
            1
            for item in path.rglob("*")
            if item.is_dir()
        )

    @classmethod
    def detect_languages(cls, path: Path):

        languages = {}

        for file in path.rglob("*"):

            if not file.is_file():
                continue

            extension = file.suffix.lower()

            if extension in cls.LANGUAGE_EXTENSIONS:

                language = cls.LANGUAGE_EXTENSIONS[extension]

                languages[language] = (
                    languages.get(language, 0) + 1
                )

        return languages

    @classmethod
    def detect_frameworks(cls, path: Path):

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