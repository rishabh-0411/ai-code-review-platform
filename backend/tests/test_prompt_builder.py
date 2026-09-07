from app.services.repository_indexer import RepositoryIndexer
from app.services.repository_scanner import RepositoryScanner
from app.services.file_selector import FileSelector
from app.services.file_reader import FileReader
from app.services.prompt_builder import PromptBuilder

index = RepositoryIndexer.build_index("..")

repository_info = RepositoryScanner.scan("..")

selected = FileSelector.select_files(index)

contents = FileReader.read(selected)

prompt = PromptBuilder.build(repository_info, contents)

print(prompt[:3000])