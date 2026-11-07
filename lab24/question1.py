# Example of dividing microorganisms and monitoring their population

class Bacterium:
    def __init__(self,name,population):
        self.name=name
        self.population=population
    def divide(self):
        self.population *= 2
    def describe(self):
        return f'{self.name}: {self.population}'


ecoli = Bacterium("E.coli",20)
print(ecoli.describe())
ecoli.divide()
print(ecoli.describe())
ecoli.divide()
print(ecoli.describe())
ecoli.divide()
print(ecoli.describe())
ecoli.divide()
print(ecoli.describe())
ecoli.divide()
print(ecoli.describe())
ecoli.divide()
print(ecoli.describe())


streptococcus= Bacterium("strep",100)
streptococcus.divide()
print(streptococcus.describe())


#function

def bact(name,pop):
    pop *= 2
    print(f'{name} : {pop}')
    return pop


outputpop=bact("E.coli",20)
bact("E.coli",outputpop)