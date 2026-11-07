import numpy as np
a = np.array([1, 2])
b = np.array([0, 5])
def maximum(a, b):
    return np.maximum(a, b)
c = maximum(a, b)
print(c)