nums = list(map(int, input().strip()))

if nums[0] == 0:
    print(0)
else:
    n = len(nums)
    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1  # 초기 조건 설정

    for i in range(2, n + 1):
        one_digit = nums[i - 1]
        two_digits = nums[i - 2] * 10 + nums[i - 1]

        if 1 <= one_digit <= 9:
            dp[i] += dp[i - 1]
        if 10 <= two_digits <= 26:
            dp[i] += dp[i - 2]

    print(dp[n] % 1000000)
