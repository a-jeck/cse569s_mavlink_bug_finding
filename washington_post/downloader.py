import os
import requests
from time import sleep


START = 10000
STEP = 10
TARGET_SUCCESSFUL_DOWNLOADS = 10000
SAVE_DIR = 'input'
BASE_URL = 'https://docquery.fec.gov/dcdev/posted/'


os.makedirs(SAVE_DIR, exist_ok=True)

successful_downloads = 0
current = START

while successful_downloads < TARGET_SUCCESSFUL_DOWNLOADS:
    file_id = current
    url = f"{BASE_URL}{file_id}.fec"
    save_path = os.path.join(SAVE_DIR, f"{file_id}.fec")

    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200 and response.content.strip():
            with open(save_path, 'wb') as f:
                f.write(response.content)
            successful_downloads += 1
            print(f"Downloaded: {file_id} ({successful_downloads}/10000)")
        else:
            print(f"Skipped (not found or empty): {file_id}")
    except Exception as e:
        print(f"Error fetching {file_id}: {e}")

    current += STEP
    sleep(0.1)

print("Download complete.")
