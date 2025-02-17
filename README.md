# Invoice Generator

## Project Overview

This project generates invoices as PDF files based on user input. It utilizes datasets from Kaggle (Amazon Mobile Phones dataset and Handwritten Signatures dataset) and incorporates Python libraries to generate realistic invoices.

## Features

- Downloads the required datasets from Kaggle.
- Generates invoices based on a given number of invoices specified by the user.
- Saves the generated invoices as PDF files.
- Uses real-world product data from the Amazon Mobile Phones dataset.
- Incorporates signatures from the Handwritten Signatures dataset.
- Supports a clean start option to re-fetch data if required.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [Python's official website](https://www.python.org/downloads/).

### Required Dependencies

Install the necessary Python packages using pip:

```sh
pip install tqdm pdfkit faker pandas kagglehub
pip install --upgrade kagglehub
```

## Dataset Download

Before running the project, download the required datasets using `kagglehub`:

```python
import kagglehub

# Download Amazon Mobile Phones dataset
kagglehub.dataset_download("daishinkan002/amazon-mobile-dataset")

# Download Handwritten Signatures dataset
kagglehub.dataset_download("divyanshrai/handwritten-signatures")
```

## Running the Project

1. Ensure all dependencies are installed.
2. Run the main script and specify the number of invoices to generate:
   ```sh
   python main.py
   ```
3. Enter the number of invoices when prompted.
4. The invoices will be generated and saved as PDF files in the designated directory.

### Clean Start Option

The project includes a parameter called `IS_CLEAN_START_REQUIRED` in `main.py`. If set to `True`, it will delete all existing data files and re-fetch them from Kaggle before generating invoices. This ensures that the latest dataset is always used.

## File Structure

```
project-folder/
│── data/                     # Contains downloaded datasets
│── invoices/                 # Stores generated PDF invoices
│── templates/                # HTML templates for invoice generation
│── utils/                    # Utility scripts for various tasks
│── main.py                   # Main script to run the project
│── invoice_processing.py     # Handles invoice generation
│── requirements.txt          # List of dependencies
│── README.md                 # Project documentation
```

## License

This project is open-source and available for personal and educational use.

## Contributions

Contributions are welcome! Feel free to submit a pull request or report any issues.

## Contact

For any inquiries or issues, please reach out via GitHub or email.

