import re

dna = "ATCGCGYAATTCAC"

ambiguous = re.search(r"[^ATGC]", dna)

if ambiguous:
 print("Ambiguous bases found")
print("Ambiguous character:", ambiguous.group())

non_ambiguous = re.findall(r"[ATGC]", dna)

print("Non-ambiguous bases:", "".join(non_ambiguous))