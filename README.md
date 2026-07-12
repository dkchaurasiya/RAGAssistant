# 🚀 RAGAssistant

A **Retrieval-Augmented Generation (RAG)** application built using **Python, LangChain, Ollama, and FAISS**. This project reads a local text document, generates embeddings, stores them in a vector database, and answers user queries using semantic search and a local Large Language Model (LLM).

## ✨ Features

- 📄 Read and process text documents (`speech.txt`)
- ✂️ Intelligent document chunking using LangChain
- 🧠 Generate embeddings with Ollama (`mxbai-embed-large`)
- 🔍 Semantic search using FAISS Vector Store
- 🤖 AI-powered responses using Ollama (`gemma4`)
- 🔗 LangChain Retrieval Chain for context-aware question answering
- 💾 Local vector database
- 🔒 Fully offline (No OpenAI API required)

---

# 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.11+ | Programming Language |
| LangChain | RAG Framework |
| Ollama | Local LLM & Embedding Models |
| FAISS | Vector Database |
| LangChain Retrieval Chain | Context Retrieval |
| RecursiveCharacterTextSplitter | Document Chunking |

---

# 📂 Project Structure

```
RAGAssistant/
│
├── speech.txt
├── vector_db/
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/<your-github-username>/RAGAssistant.git

cd RAGAssistant
```

## Create Virtual Environment

### Windows

```bash
python -m venv .venv

.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv

source .venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Configure Environment

Copy the example environment file.

### Windows

```bash
copy .env.example .env
```

### Linux / macOS

```bash
cp .env.example .env
```

Update the values in `.env` if required.

---

# Install Ollama

Download and install Ollama:

https://ollama.com/download

Pull the required models:

```bash
ollama pull mxbai-embed-large
ollama pull gemma4
```

Verify:

```bash
ollama list
```

---

# ▶️ Run Application

Place your document as:

```
speech.txt
```

Execute:

```bash
python main.py
```

Example:

```
You:
What is democracy?

Assistant:
The world must be made safe for democracy...
```

---

# 🔄 LangChain RAG Workflow

```
                speech.txt
                     │
                     ▼
               TextLoader
                     │
                     ▼
      RecursiveCharacterTextSplitter
                     │
                     ▼
        Ollama Embedding Model
        (mxbai-embed-large)
                     │
                     ▼
             FAISS Vector Store
                     │
                     ▼
            LangChain Retriever
                     │
                     ▼
       LangChain Retrieval Chain
                     │
                     ▼
          Ollama LLM (gemma4)
                     │
                     ▼
               Final Response
```

---

# 📌 Example Questions

- What is democracy?
- Why does the speaker oppose conquest?
- What sacrifices does the speaker mention?
- What does the speaker say about peace?
- Who are considered the champions of mankind?
- Why did America enter the war?

---

# 📦 Dependencies

- langchain
- langchain-core
- langchain-community
- langchain-text-splitters
- langchain-ollama
- faiss-cpu
- python-dotenv

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# Future Improvements

- PDF Support
- DOCX Support
- Streamlit UI
- FastAPI REST API
- Multi-document Retrieval
- Conversation Memory
- ChromaDB Integration
- Source Citations
- Hybrid Search (BM25 + Vector Search)

---

# Skills Demonstrated

- Python
- LangChain
- Retrieval-Augmented Generation (RAG)
- Ollama
- FAISS
- Embeddings
- Semantic Search
- Vector Databases
- Prompt Engineering
- Local LLM Deployment
- Generative AI

---

# 👨‍💻 Author

**Dheerendra Kumar Chaurasiya**

GitHub: https://github.com/dkchaurasiya

---

# 📄 License

This project is licensed under the MIT License.