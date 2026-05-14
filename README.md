# RAG-Based AI Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using OpenAI, LangChain, FAISS, and Streamlit.

The application allows users to upload PDF documents and ask context-aware questions using semantic search and AI-generated responses.

---

## Features

* PDF document ingestion
* Text chunking and preprocessing
* OpenAI embeddings generation
* FAISS vector database for semantic search
* Conversational chatbot UI
* Context-aware AI responses
* Retrieval-Augmented Generation (RAG) pipeline

---

## Tech Stack

| Technology | Purpose             |
| ---------- | ------------------- |
| Python     | Backend Development |
| OpenAI API | LLM & Embeddings    |
| LangChain  | RAG Framework       |
| FAISS      | Vector Database     |
| Streamlit  | Chatbot UI          |
| PyPDF      | PDF Parsing         |

---

## Project Structure

```text
Chatbot/
│
├── data/
│   └── Resume.pdf
│
├── faiss_index/
│
├── app.py
├── ingest.py
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/AnilSami/Chatbot.git

cd Chatbot
```

### 2. Create Virtual Environment

```bash
python -m venv chatbot
```

### 3. Activate Environment

#### Windows

```bash
.\chatbot\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## Add PDF Documents

Place your PDF files inside:

```bash
./data/
```

Example:

```bash
./data/Resume.pdf
```

---

## Create Vector Database

Run the ingestion script:

```bash
python ingest.py
```

This process will:

* Load PDF documents
* Split text into chunks
* Generate embeddings
* Store embeddings in FAISS vector database

---

## Run the Application

```bash
streamlit run app.py
```

---

## How It Works

1. PDF documents are loaded and processed
2. Text is split into smaller chunks
3. OpenAI embeddings convert text into vectors
4. FAISS stores vectors for semantic similarity search
5. User asks questions in chatbot UI
6. Relevant chunks are retrieved
7. OpenAI generates context-aware responses

---

## Example Questions

* What programming languages are mentioned in the resume?
* What AI projects has the candidate worked on?
* What experience does the candidate have with RAG?
* What technologies were used in previous internships?

---

## Future Improvements

* Multi-PDF support
* Persistent chat memory
* Hybrid search (BM25 + Vector Search)
* Authentication system
* FastAPI backend
* React frontend
* Docker deployment

---

## Author

### Anil Babu Samineni

* GitHub: https://github.com/AnilSami
* LinkedIn: https://www.linkedin.com/in/anil-babu-samineni-626a9a178
