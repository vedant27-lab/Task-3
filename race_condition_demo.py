#Task 2: race_condition_demo.py (unsafe : without 'lock' )

import threading
import time
from pathlib import Path

LOG_FILE = Path("logs_race.txt")
NUM_THREADS = 10
ITERATIONS = 100

#to clear previous log files
LOG_FILE.unlink(missing_ok=True)


def log_writer(thread_id: int) -> None:
    for i in range(ITERATIONS):
        with open(LOG_FILE, "a") as f:
            f.write(f"[Thread {thread_id}] Log entry {i}\n")

#main function.
def main():
    threads = []
    start = time.perf_counter()

    for i in range(NUM_THREADS):
        t = threading.Thread(target=log_writer, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()
    print(f"Unsafe logging took {end - start:.2f} seconds")

if __name__ == "__main__":
    main()
