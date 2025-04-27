# iss program main hum user say number input leinge or uska double print krein gay jb tk woo
# double hota hota 100 say bara na hojai tb tk.


def main():
    
    curr_value: int = int(input('Enter a number: '))

    # jb tk curr_value less hai 100 say while loop true hai or chlta rahay ga
    while curr_value < 100:

        curr_value: int = curr_value * 2 # curr_value ko multilply krdiya 2 say
        print(curr_value, end=' ') # sbb numbers same line main comma separated print
    
    print()


if __name__ == '__main__':
    main()