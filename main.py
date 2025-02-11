from datetime import datetime

from generate_invoices.generate_invoices import generate_invoices
from utils.time_calculator import time_gap


def main():
    start_time = datetime.now()
    user_input = int(input("How many Invoices do you want to generate: ") ) # This will get the input as a string
    generate_invoices(user_input)
    end_time = datetime.now()
    time_gap(start_time, end_time)
if __name__ == "__main__":
    main()