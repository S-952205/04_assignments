# Iss program amin hum feet ko inches main convert krrahay hain.

# Constant hai hamesha fixed hee rahay ga
INCHES_IN_FOOT: int = 12

def main():

    feet: float = float(input('Enter number of feet: ')) 

    # Conversion feet ko inches main multiply krkay.
    inches: float = feet * INCHES_IN_FOOT
    print(f'That is {inches} inches') 


if __name__ == '__main__':
    main()