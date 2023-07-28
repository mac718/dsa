from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    min_coins = [amount + 1] * (amount + 1)
    min_coins[0] = 0

    for i in range(1, len(min_coins)):
        for coin in coins:
            if coin <= i:
                min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    return min_coins[-1] if min_coins[-1] >= amount else -1
