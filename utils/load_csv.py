import os

import pandas as pd

def load_csv(file_name):
    file_path = os.path.join(os.path.dirname(__file__), "../data/"+file_name)
    data = pd.read_csv(file_path)  # Read the CSV into a pandas DataFrame
    return data.values.tolist()