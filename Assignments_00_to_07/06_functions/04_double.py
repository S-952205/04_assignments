# iss program main hum user say number input leinge or uska double return kreingay.
def double(num: int) -> int :

    return num * 2
    



def main():
    
    num: int = int(input('\033[1;3mEnter a number:\033[0m '))
    num_times_two: int = double(num)
    print(f'Double that is: {num_times_two}')


if __name__ == '__main__':
    main()