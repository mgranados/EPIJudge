from typing import List
import math
from test_framework import generic_test


# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:
    
    primes = [True] * (n + 1)

    for i, v in enumerate(primes):
        if i < 2:
            continue

        count = 2
        multiplied = i * count
        while multiplied <= n:
            primes[multiplied] = False
            count +=1 
            multiplied = i * count

    result = [k + 2 for k,v in enumerate(primes[2:]) if v]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
