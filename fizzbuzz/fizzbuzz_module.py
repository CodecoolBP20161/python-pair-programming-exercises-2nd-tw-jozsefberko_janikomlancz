def fizzbuzz(number):
    if number != 0:
        if number % 15 == 0:
            number = "FizzBuzz"
        elif number % 3 == 0:
            number = "Fizz"
        elif number % 5 == 0:
            number = "Buzz"
    return number


def main():
    maximum_number = int(input("Please give a maximum number:"))
    for num in range(maximum_number+1):
        print(fizzbuzz(num))
    return

if __name__ == '__main__':
    main()
