### RASA

1)domain file is dierectory of everything assistant knows
-response's= are the actions taken by bot in response to intention of user
-intents= intention or task given by user
-slots=variables stored throught convo and extracted as entities
-entities= the piece of information extracted from user
-forms= form is collection of  to be filled for bot to proceed



### Extraction of entities 
1)Extracting fixed-format data (e.g., email, phone)-->	Regex-->	Precise and easy to implement.

2)Parsing dates, times, or currencies-->	Duckling-->	Handles normalization out of the box.

3)Extracting general entities like names, places-->	Spacy-->	Pre-trained for these standard entities.

4)Handling custom or domain-specific entities-->	ML Approach-->	Flexible and can learn from data to extract domain-specific information.

5)Context-sensitive entity extraction-->	ML Approach-->	Accounts for variations in meaning based on context.

###


RAG



1)RAG= retrived argumented generation is a technique combines retrival based and generation based for NLP tasks
improves quality by retriving data from documents and using it to inform user. accuracy and updated data.

2): Ollama is a platform or tool designed to simplify the use of large language models (LLMs) locally or in a managed environment.

3)LLAMA= Large Language Model Meta AI(smaller than gpt)
LLama works as generational model in RAG systems

4)LlamaIndex handles the retrieval part by indexing external data(pdf,documents) and serving it to the generation model. integrated below steps.

###




PROCESS OF  INDEXING

1)parsing the data= the raw data is divided into smaller manageable chunks like breaking page into paragraphs, sentences etc. Libraries like langchain or tools like LlamaIndex have built-in text splitters (e.g., RecursiveCharacterTextSplitter

2)creating the index= the chunks are then further specified with the meta data like keywords, document_id, source etc

3)mapping to vectors= each chunks coverted into numerical  vector by pre-defined embedding modelkepping the revelant meaning of sentences.
Common embedding models:
OpenAI’s text-embedding-ada-002
Sentence Transformers (all-MiniLM-L6-v2)
Libraries like sentence-transformers or langchain can compute these embeddings.


4)The vectors (from Step 3) and metadata (from Step 2) are stored in a vector database or indexing system. A vector database like FAISS, Pinecone, or Weaviate stores



###










