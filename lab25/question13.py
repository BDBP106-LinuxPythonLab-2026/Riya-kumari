import re

dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"

pattern = r"[^ATGC]+"

result = re.split(pattern, dna)

print("Original DNA:", dna)
print("Split DNA:", result)