from typing import List
import collections

from test_framework import generic_test, test_utils


def find_anagrams(dictionary: List[str]) -> List[List[str]]:
    sorted_string_to_anagrams = collections.defaultdict(list)
    for s in dictionary:
        sorted_string_to_anagrams[''.join(sorted(s))].append(s)
        # ''.join(sorted(s)) esto lo invierte
    return [g for g in sorted_string_to_anagrams.values() if len(g) >= 2]



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'anagrams.py',
            'anagrams.tsv',
            find_anagrams,
            comparator=test_utils.unordered_compare))
