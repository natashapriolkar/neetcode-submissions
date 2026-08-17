class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # def dfs(i, j):
        #     if i == len(nums):
        #         return 0

        #     # Not include current element
        #     LIS = dfs(i + 1, j)

        #     if j == -1 or nums[i] > nums[j]:
        #         LIS = max(LIS, 1 + dfs(i + 1, i))

        #     return LIS

        # return dfs(0, -1)
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)


        