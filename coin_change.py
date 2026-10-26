def coin_change_recursive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return -1

    fewest = None
    for coin in coins:
        if coin <= 0 or coin > amount:
            continue

        remaining_coins = coin_change_recursive(coins, amount - coin)
        if remaining_coins != -1:
            candidate = remaining_coins + 1
            if fewest is None or candidate < fewest:
                fewest = candidate

    return -1 if fewest is None else fewest


def coin_change_memoized(coins, amount, memo):
    if amount == 0:
        return 0
    if amount < 0:
        return -1
    if amount in memo:
        return memo[amount]

    fewest = None
    for coin in coins:
        if coin <= 0 or coin > amount:
            continue

        remaining_coins = coin_change_memoized(coins, amount - coin, memo)
        if remaining_coins != -1:
            candidate = remaining_coins + 1
            if fewest is None or candidate < fewest:
                fewest = candidate

    memo[amount] = -1 if fewest is None else fewest
    return memo[amount]


def coin_change_dp(coins, amount):
    if amount < 0:
        return -1

    unreachable = amount + 1
    dp = [unreachable] * (amount + 1)
    dp[0] = 0

    for current_amount in range(1, amount + 1):
        for coin in coins:
            if 0 < coin <= current_amount:
                dp[current_amount] = min(
                    dp[current_amount],
                    dp[current_amount - coin] + 1,
                )

    return dp[amount]


if __name__ == "__main__":
    coins = [1, 2, 5]
    print(coin_change_recursive(coins, 11))
    print(coin_change_memoized(coins, 11, {}))
