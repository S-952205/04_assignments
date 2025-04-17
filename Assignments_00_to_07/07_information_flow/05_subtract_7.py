# iss program main hum eik funtion banainge jo 7 substract krayga uss number say jo hum deinge

def substract_seven(num: int):

    result = num - 7
    return result


def main():
    
    num: int = 7
    num = substract_seven(num)
    print(f'this should be zero: {num}')


if __name__ == '__main__':
    main()