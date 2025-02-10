import random
import string
import sys
from datetime import datetime

from tqdm import tqdm
import random

from data_process.amazon_mobile_data import amazon_mobile_data
from utils.generate_invoice import generate_invoice
from utils.generate_invoice_from_html import generate_invoice_html
from utils.generate_invoice_pdf import generate_invoice_pdf
from utils.generate_items_to_purchase import generate_items_to_purchase
from utils.generate_random_customer import generate_customer


def generate_invoices(no_of_invoices=1):
    invoices = []
    inventory = amazon_mobile_data()
    progress_bar = tqdm(range(no_of_invoices), desc="Generating Invoices", unit="invoice", leave=True, file=sys.stdout)
    for i in range (no_of_invoices):
        customer = generate_customer()
        items_to_purchase = generate_items_to_purchase(inventory)
        generated_invoice = generate_invoice(customer, items_to_purchase, inventory)
        invoices.append(generated_invoice)
        # generate_invoice_pdf(generated_invoice, generate_random_text() +".pdf")
        generate_invoice_html(generated_invoice, file_name=generate_random_text() +".pdf")
        progress_bar.set_postfix_str(f"\033[32m{progress_bar.n + 1}/{no_of_invoices}\033[0m", refresh=True)
        progress_bar.update(1)

def generate_random_text():
    # Generate a random number sequence with 12 digits (for example)
    random_text = ''.join(random.choices(string.digits, k=12))  # 12 digits long

    return random_text

