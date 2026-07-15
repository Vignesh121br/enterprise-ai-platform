from pathlib import Path


class DocumentLoader:

    def load(self, directory: str):

        docs = []

        directory = Path(directory)

        if not directory.exists():
            return docs

        for file in directory.rglob("*"):

            if file.is_file():

                try:
                    text = file.read_text(
                        encoding="utf-8",
                        errors="ignore"
                    )

                    docs.append(
                        {
                            "filename": file.name,
                            "content": text
                        }
                    )

                except Exception:
                    continue

        return docs


document_loader = DocumentLoader()
