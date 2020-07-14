from test_framework import generic_test


def gcd(x: int, y: int) -> int:
    if x == 0:
        return y
    if y == 0:
        return x
    if x >= y:
        return gcd(x % y, y)
    if y > x:
        return gcd(x, y % x)


if __name__ == '__main__':
    exit(generic_test.generic_test_main('euclidean_gcd.py', 'gcd.tsv', gcd))
