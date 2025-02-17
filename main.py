from datetime import datetime

from generate_invoices.generate_invoices import generate_invoices, save_invoices
from utils.html_to_pdf import convert_html_to_pdfs
from utils.time_calculator import time_gap


def main():
    start_time = datetime.now()
    user_input = int(input("How many Invoices do you want to generate: ") ) # This will get the input as a string
    invoices_html = generate_invoices(user_input)
    save_invoices(invoices_html)

    end_time = datetime.now()
    time_gap(start_time, end_time)


if __name__ == "__main__":
    main()