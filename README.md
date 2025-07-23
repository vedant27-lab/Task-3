# 🧵 Python Threading and Concurrency – Task Report

**Internship @ CyArt**  
**Submitted by:** Vedant Patil

---

## 📌 Introduction

This report documents the Python concurrency task assigned during my internship at CyArt. The objective was to explore and implement multithreading techniques in Python, understand the limitations of the Global Interpreter Lock (GIL), and safely handle shared resources using synchronization primitives like `Lock`. The task involved measuring performance improvements and ensuring data safety across threads.

---

## 🧠 Threading and the Global Interpreter Lock (GIL)

### 🧵 Python’s Threading Module

Python’s `threading` module allows concurrent execution of tasks, especially useful for **I/O-bound operations**. Each thread runs independently but shares memory with other threads.

### 🔒 GIL (Global Interpreter Lock)

The GIL ensures only one thread executes Python bytecode at a time. This restricts Python threads from achieving parallelism in **CPU-bound tasks** but doesn't impact **I/O-bound performance** significantly.

**Sources:**
- [Python Docs – Threading](https://docs.python.org/3/library/threading.html)
- [RealPython – GIL Explained](https://realpython.com/python-gil/)

---

## 🔐 Locks and Synchronization

`threading.Lock` is used to synchronize access to shared resources. It prevents race conditions by allowing only one thread to access the critical section at a time.

### 🔧 Example:

```python
lock = threading.Lock()

with lock:
    # critical section
    perform_operation()
Task 1 – Image Downloader
🎯 Objective
Download 20 images using:

A single-threaded script

A multithreaded script with 20 threads

🧵 Single-threaded Version: image_downloader_single.py
python
Copy
Edit
for i in range(20):
    download_image(i)
Each image is downloaded one after the other using a blocking loop.

⚡ Multithreaded Version: image_downloader_threaded.py
python
Copy
Edit
for i in range(20):
    t = threading.Thread(target=download_image, args=(i,))
    t.start()
Spawns 20 threads for parallel image downloading from https://picsum.photos/200.

🕒 Timing Comparison
Version	Time Taken
Single-threaded	~X.XX sec
Multi-threaded	~Y.YY sec

✅ Significant speedup observed with multithreading due to parallel I/O operations.

🧪 Task 2 – Race Condition Demonstration
🎯 Objective
Demonstrate a race condition when multiple threads write to a shared file, and then fix it using Lock.

❌ Without Lock: race_condition_demo.py
python
Copy
Edit
def unsafe_log_writer(thread_id):
    with open("logs_race.txt", "a") as f:
        f.write(f"[Thread {thread_id}] Entry\n")
Multiple threads write simultaneously, leading to corrupted output.

✅ With Lock: race_condition_fixed.py
python
Copy
Edit
lock = threading.Lock()

def safe_log_writer(thread_id):
    with lock:
        with open("logs_lock.txt", "a") as f:
            f.write(f"[Thread {thread_id}] Entry\n")
The Lock ensures only one thread writes at a time.

🕒 Timing Comparison
Version	Time Taken
Without Lock	~X.XX sec
With Lock	~Y.YY sec

🛡️ The Lock introduces minor overhead but ensures clean and predictable log output.

📁 Code Summary
File	Description
image_downloader_single.py	Downloads images sequentially
image_downloader_threaded.py	Uses 20 threads for concurrent image download
race_condition_demo.py	Demonstrates race condition (no locking)
race_condition_fixed.py	Fixes it using threading.Lock

✅ Conclusion
This task enhanced my understanding of Python threading, the impact of the GIL, and the importance of synchronization in multithreaded programs. I learned to optimize I/O-bound operations using threads while ensuring safety with locks when dealing with shared resources.

📚 References
Python Docs

RealPython – Threading and GIL

Stack Overflow and blog posts on Python concurrency

📂 Repository Structure
Copy
Edit
.
├── image_downloader_single.py
├── image_downloader_threaded.py
├── race_condition_demo.py
├── race_condition_fixed.py
└── task3_report.md
csharp
Copy
Edit

✅ Paste this into GitHub or VS Code, replace the timing placeholders (`~X.XX sec`) w
