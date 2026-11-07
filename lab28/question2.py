# Do the following.
#1. Read lab genes.fasta with SeqIO.parse() into a list and print how many records it has.
#2. Print a table of ID, length, GC % (1 decimal place) and the protein translated up to
#the first stop codon.
#3. Write the genes with GC content of at least 50% to lab high gc.fasta, and print how
#many were written.
#4. Print the IDs sorted from highest to lowest GC content, using sorted() with a lambda.

from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

#read FASTA file into a list
records=list(SeqIO.parse("labgenes.fasta","fasta"))
print("Total number of records:",len(records))

#2. Print table of ID, length, GC% and protein

print("\nID\t\tLength\tGC%\tProtein")

for record in records:
 Sequence = record.Seq

# Calculate length
length = len(Sequence)

#2 Calculate GC percentage
gc = gc_fraction(Sequence) * 100

# Translate up to first stop codon
protein = Sequence.translate(to_stop=True)

print(f"{record.id}\t{length}\t{gc:.1f}%\t{protein}")

#3Write genes with GC content >= 50%

high_gc = []

for record in records:
 gc = gc_fraction(record.seq) * 100

if gc >= 50:
    high_gc.append(record)

SeqIO.write(high_gc, "high_gc.fasta", "fasta")

print("\nNumber of high GC genes written:", len(high_gc))

#4Sort IDs from highest to lowest GC content

sorted_records = sorted(
records,
key=lambda record: gc_fraction(record.seq),
reverse=True
)

print("\nIDs sorted by GC content (highest to lowest):")

for record in sorted_records:
 print(record.id)
