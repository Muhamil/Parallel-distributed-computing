import asyncio
import sys

# First coroutine to calculate the sum of first N integers
@asyncio.coroutine
def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += i
        yield from asyncio.sleep(1)  # Non-blocking sleep to simulate work
    future.set_result('First coroutine (sum of N integers) result = %s' % count)

# Second coroutine to calculate the factorial of a number
@asyncio.coroutine
def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i
        yield from asyncio.sleep(2)  # Non-blocking sleep to simulate work
    future.set_result('Second coroutine (factorial) result = %s' % count)

# Callback function to handle the result from the futures
def got_result(future):
    print(future.result())

# Main function to execute coroutines
if __name__ == "__main__":
    # Read num1 and num2 from command line arguments
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Create the event loop
    loop = asyncio.get_event_loop()

    # Create futures for both coroutines
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Define the tasks to run concurrently
    tasks = [
        first_coroutine(future1, num1),
        second_coroutine(future2, num2)
    ]

    # Add done callbacks to futures to print results when finished
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # Run the tasks using the event loop
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
