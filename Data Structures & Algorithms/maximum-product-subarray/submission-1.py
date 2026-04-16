class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # res = nums[0]
        # for i in range(len(nums)):
        #     cur = nums[i]
        #     res = max(res, cur)
        #     for j in range(i + 1, len(nums)):
        #         cur *= nums[j]
        #         res = max(res, cur)

        # return res

        # Using one pass iteration - Kadane's algorithm / prefix suffix

        prefix = suffix = 0
        res = nums[0]
        n = len(nums)
        for i in range (n):
            prefix = nums[i] * (prefix or 1)
            suffix = nums[n - 1 - i] * (suffix or 1)
            res = max(res, max(prefix, suffix))

        return res

        