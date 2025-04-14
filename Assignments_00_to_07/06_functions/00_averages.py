# iss program main hum 2 number ka average nikal kr display krein gay function ko 2 number deinge
# woo find kray ga average.


# yeh function 2 arguments laega unhein plus kray ga phir uss sum ko 2 say divide krayga average miljaiga
def average(a: float, b: float):
    sum: float = a + b
    return sum / 2



def main():
    
    avg_one = average(0, 10)
    avg_two = average(8, 10)
    final = avg_one + avg_two

    print(f'Avg_One: {avg_one}')
    print(f'Avg_Twe: {avg_two}')
    print(f'Final: {final}')



if __name__ == '__main__':
    main()