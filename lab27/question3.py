import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)

length = rng.integers(50, 800, size=100)

weight = length * 0.11 + rng.normal(0, 3, size=100)

membrane = rng.random(100) < 0.3

fig, ax = plt.subplots()

# Membrane proteins
ax.scatter(
    length[membrane],
    weight[membrane],
    color='red',
    marker='^',
    alpha=0.6,
    label='Membrane Proteins'
)

# Soluble proteins
ax.scatter(
    length[~membrane],
    weight[~membrane],
    color='blue',
    marker='o',
    alpha=0.6,
    label='Soluble Proteins'
)

ax.set_xlabel("Protein Length (Amino Acids)")
ax.set_ylabel("Molecular Weight (kDa)")

ax.set_title("Protein Length vs Molecular Weight")

ax.legend()

# Save figure
plt.savefig("protein_size.png", dpi=150)

plt.show()

# Open saved figure
import matplotlib.image as mpimg

img = mpimg.imread("protein_size.png")

plt.imshow(img)
plt.axis('off')
plt.show()