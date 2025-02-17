import shutil

def download_from_colab(is_colab):
    if is_colab:
        print("Downloading the invoices...")
        from google.colab import files

        # Specify the path to the folder you want to zip
        folder_path = './invoices'

        # Specify the path to save the zip file
        zip_file_path = '/content/invoices.zip'

        # Create a zip archive of the folder
        shutil.make_archive(zip_file_path.replace('.zip', ''), 'zip', folder_path)
        files.download(zip_file_path)

