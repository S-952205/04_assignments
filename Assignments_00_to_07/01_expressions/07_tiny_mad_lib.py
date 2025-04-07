# hum eik mad libs program banayaMad Libs ek funny word game hai jismein aap adjective 
# noun, verb waghera daal kar khali jagahon ko bharte hain. Ye words ek pre-written
# story ya sentence mein fill hote hain, jisse unexpected aur hasi-mazak wali kahani ban jati hai!

SENTENCE_START:str = "Panaversity is fun. I learned to program and used Python to make my"

def main():

    adjective: str = input('\033[1;3mPlease type an adjective and press enter:\033[0m ')
    noun: str = input('\033[1;3mPlease type a noun and press enter:\033[0m ')
    verb:str = input('\033[1;3mPlease type a verb and press enter:\033[0m ')

    print(f'{SENTENCE_START} {adjective} {noun} {verb}')
    


if __name__ == '__main__':
    main()