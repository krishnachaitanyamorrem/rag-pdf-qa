# 📄 AI PDF Q&A System (RAG)

## 🚀 Overview

This project is an AI-powered PDF Question Answering system built using **Retrieval-Augmented Generation (RAG)**.
Users can upload any PDF and ask questions, and the system generates accurate answers based on the document content.

---

## 🧠 How It Works

PDF → Text → Chunking → Embeddings → Vector DB (FAISS) → Retrieval → LLM → Answer

---

## ⚙️ Tech Stack

* Streamlit (Frontend UI)
* LangChain (Pipeline)
* FAISS (Vector Database)
* HuggingFace Transformers (LLM)
* Sentence Transformers (Embeddings)

---

## ✨ Features

* Upload any PDF 📄
* Ask questions in natural language 💬
* Context-aware answers using RAG 🤖
* Fast similarity search with FAISS ⚡

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📸 Demo

(Add screenshots here after running your app)

---

## 📁 Project Structure

```
rag-pdf-qa/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 👨‍💻 Author

Krishna Chaitanya Morrem
