class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        count = {}
        freq = [[] for i in range(len(nums)+ 1)] # +1 because the maximum possible frequence of a number is equal to the total number of elements in the array
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for key, val in count.items():
            freq[val].append(key)

        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
                    


        