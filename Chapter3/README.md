# Multiprocessing in Python: Examples and Explanations

This repository contains a collection of Python scripts demonstrating various features of the `multiprocessing` module, which is used for process-based parallelism. Each script highlights different aspects of process management, inter-process communication, and synchronization in Python. Below is a brief explanation of each script.

---

## 1. **`COMMUNICATING_WITH_PIPE.PY`**
This script demonstrates how to use **pipes** for inter-process communication (IPC). It creates two processes: the first process generates numbers from 0 to 9 and sends them through a pipe. The second process receives the numbers, squares them, and sends them to another pipe. The results are passed between processes using these pipes, allowing the processes to communicate with each other efficiently.

![pipe](https://github.com/user-attachments/assets/32e378de-2ddc-4f58-a7bf-eeb1288dedb0)
---

## 2. **`COMMUNICATING_WITH_QUEUE.PY`**
This script illustrates the **producer-consumer pattern** using a **queue** for inter-process communication. The producer process generates random numbers and places them in the queue. The consumer process retrieves and processes the items from the queue. Queues provide a thread-safe way for processes to share data, ensuring synchronization and proper data handling across multiple processes.

![comm with queue](https://github.com/user-attachments/assets/33791fc2-1009-4842-b393-a6f30d689a4e)
---

## 3. **`DEROM.PY`**
This script showcases how to work with **daemon** and **non-daemon processes** in Python. The daemon process runs in the background and is automatically terminated when the main program exits. The non-daemon process runs independently and does not terminate until it finishes its execution. This example demonstrates the difference in behavior and the use cases for both types of processes.

![derom](https://github.com/user-attachments/assets/b6449db6-8965-437c-806d-b8a1b0e2f91a)
---

## 4. **`KILLING_PROCESSES.PY`**
This script demonstrates how to **terminate a process** using the `terminate()` method. It starts a process and then explicitly stops it. The script also checks the status of the process before and after termination, using `is_alive()` to verify if the process is still running and `exitcode` to check the process's termination status.

![killing process](https://github.com/user-attachments/assets/9a020783-88b4-443a-8556-22ea90df0ae0)
---

## 5. **`MYFUNC.PY`**
This is a simple helper function `myFunc(i)` that prints numbers from 0 to `i`. It is used in other scripts to demonstrate how processes can execute a given function. The function is designed to be flexible and can be called with different parameters.

---

## 6. **`NAMING_PROCESSES.PY`**
This script demonstrates how to explicitly **name processes** in Python using the `multiprocessing` module. By providing a name for each process, it becomes easier to track and debug processes in larger applications. If no name is provided, processes will be given default names like `Process-1`, `Process-2`, etc.

![naming process](https://github.com/user-attachments/assets/6037001f-7579-475a-9575-43eb222f0cf0)
---

## 7. **`PROCESS_IN_SUBCLASS.PY`**
This script demonstrates the creation of a custom process class by subclassing `multiprocessing.Process`. By overriding the `run()` method, the behavior of the process can be customized. This is useful when more complex behavior is required for a process, such as handling specific initialization or finalization tasks.

![process in subclass](https://github.com/user-attachments/assets/654b4f16-ac48-451b-b6bd-1db650fa9cb8)
---

## 8. **`PROCESS_POOL.PY`**
This script shows how to use a **process pool** to parallelize tasks. A pool of worker processes is created, and the function `function_square(data)` is applied to each item in the input list. Using a pool of processes helps to efficiently manage a large number of tasks by reusing existing processes instead of creating new ones for each task.

![process pool](https://github.com/user-attachments/assets/b2763081-24b9-4407-b1f9-1e8028a0fafb)
---

## 9. **`PROCESS_BARRIER.PY`**
This script demonstrates the use of a **Barrier** to synchronize multiple processes. A Barrier ensures that all processes reach a specific point before proceeding. This synchronization mechanism is helpful in scenarios where processes need to work in coordination. The script also uses a **Lock** to serialize the output, ensuring that print statements from multiple processes do not interfere with each other.

![process barrier](https://github.com/user-attachments/assets/1200eb0a-1b49-4e5d-8c05-bd7a6ba8fab5)
---

## 10. **`RUN_BGPROCESS_NO_DERMON.PY`**
This script shows how to run processes without daemon settings. In this case, both processes (a background and a non-background process) are non-daemon. They run independently, and the main program waits for their completion. Non-daemon processes continue executing even after the main program ends, which is useful for long-running tasks that should not be interrupted.

![run bg process deamon](https://github.com/user-attachments/assets/63f9f048-02bc-447f-9642-a3aea00b2280)
---

## 11. **`NO_BG_PROCESS.PY`**
This script demonstrates running processes with **daemon settings**. The daemon process runs in the background and automatically terminates when the main program ends. The non-daemon process runs independently and continues executing after the main program exits. This script helps understand how background and foreground processes can be controlled using the `daemon` attribute.

![run bg process](https://github.com/user-attachments/assets/5f156286-9d3b-44f5-b4b3-ef42cd697382)
---

## 12. **`SPAWNING_PROCESS_NAMESPACE.PY`**
This script shows how to spawn multiple processes, each executing a function (`myFunc`) with different arguments. The processes are created and started using the `multiprocessing.Process` class, passing the function and its arguments via the `args` parameter. This approach is useful for executing the same task in parallel with different inputs.

![spawning process namespace](https://github.com/user-attachments/assets/0f96bf0b-ffc2-4ca5-abd4-0f4402a801fc)
---

## 13. **`SPAWNING_PROCESS.PY`**
This script demonstrates the basic concept of **spawning a process** using the `multiprocessing` module. For each iteration, a new process is created to execute the function `myFunc(i)` with different arguments. Each process is started and then joined to ensure that the main program waits for all processes to complete before exiting.

![spawning process](https://github.com/user-attachments/assets/e45ce93f-0ab5-4aa5-bfbb-4bc98d09c07d)
---


