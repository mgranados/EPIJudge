from test_framework import generic_test


def fibonacci(n: int) -> int:
    if n <= 1:
        return n

    f_minus2, f_minus1 = 0, 1
    for _ in range(1, n):
        f = f_minus2 + f_minus1
        f_minus2 = f_minus1
        f_minus1 = f


    return f_minus1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('fibonacci.py', 'fibonacci.tsv',
                                       fibonacci))
