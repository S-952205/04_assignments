# iss program main humnay rolling dice game banaya hai 3 dafa hum roll dice krein gay or un dices
# ka total display krein gay.


# yeh python ka module humein random number generate rkay deta hai
import random

# vairable holding 6 1 dice main 6 tk numbers hotay.
NUM_SIDES = 6

# 1st function
def roll_dice():

    # Yeh die1 sirf roll_dice() ke andar hai issay isimain use krsktay sirf.
    die1: int = random.randint(1, NUM_SIDES)  
    die2: int = random.randint(1, NUM_SIDES)

    total: int = die1 + die2
    print(f'''Die 1: {die1}, Die 2: {die2}, total of two dice: {total}''')

# 2nd function
def main():

    die1: int = 10  # Yeh die1 sirf main() ke andar hai 
    print(f'Die1 in main() starts as: {die1}')

    roll_dice()
    roll_dice()
    roll_dice()

    print(f'Die 1 in main is: {die1}')



if __name__ == '__main__':
    main()