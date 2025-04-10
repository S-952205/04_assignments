# Iss program main hum nay max length rakhi constant or user say list input leinge or list
# say last element remove krein ga or print krein gay tb tk jb tk list kay element kee length max
# length kay barabar na hojai agar list main element max-length say kmm hain tw element list 
# say remove nhi hongein


MAX_LEN = 4  # List ki maximum allowed length

# shorten() function check karta hai agar list ki length > maxlength(4) say last elements
# remove honge aur print honge
def shorten(lst):
    while len(lst) > MAX_LEN:
        last_elem =  lst.pop() # .pop() - last element remove karta hai
        print(f'Last Element {last_elem}') # Removed element print karo



def get_lst():

    lst: list = []
    element = input('Please enter an element of a list and press enter to stop. ')

    while element != "":
        lst.append(element)
        element = input('Please enter an element of a list and press enter to stop. ')
    return lst
        
def main():
    lst: list = get_lst()
    shorten(lst)
    


if __name__ == '__main__':
    main()
