from langchain_core.vectorstores import InMemoryVectorStore
from config import EMBEDDING_MODEL
import logging

DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)

def index_documents(document_chunks):
    """Index document chunks into vector database."""
    try:
        DOCUMENT_VECTOR_DB.add_documents(document_chunks)
        logging.info(f"Indexed {len(document_chunks)} document chunks into vector database.")
    except Exception as e:
        logging.error("Error indexing documents: " + str(e))
        raise

def find_related_documents(query):
    """Find related documents based on query."""
    try:
        results = DOCUMENT_VECTOR_DB.similarity_search(query)
        logging.info(f"Found {len(results)} related documents for query: {query}")
        return results
    except Exception as e:
        logging.error("Error searching for related documents: " + str(e))
        raise
