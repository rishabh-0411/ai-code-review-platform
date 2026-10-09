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
    }

    @classmethod
    def build_index(cls, repository_path: str) -> dict[str, Any]:

        root = Path(repository_path)

        files = []
        directories = []

        for item in root.rglob("*"):

            # Only check the path relative to the repository root
            relative_parts = item.relative_to(root).parts

            if any(part in cls.IGNORE_DIRECTORIES for part in relative_parts):
                continue

            if item.is_dir():
                directories.append(item)
            else:
                files.append(item)
        print("\n========== INDEXER ==========")
        print("Files:", len(files))
        print("Directories:", len(directories))

        for file in files[:20]:
            print(file)

        print("=============================\n")
        return {
            "root": root,
            "files": files,
            "directories": directories,
        }
