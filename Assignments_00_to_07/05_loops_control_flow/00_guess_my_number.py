# iss program main humnay correct number guess krna jo program nay guess kiya hua same woo tb hamara
# guess correct hoga.

import random

secret_number: int = random.randint(1, 99)
print('I m thinking of a number between 1 and 99...')

def main():
    guess: int = int(input('Enter a guess: '))

    # jb tk guess same na hojai secret_number kay while loop chlta rahay ga
    while guess != secret_number:

        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        guess: int = int(input('Enter a guess: '))

    print(f"Congrats! the number was: {secret_number}")



if __name__ == '__main__':
    main()
