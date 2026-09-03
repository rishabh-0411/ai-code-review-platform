from fastapi import APIRouter
from app.services.repository_scanner import RepositoryScanner
from app.schemas.repository import (
    CloneRepositoryRequest,
    ScanRepositoryRequest,
)

from app.schemas.repository import CloneRepositoryRequest
from app.services.github_service import GitHubService

router = APIRouter(
    prefix="/repositories",
    tags=["Repositories"],
)


@router.post("/clone")
def clone_repository(request: CloneRepositoryRequest):
    return GitHubService.clone_repository(
        str(request.repo_url)
    )

@router.post("/scan")
def scan_repository(request: ScanRepositoryRequest):
    return RepositoryScanner.scan(request.repository_path)