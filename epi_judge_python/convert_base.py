from test_framework import generic_test
import math

def convert_base(num_as_string: str, b1: int, b2: int) -> str:
    symbol = ''
    if num_as_string[0] in '-+':
        symbol = '-'
        num_as_string= num_as_string[1:]

    base_dig = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C',
                'D', 'E','F']

    if num_as_string == '0':
        return '0'

    # convert b1 -> base 10 
    in_10 = 0
    for i in reversed(range(len(num_as_string))):
        num = base_dig.index(num_as_string[i])
        in_10 += num * pow(b1, len(num_as_string) - 1 - i)

    # convert base 10 ->  b2
    #max_b2 = math.floor(math.log(in_10, b2))
    #result = [] # append to LIST never str
    #for j in reversed(range(max_b2 + 1)):
    #    # divide int and multiply
    #    to_convert = in_10 // pow(b2, j)
    #    in_10 -= to_convert * pow(b2, j)
    #    result.append(base_dig[to_convert])
    
    result = []
    while in_10:
        to_convert = in_10 % b2
        in_10 //= b2
        result.append(base_dig[to_convert])

    # 7A1
    return symbol + ''.join(reversed(result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
