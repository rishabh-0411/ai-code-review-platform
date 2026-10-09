from pydantic import BaseModel, HttpUrl


class CloneRepositoryRequest(BaseModel):
    repo_url: HttpUrl

class ScanRepositoryRequest(BaseModel):
    repository_path: str

class ReviewRepositoryRequest(BaseModel):
    repository_path: str

class ReviewIssue(BaseModel):
    category: str
    severity: str
    description: str
    file: str | None = None
    line: int | None = None


class ReviewResponse(BaseModel):
    overall_score: float
    strengths: list[str]
    issues: list[ReviewIssue]
    recommendations: list[str]