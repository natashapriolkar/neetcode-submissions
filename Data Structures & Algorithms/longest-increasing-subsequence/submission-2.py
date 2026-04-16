class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Recursive function to find the length of LIS at index i given the previous chosen value is prev

        def dfs(i, prev):
            if i == len(nums):
                return 0

            # Skip the current element at index i
            skip = dfs(i + 1, prev)
            # Take the the current element at index i
            take = 0
            if nums[i] > prev:
                take = 1 + dfs(i + 1, nums[i])

            return max(skip, take)

        length = dfs(0, float('-inf'))
        return length

        