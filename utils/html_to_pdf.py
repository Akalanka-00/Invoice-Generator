import io
import sys

import pdfkit
import time

from tqdm import tqdm


def convert_html_to_pdfs(html_files):
    pdf_options = {"quiet": ""}  # Suppress wkhtmltopdf logs
    pdf_files = []  # Initialize an empty list to hold PDF data

    # Initialize progress bar after pdf_files is populated
    progress_bar = tqdm(range(len(html_files)), desc="Converting Invoices to pdf\t", unit="invoice", leave=True, file=sys.stdout)

    for idx, html in enumerate(html_files):
        pdf_buffer = io.BytesIO()

        # Check if input is a file path or raw HTML content
        if isinstance(html, str) and html.endswith(".html"):
            pdf_data = pdfkit.from_file(html, False, options=pdf_options)
        else:
            pdf_data = pdfkit.from_string(html, False, options=pdf_options)

        pdf_buffer.write(pdf_data)
        pdf_buffer.seek(0)  # Reset buffer position

        # Generate a unique name for the PDF (timestamp-based)
        file_name = f"{int(time.time() * 1000)}_{idx + 1}.pdf"

        # Append the dictionary with 'file' and 'name'
        pdf_files.append({"file": pdf_buffer, "name": file_name})

        # Update progress bar with the current status
        progress_bar.set_postfix_str(f"\033[32m{idx + 1}/{len(html_files)}\033[0m", refresh=True)
        progress_bar.update(1)

    return pdf_files