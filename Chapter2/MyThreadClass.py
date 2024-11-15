import time
import os
from random import randint
from threading import Thread

# MyThreadClass inherits from Thread, simulating a thread that runs for a random duration
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        # Initialize the thread with a name and duration for the sleep
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Print the thread's start message with its name and process ID
        print("---> " + self.name + \
              " running, belonging to process ID " + str(os.getpid()) + "\n")
        
        # Simulate work by sleeping for the specified duration
        time.sleep(self.duration)
        
        # Print the thread's completion message
        print("---> " + self.name + " over\n")

# Main function to manage the creation, execution, and joining of threads
def main():
    start_time = time.time()  # Track the start time to measure execution time
    
    # Thread Creation: Create 9 threads with random durations (1 to 10 seconds)
    thread1 = MyThreadClass("Thread#1 ", randint(1, 10))
    thread2 = MyThreadClass("Thread#2 ", randint(1, 10))
    thread3 = MyThreadClass("Thread#3 ", randint(1, 10))
    thread4 = MyThreadClass("Thread#4 ", randint(1, 10))
    thread5 = MyThreadClass("Thread#5 ", randint(1, 10))
    thread6 = MyThreadClass("Thread#6 ", randint(1, 10))
    thread7 = MyThreadClass("Thread#7 ", randint(1, 10))
    thread8 = MyThreadClass("Thread#8 ", randint(1, 10))
    thread9 = MyThreadClass("Thread#9 ", randint(1, 10))

    # Thread Running: Start all the threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # Thread Joining: Ensure the main thread waits for all threads to finish before continuing
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()

    # End: Print final completion message
    print("End")

    # Execution Time: Calculate and display the total execution time
    print("--- %s seconds ---" % (time.time() - start_time))

# Run the main function when the script is executed
if __name__ == "__main__":
    main()

# Explanation:
# - The program creates 9 threads that simulate tasks with random durations.
# - Each thread starts by printing a message with its name and the process ID.
# - After a random sleep duration (simulating work), each thread prints its completion message.
# - The main thread waits for all threads to finish using `join()`.
# - Finally, it prints "End" and the total execution time taken for all threads to complete.
