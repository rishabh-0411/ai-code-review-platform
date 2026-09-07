from pathlib import Path
class FileReader:

    MAX_FILE_SIZE = 10000

    @classmethod
    def read(cls, files: list[Path]) -> list[dict]:

        contents = []

        for file in files:

            try:

                text = file.read_text(
                    encoding="utf-8",
                    errors="ignore",
                )

                text = text[: cls.MAX_FILE_SIZE]

                contents.append(
                    {
                        "path": str(file),
                        "content": text,
                    }
                )

            except Exception:

                continue

        return contents