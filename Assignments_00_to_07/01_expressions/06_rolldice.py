# iss program main do dice roll krni or dono dice ka result or dono ka total result show krna hai.


import random

# Eik dice pay 6 sides hotein numbers kein
NUM_SIDES: int = 6

def main():

    die_1: int = random.randint(1, NUM_SIDES)
    die_2: int = random.randint(1, NUM_SIDES)

    total_of_dices: int = die_1 + die_2

    # Result display
    print(f'Dices have {NUM_SIDES} sides each')
    print(f'First die: {die_1}') 
    print(f'Second die: {die_2}')
    print(f'Total of two dice: {total_of_dices}')



if __name__ == '__main__':
    main()

