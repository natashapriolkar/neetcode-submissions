class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid  = l + (r - l) // 2
            res = min(nums[mid], res)
            if nums[mid] >= nums[l]:
                #this is sorted half so the min element will be in second half
                l = mid + 1
            else:
                r = mid - 1


        return res

        