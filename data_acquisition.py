import os

from utils.load_csv import load_csv


def amazon_data():
    target_directory = './data'
    absolute_path = os.path.abspath(target_directory)
    amazon_file_name = "Amazon_Mobile_Data.csv"

    data = load_csv(os.path.join(absolute_path, amazon_file_name))
    filtered_data = filter_columns(data)
    return filtered_data

def filter_columns(data):
    filtered_data = []
    for row in data:
        filtered_data.append({"id": row[0], "name": row[1], "price": currency_refactor(row[2])})
    return filtered_data

def currency_refactor(currency):
    amount = currency.replace('₹', '').replace(',', '').strip()
    exchange_rate = 0.012
    usd_amount = float(amount) * exchange_rate
    return round(usd_amount, 2)