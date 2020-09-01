from typing import List

from test_framework import generic_test


def flip_color(x: int, y: int, image: List[List[bool]]) -> None:
    # BFS => visit all adjacent and check if color needs switch
    color = not image[x][y]

    def flip_helper(x, y, image):
        if image[x][y] != color:
            image[x][y] = color
            if x < len(image) - 1:
                flip_helper(x + 1, y, image)
            if x > 0:
                flip_helper(x - 1, y, image)
            if y < len(image) - 1:
                flip_helper(x, y + 1, image)
            if y > 0:
                flip_helper(x, y - 1, image)

    flip_helper(x, y, image)

    return image


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_connected_regions.py',
                                       'painting.tsv', flip_color_wrapper))
