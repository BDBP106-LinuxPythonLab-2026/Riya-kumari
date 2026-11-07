import numpy as np
# Create a 5x10 array
a = np.random.rand(5, 10) * 100
print("Original gene expression:")
print(a)

# Calculate mean of each row
row_mean = np.mean(a, axis=1, keepdims=True)

# Subtract row mean
normalized = a - row_mean

print("\nNormalized gene expression:")
print(normalized)

# Calculate sum of each column
column_sum = np.sum(normalized, axis=0)

print("\nColumn sums:")
print(column_sum)

# Set threshold
threshold = 50

# Find samples above threshold
samples = np.where(column_sum > threshold)

print("\nSamples above threshold:")
print(samples)