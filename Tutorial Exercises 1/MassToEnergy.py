def mass_to_energy(m):
    """return equivalent energy of mass m"""
    c = 299792458  # speed of light
    E = m * (c ** 2)  # calculate energy
    return E


mass = float(input("Enter mass (kg): "))
print("Energy equivalent of", mass, "kilograms:", mass_to_energy(mass), "joules")
