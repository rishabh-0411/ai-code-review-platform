from pathlib import Path


class DockerDetector:

    @classmethod
    def detect(cls, path: Path):

        docker_files = [
            "Dockerfile",
            "docker-compose.yml",
            "docker-compose.yaml",
        ]

        return any(
            (path / file).exists()
            for file in docker_files
        )