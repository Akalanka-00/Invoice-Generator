import os
import random
import sys
import time

from tqdm.auto import tqdm


def apply_invoice_templates(invoices):
    html_invoices = []
    templates = fetch_templates()
    for invoice in invoices:
        template = random.choice(templates)
        html_invoices.append(apply_template(invoice, template))
    return html_invoices


def apply_template(invoice, template):
    absolute_path = os.path.abspath(f'./templates/{template}')
    with open(absolute_path, 'r', encoding='utf-8') as file:
        template_content = file.read()
    template_content = populated_template(template_content, invoice)
    return template_content

def fetch_templates():
    directory_path = './templates'
    html_files = [file for file in os.listdir(directory_path) if file.endswith('consult_elite.html')]
    return html_files


def populated_template(template, invoice):
    # Replace top-level placeholders
    template = template.replace("{{invoice_number}}", invoice['Invoice Number'])
    template = template.replace("{{invoice_date}}", invoice['Invoice Date'])
    template = template.replace("{{invoice_time}}", invoice['Invoice Time'])
    template = template.replace("{{company_logo_url}}", invoice['Company']['logo'])

    # Company details
    template = template.replace("{{company_name}}", invoice['Company']['company_name'])
    template = template.replace("{{company_address}}", invoice['Company']['address'])
    template = template.replace("{{company_city}}", invoice['Company']['city'])
    template = template.replace("{{company_country}}", invoice['Company']['country'])
    template = template.replace("{{company_email}}", invoice['Company']['email'])
    template = template.replace("{{company_phone}}", invoice['Company']['phone'])
    template = template.replace("{{signature_image_url}}", invoice['Company']['signature'])
    template = template.replace("{{signed_by_name}}", invoice['Company']['company_name'])
    template = template.replace("{{signed_by_job_post}}", invoice['Company']['position'])
    template = template.replace("{{company_web}}", invoice['Company']['web'])

    # Customer details
    template = template.replace("{{customer_name}}", invoice['Customer']['Name'])
    template = template.replace("{{customer_address}}", invoice['Customer']['Address'])
    template = template.replace("{{customer_phone}}", invoice['Customer']['Phone'])

    # Calculate totals
    subtotal = invoice["Total Amount"]
    tax_amount = invoice["Tax Amount"]  # 18% tax
    tax_rate = invoice["Tax Rate"]
    grand_total = subtotal + tax_amount

    # Replace financial placeholders
    template = template.replace("{{subtotal}}", f"${subtotal:,.2f}")
    template = template.replace("{{tax_rate}}", str(tax_rate))
    template = template.replace("{{tax_amount}}", f"${tax_amount:,.2f}")
    template = template.replace("{{grand_total}}", f"${grand_total:,.2f}")

    # Generate items HTML
    items_html = populate_items(invoice['Items'])

    # Replace items loop section
    template = template.replace(
        '{% for item in items %}\n' +
        '                <tr>\n' +
        '                    <td class="col-num">{{loop.index}}</td>\n' +
        '                    <td class="product-title">{{item.title}}</td>\n' +
        '                    <td class="col-price">{{item.price}}</td>\n' +
        '                    <td class="col-qty">{{item.quantity}}</td>\n' +
        '                    <td class="col-total">{{item.price * item.quantity}}</td>\n' +
        '                </tr>\n' +
        '                {% endfor %}',
        items_html
    )

    return template


def html_img(abs_path):
    """Returns the absolute file URL for wkhtmltopdf to access the image."""
    script_dir = os.path.dirname(os.path.abspath(__file__))  # Get the script's directory
    # abs_path = os.path.abspath(os.path.join(str(script_dir), abs_path))  # Resolve absolute path
    return abs_path

def populate_items(items):
    items_html = ""
    for index, item in enumerate(items, start=1):
        item_total = item['Unit Price'] * item["Item Name"]['quantity']
        item_html = f"""
                <tr>
                    <td class="col-num">{index}</td>
                    <td class="product-title">{item["Item Name"]['name']}</td>
                    <td class="col-price">${item['Unit Price']:,.2f}</td>
                    <td class="col-qty">{item['Quantity']}</td>
                    <td class="col-total">${item_total:,.2f}</td>
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