
def analyse_dna_decorator(func):
    def wrapper(sequence):
        gc = sequence.count('G') + sequence.count('C')
        percentage = (gc / len(sequence)) * 100

        print(f"GC Content: {percentage}%")

        if percentage > 50:
            print("GC rich sequence")
        else:
            print("AT rich sequence")

        return func(sequence)
    return wrapper

@analyse_dna_decorator
def analyse_dna(sequence):
    return sequence

analyse_dna("ATGCGTACGTCA")