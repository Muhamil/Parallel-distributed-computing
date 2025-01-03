import concurrent.futures
import time

# Define the list of numbers from 1 to 10
number_list = list(range(1, 11))

# The count(number) function counts the numbers from 1 to 100000000,
# and then returns the product of number × 100,000,000
def count(number):
    i = 0
    for _ in range(0, 100000000):
        i += 1
    return i * number

# The evaluate(item) function evaluates the count function on the item parameter.
# It prints out the item value and the result of count(item)
def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))

# Main execution
if __name__ == '__main__':
    # Sequential execution
    start_time = time.time()  # use time.time() instead of time.clock() (deprecated)
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in %s seconds' % (time.time() - start_time))

    # Thread Pool Execution
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution in %s seconds' % (time.time() - start_time))

    # Process Pool Execution
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution in %s seconds' % (time.time() - start_time))
