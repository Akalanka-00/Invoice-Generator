import os
import pdfkit

def generate_invoice_html(invoice_data, template_name="basic.html", file_name="invoice.pdf"):

    path_to_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'  # Update this with the correct path
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)
    file_path = os.path.join(os.path.dirname(__file__), "../invoices/" + file_name)
    os.makedirs(os.path.join(os.path.dirname(__file__), "../invoices/"), exist_ok=True)

    template_path = os.path.join(os.path.dirname(__file__), "../templates/" + template_name)

    # Read the HTML template
    with open(template_path, "r") as file:
        template = file.read()

    # Replace placeholders with actual invoice data
    template = template.replace("{{invoice_number}}", invoice_data['Invoice Number'])
    template = template.replace("{{invoice_date}}", invoice_data['Invoice Date'])
    template = template.replace("{{due_date}}", invoice_data['Due Date'])

    # Replace company details
    template = template.replace("{{company_name}}", invoice_data['Company']['Name'])
    template = template.replace("{{company_address}}", invoice_data['Company']['Address'])

    # Replace customer details
    template = template.replace("{{customer_name}}", invoice_data['Customer']['Name'])
    template = template.replace("{{customer_address}}", invoice_data['Customer']['Address'])

    # Loop through the items and replace them dynamically
    items_html = ""
    for item in invoice_data['Items']:
        item_html = f"""
        <tr class="item">
            <td>{item['Item Name']}</td>
            <td>${item['Unit Price (in USD)']}</td>
        </tr>
        """
        items_html += item_html

    # Replace item details
    template = template.replace("{{items}}", items_html)

    # Replace total
    template = template.replace("{{total_amount}}", f"${round(invoice_data['Total Amount'],2)}")

    pdf_path = file_path.replace(".html", ".pdf")
    if file_path.endswith(".pdf"):
        file_path = file_path.replace(".pdf", ".html")

    with open(file_path, "w") as file:
        file.write(template)

    save_html_as_pdf(file_path, pdf_path)





def save_html_as_pdf(html_path, pdf_path):
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    pdfkit.from_file(html_path, pdf_path, configuration=config)
    os.remove(html_path)
