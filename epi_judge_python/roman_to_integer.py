from test_framework import generic_test


def roman_to_integer(s: str) -> int:
    # <- add 
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    sum = 0
    for i in range(len(s) -1 , -1, -1):
        if i < len(s) - 1: # index error
            if romans[s[i]] < romans[s[i+1]]:
                sum -= romans[s[i]]
            else:
                sum += romans[s[i]]
        else:
            sum += romans[s[i]]


    return sum


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('roman_to_integer.py',
                                       'roman_to_integer.tsv',
                                       roman_to_integer))
