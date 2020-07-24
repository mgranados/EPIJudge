import collections
import copy
import functools
from typing import List

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))


def search_maze(maze: List[List[int]], s: Coordinate,
                e: Coordinate) -> List[Coordinate]:

    result_path = []

    def do_dfs(current):
        if current.x < 0 or current.y < 0 or current.x >= len(maze) or current.y >= len(maze[current.x]) or maze[current.x][current.y] == BLACK:
            return False

        result_path.append(current)
        maze[current.x][current.y] = BLACK

        if current == e:
            return True

        up = Coordinate(current.x, current.y+1)
        if do_dfs(up):
            return True
        right = Coordinate(current.x + 1, current.y)
        if do_dfs(right):
            return True
        down = Coordinate(current.x - 1, current.y)
        if do_dfs(down):
            return True
        left = Coordinate(current.x, current.y -1)
        if do_dfs(left):
            return True

        del result_path[-1] # LITERAL BACKTRACKING
        return False
            

    do_dfs(s)


    return result_path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure('Path doesn\'t lay between start and end points')

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure('Path contains invalid segments')

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('search_maze.py', 'search_maze.tsv',
                                       search_maze_wrapper))
