class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # numsSet = set(nums)
        # if len(nums) ==  len(numsSet):
        #     return False
        # return True

        # count = Counter(nums)
        # for num, cnt in count.items():
        #     if cnt > 1:
        #         return True

        # return False
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for key, value in count.items():
            if value > 1:
                return True

        return False

        
        