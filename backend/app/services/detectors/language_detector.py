from pathlib import Path


class LanguageDetector:

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
    def detect(cls, path: Path):

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