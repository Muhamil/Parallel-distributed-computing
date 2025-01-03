import numpy
from mpi4py import MPI

# Define the comm, size, and rank parameters
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

# Set the size of the array
array_size = 10

# Define the data to be sent and received
recvdata = numpy.zeros(array_size, dtype=numpy.int)
senddata = (rank + 1) * numpy.arange(array_size, dtype=numpy.int)

# Print the process sending data
print("Process %s sending %s" % (rank, senddata))

# Execute the Reduce operation (root process is 0, operation is MPI.SUM)
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)

# Print the result after Reduce operation (only the root process will print)
if rank == 0:
    print('On task', rank, 'after Reduce: data =', recvdata)
