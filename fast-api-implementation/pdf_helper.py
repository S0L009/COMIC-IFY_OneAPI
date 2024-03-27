from pypdf import PdfReader 

def read_n_return_pages(pdf_path):
  # extracts all text-content from the given pdf pages one-by-one
  reader = PdfReader(pdf_path) 
  return [page.extract_text() for page in reader.pages]