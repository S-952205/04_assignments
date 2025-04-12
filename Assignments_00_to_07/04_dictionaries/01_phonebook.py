# Iss program main hum user say name or number input leinge or ussay dictionary main store krein gay
# or phir dictionary name or num kay sath display krein gay or eik function esa hoga jissay user name
# say number seacrh krsakay ga.


# yeh function user say name or number input laekr dictionary main add krraha hai
def read_phone_numbers():

    phonebook: dict = {} # start main empty user input kay baad ismain key:value pair main data hoga

    while True: 

        name: str = input('Enter a name: ')
        if name == "": # agar user blank chor kr enetr dabay tw loop yahan break hojaiga
            break

        number = str(input('Enter a number: '))

        phonebook[name] = number # dictionary main data key: value main add {name:number}

    return phonebook

# yeh funtion poori phonebook with name and number display krraha hai
def print_phonebook(phonebook):

    for name in phonebook:
        print(f'{name} -> {phonebook[name]}')



# iss function say hum name inpute dekr uska number dekhrahay
def lookup_numbers(phonebook):

    while True:
        name: str = input('Enter name to lookup: ')
        if name == "":
            break

        # agar name nhi hai phonebook main tw
        if name not in phonebook:
            print(f'{name} is not in the phonebook')
        else:
            print(phonebook[name])
    


def main():
    phonebook: dict = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
