# iss program main hum user say string leinge or repeat yani kitni dafa string repeat
# krna hai print krna hai.
from colorama import Fore, init
init()

def print_multiple(message: str, repeats: int):
    
    for _ in range(repeats):
        print(message)


def main():
    
    message: str = input(f'{Fore.BLUE}Please type a message:{Fore.RESET} ')
    repeats: int = int(input(f'{Fore.BLUE}Enter a number of times to repeat your message:{Fore.RESET} '))
    print_multiple(message, repeats)


if __name__ == '__main__':
    main()
    