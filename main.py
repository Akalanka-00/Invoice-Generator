from data_acquisition import amazon_data
from data_preparation import clean_data, download_signatures_dataset, clear_caches, download_amazon_data
from utils.init_kaggle import init_kaggle


def main():
    init_kaggle()

    # user_input = int(input("How many Invoices do you want to generate: ") )
    # start_time = datetime.now()
    #
    # end_time = datetime.now()
    # time_gap(start_time, end_time)

    #data_preprocessing()
    data_acquisition()

def data_preprocessing():
    is_colab = init_kaggle()
    clean_data()

    download_amazon_data()
    download_signatures_dataset()
    clear_caches()
    print("Data preparation is complete.")

def data_acquisition():
    amazon_data()

if __name__ == "__main__":
    main()