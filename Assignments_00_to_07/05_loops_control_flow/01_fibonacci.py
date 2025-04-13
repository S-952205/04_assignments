# iss program main hum fibonacci sequence generate krein gay fibonacci series main pehlay 2 number
# fixed hota hain f(0) = 0 or f(1) = 1 yani 0 or 1 fibonacci sequence main hr agla number pichlay 2
# ka sum hota hai ex: 0 1 1 2 3 5 8 13 21.


# MAX_TERM_VALUE = 10000 constant hai. Yeh woh maximum value hai jahan 
# tak hum Fibonacci terms print karna chahte hain.
MAX_TERM_VALUE: int = 10000

def main():
    
    curr_term: int = 0 # hamesha pehla num 0 hota 
    next_term: int = 1 # or dusra num 1 hota fibonacci ka

    # while loop tab tak chalta hai jab tak curr_term MAX_TERM_VALUE (10,000) se chota ya barabar hai.
    while curr_term <= MAX_TERM_VALUE:

        print(curr_term)

        term_after_next: int = curr_term + next_term # 0 + 1 = 1 stored in term_after_next
        
        # variables ko update kardiya
        curr_term = next_term # curr_term 0 tha ab 1 hai 
        next_term = term_after_next # next_term 1 tha ab 1 hai


if __name__ == '__main__':
    main()