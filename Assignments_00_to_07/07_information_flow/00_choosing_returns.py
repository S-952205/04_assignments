# iss program main hum user say uski age input leinge or batainge kya wo adult hai ky nhi

ADULT_AGE: int = 18 # adult age in USA

def isAdult(age: int):
    return age >= ADULT_AGE

def main():
    age: int = int(input('\033[1;3mHow old is this person?:\033[0m '))
    
    if isAdult(age):
        print('True\nEntered age is an adult age')
    else:
        print('False\nEntered age is not an adult age')


if __name__ == '__main__':
    main()