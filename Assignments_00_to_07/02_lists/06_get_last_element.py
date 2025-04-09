# iss program main hum user say input leinge eik eik element or list banainge or
# list ka last element get krkay display krein gay.

def get_last_element(lst: list):
    
    print("Last Element of list: " + lst[-1]) # last element display krayga


# user say input main element laekr list banaiga
def get_list():

    lst: list = []
    element: str = input('Enter an element of a list and press enter to stop. ')

    while element != "":
        lst.append(element)
        element: str = input('Enter an element of a list and press enter to stop. ')
    
    return lst


def main():

    lst = get_list()
    get_last_element(lst)


if __name__ == '__main__':
    main()


