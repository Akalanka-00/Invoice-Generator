import os

from utils.load_csv import load_csv


def amazon_data():
    target_directory = './data'
    absolute_path = os.path.abspath(target_directory)
    amazon_file_name = "Amazon_Mobile_Data.csv"

    data = load_csv(os.path.join(absolute_path, amazon_file_name))
    filtered_data = filter_columns(data)
    print(filtered_data)

def filter_columns(data):
    filtered_data = []
    for row in data:
        filtered_data.append(row[1])
    return filtered_data