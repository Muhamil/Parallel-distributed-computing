from threading import Thread
from queue import Queue
import time
import random


# Producer thread that produces items and puts them in the queue
class Producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue  # Initialize with the shared queue

    def run(self):
        # Produce 5 random items
        for i in range(5):
            item = random.randint(0, 256)  # Generate a random number between 0 and 256
            self.queue.put(item)  # Put the item in the queue
            print('Producer notify : item N°%d appended to queue by %s\n' % (item, self.name))
            time.sleep(1)  # Sleep for 1 second to simulate production delay


# Consumer thread that consumes items from the queue
class Consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue  # Initialize with the shared queue

    def run(self):
        while True:
            item = self.queue.get()  # Get an item from the queue
            print('Consumer notify : %d popped from queue by %s' % (item, self.name))
            self.queue.task_done()  # Mark the task as done (for Queue management)


if __name__ == '__main__':
    queue = Queue()  # Create a shared queue

    # Create the producer and consumer threads
    t1 = Producer(queue)
    t2 = Consumer(queue)
    t3 = Consumer(queue)
    t4 = Consumer(queue)

    # Start the threads
    t1.start()
    t2.start()
    t3.start()
    t4.start()

    # Wait for all threads to complete
    t1.join()
    t2.join()
    t3.join()
    t4.join()


# Explanation:
# This program demonstrates thread synchronization using the Queue module in Python. The Queue provides a thread-safe FIFO (First-In-First-Out)
# structure for sharing data between threads. Here, we have one producer thread and multiple consumer threads.
# 
# - The producer thread generates random numbers and appends them to the queue.
# - The consumer threads pop items from the queue as they become available and process them.
# 
# The queue ensures thread-safe operations between producer and consumer threads. The `put()` and `get()` methods of the queue ensure that 
# data is safely shared and synchronized. The consumer threads will block (wait) until there are items available in the queue to consume.
# 
# - The `task_done()` method is used to signal that a consumer thread has finished processing an item.
# 
# In summary, the program simulates a producer-consumer problem where a producer generates items and multiple consumers process them concurrently.
# The use of thread synchronization via the queue ensures that there is no race condition or data inconsistency between the threads.
