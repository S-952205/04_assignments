# iss program main hum user say 3 input leinge jo user data hoga or ussay return krein gay.


def get_user_Data():
    
    first_name: str = input('what is your first name?: ')
    last_name: str = input('what is your last name?: ')
    email: str = input('what is your email address?: ')

    # tuple packing jb hum multiple values return krtay issay hum tuple packing kehtay hain
    # mtlb teeno values humein tuple main mileinge esay (first_name, last_name, email).
    return first_name, last_name, email 



def main():

    # tuple unpacking: humnay data variable main store krdiya tuples 
    # ka number or variable ka number same rehna chahiye abhi hum issay use nhi krrahay yeh sirf yaad 
    # rakhnay kayliye hai kay unpacking kesay hoti.
    # fname, lname, email = get_user_Data()  


    user_data = get_user_Data()
    print(f'Recieved the following data: {user_data}')


if __name__ == '__main__':
    main()