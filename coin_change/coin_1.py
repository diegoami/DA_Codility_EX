from sys import maxsize
def dynamic_coin_changing(C, k):
    n = len(C)
    dp = [0] + [maxsize]*k

    for i in range(1, n + 1):
        for j in range(C[i - 1], k + 1):
            dp[j] = min(dp[j - C[i - 1]] + 1, dp[j])
        print(dp)
    return dp

print(dynamic_coin_changing([1,2,5], 13))