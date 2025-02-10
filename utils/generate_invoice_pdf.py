import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
# from templates.basic import generate_invoice_title, generate_customer_details, generate_items_list, generate_totals

def generate_invoice_pdf(invoice_data, file_name="invoice.pdf"):
    # Create a canvas object to write the PDF
    file_path = os.path.join(os.path.dirname(__file__), "../invoices/" + file_name)
    os.makedirs(os.path.join(os.path.dirname(__file__), "../invoices/"), exist_ok=True)
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Set up margins and initial positions
    margin = 30
    y_position = height - margin

    # Generate Invoice Title and Basic Information
    y_position = generate_invoice_title(c, invoice_data, width, y_position)
    if y_position < margin:  # If there is not enough space, add a page
        c.showPage()
        y_position = height - margin
        y_position = generate_invoice_title(c, invoice_data, width, y_position)

    # Generate Customer Details
    y_position = generate_customer_details(c, invoice_data['Customer'], y_position)
    if y_position < margin:  # If there is not enough space, add a page
        c.showPage()
        y_position = height - margin
        y_position = generate_customer_details(c, invoice_data['Customer'], y_position)

    # Generate Items List
    y_position = generate_items_list(c, invoice_data['Items'], y_position)
    if y_position < margin:  # If there is not enough space, add a page
        c.showPage()
        y_position = height - margin
        y_position = generate_items_list(c, invoice_data['Items'], y_position)

    # Generate Totals
    y_position = generate_totals(c, invoice_data, y_position)
    if y_position < margin:  # If there is not enough space, add a page
        c.showPage()
        y_position = height - margin
        y_position = generate_totals(c, invoice_data, y_position)

    # Save the PDF file
    c.save()

# Example of how to handle the layout for the individual sections:
def generate_invoice_title(c, invoice_data, width, y_position):
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, y_position, f"Invoice Number: {invoice_data['Invoice Number']}")
    y_position -= 20
    c.drawString(100, y_position, f"Invoice Date: {invoice_data['Invoice Date']}")
    y_position -= 40  # Space before customer details
    return y_position

def generate_customer_details(c, customer, y_position):
    c.setFont("Helvetica", 10)
    c.drawString(100, y_position, f"Customer Name: {customer['Name']}")
    y_position -= 15
    c.drawString(100, y_position, f"Address: {customer['Address']}")
    y_position -= 15
    c.drawString(100, y_position, f"Email: {customer['Email']}")
    y_position -= 15
    c.drawString(100, y_position, f"Phone: {customer['Phone']}")
    y_position -= 40  # Space before items list
    return y_position

def generate_items_list(c, items, y_position):
    c.setFont("Helvetica", 10)
    for item in items:
        c.drawString(100, y_position, f"Item: {item['Item Name']} x{item['Quantity']} @ ${item['Unit Price (in USD)']:.2f}")
        y_position -= 15
        c.drawString(100, y_position, f"Total: ${item['Total']:.2f}")
        y_position -= 20
    return y_position

def generate_totals(c, invoice_data, y_position):
    c.setFont("Helvetica-Bold", 12)
    c.drawString(100, y_position, f"Total Amount: ${invoice_data['Total Amount']:.2f}")
    y_position -= 15
    c.drawString(100, y_position, f"Tax Amount: ${invoice_data['Tax Amount']:.2f}")
    y_position -= 15
    c.drawString(100, y_position, f"Total (with Tax): ${invoice_data['Total Amount (with Tax)']:.2f}")
    return y_position
