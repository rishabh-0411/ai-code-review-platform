from pathlib import Path
from typing import Any


class RepositoryIndexer:

    IGNORE_DIRECTORIES = {
        ".git",
        ".venv",
        "__pycache__",
        "node_modules",
        ".idea",
        ".vscode",
        "build",
        "dist",
        "temp"
    }

    @classmethod
    def build_index(cls, repository_path: str) -> dict[str, Any]:

        root = Path(repository_path)

        files = []
        directories = []

        for item in root.rglob("*"):

            if any(part in cls.IGNORE_DIRECTORIES for part in item.parts):
                continue

            if item.is_dir():
                directories.append(item)
            else:
                files.append(item)

        return {
            "root": root,
            "files": files,
            "directories": directories,
        }