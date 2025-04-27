# iss program main humnay 1 say 100 kay beech random number generate krnay hain total 10 dafa
# or eik line main print krnay

import random

N_NUMBER: int = 10 # 10 dafa print krna tbhi 10 store
MIN_VAL: int = 1
MAX_VAL: int = 100


def main():
    
    for _ in range(N_NUMBER):

        num: int = random.randint(MIN_VAL, MAX_VAL)
        print(f'{num}', end=' ')
    
    print()


if __name__ == '__main__':
    main()