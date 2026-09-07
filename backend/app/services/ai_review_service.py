from app.services.repository_indexer import RepositoryIndexer
from app.services.file_selector import FileSelector
from app.services.file_reader import FileReader
from app.services.prompt_builder import PromptBuilder
from app.services.gemini_client import GeminiClient
from app.services.review_parser import ReviewParser
from app.utils.path_validator import PathValidator

from app.services.detectors.language_detector import LanguageDetector
from app.services.detectors.framework_detector import FrameworkDetector
from app.services.detectors.package_detector import PackageDetector
from app.services.detectors.docker_detector import DockerDetector
from app.services.detectors.documentation_detector import DocumentationDetector


class AIReviewService:

    @classmethod
    def review(cls, repository_path: str):

        repository_path = PathValidator.validate_repository_path(
            repository_path
        )

        index = RepositoryIndexer.build_index(str(repository_path))

        repository_info = {
            "files": len(index["files"]),
            "directories": len(index["directories"]),
            "languages": LanguageDetector.detect(index),
            "frameworks": FrameworkDetector.detect(index),
            "package_managers": PackageDetector.detect(index),
            "docker": DockerDetector.detect(index),
            "documentation": DocumentationDetector.detect(index),
        }

        selected_files = FileSelector.select_files(index)

        file_contents = FileReader.read(selected_files)

        prompt = PromptBuilder.build(
            repository_info=repository_info,
            files=file_contents,
        )

        review = GeminiClient.generate(prompt)

        review = ReviewParser.parse(review)

        return review 