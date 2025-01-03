import asyncio

# Coroutine for factorial calculation
@asyncio.coroutine
def factorial(number):
    f = 1
    for i in range(2, number + 1):
        print("Asyncio.Task: Compute factorial(%s)" % (i))
        yield from asyncio.sleep(1)  # Non-blocking sleep
        f *= i
    print("Asyncio.Task - factorial(%s) = %s" % (number, f))

# Coroutine for Fibonacci calculation
@asyncio.coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print("Asyncio.Task: Compute fibonacci (%s)" % (i))
        yield from asyncio.sleep(1)  # Non-blocking sleep
        a, b = b, a + b
    print("Asyncio.Task - fibonacci(%s) = %s" % (number, a))

# Coroutine for binomial coefficient calculation
@asyncio.coroutine
def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print("Asyncio.Task: Compute binomial_coefficient (%s)" % (i))
        yield from asyncio.sleep(1)  # Non-blocking sleep
    print("Asyncio.Task - binomial_coefficient(%s, %s) = %s" % (n, k, result))

# Main function to execute tasks concurrently
if __name__ == '__main__':
    # List of tasks to be performed in parallel
    task_list = [asyncio.Task(factorial(10)),
                 asyncio.Task(fibonacci(10)),
                 asyncio.Task(binomial_coefficient(20, 10))]

    # Acquire event loop and start computation
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))  # Execute tasks concurrently
    loop.close()
