class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        setNums = set(nums)
        for n in nums:
            # verify if n is the first number in the list
            if (n-1) not in setNums:
                length = 1 # consider that length is 1 atleast 1 is the longest consecutive sequence
                # check next number in sequence exists
                while (n + length) in setNums:
                    length += 1
                longest = max(longest, length)
            
        return longest
                     


        