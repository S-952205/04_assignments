# iss program main hum user say input leinge user agar joke deta input tw hum joke 
# pint krdein gay agr kuch or dega input tw hum sorry print krdein gay yeh program simple joke bot 
# hai jo joke print kray ga.

from colorama import Fore, init
init()

PROMPT: str = 'What do you want?'
SORRY: str = "Sorry I only tell jokes."
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"


def main():

    # user say input liya
    user_input: str = input(f'{Fore.BLUE}{PROMPT}{Fore.RESET} ').lower()

    # Check karo agar user ne "Joke" likha tw joke print kro
    if user_input == 'joke':
        print(JOKE)
    else:
        print(SORRY)



if __name__ == '__main__':
    main()