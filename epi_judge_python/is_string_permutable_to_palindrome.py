from test_framework import generic_test


def can_form_palindrome(s: str) -> bool:
    char_count = {}
    for char in s:
        if not char in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

    odd = 0
    even = 0
    for counted in char_count.values():
        if counted % 2 == 0:
            even += 1
        else:
            odd += 1

    if odd > 1:
        return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_string_permutable_to_palindrome.py',
            'is_string_permutable_to_palindrome.tsv', can_form_palindrome))
