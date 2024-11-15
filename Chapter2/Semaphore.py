import logging
import threading
import time
import random

# Configure logging format to include time, thread name, log level, and message
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Semaphore is initialized with 0, meaning the consumer will initially be blocked
semaphore = threading.Semaphore(0)
item = 0  # Shared resource (item number) to be produced and consumed


# Consumer thread function: waits for the producer to produce an item
def consumer():
    logging.info('Consumer is waiting')  # Log that the consumer is waiting for the item
    semaphore.acquire()  # Wait for the semaphore to be released by the producer
    logging.info('Consumer notify: item number {}'.format(item))  # Log the item consumed


# Producer thread function: produces an item and notifies the consumer
def producer():
    global item
    time.sleep(3)  # Simulate time taken for production
    item = random.randint(0, 1000)  # Produce a random item number
    logging.info('Producer notify: item number {}'.format(item))  # Log the produced item
    semaphore.release()  # Release the semaphore to notify the consumer


# Main function that starts the producer and consumer threads
def main():
    for i in range(10):  # Loop to run producer-consumer pair 10 times
        t1 = threading.Thread(target=consumer)  # Create a consumer thread
        t2 = threading.Thread(target=producer)  # Create a producer thread

        t1.start()  # Start the consumer thread
        t2.start()  # Start the producer thread

        t1.join()  # Wait for the consumer thread to finish
        t2.join()  # Wait for the producer thread to finish


# Entry point of the program
if __name__ == "__main__":
    main()

# This program simulates a producer-consumer scenario where the producer creates an item and the consumer consumes it.
# The producer uses the `semaphore.release()` to notify the consumer that an item is available.
# The consumer waits for the producer to produce an item by calling `semaphore.acquire()`, which blocks until the producer signals it.
# Logging is used to track when each thread is waiting, producing, or consuming.
