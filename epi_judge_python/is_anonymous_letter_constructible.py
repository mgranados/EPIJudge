from test_framework import generic_test
import collections


def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    # tiempo lineal = O(n) + O(m)
    mag_count = {}
    for char in magazine_text:
        if char in mag_count:
            mag_count[char] += 1
        else:
            mag_count[char] = 1

    for char in letter_text:
        if char not in mag_count:
            return False
        if char in mag_count:
            mag_count[char] -= 1

        if mag_count[char] < 0:
            return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
