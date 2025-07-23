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
