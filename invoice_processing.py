import random
import sys
from datetime import datetime

from faker import Faker
from tqdm import tqdm

fake = Faker()
inventory = []

def generate_invoice_dataset(data, no_of_invoices=1):
    invoices = []
    progress_bar = tqdm(range(no_of_invoices), desc="Generating Invoices\t\t\t", unit="invoice", leave=True, file=sys.stdout)

    if data is None:
        raise ValueError("Error: 'data' is None. Make sure it is properly initialized.")
    for i in range(no_of_invoices):
        invoices.append(generate_invoice_data(data))
        progress_bar.set_postfix_str(f"\033[32m{i + 1}/{no_of_invoices}\033[0m", refresh=True)
        progress_bar.update(1)
    return invoices
    pass

def generate_invoice_data(data):
    customer = generate_customer()
    items_to_purchase = generate_items_to_purchase(data)
    invoice_number = datetime.now().strftime('%Y%m%d%H%M%S')
    invoice_date = datetime.now().strftime('%Y-%m-%d')

    # Initialize total amount
    total_amount = 0
    invoice_items = []

    # Calculate total for each item based on the selected quantity
    for item, quantity in items_to_purchase.items():
        # Find the product in the amazon data
        for product in inventory:
            if product["name"] == item:
                unit_price = product["price"]  # The price is in the 3rd column
                item_total = unit_price * quantity
                invoice_items.append({
                    'Item Name': item,
                    'Quantity': quantity,
                    'Unit Price': unit_price,
                    'Total': item_total
                })
                total_amount += item_total
    # Apply tax (if any)
    tax_rate = 0.18  # Example: 18% tax
    tax_amount = total_amount * tax_rate
    total_amount_with_tax = total_amount + tax_amount
    company = generate_company()

    invoice = {
        'Invoice Number': invoice_number,
        'Invoice Date': invoice_date,
        'Customer': customer,
        'Items': invoice_items,
        'Total Amount': total_amount,
        'Tax Amount': tax_amount,
        'Total Amount (with Tax)': total_amount_with_tax,
        'Company': company,
        'Due Date': '2025-04-25'
    }
    return invoice


def generate_items_to_purchase(amazon_data, num_items=3):

    selected_products = random.sample(amazon_data, num_items)

    items_to_purchase = {}

    for product in selected_products:
        product_name = product["name"]  # Assuming product title is in the first column
        quantity = random.randint(1, 5)
        items_to_purchase[product_name] = quantity

    return items_to_purchase

def generate_customer():
    customer = {
        'Name': fake.name(),
        'Address': fake.address(),
        'Email': fake.email(),
        'Phone': fake.phone_number(),
        'Country': fake.country(),
        'City': fake.city(),
        'Postal Code': fake.zipcode()
    }
    return customer

def generate_company():
    # Generate the invoice
    company = {'Name': 'Sparksuite, Inc.',
               'Address': '12345 Sunny Road, Sunnyville, CA 12345'
               }
    return company