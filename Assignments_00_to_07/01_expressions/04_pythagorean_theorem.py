# iss program main humnay user sy do sides input lein right triangle kee ab(perpendiculer) 
# bc(perpendiculer) or pythagoras theorem kay zariye say 3rd side (Hypotenus) nikali.


# math module say hum math related functionality letay jesay humnay sqrt ka method use kiye
import math 

def main():

    ab: float = float(input('Enter the length of AB: ')) # 1 side length
    ac: float = float(input('Enter the length of AC: ')) # 2 side length

    # ab or ac ka square niklay ga or woo sum hokr 3rd side bc kee length ajaigee.
    bc: float = math.sqrt(ab ** 2 + ac ** 2) 
    print(f'the length of the BC ( The Hypotenus ) is: {bc}')


if __name__ == '__main__':
    main()