# import os
# from langchain_ollama import OllamaEmbeddings
# from langchain_ollama.llms import OllamaLLM

# # Define constants
# PDF_STORAGE_PATH = 'document_store/pdfs/'
# EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
# LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

# # Ensure storage path exists
# os.makedirs(PDF_STORAGE_PATH, exist_ok=True)

import os
import logging
from langchain_ollama import OllamaEmbeddings
from langchain_ollama.llms import OllamaLLM

# Define constants
PDF_STORAGE_PATH = 'document_store/pdfs/'
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")

# Ensure storage path exists
os.makedirs(PDF_STORAGE_PATH, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
