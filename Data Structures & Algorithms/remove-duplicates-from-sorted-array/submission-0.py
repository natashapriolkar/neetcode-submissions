class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        sortedS = sorted(set(nums))
        nums[:len(sortedS)] = sortedS
        return len(sortedS)
        