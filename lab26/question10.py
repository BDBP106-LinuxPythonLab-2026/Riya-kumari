import numpy as np
t = np.arange(0, 121, 20)
population = 100 * 2**(t/20)
print("Time points:", t)
print("Population:", population)
print("Final population is",
      population[-1] / population[0], "times larger")
print("Time points where population > 1000:")
print(t[population > 1000])