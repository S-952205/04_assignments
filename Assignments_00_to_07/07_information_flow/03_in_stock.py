# iss program main hum user say input leinge fruit or eik function banainge jo 
# bataiga kay jo fruit user nay diya woo stock main moojood hai or hain tw kitnay hain

def num_in_stock(fruit: str):
    
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'peer':
        return 1000
    
    else: 
        return 0 


def main():

    fruit: str = input('\033[1:3mEnter a fruit:\033[0m ')
    stock: int = num_in_stock(fruit)

    if stock == 0:
        print('This fruit is not in stock.')
    
    else:
        print('This fruit is in stock ! here is how many: ')
        print(stock)



if __name__ == '__main__':
    main()