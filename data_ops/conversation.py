
import os
from langchain_community.vectorstores import Milvus
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage

embeddings = OpenAIEmbeddings()

# Initialize Milvus
vector_db = Milvus(
    embeddings,
    collection_name=os.environ["MILVUS_COLLECTION"],
    connection_args={"host": os.environ["MILVUS_HOST"], "port": os.environ["MILVUS_PORT"]},
)

chat = ChatOpenAI(model="gpt-4-1106-preview") # GPT 4 is quite expensive in comparison to GPT 3.5, leave model name blank to use GPT 3.5 and save cost

# Setup Conversation
context_set = set()
context = "I do not have any context right now."
messages = [SystemMessage(content=context)]


# ----------------------------------------------- #

# to do:
# A lot of the time our vector similarity search will yeild in same result
# We should store search results in a set, so that they can't be duplicated
# And then convert to text


# ---

# Ask questions
user_query = "What is NCFMP"
question = HumanMessage(content=user_query)

# Convert query to embedding and perform similarity search
similar_items = vector_db.similarity_search(user_query)

# Include similar items/context in the chat

context_set.update(set([item.page_content for item in similar_items]))
context = "\n".join(context_set)
messages[0] = SystemMessage(content=context)
messages.append(question)

response = chat.invoke(messages)
messages.append(response)

print(response.content)


# ---

# Ask questions
user_query = "Is there anyone I can contact regarding NCFMP"
question = HumanMessage(content=user_query)

# Convert query to embedding and perform similarity search
similar_items = vector_db.similarity_search(user_query)

# Include similar items/context in the chat
context_set.update(set([item.page_content for item in similar_items]))
context = "\n".join(context_set)
messages[0] = SystemMessage(content=context)
messages.append(question)

response = chat.invoke(messages)
messages.append(response)

print(response.content)


# ---

# Ask questions
user_query = "What products were produced"
question = HumanMessage(content=user_query)

# Convert query to embedding and perform similarity search
similar_items = vector_db.similarity_search(user_query)

# Include similar items/context in the chat
context_set.update(set([item.page_content for item in similar_items]))
context = "\n".join(context_set)
messages[0] = SystemMessage(content=context)
messages.append(question)

response = chat.invoke(messages)
messages.append(response)

print(response.content)

# ---

# Ask questions
user_query = "What is the role of Dewberry in all of this?"
question = HumanMessage(content=user_query)

# Convert query to embedding and perform similarity search
similar_items = vector_db.similarity_search(user_query)

# Include similar items/context in the chat
context_set.update(set([item.page_content for item in similar_items]))
context = "\n".join(context_set)
messages[0] = SystemMessage(content=context)
messages.append(question)

response = chat.invoke(messages)

messages.append(response)

print(response.content)

# ---

# Ask questions
user_query = "Now lets move to different topic, tell me what is the PERIOD OF PERFORMANCE  for floodcast"
question = HumanMessage(content=user_query)

# Convert query to embedding and perform similarity search
similar_items = vector_db.similarity_search(user_query)

# Include similar items/context in the chat
context_set.update(set([item.page_content for item in similar_items]))
context = "\n".join(context_set)
messages[0] = SystemMessage(content=context)
messages.append(question)

response = chat.invoke(messages)

messages.append(response)

print(response.content)