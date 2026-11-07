import numpy as np
counts = np.array([100, 200, 400, 800, 1600])
# Calculate log2
log_values = np.round(np.log2(counts), 2)
# Calculate total
total = np.sum(counts)
# Calculate percentage
percentage = np.round((counts / total) * 100, 1)
print("Gene counts:", counts)
print("Log2 values:", log_values)
print("Total counts:", total)
print("Percentages:", percentage)