class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, amount):
            if amount == 0:
                return 1
            if amount < 0 or i >= len(coins):
                return 0
            if (i, amount) in memo:
                return memo[(i, amount)]
            res = 0
            if amount >= 0:
                res = dfs(i + 1, amount)
                res += dfs(i, amount - coins[i])
                
            memo[(i, amount)] = res
            return memo[(i, amount)]

        return dfs(0, amount)

        