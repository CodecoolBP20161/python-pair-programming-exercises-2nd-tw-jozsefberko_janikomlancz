import random


def passwordgen():

    pwd = []
    for char in range(random.randrange(8, 21)):
        pwd.append(chr(random.randint(33, 126)))
    pwds = "".join(pwd)
    return pwds


def main():
    print("This is your new password:", passwordgen())
    return


if __name__ == '__main__':
    main()
