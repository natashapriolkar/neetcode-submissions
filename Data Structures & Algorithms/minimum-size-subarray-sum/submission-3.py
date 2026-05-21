class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # res = float('inf')
        # for i in range(len(nums)):
        #     curSum = 0
        #     for j in range(i, len(nums)):
        #         curSum += nums[j] 
        #         if curSum >= target:
        #             res = min(res, j - i + 1)
        #             break

        # return 0 if res == float('inf') else res


        l = r = 0
        curSum = 0
        res = float('inf')
        while r < len(nums):
            curSum += nums[r]
            while curSum >= target:
                res = min(res, r - l + 1)
                curSum -= nums[l]
                l += 1
            r += 1

        return 0 if res == float('inf') else res


        