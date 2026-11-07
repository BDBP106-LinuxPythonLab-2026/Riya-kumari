import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(3)

organisms = ["E. coli", "S. cerevisiae",
             "P. falciparum", "S. coelicolor"]

mean_gc = [51, 38, 19, 72]

# Create 2x2 subplot grid
fig, axes = plt.subplots(2, 2, sharex=True, sharey=True)

bins = np.arange(0, 101, 2)

# Flatten axes
axes = axes.flatten()

for i, ax in enumerate(axes):

    gc = rng.normal(mean_gc[i], 4, size=1000)

    ax.hist(gc, bins=bins, edgecolor='black')

    # Mean dashed line
    ax.axvline(mean_gc[i], color='red', linestyle='--')

    ax.set_title(f"{organisms[i]} (Mean = {mean_gc[i]}%)")

# Label outer axes
axes[0].set_ylabel("Frequency")
axes[2].set_ylabel("Frequency")

axes[2].set_xlabel("GC Content (%)")
axes[3].set_xlabel("GC Content (%)")

fig.suptitle("GC Content Distribution of Organisms")

plt.tight_layout()

plt.show()