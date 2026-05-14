# Chatbot
RAG-based AI chatbot using OpenAI, LangChain, FAISS, and Streamlit for semantic PDF document question answering.

# RAG-Based AI Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using OpenAI, LangChain, FAISS, and Streamlit.  
The application allows users to upload PDF documents and ask context-aware questions using semantic search and LLM-powered responses.

---

## Features

- PDF document ingestion
- Text chunking and preprocessing
- OpenAI embeddings generation
- FAISS vector database for semantic search
- Conversational chatbot UI using Streamlit
- Context-aware AI responses
- Retrieval-Augmented Generation (RAG) pipeline

---

## Tech Stack

- Python
- OpenAI API
- LangChain
- FAISS
- Streamlit
- PyPDF
- dotenv

---

## Project Structure

```bash
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
