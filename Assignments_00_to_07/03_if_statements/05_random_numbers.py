# iss program main humnay 10 random number print kranay hain 1 say 100 kay beech.

import random

N_NUMBERS : int = 10 # 10 number print krnay tw 10 store
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():

    number: list = []

    for _ in range(N_NUMBERS): # _ underscore ka matlab hai ke hum loop variable ko use nahi kar rahe.
        num = random.randint(MIN_VALUE, MAX_VALUE) # 1 say 100 kay beech main number generate krkay dega
        number.append(str(num)) # num say str main convert krdiya example: 45 --> '45'

    print(' '.join(number)) # " ".join(numbers) in numbers ko ek line mein space-separated print karta hai ex: '45 22 49'.
    # join method integer pay nhi string pay use hota tbhi pehlay humnay num ko string main convert kiya.

if __name__ == '__main__':
    main()