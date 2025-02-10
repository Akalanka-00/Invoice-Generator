from utils.currency_convert import currency_convert
from utils.load_csv import load_csv


def amazon_mobile_data():
    data = load_csv("Amazon_Mobile_Data.csv")
    for product in data:
        amount_str = product[2]
        cleaned_str = amount_str.replace('₹', '').replace(',', '').strip()
        product[2] = currency_convert(cleaned_str)
    return data
