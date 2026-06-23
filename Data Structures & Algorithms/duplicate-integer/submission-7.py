class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # numsSet = set(nums)
        # if len(nums) ==  len(numsSet):
        #     return False
        # return True

        count = Counter(nums)
        for num, cnt in count.items():
            if cnt > 1:
                return True

        return False
        