from test_framework import generic_test
import math

def power(x: float, y: int) -> float:
    # 2 ^ 4 * 2 ^ 3 = 2 ^ 7
    # (2 ^ m) ^ n = 2 ^ (m * n)
    result = 1
    power_2 = math.floor(abs(y/2))
    odd = y % 2 == 1
    for i in range(power_2):
        result *= x * x

    if odd:
        result *= x

    if y < 0:   
        return 1 / result
 
    return result 

# at worst 2* biggest power of 2 ~ O(n)

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
