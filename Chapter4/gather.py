from mpi4py import MPI

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
data = (rank + 1) ** 2

gathered_data = comm.gather(data, root=0)
if rank == 0:
    print(f"Rank {rank} receiving data from other processes:")
    for i in range(1, size):
        value = gathered_data[i]
        print(f"Process {rank} received {value} from process {i}")
