import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 points
x = np.linspace(-20, 20, 1000)

# Calculate functions
f1 = np.log(1 / np.cos(x)**2)

f2 = np.log(1 / np.sin(x)**2)

# Remove numerical singularities
f1[np.abs(np.cos(x)) < 0.01] = np.nan
f2[np.abs(np.sin(x)) < 0.01] = np.nan

# Plot
plt.figure(figsize=(10, 6))

plt.plot(x, f1, label='f1(x) = ln(1/cos²x)')

plt.plot(x, f2, label='f2(x) = ln(1/sin²x)')

plt.xlabel("x")
plt.ylabel("Function Value")

plt.title("Logarithmic Trigonometric Functions")

plt.legend()

plt.grid()

plt.show()