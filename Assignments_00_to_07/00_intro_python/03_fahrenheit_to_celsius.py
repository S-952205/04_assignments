# yeh program user say fahrenheit main temperature lega or ussay celsius main convert krkay
# display kray ga.

def main():
    
    # Step 1: Fahrenheit input (convert to float agar int bhee dega tw float main value hogi convert)
    fahrenheit: float = float(input('Enter temperature in Fahrenheit: '))

    # Step 2: fahrenheit say celsius main convert krdiya formula say 
    celsius = (fahrenheit - 32) * 5.0/9.0

     # Step 3: Result desplay krdiya celcius main   
    print(f'Temperature: \033[1;3m{fahrenheit}F\033[0m = {celsius}C')



if __name__ == '__main__':
    main()