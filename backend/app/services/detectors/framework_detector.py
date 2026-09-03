class FrameworkDetector:

    @staticmethod
    def _find_file(index, filename):

        return next(
            (
                file
                for file in index["files"]
                if file.name == filename
            ),
            None,
        )

    @classmethod
    def detect(cls, index):

        frameworks = []

        requirements = cls._find_file(index, "requirements.txt")

        if requirements:

            content = requirements.read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "fastapi" in content:
                frameworks.append("FastAPI")

            if "django" in content:
                frameworks.append("Django")

            if "flask" in content:
                frameworks.append("Flask")

        package_json = cls._find_file(index, "package.json")

        if package_json:

            content = package_json.read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if '"react"' in content:
                frameworks.append("React")

            if '"next"' in content:
                frameworks.append("Next.js")

        pom = cls._find_file(index, "pom.xml")

        if pom:

            content = pom.read_text(
                encoding="utf-8",
                errors="ignore",
            ).lower()

            if "spring-boot" in content:
                frameworks.append("Spring Boot")

        return frameworks