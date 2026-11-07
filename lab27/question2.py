import numpy as np
import matplotlib.pyplot as plt

genes = ["GAPDH", "ACTB", "TP53", "MYC", "EGFR"]

control = np.array([950, 1200, 310, 150, 420])

treated = np.array([940, 1180, 610, 75, 430])

x = np.arange(len(genes))
width = 0.4

fig, ax = plt.subplots()

# Draw bars
ax.bar(x - width/2, control, width, label='Control')

ax.bar(x + width/2, treated, width, label='Treated')

# Set gene names
ax.set_xticks(x, labels=genes)

ax.set_xlabel("Genes")
ax.set_ylabel("Expression Level")
ax.set_title("Gene Expression: Control vs Treated")

ax.legend()

# Calculate fold change
fold_change = treated / control

print("Fold Change:")

for gene, value in zip(genes, fold_change):
    print(gene, ":", round(value, 2))

plt.show()