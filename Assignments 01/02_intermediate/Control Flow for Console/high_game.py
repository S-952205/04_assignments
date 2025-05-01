# iss program main hum game banainge high-game jismain 5 rounds hongein or game main 2 dafa 1 to 100
# numbers generate kreingay 1 computer kayliye or 1 hamaray liye computer ka hum nhi dekhein gay
# hum sirf apna dekhein gay or input leinge user say higher ya lower agr user higher deta means kay uska number 
# computer say high hai or high hua tw uska score 1 say increase hoga agr user nay lower diya or lower hee hua number bhee
# tw same score 1 say increase agar tie hua user or computer ka number same hua tw computer jeet jaiga same esay hee 5
# rounds hongein or last main user ko uski progress dikhai jaigee.

import random


def main():
    
    ROUNDS: int = 5  # 5 rounds ka game hai tw 5 store krdiya 5 dafa loop chalinge neechay
    score: int = 0   # score start main zero hr round main correct honay pay 1 say increase hoga

    print('\n---------------------------------')
    print('Welcome to the High-Low Game!')            # kuch nhi simple heading game kee
    print('---------------------------------\n')

    # for loop 5 round kay liye 5 dafa code chalay ga
    for round_num in range(1, ROUNDS + 1):

        print(f'Round {round_num}')

        # random numbers generate krrahay or store krrahay dono variables main
        comp_random: int = random.randint(1, 100)
        user_guess: int = random.randint(1, 100)

        print(f'Your number is {user_guess}')

        # higher or lower user say lerahay
        user_input: str = input('Do you think your number is higher or lower than the computers?: ') 

        # if main 2 conditions hain first condition main 2 conditions hain dono true hongein tw poori true or score gain
        # agr first true nhi tw second main dono true honi chahiye tb second poori true or score gain agr dono nhi phir
        # elif or last else.
        if (
            (user_input == 'higher' and user_guess > comp_random)
            or   # eik bhee true hui if chalay ga
            (user_input == 'lower' and user_guess < comp_random)
            ):
            score += 1
            print(f'You were right! the computer number was {comp_random}')

        elif user_guess == comp_random:
            print(f'Its a tie! Computer wins ties. The number was {comp_random}')

        else:
            print(f'Aww, thats incorrect the computer number was {comp_random}')

        
        print(f'Your score is now {score}') # hr round ka score print krraha hr round kay end main
        print('\n---------------------------------\n')

    print("Your final score is", score) # sb round finish honay kay baad ka total score


    # yeh last main game kee progress pay jo appreciation bnti woo display kee user kee progress kee base pay
    if score == ROUNDS:
        print('Wow! you played perfectly!')
    elif score > ROUNDS // 2:
        print('Good, you played really well!')
    else:
        print('Better luck next time!')   


    print('\n')     


if __name__ == '__main__':
    main()