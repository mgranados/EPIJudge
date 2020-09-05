from test_framework import generic_test


def reverse_bits(x: int) -> int:
    out = 0
    for i in range(64):
        # get last bit from x 
        # and reverse it
        lbs = x & 1 # 1
        out <<= 1 # 0000 => 0000"0"
        out |= lbs # 00 | 1 = 01
        x >>= 1 # remove lbs from x = 1001 => 100"
    return out


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_bits.py', 'reverse_bits.tsv',
                                       reverse_bits))
