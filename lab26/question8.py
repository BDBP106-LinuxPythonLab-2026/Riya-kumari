import numpy as np
a = np.array([12, 25, 30, 15, 45, 18, 50, 22, 10, 35])
print("Average:", np.mean(a))

print("Highest score:", np.max(a))

print("Lowest score:", np.min(a))

print("Numbers above 20:", np.sum(a > 20))

print("Scores below 20:", a[a < 20])