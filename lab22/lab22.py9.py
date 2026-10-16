def log_function_call(func):
    def wrapper(sequence):
        print("Running DNA analysis....")
        result=func(sequence)
        print("Analysis complete!")
        return result   #To preserve the original function's return value

    return wrapper
@log_function_call
def analyse_dna(sequence):
    def GC_content():
        GC=sequence.count("G")+sequence.count("c")
        return (GC/len(sequence))*100      # returning this to use this in outer (main) function
    Percentage=GC_content()
    if Percentage > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")
    print(f"GC% in a sequence is {GC_content()} that is less than 50")
(analyse_dna("ATGCATCG"))