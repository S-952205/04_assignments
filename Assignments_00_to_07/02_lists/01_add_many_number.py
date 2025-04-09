# iss rogram main hum function banainge jo number list laega or unka sum caluclate krkay return kray ga.


# yeh function sum kray ga core logic iss function main hai
def add_many_numbers(numbers: int) -> int :

    # iss variable main sum store hoga abhi yeh variable khali hai zero hai start main
    total_so_far:int = 0

    # for loop one by one number totalsofar main add hongein sum hokr
    for number in numbers:
        # total_so_far = total_so_far + number
        total_so_far += number # eik eik krkay total kay sath number plus hota jaiga or sum aiga.
    return total_so_far


def main():

    numbers: list[int] = [1, 2, 3, 4, 5] # list of numbers
    sum_of_num: int = add_many_numbers(numbers) # sum kray ga yeh function
    print(f'Sum of number of list is {sum_of_num}') # result 

if __name__ == '__main__':
    main()
        

      

