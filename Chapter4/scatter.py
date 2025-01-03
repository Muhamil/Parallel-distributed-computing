from mpi4py import MPI
import numpy as np

# Define the communicator and rank parameters
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()  # Get the number of processes

# Initialize the array to be scattered by the root process
if rank == 0:
    array_to_share = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
else:
    array_to_share = None

# Split the array into chunks to send
chunk_size = len(array_to_share) // size  # Determine chunk size for each process
chunks = [array_to_share[i:i + chunk_size] for i in range(0, len(array_to_share), chunk_size)]

# Scatter the array from the root process (rank 0)
recvbuf = comm.scatter(chunks, root=0)

# Print the received value in each process
print(f"Process = {rank}, recvbuf = {recvbuf}")
