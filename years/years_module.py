import datetime


def years(age):
    age_left = 100 - age
    hundred = age_left + int(datetime.date.today().strftime("%Y"))
    return hundred


def main():
    name = input("What is your name?: ")
    age = int(input("How old are you?: "))
    print("Hello %s! You will turn 100 in %d." % (name, years(age)))
    return


if __name__ == '__main__':
    main()
