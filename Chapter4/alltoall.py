from mpi4py import MPI
import numpy

# Define the communicator, size, and rank parameters
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

# Define the data to send (senddata) and prepare an empty array for received data (recvdata)
senddata = (rank + 1) * numpy.arange(size, dtype=int)
recvdata = numpy.empty(size, dtype=int)

# Perform the Alltoall communication
comm.Alltoall(senddata, recvdata)

# Display the data sent and received for each process
print("Process %d sending %s receiving %s" % (rank, senddata, recvdata))
