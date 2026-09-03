from pathlib import Path


class PackageDetector:

    @classmethod
    def detect(cls, path: Path):

        package_managers = []

        if (path / "requirements.txt").exists():
            package_managers.append("pip")

        if (path / "pyproject.toml").exists():
            package_managers.append("poetry")

        if (path / "package.json").exists():
            package_managers.append("npm")

        if (path / "pnpm-lock.yaml").exists():
            package_managers.append("pnpm")

        if (path / "pom.xml").exists():
            package_managers.append("Maven")

        if (path / "build.gradle").exists():
            package_managers.append("Gradle")

        return package_managers