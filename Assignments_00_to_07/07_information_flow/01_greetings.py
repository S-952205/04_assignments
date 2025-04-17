# iss program main hum user say uska name leinge or ussay greet krein gay.



def greet(name: str):
    return f'Greetings {name}!'


def main():
    name: str = input("\033[1;3mWhat's your name:\033[0m ")
    print(greet(name))


if __name__ == '__main__':
    main()