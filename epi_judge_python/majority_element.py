from typing import Iterator

from test_framework import generic_test


def majority_search(stream: Iterator[str]) -> str:
    # [a,b,b,a,c,c,a,a] 
    # majority element is a
    count_c = 0
    element = None
    for value in stream:
        if count_c == 0:
            element = value
            count_c += 1
        elif element == value:
            count_c += 1
        elif element != value:
            count_c -= 1

    return element


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('majority_element.py',
                                       'majority_element.tsv',
                                       majority_search_wrapper))
