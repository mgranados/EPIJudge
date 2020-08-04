from typing import List

from test_framework import generic_test

# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    size = len(partial_assignment)
    cols_seen = {} #{ 0: [], 1: []}

    square = []
    for row in range(size):
        seen = [0] * 9
        # CHECK cols in rows  
        # [ - - - > ]
        # [ - - - > ]
        # [ - - - > ]
        # [ - - - > ]
        for col in range(size):
            if partial_assignment[row][col] != 0:
                if seen[partial_assignment[row][col] -1]:
                    return False
                else:
                    seen[partial_assignment[row][col] - 1] = 1
            # CHECK rows per cols 
            # [ | | | | ]
            # [ | | | | ]
            # [ | | | | ]
            # [ v v v v ]
            if partial_assignment[row][col] != 0:
                if not col in cols_seen:
                    cols_seen[col] = [partial_assignment[row][col]]
                elif partial_assignment[row][col] in cols_seen[col]:
                    return False
                else:
                    cols_seen[col].append(partial_assignment[row][col])
    # CHECK square three more
    #  0 1 2   3 4 5
    # [x x x] [x x x]
    # [x x x] [x x x]
    # [x x x] [x x x]
    for row in range(0, size, 3):
        for col in range(0, size, 3):
            # start to review the square
            curr_square = [0] * 9
            for srow in range(row, row + 3):
                for scol in range(col, col + 3):
                    if partial_assignment[srow][scol] != 0:
                        if curr_square[partial_assignment[srow][scol] -1]:
                            return False
                        else:
                            curr_square[partial_assignment[srow][scol] - 1] = 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
