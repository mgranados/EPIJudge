from test_framework import generic_test


def parity(x: int) -> int:
    # ^ XOR gives parity of bits
    x ^= x >> 32 # compare with half 
    x ^= x >> 16 # compare with half 
    x ^= x >> 8 # compare with half 
    x ^= x >> 4 # compare with half 
    x ^= x >> 2 # compare with half 
    x ^= x >> 1 # compare with half 
    return x & 0x1 # mask only lowest bit



if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
