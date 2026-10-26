# Empirical Comparison

I tested `coins = [1, 2, 5]` with amounts 5, 10, 15, 20, and 25 The table reports the median of three runs measured with `perf_counter()`; each memoized run starts with a fresh dictionary. The benchmark script also checks that all three approaches return the same result.

| Amount | Naive recursion | Memoization | Bottom-up DP |
|---:|---:|---:|---:|
| 5 | 0.004 ms | 0.003 ms | 0.003 ms |
| 10 | 0.052 ms | 0.005 ms | 0.003 ms |
| 15 | 1.230 ms | 0.016 ms | 0.013 ms |
| 20 | 10.021 ms | 0.011 ms | 0.010 ms |
| 25 | 144.955 ms | 0.014 ms | 0.008 ms |

Naive recursion became much slower as the amount increased, while memoization and bottom-up DP stayed fast across these tests. For amount 25, naive recursion took about 145 ms, compared with about 0.014 ms for memoization and 0.008 ms for bottom-up DP.
