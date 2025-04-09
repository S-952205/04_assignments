# iss program main hum list ka pehla element display kreingein user say input laekr list banainge phir. 


# yeh function list ka first element print krwai ga
def get_first_element(lst: list):

    print('First Element of list: ' + lst[0]) 


# yeh function user say input lega or list create kray ga.
def get_list():

    lst: list = [] # Khali list banayi
    element: str = input('Please enter an element of the list and press enter to stop. ')

    # jb tk element main value hai while loop chalta rahay ga or input leta rahay ga while loop tb false hoga jb
    # user input empty rakh kr enter dabaiga tw empty input yeh hota ("") tw "" ! = "" mtlb false hogya loop ruk jaiga.
    while element != "": 
        lst.append(element) # Element list mein add karo
        element: str = input('Please enter an element of the list and press enter to stop. ')

    return lst  # Complete list return karo


def main():

    lst = get_list()
    get_first_element(lst)


if __name__ == '__main__':
    main()