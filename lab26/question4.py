import numpy as np
a = np.random.randint(1, 100, (3, 3))
print("Original matrix:")
print(a)
a[:, [0, 1]] = a[:, [1, 0]]
print("After swapping columns:")
print(a)