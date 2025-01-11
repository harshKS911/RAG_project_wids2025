from load import load_documents
from split import split_documents

# Load the documents
documents = load_documents()

# Split the documents into chunks
chunks = split_documents(documents)
last_page_id= None
current_chunk_index=0

for chunk in chunks:
    source= chunk.metadata.get("source")
    page= chunk.metadata.get("page")
    current_page_id= f"{source}:{page}"

    if current_page_id == last_page_id:
        current_chunk_index +=1
    else:
        current_chunk_index =0
    
    last_page_id=current_page_id
    chunk_id= f"{current_page_id}:{current_chunk_index}"
    chunk.metadata["id"]=chunk_id

    print(chunk_id)

    

    