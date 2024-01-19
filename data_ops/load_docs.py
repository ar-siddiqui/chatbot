import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Milvus
from langchain_openai import OpenAIEmbeddings

# Initialize Text Splitter and Embeddings
text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
embeddings = OpenAIEmbeddings()

# Initialize Milvus
vector_db = Milvus(
    embeddings,
    collection_name=os.environ["MILVUS_COLLECTION"],
    connection_args={"host": os.environ["MILVUS_HOST"], "port": os.environ["MILVUS_PORT"]},
)

# Directory containing documents
documents_directory = "./documents"

# Batch limit for chunk insertion
batch_limit = 1000

# Function to add chunks to Milvus and clear the list
def add_chunks_to_milvus(chunks):
    print(f"Adding {len(chunks)} chunks to Milvus.")
    vector_db.add_documents(chunks)
    chunks.clear()

# Accumulate chunks and process in batches
all_chunks = []

# Process each document in the directory
for filename in os.listdir(documents_directory):
    if filename.endswith(".txt"):  # Ensure it's a text file
        file_path = os.path.join(documents_directory, filename)
        loader = TextLoader(file_path)
        docs = loader.load()

        # Split the document into chunks and accumulate
        chunks = text_splitter.split_documents(docs)
        all_chunks.extend(chunks)
        print(f"Processed {filename}: {len(chunks)} chunks")

        # Check if limit reached, then insert to Milvus
        if len(all_chunks) >= batch_limit:
            add_chunks_to_milvus(all_chunks)

# Add any remaining chunks to Milvus
if all_chunks:
    add_chunks_to_milvus(all_chunks)



