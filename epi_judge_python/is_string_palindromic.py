from test_framework import generic_test


def is_palindromic(s: str) -> bool:
    # check extremes
    #   ↓        ↓
    # [ 1, 2, 3, 4]
    #      ↓  ↓
    # [ 1, 2, 3, 4]

    # [~i] = 1 = -1
    return all(s[i] == s[~i] for i in range(len(s) // 2))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_string_palindromic.py',
                                       'is_string_palindromic.tsv',
                                       is_palindromic))
