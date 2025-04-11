# iss program main humnay user say year lena hai or batana hai kay jo year diya gya kya woo leap
# year hai ya nhi hai leap year woo year hota jismain 366 days hotay feb main 29 days hoty hain
# leap year ko check krnay kayliye georgian method hai usko follow krkay krsktay jokay yeh hai
# Leap Year ki Conditions (Gregorian Calendar ke Mutabiq):
# Condition 1: Year 4 se poora divide ho (evenly divisable by 4) (year % 4 == 0)
# Condition 2: Agar year 100 se divide ho, to leap year nahi hai UNLESS
# Condition 3: Year 400 se bhi divide ho (year % 400 == 0) 
# Evenly divisible = Zero remainder.


def main():

    year: int = int(input('Please input a year: '))

    # Condition 1 check kari (Divisible by 4?)
    if year % 4 == 0:  
        # Condition 2 check kari (Divisible by 100?)
        if year % 100 == 0: 
            # Condition 3 check kari (Divisible by 400?)
            if year % 400 == 0: 
                print("That's a leap year")
            else:
                print("That's a leap year")
        else:
            print("That's a leap year")   
    else:
        print("That's not a leap year")

if __name__ == '__main__':
    main()