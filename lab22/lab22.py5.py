import time

def measure_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result

    return wrapper

@measure_time
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

print("Factorial of 50:", factorial(50))