from typing import List


def maxProfit(prices: List[int]) -> int:
    l = 0
    r = 0
    res = 0
    while r < len(prices):
        if prices[r] < prices[l]:
            l = r
        res = max(res, prices[r] - prices[l])
        r += 1
    return res
