# iss program main hum earth pay weight leingay or dekhein gay woo weight sb planets pay kya bnta hai
# sub planets kee alag gravity hoti hai gravitation constant means eik onject ka weight kis planet pay
# kitna hoga.


planetary_constants: dict = {
    'Mercury': 37.6,
    'Venus': 88.9,
    'Mars': 37.8,
    'Jupiter': 236.0,
    'Saturn': 108.1,
    'Uranus': 81.5,
    'Neptune': 114.0,
}

def planetary_weight():
    
    earth_weight: float = float(input('Enter your weight on earth: '))
    planet_choice: str = input('Enter the planet name you are goint to visit soon: ')

    # dictionary main dekhay ga woo planet jo humnay input say liya agr mila tw baki kee calculation hogi
    if planet_choice in planetary_constants:

        planet_weight: float = earth_weight * planetary_constants[planet_choice] / 100 
        print(f'Your weight on {planet_choice} is {planet_weight}')

    else:
        print('Sorry, I don’t recognize that planet name.')
    
 

if __name__ == '__main__':
    planetary_weight()