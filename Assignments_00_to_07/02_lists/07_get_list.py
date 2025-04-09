# iss program main hum user say eik eik krkay value leinge input or phir list banakr
# list display krdeinge jb user empty input chor kr enter kray ga list display hogi
# while loop kee condition false hojaigi.

def main():

    lst: list = [] # empty list

    val: str = input('Enter a value: ') # first value lee input

    while val: # agar user ka input empty nhi hai tw val true hai.
        lst.append(val) # list main value add kee
        val: str = input('Enter a value: ') # user say second value lee

    print(f'Here is the list: {lst}')


if __name__ == '__main__':
    main()