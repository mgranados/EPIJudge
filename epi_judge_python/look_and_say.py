from test_framework import generic_test


def look_and_say(n: int) -> str:
    if not n:
        return ''

    if n == 1:
        return '1'

    result = "1"
    for _ in range(1, n):
        last_number = None
        reps = 0
        local = []
        for char in result:
            # "describe" it
            if not last_number:
                last_number = char
                reps = 1
            elif char == last_number:
                reps += 1
            else: # reset
                local.append(str(reps) + last_number)
                last_number = char
                reps = 1
        local.append(str(reps) + last_number)
        result = "".join(local)


    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('look_and_say.py', 'look_and_say.tsv',
                                       look_and_say))
