import os
from pypdf import PdfReader, PdfWriter

# Directory containing PDF files
directory = "pdfs-to-merge"

# Output file name
output_file = "output-dir/merged_output.pdf"

# Ensure the output directory exists
os.makedirs(os.path.join(directory, "output-dir"), exist_ok=True)

# Create a PdfWriter object
writer = PdfWriter()

# Iterate over all PDF files in the directory
for file_name in sorted(os.listdir(directory)):
    if file_name.endswith(".pdf"):
        file_path = os.path.join(directory, file_name)
        print(f"Adding: {file_name}")
        
        # Read the PDF file
        reader = PdfReader(file_path)
        
        # Append all pages to the writer
        writer.append(reader)

# Write the merged PDF to an output file
output_path = os.path.join(directory, output_file)
with open(output_path, "wb") as output_pdf:
    writer.write(output_pdf)

print(f"Merged PDF saved as: {output_path}")
