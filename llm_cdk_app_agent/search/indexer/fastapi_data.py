import subprocess
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import DirectoryLoader, TextLoader, PythonLoader
from langchain.text_splitter import (
    RecursiveCharacterTextSplitter,
    Language,
)


# Recursively split docs text
def split_fastapi_docs():
    """Recursively split text."""
    loader = DirectoryLoader("fastapi-docs", glob="**/*.md", loader_cls=UnstructuredMarkdownLoader)
    docs = loader.load()

    print("Docs before md splitter->", len(docs))
    md_splitter = RecursiveCharacterTextSplitter.from_language(language=Language.MARKDOWN, chunk_size=250, chunk_overlap=0)
    md_docs = md_splitter.split_documents(docs)

    return md_docs


if __name__ == "__main__":
    print(len(split_docs()))
