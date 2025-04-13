# Program likha jo user se ek number input le aur us number ko double karke
# print karta rahay, jab tak ke woh number 100 say bada na ho jaye.


def main():
   
    curr_value: int = int(input('Enter a number: '))

    # tb tk chlay ag loop jb tk curr_value 100 say bara na hojai.
    while curr_value < 100:
        curr_value = curr_value * 2 # curr_value multiply 2 say hoga or curr_value main store hojaiga
        # curr value print end='' ka mtlb hai eik hee line main number print hongein space-separated
        print(curr_value, end=' ')

    print()

if __name__ == '__main__':
    main()
