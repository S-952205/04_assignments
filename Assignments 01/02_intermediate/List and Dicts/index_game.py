# iss program main humnay index game banana hai iss game main hum list pay multiple operation
# perform krwain gay means list access krna, list modify krna, list slicing jo method user choose kray
# ga woo action perform hoga or ussay related baki kaam or result.

from colorama import Fore, init
init()

# yeh methid list kay element ko index say access kray ga
def access_element(lst, index):

    try:
        get_element = lst[index]
        return get_element
    except IndexError:
        print('Index out of range.')

# yeh method list ko modify krraha hai
def modify_element(lst, index, value):

    try:
        lst[index] = value
        return lst
    except IndexError:
        print('Index out of range.')

# yeh method list slicing krraha hai list ka specific part get krraha hai
def slicing(lst, start, end):

    try:
        return lst[start:end]
    except IndexError:
        print('Index out of range.')



def index_game():
    
    print('\n')
    mix_list: list = ['tools', 24, 'Zain', 7, 'movie']
    print(f'Current list: {mix_list}')
    print('-----------------------------------------------\n')

    # user say action input leliya jo woo list pay perform krna chahraha hai
    print(f"Choose an operation: {Fore.BLUE}access, modify, slice{Fore.RESET}")
    action: str = input('Enter acton: ').lower()

    # jo action user select krayga uski base pay condition chalay gee or uss condition ka code run hoga
    if action == 'access':
        index: int = int(input('Enter index to access: '))
        print(access_element(mix_list, index))
        print('\n')

    elif action == 'modify':
        index: int = int(input('Enter index to modify: '))
        new_value = input('Enter new value: ')
        print('Modified List',modify_element(mix_list, index, new_value))
        print('\n')

    elif action == 'slice':
        start: int = int(input('Enter start index: '))
        end: int = int(input('Enter end index: '))
        print('Sliced List',slicing(mix_list, start, end))
        print('\n')

    else:
        print('Invalid Action') # action upper diye gai 3 ka illawa koi or hua tw invalid hoga
        print('\n')



if __name__ == '__main__':
    index_game()