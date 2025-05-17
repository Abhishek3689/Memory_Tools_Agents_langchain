# 🧠 ChatBot with Multi-Source Knowledge Integration

A conversational AI assistant that can answer questions based on information from multiple sources such as webpages, PDFs, and text documents. The system leverages **LLMs**, **FAISS vector store**, **retrieval-augmented generation (RAG)**, and memory to provide context-aware responses.

---

## 🚀 Features

- ✅ Supports document ingestion from:
  - 📄 PDFs
  - 🌐 Web pages (via scraping or URL extraction)
  - 📝 Text files
- 🔍 Uses **FAISS** for efficient similarity search
- 💬 Implements **ConversationChain** with persistent memory
- 🤖 Built with **LangChain** and **LLM** (e.g., GPT, Llama, etc.)
- 📁 Easy document upload and processing

---

## 📦 Requirements

Make sure you have the following installed:

- Python 3.9+
- pip
- Virtual environment (recommended)

### Dependencies:

```bash
pip install langchain openai faiss-cpu pypdf requests beautifulsoup4 sentence-transformers chromadb
