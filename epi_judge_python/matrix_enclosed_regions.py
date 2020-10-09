from typing import List

from test_framework import generic_test
import collections

def fill_surrounded_regions(board: List[List[str]]) -> None:
    m = len(board)
    n = len(board[0])
    q = collections.deque()

    for k in range(m):
        for i, j in ((k,0), (k, n - 1)):
            q.append((i, j))

    for k in range(n):
        for i, j in ((0,k), (m - 1, k)):
            q.append((i, j))

    while q:
        x, y = q.popleft()
        if 0 <= x < m and 0 <= y < n and board[x][y] == 'W':
            board[x][y] = 'R'
            q.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    for x in range(m):
        for y in range(n):
            if board[x][y] != 'R':
                board[x][y] = 'B'
            else:
                board[x][y] = 'W'

def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('matrix_enclosed_regions.py',
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
