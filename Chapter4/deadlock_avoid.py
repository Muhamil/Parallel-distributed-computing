from mpi4py import MPI

# Initialize the MPI communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process
rank = comm.rank

# Print the rank of the process
print("My rank is %i" % rank)

# Logic for process of rank 1
if rank == 1:
    data_send = "a"
    destination_process = 5
    source_process = 5
    # Receive data from process 5
    data_received = comm.recv(source=source_process)
    # Send data to process 5
    comm.send(data_send, dest=destination_process)
    print("Sending data %s to process %d" % (data_send, destination_process))
    print("Data received is = %s" % data_received)

# Logic for process of rank 5
if rank == 5:
    data_send = "b"
    destination_process = 1
    source_process = 1
    # Send data to process 1
    comm.send(data_send, dest=destination_process)
    # Receive data from process 1
    data_received = comm.recv(source=source_process)
    print("Sending data %s to process %d" % (data_send, destination_process))
    print("Data received is = %s" % data_received)
