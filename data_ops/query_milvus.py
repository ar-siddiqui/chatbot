import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Milvus
from langchain_openai import OpenAIEmbeddings, ChatOpenAI


# Initialize Text Splitter and Embeddings
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
embeddings = OpenAIEmbeddings()

# Initialize Milvus
vector_db = Milvus(
    embeddings,
    collection_name=os.environ["MILVUS_COLLECTION"],
    connection_args={"host": os.environ["MILVUS_HOST"], "port": os.environ["MILVUS_PORT"]},
)


# Perform a similarity search
query = "What is ncfmp?"
results = vector_db.similarity_search(query)

# Output the result
if results:
    print(results[0].page_content)
else:
    print("No results found for the query.")