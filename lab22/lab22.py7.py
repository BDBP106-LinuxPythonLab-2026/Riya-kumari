import math
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

@measure_time
def population_growth(initial, rate, t):
    def exponential_growth():
        P = initial   # Initialize population with the initial value
        for i in range(1000000):
            P = P + math.exp(rate * t)  #Update population by adding the growth amount
        return P

    P = exponential_growth()
    print(round(P))
    return P

population_growth(100, 1, 10)