import threading
import time
import os
from threading import Thread
from random import randint

# Lock Definition: A lock to synchronize access to the critical section
threadLock = threading.Lock()

# MyThreadClass inherits from Thread and simulates a task that runs for a random duration
class MyThreadClass(Thread):
    def __init__(self, name, duration):
        # Initialize the thread with a name and duration for the sleep
        Thread.__init__(self)
        self.name = name
        self.duration = duration

    def run(self):
        # Acquire the lock before entering the critical section
        threadLock.acquire()
        print("---> " + self.name + \
              " running, belonging to process ID " + str(os.getpid()) + "\n")
        threadLock.release()  # Release the lock after entering the critical section

        time.sleep(self.duration)  # Simulate task duration by sleeping
        print("---> " + self.name + " over\n")  # Task completion message

# Main function to create, start, and manage multiple threads
def main():
    start_time = time.time()  # Track execution start time
    
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

    # Thread Joining: Wait for all threads to complete before continuing
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
# - This program creates 9 threads with random sleep durations and executes them concurrently.
# - Each thread tries to acquire a lock before printing its start message, ensuring that the output is synchronized.
# - The main thread waits for all the created threads to finish before printing "End" and the execution time.
# - The use of a thread lock prevents multiple threads from printing their messages at the same time, ensuring clean output.
