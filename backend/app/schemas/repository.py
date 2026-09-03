from pydantic import BaseModel, HttpUrl


class CloneRepositoryRequest(BaseModel):
    repo_url: HttpUrl

class ScanRepositoryRequest(BaseModel):
    repository_path: str