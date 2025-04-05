# iss program main humnay user say woo number input liye jiska ussay square nekalna hai.

def main():

    number = float(input('\033[1;3mType a number to see its square:\033[0m '))

    # Number ko khud se multiply karke square nikalte hain.
    square = number * number
    print(f'{number} squared is {square}')


if __name__ == '__main__':
    main()