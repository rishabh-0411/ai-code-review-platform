from pathlib import Path
import shutil
import logging
import uuid

from fastapi import HTTPException
from git import Repo, GitCommandError


logger = logging.getLogger(__name__)


class GitHubService:
    """
    Handles cloning GitHub repositories.
    """

    TEMP_DIR = Path("temp")

    @classmethod
    def clone_repository(cls, repo_url: str) -> dict:

        if not repo_url.startswith(("https://github.com/", "http://github.com/")):
            raise HTTPException(
                status_code=400,
                detail="Only GitHub repository URLs are supported.",
            )

        cls.TEMP_DIR.mkdir(exist_ok=True)

        repo_name = repo_url.rstrip("/").split("/")[-1]

        destination = cls.TEMP_DIR / f"{repo_name}_{uuid.uuid4().hex[:8]}"

        if destination.exists():

            logger.info("Repository already exists: %s", destination)

            return {
                "success": True,
                "message": "Repository already exists.",
                "path": str(destination),
            }

        try:

            Repo.clone_from(repo_url, destination)

            logger.info("Repository cloned: %s", destination)

            return {
                "success": True,
                "message": "Repository cloned successfully.",
                "path": str(destination),
            }

        except GitCommandError:

            logger.exception("Git clone failed.")

            if destination.exists():
                shutil.rmtree(destination)

            raise HTTPException(
                status_code=400,
                detail="Failed to clone repository. Check the URL or repository permissions.",
            )

        except Exception:

            logger.exception("Unexpected clone error.")

            if destination.exists():
                shutil.rmtree(destination)

            raise HTTPException(
                status_code=500,
                detail="Internal server error while cloning repository.",
            )