# iss program main hum function banainge jo integer layga input or uss integer ka eik 
# digit print kray ga.

from colorama import Fore, init
init()

def print_one_digit(number: int):

    one_digit: int = number % 10
    print(f'The ones digit is: {one_digit}')
    

def main():
    
    number: int = int(input(f'{Fore.BLUE}Enter a number: {Fore.RESET}'))
    print_one_digit(number)

if __name__ == '__main__':
    main()