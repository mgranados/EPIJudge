from test_framework import generic_test


def count_bits(x: int) -> int:
    # O(k) (number of bits set)
    num_bits = 0
    while x:
        # trampa loca unset lowest set bit
        num_bits += 1
        x &= x - 1 # remove last set bit
    return num_bits;



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('count_bits.py', 'count_bits.tsv',
                                       count_bits))
