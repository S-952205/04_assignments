# iss program main hum user say say correct affirmation leinge jo affirmation pehlay say stored hai user ko same 
# wohi input main deni hogi tb program correct hoga.

# yeh global variable hai issay function main access krsktay magar issay modify ya change nhi
# krsktay function main global varible sirf read or compare kayliye hain.
AFFIRMATION: str = 'I m capable of doing anything i put my mind to.'
print(f'Please type the following affirmation: {AFFIRMATION} ')

def main():

    # Yeh local variable hai main issay modify krskta update krskta error nhi ayga
    # qynke yeh function kay under hai apnay scope main hai.
    user_feedback:str = input()
    
    # while loop tab tak chalay ga jab tak user ka input AFFIRMATION ke equal nahi hota.
    while user_feedback != AFFIRMATION:
        print('That was not the affirmation')
        print(f'Please type the following affirmation {AFFIRMATION} ')

        user_feedback:str = input()
    
    print(f"That's right! :)")


if __name__ == '__main__':
    main()