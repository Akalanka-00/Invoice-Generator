import io
import sys
import pdfkit
import time
from tqdm.auto import tqdm

def convert_html_to_pdfs(html_files, is_colab):
    wkhtmltopdf_path = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    if is_colab:
        wkhtmltopdf_path = '/usr/local/bin/wkhtmltopdf'
    else:
        wkhtmltopdf_path = 'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'
    # Configure the path to wkhtmltopdf
    config = pdfkit.configuration(wkhtmltopdf=wkhtmltopdf_path)  # Adjust path
    pdf_options = {
        'page-size': 'A3',
        'viewport-size': '1280x1696',
        'encoding': 'UTF-8',
        'quiet': '',
        'enable-local-file-access': '',  # Required for SVG/icons
        'load-error-handling': 'ignore'
    }  # Show errors by removing "quiet"
    pdf_files = []

    progress_bar = tqdm(range(len(html_files)), desc="Converting Invoices\t\t\t", unit="invoice", leave=True, file=sys.stdout)

    for idx, html in enumerate(html_files):
        try:
            if isinstance(html, str) and html.endswith(".html"):
                pdf_data = pdfkit.from_file(html, False, options=pdf_options, configuration=config)
            else:
                pdf_data = pdfkit.from_string(html, False, options=pdf_options, configuration=config)

            if not pdf_data:
                raise ValueError("PDF generation returned empty data.")

            pdf_buffer = io.BytesIO(pdf_data)
            pdf_buffer.seek(0)
            file_name = f"{int(time.time() * 1000)}_{idx + 1}.pdf"
            pdf_files.append({"file": pdf_buffer, "name": file_name})

            progress_bar.set_postfix_str(f"\033[32m{idx + 1}/{len(html_files)}\033[0m")
            progress_bar.update(1)
        except Exception as e:
            print(f"\nError processing file {idx + 1}: {e}")
            raise

    progress_bar.close()
    return pdf_files