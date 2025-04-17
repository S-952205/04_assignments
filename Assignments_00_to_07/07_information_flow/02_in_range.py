# hum iss program main eik function banarahay jo yeh check krkay ga kay n low or high
# kay beech main hai y low or high kay equal bhee hoskta.


def in_range(n, low, high):
    
    if n >= low and n <= high:
        return True
    
    return False


def main():
    
    n = int(input('Enter a number: '))
    low = int(input('Enter the lower: '))
    high = int(input('Enter the higher: '))
    print(in_range(n, low, high))



if __name__ == '__main__':
    main()