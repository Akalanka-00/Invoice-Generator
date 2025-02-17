from datetime import datetime
from data_acquisition import amazon_data
from data_preparation import clean_data, download_signatures_dataset, clear_caches, download_amazon_data
from invoice_processing import generate_invoice_dataset
from invoice_generation import apply_invoice_templates, save_invoices
from utils.html_to_pdf import convert_html_to_pdfs
from utils.init_kaggle import init_kaggle
from utils.time_calculations import perform_time

IS_CLEAN_START_REQUIRED = False
def main():
    is_colab = init_kaggle()

    user_input = int(input("How many Invoices do you want to generate: ") )
    start_time = datetime.now()

    data_preprocessing()
    data = data_acquisition()
    invoices = generate_invoice_dataset(data, user_input)
    html_invoices = apply_invoice_templates(invoices)
    pdf_invoices = convert_html_to_pdfs(html_invoices)
    save_invoices(pdf_invoices)

    end_time = datetime.now()
    perform_time(start_time, end_time)

def data_preprocessing():

    clean_data(IS_CLEAN_START_REQUIRED)
    download_amazon_data()
    download_signatures_dataset()
    clear_caches()
    print("Data preparation is complete.")

def data_acquisition():
    _amazon_data = amazon_data()
    return _amazon_data

if __name__ == "__main__":
    main()