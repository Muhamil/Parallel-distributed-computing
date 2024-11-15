import threading
import time
import random

# Box class simulating a shared resource with locking mechanisms
class Box:
    def __init__(self):
        # RLock (Reentrant Lock) allows a thread to acquire the lock multiple times
        self.lock = threading.RLock()
        self.total_items = 0  # Keeps track of the total items in the box

    # Execute method to modify the total_items safely
    def execute(self, value):
        with self.lock:  # Ensures thread-safety when modifying total_items
            self.total_items += value

    # Method to add an item to the box
    def add(self):
        with self.lock:
            self.execute(1)  # Increment total_items by 1

    # Method to remove an item from the box
    def remove(self):
        with self.lock:
            self.execute(-1)  # Decrement total_items by 1

# Adder thread function, simulates adding items to the box
def adder(box, items):
    print("N° {} items to ADD \n".format(items))  # Display the number of items to add
    while items:
        box.add()  # Add one item to the box
        time.sleep(1)  # Simulate time taken to add an item
        items -= 1  # Decrease the number of items to add
        print("ADDED one item -->{} item to ADD \n".format(items))  # Display progress

# Remover thread function, simulates removing items from the box
def remover(box, items):
    print("N° {} items to REMOVE \n".format(items))  # Display the number of items to remove
    while items:
        box.remove()  # Remove one item from the box
        time.sleep(1)  # Simulate time taken to remove an item
        items -= 1  # Decrease the number of items to remove
        print("REMOVED one item -->{} item to REMOVE \n".format(items))  # Display progress

# Main function to start threads
def main():
    items = 10  # Initial number of items
    box = Box()  # Create a Box instance

    # Create threads for adding and removing items
    t1 = threading.Thread(target=adder, args=(box, random.randint(10, 20)))  # Random number of items to add
    t2 = threading.Thread(target=remover, args=(box, random.randint(1, 10)))  # Random number of items to remove
    
    t1.start()  # Start the adder thread
    t2.start()  # Start the remover thread

    t1.join()  # Wait for the adder thread to finish
    t2.join()  # Wait for the remover thread to finish

# Entry point of the program
if __name__ == "__main__":
    main()

# This program simulates two threads: one for adding items and another for removing items from a shared Box resource.
# The Box class uses an RLock to ensure thread-safety when accessing or modifying the total_items variable.
# The adder and remover threads repeatedly add and remove a random number of items from the Box, simulating a producer-consumer-like scenario.
# Each thread waits for 1 second between each operation to simulate real-world delays.
# RLocks allow a thread to acquire the lock multiple times, making it suitable when a thread needs to lock it recursively.
