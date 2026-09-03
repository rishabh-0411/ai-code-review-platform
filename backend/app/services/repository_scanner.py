from app.services.detectors.language_detector import LanguageDetector
from app.services.detectors.framework_detector import FrameworkDetector
from app.services.detectors.package_detector import PackageDetector
from app.services.detectors.docker_detector import DockerDetector
from app.services.detectors.documentation_detector import DocumentationDetector
from app.services.repository_indexer import RepositoryIndexer


class RepositoryScanner:

    @classmethod
    def scan(cls, repository_path: str):

        index = RepositoryIndexer.build_index(repository_path)

        return {
            "files": len(index["files"]),
            "directories": len(index["directories"]),
            "languages": LanguageDetector.detect(index),
            "frameworks": FrameworkDetector.detect(index),
            "package_managers": PackageDetector.detect(index),
            "docker": DockerDetector.detect(index),
            "documentation": DocumentationDetector.detect(index),
        }