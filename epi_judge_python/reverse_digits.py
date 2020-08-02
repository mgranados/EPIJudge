from test_framework import generic_test
import math

def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    result_pow = 0
    result = 0
    abs_x = abs(x)
    power = math.floor(math.log10(abs_x))

    while power >= 0:
        current = math.floor(abs_x / (10 ** power))
        result += current * (10 ** result_pow)
        abs_x -= current * 10 ** power
        power -= 1
        result_pow += 1

    return result * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
