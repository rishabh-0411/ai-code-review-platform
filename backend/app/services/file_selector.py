from pathlib import Path


class FileSelector:

    IMPORTANT_FILES = {
        "main.py",
        "app.py",
        "api.py",
        "models.py",
        "schemas.py",
        "database.py",
        "config.py",
        "settings.py",
        "requirements.txt",
        "package.json",
        "Dockerfile",
        "docker-compose.yml",
        "docker-compose.yaml",
    }

    IMPORTANT_DIRECTORIES = {
        "app",
        "src",
        "backend",
        "frontend",
        "services",
        "api",
        "routes",
    }

    CODE_EXTENSIONS = {
        ".py",
        ".js",
        ".ts",
        ".tsx",
        ".jsx",
        ".java",
        ".cpp",
        ".c",
        ".go",
        ".rs",
    }

    @classmethod
    def select_files(cls, index: dict) -> list[Path]:

        selected = []

        for file in index["files"]:

            if file.name in cls.IMPORTANT_FILES:
                selected.append(file)
                continue

            if file.suffix.lower() in cls.CODE_EXTENSIONS:
                selected.append(file)

        return selected