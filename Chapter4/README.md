# MPI Communication Examples

This repository contains various examples of MPI (Message Passing Interface) communications using Python's `mpi4py` library. These examples cover several fundamental MPI operations such as point-to-point communication, deadlock avoidance, broadcasting, gathering, scattering, all-to-all communication, and reduction operations.

## Files

### 1. `POINT_TO_POINT_COMM.py`

This script demonstrates point-to-point communication using `send` and `recv`. It sends data between processes based on their ranks. 
- **Process 0** sends an integer `10000000` to process 4.
- **Process 1** sends a string `"hello"` to process 8.
- **Process 4** receives data from process 0.
- **Process 8** receives data from process 1.

![point to point](https://github.com/user-attachments/assets/c0c5e5b9-cd4d-4d42-832e-dbb53e1c151d)


### 2. `DEADLOCK_AVOID.PY`

This script demonstrates how to avoid deadlock in MPI communication by ensuring the correct order of `send` and `recv` operations.
- **Process 1** receives data from process 5, then sends data to process 5.
- **Process 5** sends data to process 1, then receives data from process 1.

![deadlock avoid](https://github.com/user-attachments/assets/aca6ab04-a6e5-48a7-b928-d26a449cd4ea)


### 3. `BROADCAST.PY`

This script demonstrates broadcasting, where a variable is shared from the root process (rank 0) to all other processes.
- **Process 0** initializes a variable and broadcasts it to all processes.

![broadcast](https://github.com/user-attachments/assets/22c672d1-6000-410a-9371-a20772195bf2)


### 4. `GATHER.PY`

This script demonstrates gathering data from all processes to the root process (rank 0).
- Each process computes a value `(rank + 1) ** 2` and sends it to process 0.

![gather](https://github.com/user-attachments/assets/14a60f02-2a40-486a-87f0-4120c0e9837d)

### 5. `SCATTER.PY`

This script demonstrates scattering data from the root process to all other processes.
- **Process 0** initializes an array and scatters it to all processes.

![scatter](https://github.com/user-attachments/assets/60da79d4-a05e-447a-904d-597e8c0c99bc)

### 6. `ALLTOALL.PY`

This script demonstrates an all-to-all communication, where each process sends data to every other process.
- Each process sends a sequence of numbers and receives data from every other process.

![spawning process](https://github.com/user-attachments/assets/e45ce93f-0ab5-4aa5-bfbb-4bc98d09c07d)


### 7. `REDUCTION_OPERATION.PY`

This script demonstrates a reduction operation, where each process contributes data, and the root process (rank 0) computes the sum of all the data.
- Each process sends its data, and the root process receives the sum of all the data.

![reduction operation](https://github.com/user-attachments/assets/41a358a7-ac21-49ed-b44e-a04145cc80a5)
