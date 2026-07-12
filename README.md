# 🚀 RAGAssistant

A simple Retrieval-Augmented Generation (RAG) application built using **Python**, **LangChain**, **Ollama**, and **FAISS**. It reads a local text file, creates embeddings, stores them in a vector database, and retrieves relevant information to answer user questions.

## Features

- Read text documents (`speech.txt`)
- Split documents into chunks
- Generate embeddings using Ollama
- Store embeddings in FAISS
- Perform semantic similarity search
- Generate context-aware responses using a local LLM
- Fully offline (no OpenAI API required)

---

## Tech Stack

- Python
- LangChain
- Ollama
- FAISS
- mxbai-embed-large (Embedding Model)
- Gemma4 / Llama2 (LLM)

---

## Project Structure

```
RAGAssistant/
│
├── speech.txt
├── main.py
├── vector_db/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/<your-github-username>/RAGAssistant.git

cd RAGAssistant
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download and install Ollama from:

https://ollama.com/download

Pull the required models:

```bash
ollama pull mxbai-embed-large
ollama pull gemma4
```

---

## Usage

Place your document in the project folder as:

```
speech.txt
```

Run the application:

```bash
python main.py
```

The application will:

1. Read `speech.txt`
2. Split the text into chunks
3. Generate embeddings
4. Store vectors in FAISS
5. Retrieve relevant context
6. Generate answers using Ollama

---

## RAG Workflow

```
speech.txt
      │
      ▼
TextLoader
      │
      ▼
Text Splitter
      │
      ▼
Ollama Embeddings
      │
      ▼
FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Ollama LLM
      │
      ▼
Answer
```

---

## Example

**Question**

```
Who is the chairman of the drafting committee?
```

**Answer**

```
Dr. B.R. Ambedkar was the chairman of the drafting committee.
```

---

## Future Improvements

- Support PDF documents
- Support DOCX files
- Streamlit Web UI
- FastAPI REST API
- Multi-document support
- Chat history
- ChromaDB integration

---

## Skills Demonstrated

- Python
- LangChain
- Retrieval-Augmented Generation (RAG)
- Ollama
- FAISS
- Embeddings
- Semantic Search
- Prompt Engineering
- Large Language Models (LLMs)

---

## Author

**Dheerendra Kumar Chaurasiya**

GitHub: https://github.com/dkchaurasiya

---

## License

MIT License