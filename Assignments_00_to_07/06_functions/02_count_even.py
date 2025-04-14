# humnay eik program banana hai jo user say integer lay or phir uss integer ko humnay list main
# add krna hai or phir list main kitnay even number hain unka count dikhana hai kay 2 even number
# hain ya 3 ya 4 etc.


# yeh function integer lega or list main add krkay list return krayga
def get_lst_of_int():

    lst: list = []
    user_input = input('Enter an integer and press enter to stop: ')

    while user_input != "":
        lst.append(int(user_input))
        user_input= input('Enter an integer and press enter to stop: ')

    return lst

def count_even(list_integer):
    
    count: int = 0

    for num in list_integer:
        if num % 2 == 0: # Agar even hai (2 se divide karne par remainder 0)
            count += 1
    
    print(count)



def main():
    lst: list = get_lst_of_int()
    count_even(lst)


if __name__ == '__main__':
    main()
