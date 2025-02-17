import os


def init_kaggle():
    try:
        from google.colab import files
        is_colab = True
    except ImportError:
        is_colab = False

    if is_colab:
        if not os.path.exists('/root/.kaggle/kaggle.json'):
            uploaded = files.upload()

            os.makedirs('/root/.kaggle', exist_ok=True)
            os.rename('kaggle.json', '/root/.kaggle/kaggle.json')

            os.chmod('/root/.kaggle/kaggle.json', 600)
        else:
            print("kaggle.json already exists.")
    else:
        print("You are running on a local machine. Please upload the file manually.")
    return is_colab