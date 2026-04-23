# 🤖 RAG Chatbot using LangGraph & Ollama

## 📌 Overview
This project is a Retrieval-Augmented Generation (RAG) chatbot that answers user queries based on a PDF knowledge base.

It uses embeddings + vector database + LLM to generate accurate answers.

---

## 🛠️ Tech Stack
- Python
- LangChain
- LangGraph
- ChromaDB
- Ollama (LLaMA 3)
- HuggingFace Embeddings

---

## 📂 Project Structure

rag-project/
│── data/
│   └── knowledge.pdf
│
│── chroma_db/
│
│── src/
│   ├── ingestion.py
│   ├── retrieval.py
│   ├── graph.py
│   ├── main.py
│
│── requirements.txt
│── README.md

---

## ⚙️ How It Works

1. PDF is loaded and split into chunks  
2. Chunks are converted into embeddings  
3. Stored in Chroma vector database  
4. User query is matched with relevant chunks  
5. LLM generates answer using context  

---

## 🚀 How to Run

### Step 1: Install dependencies
pip install -r requirements.txt

### Step 2: Run ingestion
python src/ingestion.py

### Step 3: Run chatbot
python src/main.py

---

## 💬 Sample Queries

- What is refund policy?
- What is cancellation policy?
- Tell me about shipping

---

## ⚠️ Features

✅ Works without OpenAI (uses Ollama)  
✅ PDF-based Q&A  
✅ Human fallback response  
✅ Modular architecture  

---

## 📸 Output Example

You: What is refund policy?  
Bot: Refunds are allowed within 7 days  

---

## 📌 Future Improvements

- Add Streamlit UI  
- Add chat memory  
- Support multiple PDFs  

---

## 👨‍💻 Author

Sanika Pawar
