from typing import List

from test_framework import generic_test


def get_max_trapped_water(heights: List[int]) -> int:
    left, right = 0, len(heights) - 1
    max_area = 0
    while left < right:
        base = right - left
        height = min(heights[right], heights[left])
        max_area = max(max_area, base * height)
        if heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
    return max_area


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('max_trapped_water.py',
                                       'max_trapped_water.tsv',
                                       get_max_trapped_water))
