def exp_sum(n):
    if n < 0:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1 # Base case: one way to make 0
    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]
    return dp[n]

print(exp_sum(4))  #5 -> 1+1+1+1, 1+1+2, 1+3, 2+2, 4
print(exp_sum(5)) # 7 -> 1+1+1+1+1, 1+1+1+2, 1+1+3, 1+2+2, 1+4, 5, 2+3
print(exp_sum(10)) #42
print(exp_sum(50)) #204226
print(exp_sum(4096))
