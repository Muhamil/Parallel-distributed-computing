from random import randrange
from threading import Barrier, Thread
from time import ctime, sleep

# Number of runners
num_runners = 3

# Barrier to synchronize runners at the finish line
finish_line = Barrier(num_runners)

# List of runners
runners = ['Huey', 'Dewey', 'Louie']

def runner():
    # Each runner performs the following actions
    name = runners.pop()  # Remove and get the name of the runner
    sleep(randrange(2, 5))  # Simulate running with random time (2–5 seconds)
    print('%s reached the barrier at: %s \n' % (name, ctime()))  # Print when runner reaches the barrier
    finish_line.wait()  # Wait at the barrier until all threads arrive

def main():
    threads = []  # List to store threads
    print('START RACE!!!!')  
    for i in range(num_runners):
        # Create and start threads for each runner
        threads.append(Thread(target=runner))
        threads[-1].start()
    for thread in threads:
        thread.join()  # Wait for all threads to complete
    print('Race over!')  # End message

if __name__ == "__main__":
    main()

#This program simulates a race between three runners: Huey, Dewey, and Louie.
# Each runner is a separate thread that takes a random amount of time (2-5 seconds) to reach a common finish line.
# A Barrier ensures all runners wait at the finish line until everyone arrives. Once all runners are there, the program prints that the race is over. 
# It shows when each runner reaches the barrier with their name and the time.
# Barrier to synchronize runners, ensuring all runners reach the finish line before proceeding
# Function that simulates a runner's actions during the race.