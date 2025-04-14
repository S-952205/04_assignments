# iss program main hum user say 1 number input leingay or uskay sb divisor print krein gay
# (wo numbers jo uss number ko bilkul divide kar sakte hain, remainder nahi bachta)
# Socho aapke paas 6 candies hain. agar aap 3 friends mein equal baant sakte hain (2-2 candies each),
# toh 3 divisor hai.


def print_divisor(num):
    
    print("Here are the divisors of", num)

    for i in range(num):
        curr_divisor = i + 1   # 1 main 0 aya first time 0 + 1 = 1 curr_divisor = 1 issi trhn i = 1, i = 2 ...... 
        if num % curr_divisor == 0: # num % 1 == 0 tw print curr_divisor yani num in in number say complete divide hota
            print(curr_divisor)


def main():

    num: int = int(input('Enter a number: '))
    print_divisor(num)     


if __name__ == '__main__':
    main()