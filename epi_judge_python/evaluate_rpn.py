from test_framework import generic_test


def evaluate(expression: str) -> int:
    stack = []
    listed = expression.split(',')
    ops = {
        '+': lambda x,y: x + y,
        '-': lambda x,y: y - x,
        '*': lambda x,y: x * y,
        '/': lambda x,y: y // x,
    }

    if len(listed) == 1:
        return int(listed[0])

    for op in listed:
        if op in ops:
            first = stack.pop()
            second = stack.pop()

            selected = ops[op]
            op_result = selected(first, second)

            stack.append(op_result)

        else:
            stack.append(int(op))

    return stack[-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
