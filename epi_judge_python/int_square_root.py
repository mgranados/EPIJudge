from test_framework import generic_test


def square_root(k: int) -> int:
    if k == 0:
        return k

    low = 1
    end = k
    while low <= end:
        mid = low + (end - low) // 2
        if mid * mid == k: #we done
            return mid
        elif mid * mid > k: # let's keep going bin
            end = mid
        elif mid * mid < k: # let's keep going
            n_mid = mid +1
            if (n_mid * n_mid) > k: # but if next is > k we done
                return mid
            else: 
                low = mid

    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_square_root.py',
                                       'int_square_root.tsv', square_root))
