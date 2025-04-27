# iss program main hum suer say number input leinge or uska double print kratay raheingay jb tk woo 
# 100 say bara na hojai.


def main():
    
    # user input 
    curr_value: int = int(input('Enter a number: '))

    # curr_value jb tk 100 say less hai loop true hai or chlta rahay ga
    while curr_value < 100:
        curr_value = curr_value * 2 # curr_value ko 2 say multiple krkay curr_value ko update krdo
        print(curr_value, end=' ') # simple print sb numbers same line main comma separated
    
    print()


if __name__ == '__main__':
    main()