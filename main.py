import os
import requests
from PyPDF2 import PdfMerger, PdfReader

# List of PDF URLs
pdf_links = [
    "https://www.africau.edu/images/default/sample.pdf",
    "https://www.africau.edu/images/default/sample.pdf",
    # add more links as needed
]

# Directory to store downloaded PDFs
download_dir = 'downloaded_pdfs'

if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Initialize PDF merger
merger = PdfMerger()

for i, link in enumerate(pdf_links):
    response = requests.get(link)
    filename = os.path.join(download_dir, f'pdf{i+1}.pdf')
    with open(filename, 'wb') as output_pdf:
        output_pdf.write(response.content)
    merger.append(PdfReader(filename))

# Output combined PDF
with open('combined.pdf', 'wb') as output_pdf:
    merger.write(output_pdf)
