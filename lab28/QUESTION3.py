from Bio.Seq import Seq

# Given DNA sequence
mystery = Seq("CCATGGCTTGGAAATAGCATGCCCTAA")

# 1. Translate all six reading frames

# Forward strand
for i in range(3):
    frame = mystery[i:]
    frame = frame[:len(frame) - len(frame) % 3]
    protein = frame.translate()
    print(f"+{i+1} frame:", protein)

# Reverse complement strand
reverse = mystery.reverse_complement()

for i in range(3):
    frame = reverse[i:]
    frame = frame[:len(frame) - len(frame) % 3]
    protein = frame.translate()
    print(f"-{i+1} frame:", protein)


# 2. Find the longest ORF

all_frames = []

for seq in [mystery, reverse]:
    for i in range(3):
        frame = seq[i:]
        frame = frame[:len(frame) - len(frame) % 3]
        protein = str(frame.translate())

        start = 0

        while True:
            m = protein.find("M", start)

            if m == -1:
                break

            stop = protein.find("*", m)

            if stop != -1:
                orf = protein[m:stop]
                all_frames.append(orf)

            start = m + 1

longest_orf = max(all_frames, key=len)

print("\nLongest ORF:", longest_orf)
print("Length:", len(longest_orf), "amino acids")