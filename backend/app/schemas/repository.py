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


class ReviewResponse(BaseModel):
    overall_score: float
    strengths: list[str]
    issues: list[ReviewIssue]
    recommendations: list[str]