import numpy as np
sequence = "GATTACA"
mapping = {
    'A': [1, 0, 0, 0],
    'C': [0, 1, 0, 0],
    'G': [0, 0, 1, 0],
    'T': [0, 0, 0, 1]
}
encoded = np.array([mapping[base] for base in sequence])
print("DNA Sequence:", sequence)
print("One-Hot Encoded Array:")
print(encoded)