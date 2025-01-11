from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader


def load_documents():
    document_loader = PyPDFDirectoryLoader("data")
    return document_loader.load()





