from pathlib import Path
import shutil

from git import Repo, GitCommandError


class GitHubService:
    """
    Handles cloning GitHub repositories.
    """

    TEMP_DIR = Path("temp")

    @classmethod
    def clone_repository(cls, repo_url: str):
        cls.TEMP_DIR.mkdir(exist_ok=True)

        repo_name = repo_url.rstrip("/").split("/")[-1]
        destination = cls.TEMP_DIR / repo_name

        if destination.exists():
            return {
                "success": True,
                "message": "Repository already exists.",
                "path": str(destination),
            }

        try:
            Repo.clone_from(repo_url, destination)

            return {
                "success": True,
                "message": "Repository cloned successfully.",
                "path": str(destination),
            }

        except GitCommandError:
            if destination.exists():
                shutil.rmtree(destination)

            return {
                "success": False,
                "message": "Failed to clone repository. Check the URL or repository permissions.",
            }

        except Exception as e:
            if destination.exists():
                shutil.rmtree(destination)

            return {
                "success": False,
                "message": str(e),
            }