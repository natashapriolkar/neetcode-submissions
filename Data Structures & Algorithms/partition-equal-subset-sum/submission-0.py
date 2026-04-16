class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        def dfs(i, target):
            if i >= len(nums) or target < 0:
                return False
            if target == 0:
                return True
            return dfs(i+1, target) or dfs(i+1, target - nums[i])

        return dfs(0, sum(nums) // 2)
        