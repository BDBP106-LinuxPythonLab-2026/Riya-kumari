import re

dna = "ATCGCGAATTCAC"
pattern = r"GC[ATGC]GC"

if re.search(pattern, dna):
 print("BisI restriction site found")
else:
 print("BisI restriction site not found")