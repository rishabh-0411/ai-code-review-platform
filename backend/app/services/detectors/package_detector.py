class PackageDetector:

    @staticmethod
    def _exists(index, filename):

        return any(
            file.name == filename
            for file in index["files"]
        )

    @classmethod
    def detect(cls, index):

        managers = []

        if cls._exists(index, "requirements.txt"):
            managers.append("pip")

        if cls._exists(index, "pyproject.toml"):
            managers.append("poetry")

        if cls._exists(index, "package.json"):
            managers.append("npm")

        if cls._exists(index, "pnpm-lock.yaml"):
            managers.append("pnpm")

        if cls._exists(index, "pom.xml"):
            managers.append("Maven")

        if cls._exists(index, "build.gradle"):
            managers.append("Gradle")

        return managers