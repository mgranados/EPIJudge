from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    # O(n) 
    # set begin
    begin = prices[0]
    max_diff = 0

    for i in range(1, len(prices)):
        if begin > prices[i]:
            begin = prices[i] 
        else:
            # max(prices[i] - begin , max_diff)
            if prices[i] - begin > max_diff:
                max_diff = prices[i] - begin

    # Variant
    #subarray_length = 1
    #max_sub = 0
    #for i in range(1, len(prices)):
    #    if begin != prices[i]:
            #max_sub = max(max_sub, subarray_length)
            #subarray_length = 1
    #        begin = prices[i]
    #    else:
    #        subarray_length += 1
    #return max_sub

    return max_diff 


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
