class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)

        # The DP table should be (n+1) x (m+1) to handle base cases
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

        # The loops should iterate up to n and m
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                # We use i-1 and j-1 to access the characters in the strings
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The final answer is at the bottom-right corner of the DP table
        return dp[n][m]