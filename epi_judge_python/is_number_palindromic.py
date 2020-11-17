from test_framework import generic_test
import math

def is_palindrome_number(x: int) -> bool:
    # avoid converting to string
    if x < 0:
        return False
    if x == 0:
        return True

    loged = math.floor(math.log10(x))
    while loged > 0:
        l = math.floor(x / math.pow(10,loged))
        r = x % 10 
        if l != r:
            return False
        x = x - l * math.pow(10, loged)
        x = math.floor(x/10)
        loged -= 2

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
