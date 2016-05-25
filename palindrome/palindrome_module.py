
def palindrome(stri):
    stri = stri.replace(" ", "")
    reverse = str(stri[::-1])
    print(reverse)
    if stri.lower() == reverse.lower():
        print('That is a palindrome!')
        return True
    else:
        print('That is not a palindrome!')
        return False


def main():
    stri = input('Enter a word to check: ')
    palindrome(stri)
    return


if __name__ == '__main__':
    main()
