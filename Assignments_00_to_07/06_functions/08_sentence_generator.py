# iss program main hum user say word input leinge word ya tw noun hoga ya tw verb or adjective
# or user say part of speech input leinge integer main dono input lenay kay baad conditions check
# kee base pay word input sentence main add krkay sentence print krein gay..

from colorama import Fore, init
init()

def make_sentence(word, part_of_speech):
    
    if part_of_speech == 0:
        # noun
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        # verb
        print(f"It's so nice outside today it makes me want to {word} !")
    elif part_of_speech == 2:
        # adjective
        print(f"Looking out my window, the sky is big and {word} !")
    else:
        print('Part of speech must be 0, 1 or 2! can not make sentence.')


def main():

    word: str = input(f'{Fore.BLUE}Please type a noun, verb, or adjective:{Fore.RESET} ')
    print('Is this a noun, verb or adjective?')
    part_of_speech: int = int(input(f'{Fore.BLUE}Type 0 for noun, 1 for verb, 2 for adjective:{Fore.RESET} ')) 
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()