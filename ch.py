from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from embeddings import get_embedding_function
from langchain_chroma import Chroma
from langchain.schema.document import Document 
#added all relevant libraries for RAG framework 


CHROMA_PATH = "chroma" #path to chroma directiry, vector database stores data
DATA_PATH= "data" #path to directory where all pdf files present

   


def split_documents(documents: list[Document]): #function defined for splitting the document into smll chunks for managing
    text_splitter =RecursiveCharacterTextSplitter(
        chunk_size=800, #each chunk is of size 800 characters
        chunk_overlap=80,#overlapping characters in chunks for better context understanding
        length_function=len,
        is_separator_regex=False,#regex false becoz its used for complex and pattern based matching and splitting
        #not using regex to make it efficient and faster
    )
    return text_splitter.split_documents(documents)



def load_documents():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()
#fucntion declared for loading all the pdf files in directory return them as document objects

def calculate_chunk_ids(chunks):

  
    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        # If the page ID is the same as the last one, increment the index.
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0

        # Calculate the chunk ID.
        chunk_id = f"{current_page_id}:{current_chunk_index}"
        last_page_id = current_page_id

        # Add it to the page meta-data.
        chunk.metadata["id"] = chunk_id

    return chunks
#function which gives every chunk a unique id which includes the page number and chunk index number
   




def add_to_chroma(chunks: list[Document]):
    # Load the existing database.
    db = Chroma(
        persist_directory=CHROMA_PATH, embedding_function=get_embedding_function()
    )

    # Calculate Page IDs.
    chunks_with_ids = calculate_chunk_ids(chunks)

    # Add or Update the documents.
    existing_items = db.get(include=[])  # IDs are always included by default
    existing_ids = set(existing_items["ids"])
    print(f"Number of existing documents in DB: {len(existing_ids)}")

    # Only add documents that don't exist in the DB.
    new_chunks = []
    for chunk in chunks_with_ids:
        if chunk.metadata["id"] not in existing_ids:
            new_chunks.append(chunk)

    if len(new_chunks):
        print(f"👉 Adding new documents: {len(new_chunks)}")
        new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
        db.add_documents(new_chunks, ids=new_chunk_ids)
        db.persist()
    else:
        print("✅ No new documents to add")

def main():
    documents = load_documents()
    chunks = split_documents(documents)
    add_to_chroma(chunks)





if __name__ == "__main__":
    main()