# Parallel and Concurrent Programming Examples

This repository demonstrates various concepts of parallel and concurrent programming using Python. Each script showcases a unique method or library for achieving parallelism, concurrency, or inter-process communication.

---

## Table of Contents
- [IPC.PY](#ipcpy)
- [MPI.PY](#mpipy)
- [MULTI_PROCESS.PY](#multi_processpy)
- [PCNM.PY](#pcnmpy)
- [PARALLILSM.PY](#parallilsmpy)
- [SHARED_MEM.PY](#shared_mempy)
- [SYNC.PY](#syncpy)
- [TASK_PARALILLSM.PY](#task_paralillsmpy)
- [FIBONACCI.PY](#fibonaccipy)
- [PIPE.PY](#pipepy)

---

### **IPC.PY**
Demonstrates inter-process communication using Python's `multiprocessing` module with a `Queue`.

- **Producer Process**: Generates integers (0–4) and places them into the queue.
- **Consumer Process**: Retrieves integers from the queue and processes them.
- **Purpose**: Demonstrates the producer-consumer pattern with multiprocessing.

![IPC](https://github.com/user-attachments/assets/78dcc083-0536-4f66-889f-d7d4322b9145)
---

### **MPI.PY**
Uses the `mpi4py` library to demonstrate inter-process communication in a distributed environment.

- **Rank 0**: Sends a dictionary to Rank 1.
- **Rank 1**: Receives and prints the dictionary.
- **Other Ranks**: Remain idle.
- **Purpose**: Demonstrates message passing in parallel computing.

![req2](https://github.com/user-attachments/assets/f9ab7724-6a12-4b40-b34e-eda18d009531)
---

### **MULTI_PROCESS.PY**
Compares multiprocessing and multithreading for a random number generation task.

- **Multiprocessing**: Spawns multiple processes for parallel execution.
- **Multithreading**: Uses threads to perform the same task concurrently.
- **Output**: Execution times for both methods.
- **Purpose**: Highlights performance differences between multiprocessing and multithreading.

![Multi Process](https://github.com/user-attachments/assets/414284f7-2825-47b8-b31e-82b16d27bec7)
---

### **PCNM.PY**
Demonstrates basic multiprocessing by calculating the square and cube of a number concurrently.

- **Process 1**: Computes the square of a number.
- **Process 2**: Computes the cube of a number.
- **Purpose**: Illustrates parallel task execution.

![PCNM](https://github.com/user-attachments/assets/fa455193-6591-4016-88c3-8d49d419ac6c)

---

### **PARALLILSM.PY**
Showcases data parallelism using NumPy for vector addition.

- **Key Feature**: Utilizes NumPy's internal parallelism for fast computation on large datasets.
- **Output**: Execution time and first 10 elements of the result.
- **Purpose**: Demonstrates efficient data parallelism with optimized libraries.

![parallelism](https://github.com/user-attachments/assets/e3176c4d-6502-4842-93e0-c5a0d53ca5a1)
---

### **SHARED_MEM.PY**
Demonstrates thread-safe shared memory access with locks.

- **Deposit Function**: Adds an amount to a shared balance.
- **Withdraw Function**: Subtracts an amount from the shared balance.
- **Purpose**: Highlights safe shared memory access in a multithreading environment.

![shared memory](https://github.com/user-attachments/assets/a5b253ef-8d27-44be-aeb1-de4b41e1ce30)

---

### **SYNC.PY**
Illustrates thread synchronization using a semaphore.

- **Semaphore**: Limits access to a shared resource to two threads at a time.
- **Threads**: Simulate concurrent access to a resource.
- **Purpose**: Demonstrates controlled access to shared resources using semaphores.

![sync](https://github.com/user-attachments/assets/01b585cd-9010-4699-a5d1-eb2319e6a5aa)
---

### **TASK_PARALILLSM.PY**
Demonstrates task parallelism using the `ThreadPoolExecutor`.

- **Tasks**: Executes two functions concurrently.
- **Purpose**: Highlights how to manage multiple tasks in parallel with high-level APIs.

![task parallelism](https://github.com/user-attachments/assets/4397a773-3abb-4d0c-8a7c-639e5e38e628)
---

### **FIBONACCI.PY**
Calculates the Fibonacci sequence using multithreading.

- **Threads**: Compute Fibonacci numbers concurrently for the same input.
- **Output**: Results and execution time for each thread.
- **Purpose**: Demonstrates parallel computation of a recursive algorithm.

![fibonacci](https://github.com/user-attachments/assets/1e672f0f-768a-4cad-af9d-e5fc9cb6e363)
---

### **PIPE.PY**
Showcases inter-process communication using a `Pipe`.

- **Parent Process**: Sends a message to the child process and receives a processed response.
- **Child Process**: Converts the message to uppercase and sends it back.
- **Purpose**: Demonstrates bidirectional communication between processes using pipes.

![pipe](https://github.com/user-attachments/assets/74bff237-10bf-4a5d-be2a-8caa689a45be)

---

## License
This project is licensed under the MIT License. Feel free to use and modify the code as needed.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for improvements or new examples.
