def climbStairs(n, memo = {}):
    if n <= 1:
        return 1
    if (n - 1) not in memo:
        k = (n - 1)
        memo[k] = climbStairs(k, memo)
        oneStep = memo[n - 1]
    else:
        oneStep = memo[n - 1]
    if (n - 2) not in memo:
        memo[n - 2] = climbStairs(n - 2, memo)
        twoStep = memo[n - 2]
    else:
        twoStep = memo[n - 2]
    print(oneStep + twoStep)
    return oneStep + twoStep

climbStairs(4)