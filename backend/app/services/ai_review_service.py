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
        print("\nRepository path:", repository_path)

        index = RepositoryIndexer.build_index(
            str(repository_path)
        )

        print("Indexed files:", len(index["files"]))
        print("Indexed dirs:", len(index["directories"]))

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


        print("\n========== FILE SELECTOR ==========")
        print(f"Selected files: {len(selected_files)}")

        for file in selected_files:
            print(file)

        file_contents = FileReader.read(selected_files)

        print("\n========== FILE READER ==========")
        print(f"Files read: {len(file_contents)}")

        for file in file_contents:
            print(file["path"])

        prompt = PromptBuilder.build(
            repository_info=repository_info,
            files=file_contents,
        )

        print("\n========== PROMPT (First 1500 chars) ==========")
        print(prompt[:1500])
        print("===============================================\n")

        review = GeminiClient.generate(prompt)

        print("\n========== GEMINI RESPONSE ==========")
        print(review)
        print("=====================================\n")

        review = ReviewParser.parse(review)

        return review
