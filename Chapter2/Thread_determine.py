import threading
import time

# Function A that will run in its own thread
def function_A():
    print(threading.currentThread().getName() + str('--> starting \n'))  # Print the start message with thread name
    time.sleep(2)  # Simulate some work by sleeping for 2 seconds
    print(threading.currentThread().getName() + str('--> exiting \n'))  # Print the exit message with thread name
    return

# Function B that will run in its own thread
def function_B():
    print(threading.currentThread().getName() + str('--> starting \n'))  # Print the start message with thread name
    time.sleep(2)  # Simulate some work by sleeping for 2 seconds
    print(threading.currentThread().getName() + str('--> exiting \n'))  # Print the exit message with thread name
    return

# Function C that will run in its own thread
def function_C():
    print(threading.currentThread().getName() + str('--> starting \n'))  # Print the start message with thread name
    time.sleep(2)  # Simulate some work by sleeping for 2 seconds
    print(threading.currentThread().getName() + str('--> exiting \n'))  # Print the exit message with thread name
    return


if __name__ == "__main__":
    # Create threads for each function
    t1 = threading.Thread(name='function_A', target=function_A)  # Thread for function_A
    t2 = threading.Thread(name='function_B', target=function_B)  # Thread for function_B
    t3 = threading.Thread(name='function_C', target=function_C)  # Thread for function_C

    # Start the threads
    t1.start()  # Start thread t1 which executes function_A
    t2.start()  # Start thread t2 which executes function_B
    t3.start()  # Start thread t3 which executes function_C

    # Wait for all threads to complete
    t1.join()  # Wait for thread t1 to finish
    t2.join()  # Wait for thread t2 to finish
    t3.join()  # Wait for thread t3 to finish
