import threading

# Function to be called by each thread
def my_func(thread_number):
    # Prints the thread number when the function is called by a thread
    return print('my_func called by thread N°{}'.format(thread_number))


def main():
    # List to hold thread objects
    threads = []

    # Loop to create and start 10 threads
    for i in range(10):
        t = threading.Thread(target=my_func, args=(i,))  # Create a new thread
        threads.append(t)  # Add the thread to the list
        t.start()  # Start the thread
        t.join()  # Wait for the thread to finish before starting the next one

# Entry point of the program
if __name__ == "__main__":
    main()

