from langchain_community.document_loaders import PDFPlumberLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
import logging

def load_pdf_documents(file_path):
    """Load and extract text from a PDF file."""
    try:
        document_loader = PDFPlumberLoader(file_path)
        documents = document_loader.load()
        logging.info(f"Successfully loaded {len(documents)} documents from {file_path}.")
        return documents
    except Exception as e:
        logging.error(f"Error loading PDF documents from {file_path}: {str(e)}")
        raise

def chunk_documents(raw_documents):
    """Split documents into smaller chunks for processing."""
    try:
        text_processor = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            add_start_index=True
        )
        chunks = text_processor.split_documents(raw_documents)
        logging.info(f"Successfully chunked documents into {len(chunks)} chunks.")
        return chunks
    except Exception as e:
        logging.error("Error chunking documents: " + str(e))
        raise
