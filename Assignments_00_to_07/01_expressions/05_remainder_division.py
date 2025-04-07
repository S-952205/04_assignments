# Iss program main user say 2 number larkr unhein divide krkay unka result (bina decimal kay)
# or remainder display krna.


def main():

    #  User se do numbers input liye. dividend woo hota jisay divide krana divisor woo hai jis number say divide krna.
    dividend: int = int(input('\033[1;3mPlease enter an integer to be divided:\033[0m ')) 
    divisor: int = int(input('\033[1;3mPlease enter an integer to divide by:\033[0m '))

    # Quotient or remainder calculate kiya quotient 2 numbers divide hone ke baad poora number (Bina decimal ke)
    quotient: int = dividend // divisor
    # Bacha hua number (Remainder) 
    remainder: int = dividend % divisor

    # Result
    print(f'The result is {quotient} with a remainder of {remainder}')


if __name__ == '__main__':
    main()