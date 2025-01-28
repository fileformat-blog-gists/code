from pypdf import PdfReader

# Path to the PDF file
pdf_file = "pdf-to-extract-text/input.pdf"

# Create a PDF reader object
reader = PdfReader(pdf_file)

# Loop through the pages and extract text
for page_number, page in enumerate(reader.pages, start=1):
    print(f"Page {page_number}:")
    print(page.extract_text())
    print("-" * 50)  # Separator for readability
