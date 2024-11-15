import logging
import threading
import time

# Configuring logging to display thread activities
LOG_FORMAT = '%(asctime)s %(threadName)-17s %(levelname)-8s %(message)s'
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

# Shared resource (a list of items) and a Condition object for synchronization
items = []
condition = threading.Condition()

# Consumer class representing a thread that consumes items from the shared resource
class Consumer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def consume(self):
        with condition:  # Acquire the condition lock
            if len(items) == 0:  # Check if there are no items to consume
                logging.info('No items to consume')  # Log the condition
                condition.wait()  # Wait for an item to be produced

            # Consume an item from the shared resource
            items.pop()
            logging.info('Consumed 1 item')  # Log the consumption

            condition.notify()  # Notify other threads that an item was consumed

    def run(self):
        for _ in range(20):  # Simulate consuming items 20 times
            time.sleep(2)  # Simulate delay in consuming
            self.consume()

# Producer class representing a thread that produces items for the shared resource
class Producer(threading.Thread):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def produce(self):
        with condition:  # Acquire the condition lock
            if len(items) == 10:  # Check if the shared resource is full
                logging.info(f'Items produced {len(items)}. Stopped')  # Log the condition
                condition.wait()  # Wait until an item is consumed

            # Produce an item and add it to the shared resource
            items.append(1)
            logging.info(f'Total items {len(items)}')  # Log the production

            condition.notify()  # Notify other threads that an item was produced

    def run(self):
        for _ in range(20):  # Simulate producing items 20 times
            time.sleep(0.5)  # Simulate delay in producing
            self.produce()

# Main function to create and start producer and consumer threads
def main():
    # Create producer and consumer threads
    producer = Producer(name='Producer')
    consumer = Consumer(name='Consumer')

    # Start both threads
    producer.start()
    consumer.start()

    # Wait for both threads to finish
    producer.join()
    consumer.join()

if __name__ == "__main__":
    main()

# This program demonstrates a classic producer-consumer problem using threads and a shared resource.
# - Producer threads produce items and add them to a shared list.
# - Consumer threads consume items from the shared list.
# - A Condition object is used to synchronize access to the shared list.
# - The program logs every action (producing, consuming, waiting) to show thread interactions in real-time.
