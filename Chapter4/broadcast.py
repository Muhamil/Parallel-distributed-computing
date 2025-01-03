from mpi4py import MPI

# Define the communicator and rank parameter
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Process logic for sharing a variable
if rank == 0:
    # Process 0 initializes the variable to be shared
    variable_to_share = 100
else:
    # Other processes start with None
    variable_to_share = None

# Broadcast the variable, with rank 0 as the root
variable_to_share = comm.bcast(variable_to_share, root=0)

# Print the result for each process
print("Process = %d, Variable shared = %d" % (rank, variable_to_share))
