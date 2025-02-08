import streamlit as st
import logging
import sys
import os
from src.config import PDF_STORAGE_PATH, LANGUAGE_MODEL
from src.utils import save_uploaded_file
from src.document_processor import load_pdf_documents, chunk_documents
from src.vector_store import index_documents, find_related_documents
from langchain_core.prompts import ChatPromptTemplate

# Ensure 'src' directory is in the path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout)
    ]
)

PROMPT_TEMPLATE = """
You are an expert research assistant. Use the provided context to answer the query. 
If unsure, state that you don't know. Be concise and factual (max 3 sentences).

Query: {user_query} 
Context: {document_context} 
Answer:
"""

st.title("📘 Chat With Your Doc")
st.markdown("### Your Intelligent Document Assistant")
st.markdown("---")

# File Upload Section
uploaded_pdf = st.file_uploader(
    "Upload Research Document (PDF)",
    type="pdf",
    help="Select a PDF document for analysis",
    accept_multiple_files=False
)

if uploaded_pdf:
    try:
        logging.info("User uploaded a PDF file.")
        saved_path = save_uploaded_file(uploaded_pdf, PDF_STORAGE_PATH)
        logging.info(f"File saved at: {saved_path}")
        
        raw_docs = load_pdf_documents(saved_path)
        processed_chunks = chunk_documents(raw_docs)
        index_documents(processed_chunks)
        
        st.success("✅ Document processed successfully! Ask your questions below.")
        logging.info("Document processed and indexed successfully.")
        
        user_input = st.chat_input("Enter your question about the document...")
        
        if user_input:
            logging.info(f"User query received: {user_input}")
            with st.chat_message("user"):
                st.write(user_input)
            
            with st.spinner("Analyzing document..."):
                relevant_docs = find_related_documents(user_input)
                context_text = "\n\n".join([doc.page_content for doc in relevant_docs])
                conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
                response_chain = conversation_prompt | LANGUAGE_MODEL
                ai_response = response_chain.invoke({"user_query": user_input, "document_context": context_text})
                
            with st.chat_message("assistant", avatar="🤖"):
                st.write(ai_response)
            logging.info("Response generated and displayed to user.")
    
    except Exception as e:
        logging.error(f"Error occurred: {str(e)}")
        st.error("❌ An error occurred while processing the document. Please try again.")
