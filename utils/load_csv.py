import os

import pandas as pd

def load_csv(file_path):
    data = pd.read_csv(file_path)  # Read the CSV into a pandas DataFrame
    return data.values.tolist()