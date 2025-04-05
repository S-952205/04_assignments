# Yeh program user say 2 integer lega or unka sum calculate krkay display krdayga.

def main():

    print("This program adds two numbers.")

    # input() function user se string leta hai, int() se use integer mein convert karte hain.
    num_1: int = int(input('Enter the first number: ')) 
    num_2: int = int(input('Enter the second number: '))

    total: int = num_1 + num_2
    print(f'The sum of two numbers is {total}.')
    



if __name__ == '__main__':
    main()