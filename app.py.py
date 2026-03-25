import streamlit as st

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

st.title("PDF Q&A")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    loader = PyPDFLoader("temp.pdf")
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(chunks, embeddings)

    query = st.text_input("Ask question")

    if query:
        results = db.similarity_search(query, k=3)
        context = " ".join([doc.page_content for doc in results])

        tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
        model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")

        inputs = tokenizer(f"Context: {context} Question: {query}", return_tensors="pt", truncation=True)
        outputs = model.generate(**inputs, max_length=200)

        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        st.write("### Answer:")
        st.write(answer)
