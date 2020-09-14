from test_framework import generic_test
import math

def square_root(x: float) -> float:
    if x == 1.0:
        return 1.0

    left, right = 1.0, x

    if x < 1.0:
        left = x
        right = 1.0

    while not math.isclose(left, right):
        mid = (0.5 * (left + right))
        if mid * mid > x:
            right = mid
        else:
            left = mid

    return left


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('real_square_root.py',
                                       'real_square_root.tsv', square_root))
