import os
from langchain_community.vectorstores import Milvus
from langchain_openai import OpenAIEmbeddings


# Since we are using Langchain with Milvus, it would be more streamlined and consistent to let Langchain handle the initialization of the Milvus collection.
# This approach ensures that the collection is set up in a way that is compatible with how Langchain expects to interact with Milvus.
# Langchain abstracts away some of the lower-level details of Milvus and provides a higher-level interface for working with embeddings and vector databases.

embeddings = OpenAIEmbeddings()

# Initialize Milvus collection through Langchain
vector_store = Milvus(
    embeddings,
    connection_args={"host": os.environ["MILVUS_HOST"], "port": os.environ["MILVUS_PORT"]},
    collection_name=os.environ["MILVUS_COLLECTION"]
)

