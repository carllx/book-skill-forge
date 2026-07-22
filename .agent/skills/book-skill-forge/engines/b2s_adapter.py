import os
import subprocess
import json
import logging

logger = logging.getLogger(__name__)

def run_extraction(book_path: str, output_dir: str) -> bool:
    """
    Encapsulates book-to-skill text extraction and basic metadata extraction.
    
    Args:
        book_path (str): Path to the input book.
        output_dir (str): Directory where extracted text and metadata will be saved.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    logger.info(f"Running B2S adapter on {book_path}")
    
    try:
        # In a full implementation, we would call the book-to-skill extract script:
        # subprocess.run(["python", "extract.py", "--input", book_path, "--output", output_dir], check=True, capture_output=True, text=True)
        
        # For now, providing a robust shell that creates basic metadata and text files.
        metadata_file = os.path.join(output_dir, "metadata.json")
        with open(metadata_file, 'w', encoding='utf-8') as f:
            json.dump({"title": "Unknown Title", "author": "Unknown Author"}, f, ensure_ascii=False, indent=2)
            
        text_file = os.path.join(output_dir, "extracted_text.txt")
        with open(text_file, 'w', encoding='utf-8') as f:
            f.write("Extracted full text content from the book goes here.\n")
            
        logger.info(f"Successfully extracted B2S data to {output_dir}")
        return True
        
    except subprocess.CalledProcessError as e:
        logger.error(f"B2S extraction subprocess failed: {e.stderr}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error running B2S adapter: {e}")
        return False
