from pypdf import PdfReader, PdfWriter

# Input and output PDF files
input_pdf = "pdf-to-rotate/input.pdf"
output_pdf = "pdf-to-rotate/rotated_output.pdf"

# Read the PDF
reader = PdfReader(input_pdf)
writer = PdfWriter()

# Rotate the first page 90 degrees clockwise
page = reader.pages[0]
page.rotate(90)  # Rotate 90 degrees clockwise

# Add the rotated page to the writer
writer.add_page(page)

# Add the rest of the pages without modification
for i in range(1, len(reader.pages)):
    writer.add_page(reader.pages[i])

# Write the output to a new PDF file
with open(output_pdf, "wb") as file:
    writer.write(file)

print(f"Rotated page saved to {output_pdf}")
