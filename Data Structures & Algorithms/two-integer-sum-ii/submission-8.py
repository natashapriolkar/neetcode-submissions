class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # l = 0
        # r = len(numbers) - 1
        # while l < r:
        #     curSum = numbers[l] + numbers[r]
        #     if curSum > target:
        #         r -= 1
        #     elif curSum < target:
        #         l += 1

        #     else:
        #         return [l + 1, r + 1]

        # return []

        for i in range(len(numbers)):
            temp = target - numbers[i]
            l = i + 1
            r = len(numbers) - 1
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == temp:
                    return [i + 1, mid + 1]
                elif numbers[mid] > temp:
                    r = mid - 1
                else:
                    l = mid + 1

        return []        