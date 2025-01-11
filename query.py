from embeddings import get_embedding_function # A function that provides the embedding generation logic, likely transforming text into numerical vectors.
from ch import add_to_chroma
from langchain.prompts import ChatPromptTemplate #a library template for structuring the repsonses 
from langchain_community.llms.ollama import Ollama
import argparse #to handle cmd line arguments given as query from user
from langchain_chroma import Chroma


CHROMA_PATH="chroma"#path to directory of chroma (vector database)

def main():
    # Create CLI.
    parser = argparse.ArgumentParser() #parses the argument given by user
    parser.add_argument("query_text", type=str, help="The query text.")
    args = parser.parse_args()
    query_text = args.query_text#captures the query string from user
    query_rag(query_text)

def query_rag(query_text: str): #fucntion to handle the query text made by user
    embedding_function = get_embedding_function()#calls embedding funciton
    db = Chroma(
        persist_directory =CHROMA_PATH,
        embedding_function= embedding_function #converst the text to vector using embedding

    )
#
    PROMPT_TEMPLATE = """
    Answer the question based only on following context:
    {context}

    ___
    Answer the question on above context: {question}
    """
    #defined the template of responses in LLM

    results= db.similarity_search_with_score(query_text, k=5)#perdorms simlarirty seach of top 5 most related chunks to query
    context_text= "\n\n---\n\n".join([doc.page_content for doc, _score in results]) #joins the content of retrived data
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt= prompt_template.format(context=context_text,question=query_text)
    model = Ollama(model="mistral")
    response_text = model.invoke(prompt)
    sources = [doc.metadata.get("id", None) for doc, _score in results]
    formatted_response = f"Response: {response_text}\nSources: {sources}"
    print(formatted_response)
    return response_text

if __name__ == "__main__":
    main()