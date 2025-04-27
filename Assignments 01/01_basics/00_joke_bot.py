# iss program main hum user say input leinge agar user joke dega input main tw hum joke print krdeingay
# agar joke nhi deta input kuch or deta tw sorry print krdein gay yeh joke bot program hai.

from colorama import Fore, init
init()


PROMPT: str = 'What do you want?'
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = 'Sorry I only tell jokes.'


def main():
    
    user_input: str = input(f'{Fore.BLUE}{PROMPT}{Fore.RESET} ').lower()

    if user_input == 'joke':
        print(JOKE)
    else:
        print(SORRY)



if __name__ == '__main__':
    main()