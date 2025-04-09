# iss program main hum list kay hr element ka double krrahay mtlb hr element ko 2 say multiply krrahay hain.

def main():

    # original list
    numbers: list[int] = [1, 2, 3, 4]

    # len say 4 ayga list kee length range(4) range main 4 means 0 say 3 tk 4 included nhi hoga
    # humnay indices(index) nekaldiye list kay humein agar list kay each element ko modify krna tw
    # hum uss elem ka index use krkay krtay hain.
    for i in range(len(numbers)):
        elem_at_index = numbers[i] # i = 0 0 pay 1 hai elem main 1 gya.
        numbers[i] = elem_at_index * 2 # 1 ko multiply krdiya 2 say or same 0 index pay ussay daldiya.
    
    print(numbers) # yeh doubled list display kray ga ex: [2, 4, 6, 8]
        



if __name__ == '__main__':
    main()