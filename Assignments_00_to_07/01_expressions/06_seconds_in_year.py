# iss program main humnay calculate krnay seconds kay 1 saal mai kitnay
# seconds hotay hai or woo display krnay hain.

DAYS_PER_YEAR = 365
HOURS_PER_DAY = 24
MIN_PER_HOUR = 60
SEC_PER_MIN  = 60

def main():

    second_per_year = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN
    print(f'There are {second_per_year} seconds in a year.')


if __name__ == "__main__":
    main()