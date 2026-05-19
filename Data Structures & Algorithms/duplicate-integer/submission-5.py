class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # numsSet = set(nums)
        # if len(nums) != len(numsSet):
        #     return True

        # return False

        count = Counter(nums)
        for key, value in count.items():
            if value > 1:
                return True

        return False
        