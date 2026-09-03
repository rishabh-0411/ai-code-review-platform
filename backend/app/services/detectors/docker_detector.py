class DockerDetector:

    @classmethod
    def detect(cls, index):

        docker_files = {
            "Dockerfile",
            "docker-compose.yml",
            "docker-compose.yaml",
        }

        return any(
            file.name in docker_files
            for file in index["files"]
        )