#Task 1: image_downloader_single.py (single threadedd)

import requests
import time
from pathlib import Path

IMG_COUNT = 20
SAVE_DIR = Path("downloads_single")
SAVE_DIR.mkdir(exist_ok=True)

#Function to download images.
def download_image(index: int) -> None:
    url = "https://picsum.photos/200"   #using this site to download images.
    response = requests.get(url)
    if response.status_code == 200:
        with open(SAVE_DIR / f"image_{index}.jpg", "wb") as f:
            f.write(response.content)
    else:
        print(f"Failed to download image {index}")

def main():
    start = time.perf_counter()
    for i in range(IMG_COUNT):
        download_image(i)
    end = time.perf_counter()
    print(f"Single-threaded download took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
