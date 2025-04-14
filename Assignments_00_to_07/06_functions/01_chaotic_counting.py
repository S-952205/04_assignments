# iss assignment mein humein ek function chaotic_counting() likhna hai jo numbers 1 se 10 tak print kare.
# Lekin is counting ke beech mein ek twist hai: Har number print karne se pehle, humein done() function call karna hai.
# done() function randomly decide karta hai (probability DONE_LIKELIHOOD ke hisaab se) ke counting rokni chahiye ya nahi.
# Agar done() function True return karta hai, to chaotic_counting() function immediately end ho jata hai
# (return statement use karke), aur phir main() function "I'm done" print karta hai.

import random

DONE_LIKELIHOOD = 0.3

def chaotic_count():
    
    for i in range(10):
        curr_num = i + 1

        # agar done function true return kray ga tw yahan loop or function khtm hojainge agr
        # done false return krraha tw number print hoga afar false ata raha tw 9 tk number print
        # hotay jainge jokay curr_num main 1 1 krkay arahay 1,2,3 etc agar false hoo tb
        # done() kabhi True nahi hua tw → Output: 1 2 3 4 5 6 7 8 9 10.
        if done():
            return # Agar done() True ho jaye, to function execution yahin se rok do, aur main() par wapas aa jao.
        
        print(curr_num, end=' ')



def done():
    # random.random() 0 se 1 ke beech ek random number generate karta hai (jaise 0.1, 0.5, 0.8) float value.
    # Agar yeh number 0.3 se chota hai (30% cases mein), toh True return hota hai.
    if random.random() < DONE_LIKELIHOOD:
        return True
    return False


def main():

    print('I m going to count until 10 or until i feel like something. whichever comes first')
    chaotic_count()
    print('I m done')


if __name__ == '__main__':
    main()