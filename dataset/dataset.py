import os
import gdown

def download_dataset():
    dataset_folder = 'dataset'
    
    if not os.path.exists(dataset_folder):
        # Google Drive folder ID
        folder_id = '1cwf4gMXh3VTAw0R7O0bI0Sq5nks1Bejv'
        url = f'https://drive.google.com/uc?id={folder_id}'

        print("Downloading dataset from Google Drive...")
        gdown.download_folder(url, output=dataset_folder, quiet=False, use_cookies=False)
        print("✅ Dataset downloaded successfully to './dataset'")
    else:
        print("📁 Dataset folder already exists. Skipping download.")

if __name__ == '__main__':
    download_dataset()
