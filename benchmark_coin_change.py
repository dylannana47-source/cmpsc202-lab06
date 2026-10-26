from statistics import median
from time import perf_counter

from coin_change import coin_change_dp, coin_change_memoized, coin_change_recursive


COINS = [1, 2, 5]
AMOUNTS = [5, 10, 15, 20, 25]
REPETITIONS = 3


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
        expected_result = None
        for _, solve in approaches:
            samples = []
            result = None
            for _ in range(REPETITIONS):
                start = perf_counter()
                current_result = solve(amount)
                samples.append((perf_counter() - start) * 1000)
                if result is None:
                    result = current_result
                elif current_result != result:
                    raise RuntimeError(
                        f"Approach returned inconsistent results for amount {amount}"
                    )
            timings.append(median(samples))
            if expected_result is not None and result != expected_result:
                raise RuntimeError(
                    f"Approaches disagree for amount {amount}: "
                    f"{result} != {expected_result}"
                )
            expected_result = result
        print(
            f"| {amount} | "
            + " | ".join(f"{elapsed:.3f} ms" for elapsed in timings)
            + " |"
        )


if __name__ == "__main__":
    main()
