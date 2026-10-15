#write a function to analyze dna sequence
def analyse_dna(sequence):
    sequence=sequence.upper()
    def gc_content():
        gc=sequence.count('G')+sequence.count('c')
        percentage=(gc/len(sequence))*100
        return percentage
    gc_percent=gc_content()
    if gc_percent > 50:
        print("Gc rich sequence")
    else:
        print("AT rich sequence")
print("enter dna sequence:")
dna_sequence="ATGCCGATTTTGC"
analyse_dna(dna_sequence)