from pathlib import Path


class DocumentationDetector:

    @classmethod
    def detect(cls, path: Path):

        return {
            "readme": (path / "README.md").exists(),
            "license": (path / "LICENSE").exists(),
            "contributing": (path / "CONTRIBUTING.md").exists(),
        }