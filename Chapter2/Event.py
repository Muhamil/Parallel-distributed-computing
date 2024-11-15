import logging
import threading
import time
import random

# Configuring logging to track thread activities and interactions
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resource (a list to hold items) and an Event for synchronization
items = []
event = threading.Event()  # Event to signal state changes between threads

# Consumer class representing a thread that consumes items from the shared resource
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        while True:  # Run indefinitely to simulate continuous consumption
            time.sleep(2)  # Simulate delay before attempting to consume
            event.wait()  # Wait until the event is set by the producer
            item = items.pop()  # Remove an item from the shared list
            logging.info('Consumer notify: {} popped by {}'.format(item, self.name))

# Producer class representing a thread that produces items for the shared resource
class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        for i in range(5):  # Simulate producing a fixed number of items
            time.sleep(2)  # Simulate delay before producing the next item
            item = random.randint(0, 100)  # Generate a random item
            items.append(item)  # Add the item to the shared list
            logging.info('Producer notify: item {} appended by {}'.format(item, self.name))
            event.set()  # Signal the consumer that an item is available
            event.clear()  # Reset the event after signaling

if __name__ == "__main__":
    # Create producer and consumer threads
    t1 = Producer(name='Producer')
    t2 = Consumer(name='Consumer')

    # Start the threads
    t1.start()
    t2.start()

    # Wait for the producer thread to complete
    t1.join()
    t2.join()

# Explanation:
# - A producer-consumer problem using threads and an Event object for synchronization.
# - The Producer thread generates random items and appends them to a shared list.
# - The Consumer thread waits for an Event signal and then consumes an item from the list.
# - The Event ensures the producer and consumer are synchronized, preventing the consumer from attempting to pop from an empty list.
# - Logging provides visibility into the interactions between the threads.
