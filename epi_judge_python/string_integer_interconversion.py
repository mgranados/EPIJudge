from test_framework import generic_test
from test_framework.test_failure import TestFailure
import math

def int_to_string(x: int) -> str:
    digits = '0123456789'

    answer = []
    abs_x = abs(x)

    if x == 0:
        return '0'

    if (x < 0):
        answer.append('-')

    # length of pow 10
    power_10 = math.floor(math.log10(abs_x))
    for i in reversed(range(power_10 + 1)):
        appendable = abs_x // pow(10,i)
        abs_x -= appendable * pow(10,i)
        answer.append(digits[appendable])

    return ''.join(answer)

def string_to_int(s: str) -> int:
    # "123" => 123
    # "+123" => 123
    abs_s = s[:]
    if s.startswith('+'):
        abs_s = s[1:]

    sign = 1
    if s.startswith('-'):
        sign = -1
        abs_s = s[1:]

    result = 0
    for i in reversed(range(len(abs_s))):
        result += (ord(abs_s[i]) - 48) * pow(10, len(abs_s) - 1 - i)

    return result * sign


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))
