import os
import random
import string
import sys
import time
from datetime import datetime

from tqdm import tqdm
import random

from data_process.amazon_mobile_data import amazon_mobile_data
from utils.generate_invoice import generate_invoice
from utils.generate_invoice_from_html import generate_invoice_html
from utils.generate_items_to_purchase import generate_items_to_purchase
from utils.generate_random_customer import generate_customer
from utils.html_to_pdf import convert_html_to_pdfs


def generate_invoices(no_of_invoices=1):
    invoices = []
    inventory = amazon_mobile_data()
    progress_bar = tqdm(range(no_of_invoices), desc="Generating Invoices", unit="invoice", leave=True, file=sys.stdout)
    for i in range (no_of_invoices):
        customer = generate_customer()
        items_to_purchase = generate_items_to_purchase(inventory)
        generated_invoice = generate_invoice(customer, items_to_purchase, inventory)
        # generate_invoice_pdf(generated_invoice, generate_random_text() +".pdf")
        invoice = generate_invoice_html(generated_invoice, file_name=generate_random_text() +".pdf", template_name=select_template())
        invoices.append(invoice)
        progress_bar.set_postfix_str(f"\033[32m{progress_bar.n + 1}/{no_of_invoices}\033[0m", refresh=True)
        progress_bar.update(1)

    return invoices

def save_invoices(invoices):
    pdf_invoice = convert_html_to_pdfs(invoices)
    file_path = os.path.join(os.path.dirname(__file__), "../invoices/")
    save_pdfs(pdf_invoice, file_path)




def generate_random_text():
    # Generate a random number sequence with 12 digits (for example)
    random_text = ''.join(random.choices(string.digits, k=12))  # 12 digits long

    return random_text

def select_template():
    templates = ["basic.html", "basic_mirror.html"]
    num = random.randint(1, 9)  # Generate a random integer between 1 and 9
    return templates[0] if num % 3 == 0 else templates[1]

def save_pdfs(pdf_files, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    progress_bar = tqdm(range(len(pdf_files)), desc="Saving Invoices", unit="invoice", leave=True, file=sys.stdout)

    for idx, pdf in enumerate(pdf_files):
        # Ensure the filename is unique by appending a counter or timestamp
        file_name = f"{int(time.time() * 1000)}_{idx + 1}.pdf"
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

