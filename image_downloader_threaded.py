#Task 1: image_downloader_threaded.py (multi threaded)

import threading
import requests
import time
from pathlib import Path

IMG_COUNT = 20
SAVE_DIR = Path("downloads_threaded")
SAVE_DIR.mkdir(exist_ok=True)

#Function to download images.
def download_image(index: int) -> None:
    url = "https://picsum.photos/200"
    response = requests.get(url)
    if response.status_code == 200:
        with open(SAVE_DIR / f"image_{index}.jpg", "wb") as f:
            f.write(response.content)
    else:
        print(f"Thread {index}: failed to download image")

def main():
    threads = []
    start = time.perf_counter()

    for i in range(IMG_COUNT):
        t = threading.Thread(target=download_image, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"Threaded download took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
