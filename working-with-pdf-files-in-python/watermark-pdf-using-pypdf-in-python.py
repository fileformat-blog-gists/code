from pypdf import PdfReader, PdfWriter

# Paths for the input PDF and watermark PDF
input_pdf = "pdf-to-watermark/input.pdf"
watermark_pdf = "pdf-to-watermark/watermark.pdf"
output_pdf = "pdf-to-watermark/output_with_watermark.pdf"

# Read the input PDF and watermark PDF
reader = PdfReader(input_pdf)
watermark = PdfReader(watermark_pdf)

# Create a PdfWriter object for the output PDF
writer = PdfWriter()

# Ensure the watermark has only one page (it should be one-page PDF)
watermark_page = watermark.pages[0]

# Loop through each page in the input PDF
for page in reader.pages:
    # Merge the watermark with the current page
    page.merge_page(watermark_page)
    
    # Add the merged page to the writer
    writer.add_page(page)

# Write the output PDF with watermark
with open(output_pdf, "wb") as output_file:
    writer.write(output_file)

print(f"Watermarked PDF saved as: {output_pdf}")
