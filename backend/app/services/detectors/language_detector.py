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
    def detect(cls, index):

        languages = {}

        for file in index["files"]:

            extension = file.suffix.lower()

            if extension in cls.LANGUAGE_EXTENSIONS:

                language = cls.LANGUAGE_EXTENSIONS[extension]

                languages[language] = (
                    languages.get(language, 0) + 1
                )

        return languages