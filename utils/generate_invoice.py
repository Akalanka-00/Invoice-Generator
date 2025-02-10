from datetime import datetime

from data_process.amazon_mobile_data import amazon_mobile_data
from utils.generate_items_to_purchase import generate_items_to_purchase
from utils.generate_random_customer import generate_customer


def generate_invoice(customer_details, items, amazon_data):
    # Get the products from the fetched Amazon data
    invoice_number = datetime.now().strftime('%Y%m%d%H%M%S')
    invoice_date = datetime.now().strftime('%Y-%m-%d')

    # Initialize total amount
    total_amount = 0
    invoice_items = []

    # Calculate total for each item based on the selected quantity
    for item, quantity in items.items():
        # Find the product in the amazon data
        for product in amazon_data:
            if product[1]==item:
                unit_price = product[2]  # The price is in the 3rd column
                item_total = unit_price * quantity
                invoice_items.append({
                    'Item Name': item,
                    'Quantity': quantity,
                    'Unit Price (in USD)': unit_price,
                    'Total': item_total
                })
                total_amount += item_total

    # Apply tax (if any)
    tax_rate = 0.18  # Example: 18% tax
    tax_amount = total_amount * tax_rate
    total_amount_with_tax = total_amount + tax_amount

    # Generate the invoice
    company = {'Name': 'Sparksuite, Inc.',
               'Address': '12345 Sunny Road, Sunnyville, CA 12345'
               }

    invoice = {
        'Invoice Number': invoice_number,
        'Invoice Date': invoice_date,
        'Customer': customer_details,
        'Items': invoice_items,
        'Total Amount': total_amount,
        'Tax Amount': tax_amount,
        'Total Amount (with Tax)': total_amount_with_tax,
        'Company': company,
        'Due Date': '2025-04-25'
    }


    return invoice
