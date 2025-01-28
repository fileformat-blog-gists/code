from pypdf import PdfReader, PdfWriter
import os

# Input PDF file
input_pdf = "pdf-to-split/input.pdf"

# Output directory
output_directory = "pdf-to-split/output-dir"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Read the input PDF
reader = PdfReader(input_pdf)

# Loop through each page and save it as a separate PDF
for page_num, page in enumerate(reader.pages):
    writer = PdfWriter()
    writer.add_page(page)

    # Define the output file name
    output_file = os.path.join(output_directory, f"page_{page_num + 1}.pdf")

    # Write the page to a new PDF
    with open(output_file, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Created: {output_file}")

print("PDF splitting complete!")
