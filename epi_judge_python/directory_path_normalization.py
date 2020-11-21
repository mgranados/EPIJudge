from test_framework import generic_test


def shortest_equivalent_path(path: str) -> str:
    if not path:
        return ''

    stack = []
    if path[0] == '/':
        stack.append('/')

    folders = path.split('/')
    for directory in folders:

        if not directory or directory == '.':
            continue

        if directory == '..':
            if not stack or stack[-1] == '..':
                stack.append(directory)
            else:
                stack.pop()

        else:
            stack.append(directory)
    result = '/'.join(stack)

    if result.startswith('//'):
         return result[1:]
    return result

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('directory_path_normalization.py',
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
