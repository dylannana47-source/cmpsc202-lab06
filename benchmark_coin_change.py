from time import perf_counter

from coin_change import coin_change_dp, coin_change_memoized, coin_change_recursive


COINS = [1, 2, 5]
AMOUNTS = [10, 15, 20, 25, 30, 35]


def main():
    approaches = [
        ("Naive recursion", lambda amount: coin_change_recursive(COINS, amount)),
        (
            "Memoization",
            lambda amount: coin_change_memoized(COINS, amount, {}),
        ),
        ("Bottom-up DP", lambda amount: coin_change_dp(COINS, amount)),
    ]

    print("| Amount | " + " | ".join(name for name, _ in approaches) + " |")
    print("|---:|---:|---:|---:|")
    for amount in AMOUNTS:
        timings = []
        for _, solve in approaches:
            start = perf_counter()
            solve(amount)
            timings.append((perf_counter() - start) * 1000)
        print(
            f"| {amount} | "
            + " | ".join(f"{elapsed:.3f} ms" for elapsed in timings)
            + " |"
        )


if __name__ == "__main__":
    main()
