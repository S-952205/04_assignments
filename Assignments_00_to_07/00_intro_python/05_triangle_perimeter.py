# iss program main hum user say triangle ke each side kee length input main leraha hain or perimeter
# of triangle print krrahay.

def main():
    
    side_1: float = float(input('\033[1;3mEnter the length of side 1:\033[0m '))
    side_2: float = float(input('\033[1;3mEnter the length of side 2:\033[0m '))
    side_3: float = float(input('\033[1;3mEnter the length of side 3:\033[0m '))

    perimeter = side_1 + side_2 + side_3
    print(f'The perimeter of the triangle is {perimeter}')



if __name__ == '__main__':
    main()