from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


# Template to generate invoice title and basic info
def generate_invoice_title(c, invoice_data, width, height):
    c.setFont("Helvetica-Bold", 16)
    c.drawString(30, height - 40, f"Invoice Number: {invoice_data['Invoice Number']}")
    c.setFont("Helvetica", 12)
    c.drawString(30, height - 60, f"Invoice Date: {invoice_data['Invoice Date']}")


# Template to generate customer details
def generate_customer_details(c, customer, y_position):
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y_position, "Customer Details:")
    c.setFont("Helvetica", 10)

    customer_info = [
        f"Name: {customer['Name']}",
        f"Address: {customer['Address']}",
        f"Email: {customer['Email']}",
        f"Phone: {customer['Phone']}",
        f"Country: {customer['Country']}",
        f"City: {customer['City']}",
        f"Postal Code: {customer['Postal Code']}"
    ]

    for line in customer_info:
        y_position -= 15
        c.drawString(30, y_position, line)

    return y_position


# Template to generate items list
def generate_items_list(c, items, y_position):
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y_position, "Items Purchased:")
    y_position -= 15
    c.setFont("Helvetica", 10)

    for item in items:
        c.drawString(30, y_position, f"Item: {item['Item Name']}")
        y_position -= 15
        c.drawString(30, y_position,
                     f"Quantity: {item['Quantity']} | Unit Price (in USD): ${item['Unit Price (in USD)']}")
        y_position -= 15
        c.drawString(30, y_position, f"Total: ${item['Total']}")
        y_position -= 25

    return y_position


# Template to generate totals
def generate_totals(c, totals, y_position):
    c.setFont("Helvetica-Bold", 12)
    c.drawString(30, y_position, f"Total Amount: ${totals['Total Amount']:.2f}")
    y_position -= 15
    c.drawString(30, y_position, f"Tax Amount: ${totals['Tax Amount']:.2f}")
    y_position -= 15
    c.drawString(30, y_position, f"Total Amount (with Tax): ${totals['Total Amount (with Tax)']:.2f}")

    return y_position
