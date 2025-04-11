# iss program main hum user say age laekr conditions lagain kay kya user rollercoster
# ride lay skta hai ya nhi agar woo minimum age ko satisfy kray tw woo layskta werna nhi.


MIN_HEIGHT: int = 50

def tall_enough_extention():

    # while loop infinite chlta rahayga
    while True:
        height_str:float = input('\033[1;3mHow tall are you?\033[0m ')

        if not height_str:  # agar height_str empty hai khali hai tw break krjao loop code end hojaiga yahan.
            break

        height = float(height_str) # height_str ko string say float main convert kiya takay comparison krskein

        # condition
        if height >= MIN_HEIGHT:
            print('You are tall enough to ride!')
        else:
            print('You are not tall enought to ride, but maybe yext year!')



if __name__ == '__main__':
    tall_enough_extention()