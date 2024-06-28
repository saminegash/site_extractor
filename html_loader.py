from bs4 import BeautifulSoup  # type: ignore
from langchain.document_loaders.base import BaseLoader  # type: ignore


class BeautifulSoupLoader(BaseLoader):
    def __init__(self, filename):
        self.filename = filename

    def load(self):
        with open(self.filename, 'r', encoding='utf-8') as file:
            content = file.read()
        soup = BeautifulSoup(content, 'html.parser')
        texts = [element.get_text(strip=True) for element in soup.find_all()]
        return [{"page_content": "\n".join(texts)}]
