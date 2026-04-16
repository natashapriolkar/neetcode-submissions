class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # numsSet = set(nums)
        # if len(numsSet) != len(nums):
        #     return True
        # return False

        # count = Counter(nums)
        # for key, value in count.items():
        #     if value > 1:
        #         return True
            
        # return False

        countMap = {}
        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)

        for key, value in countMap.items():
            if value > 1:
                return True
        return False
        