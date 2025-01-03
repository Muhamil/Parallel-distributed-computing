# Python Threading Examples

This repository contains a collection of Python scripts demonstrating various threading and synchronization concepts. Each script showcases a different aspect of concurrent programming using threads, locks, semaphores, and queues.

---

## Table of Contents
- [Overview](#overview)
- [Scripts](#scripts)
  - [RLOCK.PY](#rlockpy)
  - [SEMAPHORE.PY](#semaphorepy)
  - [THREAD_DEFINITION.PY](#thread_definitionpy)
  - [THREAD_DETERMINE.PY](#thread_determinepy)
  - [THREAD_NAME_AND_PROCESSES.PY](#thread_name_and_processespy)
  - [THREAD_WITH_QUEUE.PY](#thread_with_queuepy)
- [Usage](#usage)
- [License](#license)

---

## Overview
These scripts are designed to:
- Demonstrate threading concepts in Python.
- Provide real-world examples of producer-consumer problems.
- Explore synchronization mechanisms such as `RLock`, `Semaphore`, and `Queue`.

Each script is standalone and can be executed to observe the threading behavior in action.

---

## Scripts

### **RLOCK.PY**
Simulates a producer-consumer scenario with `RLock` (Reentrant Lock):
- **Producer** adds items to a shared box.
- **Consumer** removes items from the box.
- Uses a reentrant lock to ensure thread-safety during item modifications.

---

### **SEMAPHORE.PY**
Demonstrates producer-consumer behavior with a semaphore:
- The **producer** produces an item and signals the **consumer**.
- The **consumer** waits until an item is available for processing.
- Logs each thread's actions for better traceability.

---

### **THREAD_DEFINITION.PY**
A basic example of creating and joining threads:
- Demonstrates sequential execution by joining threads.
- Prints the thread number for each execution.

---

### **THREAD_DETERMINE.PY**
Simulates thread behavior with named threads:
- Runs distinct functions (`function_A`, `function_B`, `function_C`) in separate threads.
- Uses `currentThread()` to identify the executing thread.

---

### **THREAD_NAME_AND_PROCESSES.PY**
Custom thread class example:
- Inherits from `Thread` to define custom behavior.
- Overridden `run()` method for specific tasks.
- Demonstrates thread naming and execution flow.

---

### **THREAD_WITH_QUEUE.PY**
Implements a producer-consumer model using `queue.Queue`:
- The **producer** generates random items and places them in the queue.
- Multiple **consumers** retrieve items from the queue.
- Ensures thread-safety with `Queue`'s built-in synchronization.

---

