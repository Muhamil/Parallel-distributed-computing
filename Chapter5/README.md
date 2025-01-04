# Python Concurrency and Asynchronous Programming Examples

This repository contains multiple Python scripts demonstrating different aspects of concurrency and asynchronous programming. The examples range from using threads, process pools, and asyncio tasks to simulating state machines and managing asynchronous results with `asyncio.Future`.

## File Descriptions

### 1. **TAST.PY**
This script demonstrates concurrent execution using `ThreadPoolExecutor`. It calculates the cube of a number using two methods:
- First, it executes a single task.
- Then, it executes multiple tasks concurrently using `executor.submit()` and `executor.map()`.

![tast](https://github.com/user-attachments/assets/220f6d06-37c6-44a9-a758-a453e47c6717)


#### Key functionality:
- `cube(number)` calculates the cube of a given number.
- Executes a single task and multiple tasks concurrently using threads.

### 2. **SYNX.PY**
This script compares sequential execution, thread pool execution, and process pool execution using the `concurrent.futures` module. It evaluates the performance of concurrent execution in terms of execution time by calculating a large number multiple times (`count` function).

#### Key functionality:
- `count(number)` simulates CPU-bound work by performing a loop.
- Executes the tasks sequentially, using threads, and using processes for comparison.

![sync](https://github.com/user-attachments/assets/fc71098c-b223-41fc-8f4b-96c4aced81b5)


### 3. **ASYNC_TASK_MANIPULATION.PY**
This script demonstrates asynchronous programming with `asyncio`. It calculates the factorial, Fibonacci sequence, and binomial coefficient concurrently using coroutines and `asyncio.Task()`.

#### Key functionality:
- Asynchronous coroutines like `factorial()`, `fibonacci()`, and `binomial_coefficient()` are executed concurrently.
- Utilizes `asyncio.sleep()` for non-blocking behavior, making it efficient for IO-bound tasks.

![manipulating_task](https://github.com/user-attachments/assets/957a3524-66a3-404e-a45d-e3222716d3d2)

### 4. **ASYNC_COROTINE.PY**
This script simulates a finite state machine (FSM) with asynchronous state transitions using `asyncio`. Each state (`start_state`, `state1`, `state2`, `state3`, `end_state`) transitions based on random values, showcasing how to structure asynchronous workflows.

#### Key functionality:
- States are represented as coroutines.
- The script transitions between states randomly based on input values, demonstrating asynchronous state management.

![async corotine](https://github.com/user-attachments/assets/28f380d6-7b5c-43e1-9300-4c22bc34ed31)

### 5. **ASYNCIO_FUTURE.PY**
This script demonstrates the use of `asyncio.Future` to manage asynchronous operations that can return a result in the future. It shows how to work with `asyncio.Future` objects to coordinate between tasks.

#### Key functionality:
- `asyncio.Future()` is used to handle asynchronous results that are set at a later time.
- Future objects are used to synchronize the completion of asynchronous operations.

![dealing](https://github.com/user-attachments/assets/f535b204-abf6-4497-8283-dcea5ec9a87d)
