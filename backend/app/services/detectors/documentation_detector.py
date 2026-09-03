class DocumentationDetector:

    @classmethod
    def detect(cls, index):

        names = {file.name for file in index["files"]}

        return {
            "readme": "README.md" in names,
            "license": "LICENSE" in names,
            "contributing": "CONTRIBUTING.md" in names,
        }