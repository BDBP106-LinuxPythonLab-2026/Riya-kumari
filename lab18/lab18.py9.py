def extra_codon(sequence,start):
    codon = []
    for i in range (start, len(sequence) -2,3):
        codons.append(sequence[i:1+3])

    return codons
print(extract_codons("GTTTCGATTATAACG",0))
print(extracr_codons("GTTTCGATTATAACG",2))

