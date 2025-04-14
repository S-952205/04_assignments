# iss program main humnay 0 say 10 tk print kranay number or batana konsa number even ha konsa odd hai.

def main():
    
    # 0 say 9 tk i main ainge numbers
    for i in range(10):
        if odd(i): # numer 1 by 1 odd function main apss horahay or odd func calculation kay baad True ya False dega
            print('odd')
        else:
            print('even')


def odd(value):
    
    remainder = value % 2   # % (modulus operator) 2 se divide karke remainder nikalta hai.

    # Yeh line ek boolean (True/False) return karti hai agar remainder 1 hai → True return hoga agr 1
    # nhi hai tw false misal kay tor pay remainder 0 hao tw 0 == 1 false hua
    return remainder == 1   


if __name__ == '__main__':
    main()
