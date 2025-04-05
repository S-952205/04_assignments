# Yeh program user say uska favouite animal pouchayga.

def main():
    
    # Terminal mein text ko bold/italics karne ke liye special codes use hote hain (ANSI escape sequences)
    # ANSI codes for bold + italic: \033[1;3m (reset code end main \033[0m)
    animal: str = input("What's your favourite animal? ")
    print(f'My favourite animal is also \033[1;3m{animal}\033[0m!')



if __name__ == '__main__':
    main()