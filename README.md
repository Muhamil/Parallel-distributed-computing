# Parallel-distributed-computing

# Parallel Computing and Python Programming Examples

This repository contains a collection of Python scripts demonstrating parallel and concurrent programming concepts. The examples focus on multiprocessing, threading, and message passing techniques to efficiently manage execution across multiple tasks or processes.

---

## Chapter 1: Getting Started with Parallel Computing & Python

### Overview
This chapter introduces basic concepts of parallel computing using Python. The examples highlight various methods and libraries used to implement parallelism and concurrency, such as `multiprocessing`, `threading`, and `mpi4py`.

### Key Examples:
- **IPC.py**: Demonstrates inter-process communication with a `Queue`, showcasing the producer-consumer pattern.
- **MPI.py**: Uses `mpi4py` for distributed computing, illustrating message passing.
- **Multi_Process.py**: Compares multiprocessing and multithreading for random number generation tasks.
- **Sync.py**: Demonstrates thread synchronization with semaphores.

### Purpose:
These examples aim to give users a basic understanding of parallelism, synchronization, and inter-process communication in Python.

---

## Chapter 2: Thread-Based Parallelism

### Overview
This chapter focuses on thread-based parallelism and synchronization in Python. It covers various synchronization primitives such as `Barrier`, `Condition`, `Event`, and `Lock` to coordinate thread execution and ensure safe access to shared resources.

### Key Examples:
- **Barrier.py**: Demonstrates the use of a barrier to synchronize multiple threads.
- **Condition.py**: Uses a `Condition` object to synchronize a producer-consumer scenario.
- **Semaphore.py**: Shows how semaphores control access to a shared resource.
- **MyThreadClass.py**: Demonstrates how to create custom threads by subclassing `Thread`.

### Purpose:
This chapter highlights techniques to manage threads, control execution order, and prevent race conditions.

---

## Chapter 3: Process-Based Parallelism

### Overview
In this chapter, process-based parallelism is introduced using Python's `multiprocessing` module. The examples explore different aspects of process management, including process creation, communication, and termination.

### Key Examples:
- **Communicating_with_pipe.py**: Demonstrates inter-process communication using pipes.
- **Process_pool.py**: Shows how to use process pools for parallelizing tasks.
- **Killing_processes.py**: Demonstrates how to terminate processes using the `terminate()` method.

### Purpose:
The goal is to demonstrate how processes can be used for parallel execution and communication in Python, along with managing resources across processes.

---

## Chapter 4: Message Passing

### Overview
This chapter introduces MPI (Message Passing Interface) communication with the help of the `mpi4py` library. The examples demonstrate point-to-point communication, broadcasting, gathering, and other message-passing techniques in a parallel computing environment.

### Key Examples:
- **Point_to_point_comm.py**: Demonstrates point-to-point communication using `send` and `recv`.
- **Deadlock_avoid.py**: Illustrates how to avoid deadlocks in message-passing communication.
- **Gather.py**: Demonstrates gathering data from multiple processes into the root process.

### Purpose:
This chapter focuses on communication between distributed processes, enabling efficient coordination and data exchange.

---

## Chapter 5: Asynchronous Programming

### Overview
This chapter covers asynchronous programming and concurrency in Python. It introduces asynchronous techniques such as using `asyncio` and `ThreadPoolExecutor` to execute tasks concurrently and asynchronously.

### Key Examples:
- **Task.py**: Demonstrates concurrent execution using `ThreadPoolExecutor`.
- **Synx.py**: Compares sequential, thread pool, and process pool execution for performance testing.

### Purpose:
This chapter explores how to execute tasks concurrently and handle asynchronous results in Python.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and contribute to the code as needed.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue for improvements or new examples.
