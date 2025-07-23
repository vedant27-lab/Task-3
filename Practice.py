import threading
import time

def crawl(link, delay=3):
    print(f"crawl started for {link}\n")
    time.sleep(delay)
    print(f"crawn ended for {link}\n")

links = [
    "https://python.org",
    "https://docs.python.org",
    "https://peps.python.org",
]
Threads = []
for link in links:
    t = threading.Thread(target=crawl, args=(link,), kwargs={"delay":3})
    Threads.append(t)

for t in Threads:
    t.start()

for t in Threads:
    t.join()