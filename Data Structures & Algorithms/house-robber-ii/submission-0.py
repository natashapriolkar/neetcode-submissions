class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return nums[0]

        skipFirstHouse = [0] * (len(nums) - 1)
        skipLastHouse = [0] * (len(nums) - 1)

        for i in range(len(nums) - 1):
            skipFirstHouse[i] = nums[i + 1]
            skipLastHouse[i] = nums[i]

        lootSkippingLast = self.rob_helper(skipLastHouse)
        lootSkippingFirst = self.rob_helper(skipFirstHouse)

        return max(lootSkippingLast, lootSkippingFirst)

    def rob_helper(self, skippedHouseArr):
        if len(skippedHouseArr) < 2:
            return skippedHouseArr[0]
        
        dp = [0] * len(skippedHouseArr)
        dp[0] = skippedHouseArr[0]
        dp[1] = max(skippedHouseArr[0], skippedHouseArr[1])
        for i in range(2, len(skippedHouseArr)):
            dp[i] = max((dp[i-2] + skippedHouseArr[i]), dp[i-1])

        return dp[len(skippedHouseArr) - 1]
    
        