# 📄 AI PDF Question Answering System (RAG)

## 🚀 Overview

This project is an AI-powered system that allows users to upload PDF documents and ask questions based on their content.

It uses **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from the document and generate accurate, context-aware answers.

---

## 🧠 Architecture

PDF → Text Extraction → Chunking → Embeddings → FAISS → Retrieval → LLM → Answer

---

## ⚙️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **Framework**: LangChain
* **Vector Database**: FAISS
* **LLM**: HuggingFace (FLAN-T5)
* **Embeddings**: Sentence Transformers

---

## ✨ Features

* 📄 Upload any PDF
* 💬 Ask questions in natural language
* 🤖 Context-aware answers using RAG
* ⚡ Fast retrieval with FAISS

---

## 📦 Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 📸 Demo

(Add screenshots here)

---

## 📁 Project Structure

rag-pdf-qa/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

---

## 👨‍💻 Author

Krishna Chaitanya Morrem

---

## 📌 Future Improvements

* Chat history (like ChatGPT)
* Multi-PDF support
* Better LLM (LLaMA / Mistral)
* Deployment (Streamlit Cloud)

---

## 👨‍💻 Author

Krishna Chaitanya Morrem
