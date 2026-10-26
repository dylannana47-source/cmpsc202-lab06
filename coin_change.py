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


if __name__ == "__main__":
    print(coin_change_recursive([1, 2, 5], 11))
