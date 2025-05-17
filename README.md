# Multiple_Source_Chat

This project implements a chat conversation system capable of understanding and responding to user queries by reading and extracting information from multiple sources such as webpages, PDFs, and plain text files. The system leverages a Conversation Chain that integrates an LLM (Large Language Model) with

## Features

- Multi-Source Data Integration: Extracts information from webpages, PDFs, and text files.
- LLM-Powered Responses: Utilizes a large language model for generating intelligent and contextually relevant responses.
- Memory: Retains context during a conversation to enable seamless multi-turn dialogues.
- Vector Store Integration: Efficiently retrieves relevant chunks of information using vectorized similarity search.
- Conversation Chain: Combines all components to maintain coherence and provide accurate responses.

## Prerequisites

### Python 3.8+

### Libraries:
- langchain
- langchain-community
- langchain-core
- langchain-groq
- transformers
- sentence-transformers
- faiss (or another vector database)
- PyPDF or pdfplumber
- beautifulsoup4 (for web scraping)
- requests

## Setup

1. **Clone the Repository**
```
cd <your-repository-folder>
git clone https://github.com/Abhishek3689/Multiple_Source_Chat_RAG_Langhcain.git
```

2. **Install Dependencies**
```
pip install -r requirements.txt
```
3. **Configure Environment:**
- Add API keys in .env file for the LLM if required (e.g., OpenAI API Key)
- Add Groq Api keys if using Groq inference

4. ** Run The Application **
```
python app.py
```
