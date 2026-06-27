import fitz  # PyMuPDF
import io

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """Extracts raw text from a PDF file stream."""
    text = ""
    # Open the PDF from bytes
    with fitz.open(stream=file_bytes, filetype="pdf") as doc:
        # Iterate through each page and extract text
        for page in doc:
            text += page.get_text("text") + "\n"
    return text