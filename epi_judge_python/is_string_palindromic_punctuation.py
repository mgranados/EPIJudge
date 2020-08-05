from test_framework import generic_test


def is_palindrome(s: str) -> bool:
    # test from [i, , , , j]
    i = 0
    j = len(s) - 1
    while j > i:
        if not s[i].isalnum():
            i += 1
            continue
        if not s[j].isalnum():
            j -= 1
            continue

        if s[i].lower() != s[j].lower():
            return False

        i+=1
        j-=1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_palindromic_punctuation.py',
            'is_string_palindromic_punctuation.tsv', is_palindrome))
