from typing import List

from test_framework import generic_test


def n_queens(n: int) -> List[List[int]]:
    result = []
    def solver(row):
        if row == n:
            result.append(placement.copy())
            return
        for column in range(n):
            all_pass = []
            for i, c in enumerate(placement[:row]):
                # i = row
                # c = value of column
                all_pass.append(
                    abs(c - column) != 0 and # same col
                    abs(c-column) != row - i) # a diagonal

            if all(all_pass):
                placement[row] = column
                solver(row+1)


    placement = [0] * n
    solver(0)
        
    return result




def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('n_queens.py', 'n_queens.tsv', n_queens,
                                       comp))
