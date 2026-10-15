def cell_metabolism(glucose, oxygen):
    def energy_output():
        return min(glucose, oxygen // 6) * 38

    return energy_output()


# Example
glucose = int(input("Enter the number of glucose molecules: "))
oxygen = int(input("Enter the number of oxygen molecules: "))

atp = cell_metabolism(glucose, oxygen)
print("Total ATP produced:", atp)