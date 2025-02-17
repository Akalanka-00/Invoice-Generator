import os
import kagglehub
import zipfile
import shutil

#Clean data
def clean_data():
    target_directory = './data'
    if os.path.exists(target_directory):
        shutil.rmtree(target_directory)
        print(f"All files and folders inside {target_directory} have been deleted.")

    os.makedirs(target_directory, exist_ok=True)
    print(f"The {target_directory} folder has been recreated.")


# Download Amazon_Mobile_Data.csv
def download_amazon_data():
    target_directory = './data'
    absolute_path = os.path.abspath(target_directory)
    amazon_file_name = "Amazon_Mobile_Data.csv"

    if not os.path.exists(os.path.join(absolute_path, amazon_file_name)):
        path = kagglehub.dataset_download("daishinkan002/amazon-mobile-dataset")
        source_path_amazon = os.path.join(path, amazon_file_name)
        if os.path.isfile(source_path_amazon):
            shutil.move(source_path_amazon, absolute_path)
            print(f"Moved {amazon_file_name} to the 'data' folder.")
        else:
            print(f"File {amazon_file_name} not found.")
    else:
        print(f"File {amazon_file_name} already exists.")


# Download Handwritten Signatures Dataset
def download_signatures_dataset():
    target_directory = './data'
    absolute_path = os.path.abspath(target_directory)

    os.makedirs(absolute_path, exist_ok=True)

    # Download the Handwritten Signatures Dataset
    path_signatures = kagglehub.dataset_download("divyanshrai/handwritten-signatures")

    zip_file_name = 'signatures.zip'
    zip_file_path = os.path.join(target_directory, zip_file_name)

    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(path_signatures):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, path_signatures))

    print(f"Zip file created at: {zip_file_path}")
    extract_zip(target_directory, zip_file_path)

#Extract the zip file
def extract_zip(target_directory, zip_file_path):
    extract_to_folder = os.path.join(target_directory, 'signatures')
    os.makedirs(extract_to_folder, exist_ok=True)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to_folder)
    print(f"Zip file extracted to {extract_to_folder}")
    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)
        print(f"Zip file {zip_file_path} has been deleted.")


#Clear caches
def clear_caches():
    datasets_path = os.path.expanduser('~/.cache/kagglehub')
    if os.path.exists(datasets_path):
        shutil.rmtree(datasets_path)
        print(f"All files and folders inside {datasets_path} have been deleted.")