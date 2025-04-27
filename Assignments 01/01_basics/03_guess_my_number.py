# iss program main hum user say guess leinge or user ka guess agar hamaray guess ka same hai tw 
# congrats werna user kay guess ko conditions kay through dekhein gay agar woo low hai tw low print
# agar high hai tw high print

import random

def main():
    
    secret_guess: int = random.randint(1, 99)
    print('I am thinking of a number between 1 and 99...')

    user_guess: int = int(input('Enter a guess: '))
    while user_guess != secret_guess:

        if user_guess < secret_guess:
            print('your guess is too low')
        else:
            print('ypur guess is too high')
        
        user_guess: int = int(input('Enter a guess: '))


    print(f'Congrats! the number was {secret_guess}')






if __name__ == '__main__':
    main()