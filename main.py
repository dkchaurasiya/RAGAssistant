from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

from langchain_ollama import ChatOllama

# Load Text File
loader = TextLoader("speech.txt", encoding="utf-8")
documents = loader.load()

# Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)

docs = splitter.split_documents(documents)

print(f"Chunks : {len(docs)}")

# Embedding Model
embeddings = OllamaEmbeddings(
    model="mxbai-embed-large"
)

# Create Vector Store
db = FAISS.load_local(
    "vector_db",
    embeddings,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={
        "k":3
    }
)

query = input("Ask : ")

docs = retriever.invoke(query)

print("\nRetrieved Chunks\n")

for doc in docs:
    print(doc.page_content)
    print("-"*50)

llm = ChatOllama(
    model="gemma4"
)

context = "\n\n".join([doc.page_content for doc in docs])

prompt = f"""
You are a helpful assistant.

Use ONLY the context below.

Context:
{context}

Question:
{query}

Answer:
"""

response = llm.invoke(prompt)

print("\nAnswer\n")
print(response.content)