# iss program main hum list main 3 copies add krein gay data kee or return kiye baghair list main 
# data add krein gay qynke list or dictionaries mutable hain unhein modify krsktay hain return kee
# zrorart nhi hai numbers or string immutable hain unhein return krna pray ga.

# Mutable (List/Dict): Function mein direct changes hote hain (return ki zaroorat nahi).
def add_three_copies(my_list: list, data: str):

    for i in range(3):
        my_list.append(data) # 3 dafa my_list main data add hoga original list (mutable), directly modify hoti hai.
        # humnay yahan return nhi example return my_list phir bhee list modified hui immutable hai tbhi
    

def main():

    message = input('\033[1;3mEnter a message to copy:\033[0m ')

    my_list = []
    print(f'List Before: {my_list}') # empty list show hogi List Before: []

    add_three_copies(my_list, message)
    print(f'List After: {my_list}') # list main 3 values show hongein List After: ['syed', 'syed', 'syed']


if __name__ == '__main__':
    main()



