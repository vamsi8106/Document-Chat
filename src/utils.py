import os
import logging

def save_uploaded_file(uploaded_file, storage_path):
    """Save uploaded file to storage directory."""
    try:
        file_path = os.path.join(storage_path, uploaded_file.name)
        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())
        logging.info(f"File {uploaded_file.name} saved successfully at {file_path}.")
        return file_path
    except Exception as e:
        logging.error(f"Failed to save file {uploaded_file.name}: {str(e)}")
        raise
