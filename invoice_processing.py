import random
import sys
from datetime import datetime

from faker import Faker
from tqdm.auto import tqdm

from image_processing.company_logo_generator import generate_modern_logo
from image_processing.signature_bg_remove import process_all_signatures

fake = Faker()

MY_COMPANY = fake.company()
MY_ADDRESS = fake.address()
MY_EMAIL = fake.email()
MY_PHONE = fake.phone_number()

def generate_invoice_dataset(data, no_of_invoices=1):
    invoices = []
    company_list = generate_companies(data["signature"])
    progress_bar = tqdm(range(no_of_invoices), desc="Generating Invoices\t\t\t", unit="invoice", leave=True, file=sys.stdout)

    if data is None:
        raise ValueError("Error: 'data' is None. Make sure it is properly initialized.")
    for i in range(no_of_invoices):
        invoices.append(generate_invoice_data(data, random.sample(company_list, 1)[0]))
        progress_bar.set_postfix_str(f"\033[32m{i + 1}/{no_of_invoices}\033[0m", refresh=True)
        progress_bar.update(1)
    return invoices
    pass

def generate_invoice_data(data, seller_company):

    customer = generate_customer()
    items_to_purchase = generate_items_to_purchase(data["amazon"])
    invoice_number = datetime.now().strftime('%Y%m%d%H%M%S')
    invoice_date = datetime.now().strftime('%Y-%m-%d')
    # Initialize total amount
    total_amount = 0
    invoice_items = []

    # Calculate total for each item based on the selected quantity
    for item in items_to_purchase:
        # Find the product in the amazon data
        for product in data["amazon"]:
            if product["name"] == item["name"]:
                unit_price = product["price"]
                quantity = item["quantity"]
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

    invoice = {
        'Invoice Number': invoice_number,
        'Invoice Date': invoice_date,
        'Invoice Time': datetime.now().strftime('%H:%M:%S'),
        'Customer': customer, #bill to
        'Items': invoice_items,
        'Total Amount': total_amount,
        'Tax Amount': tax_amount,
        'Tax Rate': int((tax_rate*100)),
        'Total Amount (with Tax)': total_amount_with_tax,
        'Company': seller_company,
        'Due Date': '2025-04-25'
    }

    return invoice


def generate_items_to_purchase(amazon_data, num_items=3):

    selected_products = random.sample(amazon_data, num_items)

    items_to_purchase = []

    for product in selected_products:
        product_name = product["name"]  # Assuming product title is in the first column
        quantity = random.randint(1, 5)
        items_to_purchase.append({"name": product_name, "quantity":quantity})

    return items_to_purchase

def generate_customer():
    customer = {
        'Name': MY_COMPANY,
        'Address': MY_ADDRESS,
        'Email': MY_EMAIL,
        'Phone': MY_PHONE,
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

def generate_companies(signatures):
    companies = []
    for signature in signatures:
        company = fake.company()
        address = fake.address()
        email = fake.email()
        phone = fake.phone_number()
        logo = generate_modern_logo(company)
        company = {
           'company_name': company,
            'address': address,
            'email': email,
            'phone': phone,
            'logo': logo,
            'signature': signature,
            'position': fake.job(),
            'web': fake.url(),
            'city': fake.city(),
            'country': fake.country()
                   }
        companies.append(company)
    return companies
