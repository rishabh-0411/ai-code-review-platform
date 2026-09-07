from pathlib import Path

from fastapi import HTTPException


class PathValidator:

    BASE_DIRECTORY = Path("temp").resolve()

    @classmethod
    def validate_repository_path(cls, repository_path: str) -> Path:

        path = Path(repository_path).resolve()

        try:
            path.relative_to(cls.BASE_DIRECTORY)
        except ValueError:
            raise HTTPException(
                status_code=403,
                detail="Access to the requested directory is not allowed.",
            )

        if not path.exists():
            raise HTTPException(
                status_code=404,
                detail="Repository not found.",
            )

        if not path.is_dir():
            raise HTTPException(
                status_code=400,
                detail="Repository path must be a directory.",
            )

        return path