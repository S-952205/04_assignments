# is program main humnay user say nu,bers lenay or list banakr list main add krnay hain phir check krna
# hai konsa number list main kitni baar aya hai yani count dikhana nuber or count dictionary main key
# value main.

from colorama import Fore, init
init()

# Yeh function user say number input laekr list main add krraha hai.
def get_user_numbers():

    # empty list initialize kee
    user_list: list = [] 

    while True:
        num_for_list = input(f'{Fore.BLUE}Enter a number:{Fore.RESET} ')

        # agar user blank dekr enter kray loop break krdo code say bahr ajao.
        if num_for_list == '': 
            break

        # num_for_list ko int main convert krkay list main bhejdiya.
        user_list.append(int(num_for_list)) 
    
    return user_list



# iss function ko hum list deraha or yeh list say number or woo kitni dafa aya uska count key:value main
# dict main add krray ga
def count_nums(user_number):

    num_dict: dict = {}

    # list ka eik eik element num main ayga or check hoga kya num main jo hai woo num_dict main hai?
    for num in user_number:
        # agr num_dict main nhi hai tw add krdo num for ex: 3 or uska count = 1 esay dictionary main eik key:value pair
        # add krdiya [num] means num main woo number jo list say aya woo ai jo key hogya or value = 1.
        if num not in num_dict: 
            num_dict[num] = 1
        else:
            num_dict[num] += 1 # agar num jo hai woo pehlay say dict main hai tw uski value 1 say update krdoo.
    
    return num_dict

# Yeh sirf print kray ga count ko or key koo.
def print_count(num_dict):
    
   # Ye loop dictionary ki sirf keys ko iterate karta hai (num variable mein) yani num main keys ainge one by one.
   for num in num_dict:
       print(f'{num} appears {num_dict[num]} times') # num_dict[num] → Dictionary mein num key ki value deta hai.



def main():
    user_number = get_user_numbers()
    num_dict = count_nums(user_number)
    print_count(num_dict)



if __name__ == '__main__':
    main()