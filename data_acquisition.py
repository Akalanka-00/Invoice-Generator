import os
import re

from image_processing.signature_bg_remove import process_all_signatures
from utils.load_csv import load_csv


def amazon_data():
    target_directory = './data'
    absolute_path = os.path.abspath(target_directory)
    amazon_file_name = "Amazon_Mobile_Data.csv"

    data = load_csv(os.path.join(absolute_path, amazon_file_name))
    filtered_data = filter_columns(data)
    return filtered_data


def signature_data():
    target_directory = './data/signatures/Sample_Signature/sample_Signature/genuine'
    absolute_path = os.path.abspath(target_directory)

    # List all PNG files in the directory
    png_files = [f for f in os.listdir(absolute_path) if f.endswith('.png')]

    # Dictionary to store unique signatures by person ID (ZZZ)
    unique_signatures = {}

    # Regular expression to extract person ID (ZZZ) from filename
    pattern = re.compile(r"NFI-\d{3}\d{2}(\d{3})")

    for file in png_files:
        match = pattern.match(file)
        if match:
            person_id = match.group(1)  # Extract ZZZ (person's ID whose signature is in the photo)
            if person_id not in unique_signatures:  # Store only one sample per person
                unique_signatures[person_id] = file

    signature_list = list(unique_signatures.values())
    processed_signature_list = process_all_signatures(target_directory, signature_list)

    return processed_signature_list


def filter_columns(data):
    filtered_data = []

    # Iterate over each row in the data
    for row in data:
        # Check if the name already exists in filtered_data
        if not any(item["name"] == row[1] for item in filtered_data):
            # Append the row only if the name is not already present
            filtered_data.append({"id": row[0], "name": row[1], "price": currency_refactor(row[2])})
    return filtered_data


def currency_refactor(currency):
    amount = currency.replace('₹', '').replace(',', '').strip()
    exchange_rate = 0.012
    usd_amount = float(amount) * exchange_rate
    return round(usd_amount, 2)