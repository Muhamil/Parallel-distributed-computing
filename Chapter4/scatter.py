from mpi4py import MPI

# Define the communicator and rank parameters
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Initialize the array to be scattered by the root process
if rank == 0:
    array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
else:
    array_to_share = None

# Scatter the array from the root process (rank 0)
recvbuf = comm.scatter(array_to_share, root=0)

# Print the received value in each process
print("Process = %d, recvbuf = %d" % (rank, recvbuf))
