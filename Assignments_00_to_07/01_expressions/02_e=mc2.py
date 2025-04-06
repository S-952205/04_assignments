# yeh program user say mass kg main laekr ussay energy baanraha hai.


# C capital coz yeh constant hai or C mtlb speed of light
C: int = 299792458

def main():

    # User se mass (kg) main input lena.
    mass_in_kg: float = float(input('\033[1;3mEnter kilos of mass:\033[0m '))

    # energy nikali einstein ka e = mc2 square formula use krkay.
    energy_in_joules = mass_in_kg * (C**2) # ** operator square nekalnay kayliye sue hota hai

   
    print(f'e = m * C^2')  # Formula energy nikalnay ka
    print(f'm: {mass_in_kg} kg') # mass jo user nay diya input main
    print(f'c: {C} m/s') # Speed of light jo constant hai

    # Final result - kitni energy bani (joules mein)
    print(f'{energy_in_joules} joules of energy') 
    # result main long nuber hoga jismain end main e+18 ya e+koi bhee number yeh hoga yeh scientific
    # notation hai mtlb e+ kay baad koi bhee number hai utnay zero hongein.


if __name__ == '__main__':
    main()