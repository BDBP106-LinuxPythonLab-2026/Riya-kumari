# import math
# def population_growth(initial,rate, time):
#     def exponential_growth():
#         return initial + math.exp(rate*time)
#     P=exponential_growth()
#     print(round(P))
# population_growth(100,1,10)

#OR

import math
def greet(func):
    def wrapper(initial,rate,time):
        result=round(func(initial,rate,time))
        return result
    return wrapper

@greet
def population_growth(initial,rate,time):
    return initial + math.exp(rate*time)

print(population_growth(100,0.5,10))