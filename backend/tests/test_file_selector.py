from app.services.repository_indexer import RepositoryIndexer
from app.services.file_selector import FileSelector
from app.services.file_reader import FileReader


index = RepositoryIndexer.build_index("..")

files = FileSelector.select_files(index)

print(f"Selected {len(files)} files")

contents = FileReader.read(files)

print(f"Read {len(contents)} files")

for file in contents[:5]:
    print(file["path"])