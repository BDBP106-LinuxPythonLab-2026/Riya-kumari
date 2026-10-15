# Write a function protein_energy_temp() with an inner function
# calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
# random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0).
def protein_energy_temp():
    H = float(input("Enter a Enthalpy of rxn:", ))
    T = float(input("Enter a Time in Kelvin:", ))
    S = float(input("Enter Entropy of rxn:", ))

    def calculate_free_energy(H,T,S):
        return H-T*S
    G=calculate_free_energy(H,T,S)
    if G>0:
        return "stable"
    else:
        return "unstable"
print(protein_energy_temp())