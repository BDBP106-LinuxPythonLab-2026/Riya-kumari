import re

dna = "ATCGCGAATTCAC"
pattern = r"GAATTC"

if re.search(pattern, dna):
 print("EcoRI restriction site found")
else:
 print("EcoRI restriction site not found")