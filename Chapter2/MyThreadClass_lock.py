import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition: A threading Lock to synchronize access to critical sections
threadLock = threading.Lock()

# MyThreadClass inherits from Thread and represents individual threads
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        # Initialize the thread with a name and duration for the sleep
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire the lock to prevent other threads from printing concurrently
        threadLock.acquire()
        
        # Print the thread's start message with its name and process ID
        print("---> " + self.name + \
              " running, belonging to process ID " + str(os.getpid()) + "\n")
        
        # Simulate work by sleeping for the specified duration
        time.sleep(self.duration)
        
        # Print the thread's completion message
        print("---> " + self.name + " over\n")
        
        # Release the lock after finishing the critical section
        threadLock.release()

# Main function that manages the creation, execution, and synchronization of threads
def main():
    start_time = time.time()  # Track the start time to measure execution time
    
    # Thread Creation: Create 9 threads with random durations
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

    # Thread Joining: Wait for all threads to finish before proceeding
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

if __name__ == "__main__":
    main()

# Explanation:
# - The program creates 9 threads that simulate tasks with random durations.
# - The Lock ensures that only one thread can print its message at a time, avoiding mixed output.
# - Each thread acquires the lock before printing, then sleeps for a random duration (simulating work), and then releases the lock.
# - The main thread waits for all threads to finish by calling `join()` on each thread.
# - Finally, it prints the total execution time of all threads.
