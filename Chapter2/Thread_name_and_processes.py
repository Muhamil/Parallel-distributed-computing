from threading import Thread
import time
import os

# MyThreadClass inherits from Thread to create custom threads
class MyThreadClass (Thread):
   def __init__(self, name):
      # Initialize the parent Thread class
      Thread.__init__(self)
      self.name = name  # Set the name of the thread

   def run(self):
       # This method is executed when the thread starts
       print("ID of process running {}".format(self.name))  # Print the name of the thread

def main():
    from random import randint

    # Thread Creation
    thread1 = MyThreadClass("Thread#1 ")  # Create the first thread with name "Thread#1"
    thread2 = MyThreadClass("Thread#2 ")  # Create the second thread with name "Thread#2"
  
    # Thread Running
    thread1.start()  # Start the first thread, it will execute the 'run' method
    thread2.start()  # Start the second thread, it will execute the 'run' method

    # Thread joining
    thread1.join()  # Wait for thread1 to complete before proceeding
    thread2.join()  # Wait for thread2 to complete before proceeding

    # End 
    print("End")  # Print when all threads have finished

# Entry point of the program
if __name__ == "__main__":
    main()

# Explanation:
# 1. The MyThreadClass class inherits from the Thread class, allowing us to create threads with custom behavior.
# 2. The run() method is overridden to define the task each thread will execute, in this case, printing the name of the thread.
# 3. In the main() function:
#    - Two threads (thread1 and thread2) are created, each with a unique name.
#    - The start() method is called on each thread to begin their execution concurrently.
#    - The join() method ensures that the main program waits for both threads to finish before continuing.
# 4. The threads print their names when they run, and the main thread waits for them to complete before printing "End" and exiting.
# 5. The program demonstrates the basic use of threading by running two threads concurrently and synchronizing them with join().
