import os
import random
import sys
import time

from tqdm import tqdm


def apply_invoice_templates(invoices):
    html_invoices = []
    templates = fetch_templates()
    for invoice in invoices:
        template = random.choice(templates)
        html_invoices.append(apply_template(invoice, template))
    return html_invoices


def apply_template(invoice, template):
    absolute_path = os.path.abspath(f'./templates/{template}')
    with open(absolute_path, 'r') as file:
        template_content = file.read()
    template_content = populated_template(template_content, invoice)
    return template_content

def fetch_templates():
    directory_path = './templates'
    html_files = [file for file in os.listdir(directory_path) if file.endswith('.html')]
    return html_files

def populated_template(template, invoice):
    # Replace placeholders with actual invoice data
    template = template.replace("{{invoice_number}}", invoice['Invoice Number'])
    template = template.replace("{{invoice_date}}", invoice['Invoice Date'])
    template = template.replace("{{due_date}}", invoice['Due Date'])

    # Replace company details
    template = template.replace("{{company_name}}", invoice['Company']['Name'])
    template = template.replace("{{company_address}}", invoice['Company']['Address'])

    # Replace customer details
    template = template.replace("{{customer_name}}", invoice['Customer']['Name'])
    template = template.replace("{{customer_address}}", invoice['Customer']['Address'])

    # Replace item details
    template = template.replace("{{items}}", populate_items(invoice['Items']))

    # Replace total
    template = template.replace("{{total_amount}}", f"${round(invoice['Total Amount'], 2)}")
    return template

def populate_items(items):
    items_html = ""
    for item in items:
        item_html = f"""
            <tr class="item">
                <td>{item['Item Name']}</td>
                <td>${item['Unit Price (in USD)']}</td>
            </tr>
            """
        items_html += item_html

    return items_html


def save_invoices(pdf_files):
    output_dir = os.path.join(os.path.dirname(__file__), "./invoices/")
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    progress_bar = tqdm(range(len(pdf_files)), desc="Saving Invoices\t\t\t\t", unit="invoice", leave=True, file=sys.stdout)

    for idx, pdf in enumerate(pdf_files):
        # Ensure the filename is unique by appending a counter or timestamp
        file_name = f"{idx + 1}_{int(time.time() * 1000)}.pdf"
        file_path = os.path.join(output_dir, file_name)
        try:
            # Open the file in write-binary mode and save the PDF content
            with open(file_path, "wb") as f:
                pdf_data = pdf["file"].getvalue()
                if not pdf_data:
                    continue  # Skip if the PDF data is empty
                f.write(pdf_data)

            progress_bar.set_postfix_str(f"\033[32m{idx + 1}/{len(pdf_files)}\033[0m", refresh=True)
            progress_bar.update(1)
        except Exception as e:
            print(f"Error saving {pdf['name']}: {e}")