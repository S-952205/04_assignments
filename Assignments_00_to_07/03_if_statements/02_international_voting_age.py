# iss program main hum user say uski age input leinge or uski age kee basic pay conditionas lagainge check krein gay
# kya woo specific conutry main vote denay kayliye certain age hai ya nhi hai.
# \u001b[34m input ka text blue krayga.

# colorrama library hai jo terminal ko colorful krnay ka support deti hai.
from colorama import Fore, init

# Har print ke baad auto reset ho jayega init ko hum customize krsktay hain iskay parameter main mtlb humein youn
# input ya print main {Fore.RESET} phir reset kayliye nhi likha prayga sirf start main fore.blue ya koi bhe color likhein gay.
# init(autoreset=True) Har print ke baad auto reset ho jayega
init()  # Windows ke liye zaroori hai Windows terminal by default ANSI color codes ko support nahi karta.


PETURKSBOUIPO: int = 16 
STANLAU: int = 25
MAYENGUA: int = 48


def main():
    # user say age input lerahay
     user_age: int = int(input(f'{Fore.BLUE}How old are you?{Fore.RESET} '))

     # check krrahay hain kya user peturksbouipo main vote deskta
     if user_age >= PETURKSBOUIPO:
         print(f"You can vote in peturksbouipo where the voting age is {PETURKSBOUIPO}")
     else:
         print(f'You cannot vote in peturksbouipp where the voting age is {PETURKSBOUIPO}')
    
     # check krrahay hain kya user stanlau main vote deskta
     if user_age >= STANLAU:
         print(f"You can vote in stanlau where the voting age is {STANLAU}")
     else:
         print(f'You cannot vote stanlau where the voting age is {STANLAU}')    
 
     # check krrahay hain kya user mayengua main vote deskta
     if user_age >= MAYENGUA:
         print(f"You can vote in mayengya where the voting age is {MAYENGUA}")
     else:
         print(f'You cannot vote mayengya where the voting age is {MAYENGUA}')  



if __name__ == '__main__':
    main()

    



