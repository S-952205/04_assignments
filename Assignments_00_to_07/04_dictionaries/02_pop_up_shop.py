#  iss program main hum food_shop calculator banarahay hain user ko dictionary say fruit dikhanay 
# or user say pouchna woo kitnay fruits lena chahtay 1 1 fruit jo with price dictionary main hai
# unpay loop chalakr one by one dikhainge.

def main():

    fruits: dict = {'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

    # total start main zero hai
    total_amount:int = 0

    for fruit in fruits:

        price: int = fruits[fruit] # price main fruit ka price store krdiya ex: 'apple': 1.5 -> 1.5 price main
        amount: int = int(input(f'How many {fruit} you want to buy? '))  # amount kay qunatity aige kitnay khareedna chahta

        total_amount += price * amount # price multiply amount

    print(f'Total is: ${total_amount}')


if __name__ == '__main__':
    main()
    
