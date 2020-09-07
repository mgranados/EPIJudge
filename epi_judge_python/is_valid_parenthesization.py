from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    stack = []
    if len(s) == 1:
        return False
    for char in s:
        if char == '}':
            if not stack or stack[-1] != '{':
                return False
            else:
                stack.pop()
        elif char == ')':
            if not stack or stack[-1] != '(':
                return False
            else:
                stack.pop()
        elif char == ']':
            if not stack or stack[-1] != '[':
                return False
            else:
                stack.pop()
        else:
            stack.append(char)

    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
