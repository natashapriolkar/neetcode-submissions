class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp = [amount + 1] * (amount + 1)
        # dp[0] = 0

        # for a in range(1, amount+1):
        #     for c in coins:
        #         if a - c >= 0:
        #             dp[a] = min(dp[a], 1 + dp[a-c])
        # return dp[amount] if dp[amount] != amount + 1 else -1
        #Recursive approach
        memo = {}
        def dfs(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float('inf')
            if amount in memo:
                return memo[amount]
            
            res = float('inf')
            for c in coins:
                res = min(res, 1 + dfs(amount - c))
                
            memo[amount] = res
            return res

        ans = dfs(amount)
        return ans if ans != float('inf') else -1

        