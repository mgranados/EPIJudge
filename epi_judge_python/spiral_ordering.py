from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # Visit n-1 each iteration 
    spiraled_matrix = []
    def spiral_that(offset): #n-1, n,2
        if offset == len(square_matrix) - offset -1: # case of 1
            spiraled_matrix.append(square_matrix[offset][offset])
            return
        # group columns in tuples (1,4,7), (2, 5, 8), (3, 6, 9)
        verticals = list(zip(*square_matrix))
        # horizontal top
        spiraled_matrix.extend(square_matrix[offset][offset:-1-offset]) 
        # vertical right
        spiraled_matrix.extend(verticals[-1 - offset][offset:-1-offset])
        # horizontal bottom
        spiraled_matrix.extend(square_matrix[-1 -offset][-1 -
                                                         offset:offset:-1])
        # vertical left 
        spiraled_matrix.extend(verticals[offset][-1 - offset:offset:-1])
    # n-1 // offset
    # se achica
    # si tenemos un nuevo sq_matrix again
    for offset in range((len(square_matrix) + 1 // 2)):
        spiral_that(offset)

    return spiraled_matrix


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
