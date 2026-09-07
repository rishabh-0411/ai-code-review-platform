from fastapi import APIRouter
from app.services.repository_scanner import RepositoryScanner
from app.schemas.repository import (
    CloneRepositoryRequest,
    ScanRepositoryRequest,
    ReviewRepositoryRequest,
    ReviewResponse,
)

from app.services.ai_review_service import AIReviewService
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

@router.post(
    "/review",
    response_model=ReviewResponse,
)
def review_repository(request: ReviewRepositoryRequest):

    return AIReviewService.review(
        request.repository_path
    )