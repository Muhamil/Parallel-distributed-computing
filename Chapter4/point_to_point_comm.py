from mpi4py import MPI

# Initialize the MPI communicator
comm = MPI.COMM_WORLD

# Get the rank of the current process
rank = comm.rank

# Print the rank of the process
print("My rank is:", rank)

# Process logic based on rank
if rank == 0:
    # Define data and destination process
    data = 10000000
    destination_process = 4
    # Send data to the destination process
    comm.send(data, dest=destination_process)
    print(f"Sending data {data} to process {destination_process}")

elif rank == 1:
    # Define data and destination process
    destination_process = 8
    data = "hello"
    # Send data to the destination process
    comm.send(data, dest=destination_process)
    print(f"Sending data {data} to process {destination_process}")

elif rank == 4:
    # Receive data from source process (rank 0)
    data = comm.recv(source=0)
    # Print received data
    print(f"Data received is = {data}")

elif rank == 8:
    # Receive data from source process (rank 1)
    data1 = comm.recv(source=1)
    # Print received data
    print(f"Data1 received is = {data1}")
