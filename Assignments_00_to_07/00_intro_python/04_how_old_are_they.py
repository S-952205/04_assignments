# iss program main hum 5 friends kee age ko calculate krkay display krrahein hain given
# riddles ko follow krtay huay.

def main():
    
    Anton: int = 21          # Anton's age is 21
    Beth: int = Anton + 6    # Beth is 6 years older than Anton
    Chen: int = 20 + Beth    # Chen is 20 years older than Beth
    Drew: int = Chen + Anton # Drew's age is Chen's age + Anton's age
    Ethan: int = Chen        # Ethan is the same age as Chen


    # Print out all of the ages!
    print(f'Anton is {Anton}')
    print(f'Beth is {Beth}')
    print(f'Chen is {Chen}')
    print(f'Drew is {Drew}')
    print(f'Ethan is {Ethan}')



if __name__ == '__main__':
    main()