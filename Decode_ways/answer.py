class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        for i in range(1, len(s)):
            # print(dp)
            curr_ways = 0
            if int(s[i]) > 0:
                curr_ways += dp[i]
            if s[i-1] != '0' and int(s[i-1:i+1]) <= 26:
                curr_ways += dp[i - 1]
            dp[i + 1] = curr_ways
        return dp[len(s)]
